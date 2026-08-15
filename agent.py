"""CausalSentinel — OpenCausal agent.

Run:
    python agent.py --protein PCSK9 --disease "high cholesterol"
    python agent.py --batch pairs.txt          # one "PROTEIN<tab>DISEASE" per line

Pipeline:
  1. Load API keys from ../.env (keys are NEVER hard-coded here).
  2. Wrap every tool in a ToolLedger so each call's arguments and verbatim return value
     are captured — Gemini's automatic function calling otherwise swallows them.
  3. Let the model call tools freely and write ONLY two things: a one-line verdict and a
     reasoning paragraph.
  4. Render the card: the evidence table, the caveat block, the sources and the provenance
     footer are built mechanically from the ledger, so no tool-declared caveat can be
     dropped and no number can drift.
  5. Validate the model's prose against the ledger. An unsupported number, rsID or
     accession fails the run (use --allow-unvalidated to write the card anyway).

SDK: the current `google-genai` package. Model: Gemini (see MODEL).
"""
import os
import re
import json
import argparse
import datetime
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types

from tools import TOOLS
from ledger import ToolLedger
from render import render_card
from validate_card import validate, format_report

HERE = Path(__file__).resolve().parent
MODEL = "gemini-flash-lite-latest"

# The model no longer writes the card. It writes two labelled blocks; everything else is
# rendered from tool output. Keeping this instruction here (not in system_prompt.md) means
# the prompt file stays the project's readable statement of the rules.
WRITER_INSTRUCTION = """
Gather evidence by calling the tools, then reply with EXACTLY these two blocks and
nothing else:

VERDICT: <GO | NO-GO | INSUFFICIENT EVIDENCE> — one sentence explaining why.

REASONING:
<2-5 sentences weighing the evidence.>

Hard rules for what you write:
- Every number, rsID or identifier you mention must come from a tool result in THIS run.
  If you did not receive it from a tool, do not write it. An automatic validator rejects
  unsupported numbers and the run fails.
- Prefer describing evidence qualitatively; the exact figures are printed in a table you
  do not write, so you rarely need to restate them.
- If the MR tool returned found=false, say plainly that no MR estimate was available and
  do NOT treat that as evidence of no effect.
- Never describe this agent as performing, running or computing Mendelian randomization
  or colocalization. Where MR estimates exist they were retrieved from published work.
- If a tool declared a caveat, respect it — never convert a truncated or lower-bound count
  into a flat factual claim.
"""

# Models decorate labels ("**VERDICT:**", "## Reasoning"), so match the WORD and tolerate
# whatever markup surrounds it. A parser that only accepts the literal format silently
# produced one empty Reasoning section in a ten-card batch.
LABEL = r"[#*_\s]*{}\s*[:\-–]?\s*[#*_]*"
VERDICT_RE = re.compile(LABEL.format("VERDICT") + r"(.+?)(?=\n\s*\n|" + LABEL.format("REASONING") + r"|$)",
                        re.S | re.I)
REASON_RE = re.compile(LABEL.format("REASONING") + r"(.+)$", re.S | re.I)


def _clean(s: str) -> str:
    """Drop leftover markdown emphasis and tidy whitespace."""
    s = re.sub(r"^[\s*_#>-]+", "", s or "")
    s = re.sub(r"[\s*_]+$", "", s)
    return s.strip()


def split_model_output(text: str):
    """Pull the verdict line and reasoning body out of the model's reply."""
    text = text or ""
    v = VERDICT_RE.search(text)
    r = REASON_RE.search(text)
    verdict = _clean(v.group(1)) if v else ""
    reasoning = _clean(r.group(1)) if r else ""

    if not reasoning:
        # Fall back to whatever prose followed the verdict, rather than shipping a blank
        # Reasoning section.
        tail = text[v.end():] if v else text
        tail = _clean(tail)
        reasoning = tail or "_Model produced no reasoning text._"
    if not verdict:
        verdict = "INSUFFICIENT EVIDENCE — model did not emit a parseable verdict."
    return verdict, reasoning


