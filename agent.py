"""CausalSentinel - OpenCausal agent (Round 1).

Entry point. Run:
    python agent.py --protein PNPLA3 --disease MASLD

What it does:
  1. Loads API keys from ../.env (keys are NEVER hard-coded here).
  2. Reads system_prompt.md (the agent's rules + card template).
  3. Registers the Round-1 tools with Gemini.
  4. Runs Gemini's automatic function-calling loop: the model decides which tools
     to call, the SDK executes them, results feed back, and it synthesizes.
  5. Writes the causal card to cards/{protein}_{disease}_causal_card.md (+ .json).

SDK: uses the current `google-genai` package (the older `google-generativeai`
package is deprecated as of 2026).
"""
import os
import json
import argparse
import datetime
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types

from tools import TOOLS

HERE = Path(__file__).resolve().parent
# "gemini-flash-lite-latest": current fast/cheap flash model, good for a tool-calling
# agent and generous on the free tier. Alternatives: "gemini-flash-latest" (bigger),
# "gemini-3.1-flash-lite" (pinned). Full flash models may hit 429/503 on the free tier.
MODEL = "gemini-flash-lite-latest"


def main() -> None:
    # 1) keys - load_dotenv walks up the folders and finds ../.env
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise SystemExit("GEMINI_API_KEY not found. Put it in ../.env (see .env.example).")
    client = genai.Client(api_key=api_key)

    # command-line arguments
    ap = argparse.ArgumentParser(description="CausalSentinel - causal evidence card generator")
    ap.add_argument("--protein", required=True, help="Gene/protein symbol, e.g. PNPLA3")
    ap.add_argument("--disease", required=True, help="Disease name, e.g. MASLD")
    args = ap.parse_args()

    # 2) the system prompt (agent rules + the required card template)
    system_prompt = (HERE / "system_prompt.md").read_text(encoding="utf-8")

    # 3) + 4) one call runs the whole loop: passing plain Python functions as `tools`
    # turns on automatic function calling, so the model calls them and continues.
    request = (
        f"Assemble a causal evidence card for protein {args.protein} and disease "
        f"{args.disease}. Call the tools to gather evidence, then write the card in the "
        f"required format."
    )
    print(f"[CausalSentinel] Generating card for {args.protein} x {args.disease} ...")
    response = client.models.generate_content(
        model=MODEL,
        contents=request,
        config=types.GenerateContentConfig(
            tools=TOOLS,
            system_instruction=system_prompt,
        ),
    )
    card_md = response.text

    # 5) write the outputs
    out_dir = HERE / "cards"
    out_dir.mkdir(exist_ok=True)
    stem = f"{args.protein}_{args.disease}_causal_card"
    (out_dir / f"{stem}.md").write_text(card_md, encoding="utf-8")

    meta = {
        "protein": args.protein,
        "disease": args.disease,
        "generated_at": datetime.datetime.now().isoformat(timespec="seconds"),
        "model": MODEL,
        "tools_available": [t.__name__ for t in TOOLS],
        "card_markdown": card_md,
    }
    (out_dir / f"{stem}.json").write_text(
        json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"[CausalSentinel] Wrote cards/{stem}.md and cards/{stem}.json")


if __name__ == "__main__":
    main()