def generate_one(client, system_prompt, protein, disease, out_dir, allow_unvalidated=False):
    ledger = ToolLedger(TOOLS)
    request = (
        f"Assemble the target evidence for protein {protein} and disease {disease}. "
        f"Call the tools to gather evidence, then reply in the required two-block format."
    )
    response = client.models.generate_content(
        model=MODEL,
        contents=request,
        config=types.GenerateContentConfig(
            tools=ledger.wrapped(),
            system_instruction=system_prompt + "\n\n" + WRITER_INSTRUCTION,
        ),
    )
    model_text = response.text or ""
    verdict, reasoning = split_model_output(model_text)

    result = validate(verdict + "\n" + reasoning, ledger)
    card_md = render_card(protein, disease, ledger, reasoning, verdict, MODEL)

    if not result["ok"]:
        card_md += (
            "\n> **VALIDATION FAILED** — the model wrote claim tokens with no support in "
            "tool output:\n"
            + "\n".join(f"> - [{u['kind']}] `{u['token']}`" for u in result["unsupported"])
            + "\n"
        )

    out_dir.mkdir(exist_ok=True)
    stem = f"{protein}_{re.sub(r'[^A-Za-z0-9]+', '-', disease).strip('-')}_evidence_card"
    written = None
    if result["ok"] or allow_unvalidated:
        (out_dir / f"{stem}.md").write_text(card_md, encoding="utf-8")
        written = f"cards/{stem}.md"

    (out_dir / f"{stem}.json").write_text(json.dumps({
        "protein": protein,
        "disease": disease,
        "generated_at": datetime.datetime.now().isoformat(timespec="seconds"),
        "model": MODEL,
        "tools_called": ledger.called(),
        "tool_ledger": ledger.entries,
        "model_verdict": verdict,
        "model_reasoning": reasoning,
        "validation": result,
        "card_markdown": card_md,
    }, indent=2, ensure_ascii=False, default=str), encoding="utf-8")

    return {"protein": protein, "disease": disease, "validation": result,
            "verdict": verdict, "written": written, "n_tool_calls": len(ledger.entries),
            "n_words": len((verdict + " " + reasoning).split()),
            "tools_called": ledger.called()}


def main() -> None:
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise SystemExit("GEMINI_API_KEY not found. Put it in ../.env (see .env.example).")
    client = genai.Client(api_key=api_key)

    ap = argparse.ArgumentParser(description="CausalSentinel - target evidence card generator")
    ap.add_argument("--protein", help="Gene/protein symbol, e.g. PCSK9")
    ap.add_argument("--disease", help="Disease name, e.g. 'high cholesterol'")
    ap.add_argument("--batch", help="File with one 'PROTEIN<TAB>DISEASE' pair per line")
    ap.add_argument("--allow-unvalidated", action="store_true",
                    help="Write the card even when validation fails (it is annotated)")
    args = ap.parse_args()

    system_prompt = (HERE / "system_prompt.md").read_text(encoding="utf-8")
    out_dir = HERE / "cards"

    pairs = []
    if args.batch:
        for line in Path(args.batch).read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = re.split(r"\t|\s{2,}", line)
            if len(parts) >= 2:
                pairs.append((parts[0].strip(), parts[1].strip()))
    elif args.protein and args.disease:
        pairs.append((args.protein, args.disease))
    else:
        raise SystemExit("Give --protein and --disease, or --batch FILE.")

    summary = []
    for protein, disease in pairs:
        print(f"[CausalSentinel] {protein} x {disease} ...", flush=True)
        try:
            r = generate_one(client, system_prompt, protein, disease, out_dir,
                             args.allow_unvalidated)
        except Exception as e:
            print(f"  RUN FAILED: {type(e).__name__}: {e}")
            summary.append({"protein": protein, "disease": disease, "error": repr(e)})
            continue
        print(f"  tools: {r['n_tool_calls']} calls | {format_report(r['validation'])}")
        print(f"  verdict: {r['verdict'][:110]}")
        print(f"  wrote: {r['written'] or '(card withheld — validation failed)'}")
        summary.append(r)

    if len(summary) > 1:
        ok = sum(1 for s in summary if s.get("validation", {}).get("ok"))
        words = sum(len(s.get("reasoning_words", "") or "") for s in summary)
        checked = sum(s.get("validation", {}).get("checked", 0) for s in summary)
        n_words = sum(s.get("n_words", 0) for s in summary)
        density = (100.0 * checked / n_words) if n_words else 0.0
        print(f"\n[CausalSentinel] {ok}/{len(summary)} cards passed validation.")
        # A pass rate alone is a vanity metric: a model that writes nothing checkable
        # passes everything. Report how much there WAS to check alongside it.
        print(f"[CausalSentinel] claim density: {checked} checkable token(s) across "
              f"{n_words} words of reasoning ({density:.1f} per 100 words). "
              f"A low density means the pass rate is weak evidence of accuracy.")
        (out_dir / "_batch_summary.json").write_text(
            json.dumps({"cards": summary,
                        "passed": ok, "total": len(summary),
                        "claim_tokens_checked": checked,
                        "reasoning_words": n_words,
                        "claim_density_per_100_words": round(density, 2)},
                       indent=2, ensure_ascii=False, default=str), encoding="utf-8")


if __name__ == "__main__":
    main()
