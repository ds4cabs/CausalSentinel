"""Claim-to-source validator — makes hallucination measurable instead of anecdotal.

Rule enforced: any number, rsID, accession or database identifier that appears in the
text the MODEL wrote must also appear somewhere in the tool output for that run. If it
does not, the claim has no source and the run FAILS.

This is deliberately mechanical and slightly blunt. A false alarm costs one look; a
missed fabricated p-value costs the project its credibility.
"""
import json
import re

# Numbers we never flag: they are structural, not claims about data.
SAFE_NUMBERS = {"0", "1", "2", "3", "4", "5", "10", "100", "95", "0.05", "1.0", "2026"}

NUM_RE = re.compile(r"(?<![\w.])[-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?(?![\w])")
RSID_RE = re.compile(r"\brs\d+\b", re.I)
ACC_RE = re.compile(r"\b(?:CHEMBL\d+|ENSG\d+|MONDO_\d+|EFO_\d+|[OPQ][0-9][A-Z0-9]{3}[0-9])\b")


def _haystack(ledger) -> str:
    """Everything the tools returned, as one searchable string."""
    return json.dumps(ledger.results_by_tool(), ensure_ascii=False, default=str)


def _hay_numbers(hay: str):
    """Every numeric literal in the tool output, parsed once, as floats.

    Compared NUMERICALLY, never as substrings. Substring matching is what let a fabricated
    p-value of 1.2e-45 pass: formatted to one decimal it becomes "0.0", which occurs inside
    "0.029369372". Any check that can be fooled that way is worse than no check.
    """
    out = set()
    for m in NUM_RE.finditer(hay):
        try:
            out.add(float(m.group()))
        except ValueError:
            pass
    return out


def _close(a: float, b: float) -> bool:
    """True if the model's number is the tool's number, allowing honest rounding."""
    if a == b:
        return True
    if b == 0:
        return abs(a) < 1e-12
    rel = abs(a - b) / abs(b)
    # 2% covers "0.277" for 0.277233958 and "1.14" for 1.1407...; it does not cover a
    # different value of the same order of magnitude.
    return rel <= 0.02


# "over 250", "more than 100", "nearly 300", "~50" — a round number used as a BOUND, not
# as a reported value. "over 250 associations" when the tool returned 256 is true, and
# flagging it as fabricated trains the writer away from honest hedging.
_LOWER_BOUND = re.compile(r"\b(?:over|more than|greater than|at least|above|exceed\w*|"
                          r"upwards of)\s+(?:approximately\s+|about\s+|~)?(\d[\d,]*\.?\d*)", re.I)
_UPPER_BOUND = re.compile(r"\b(?:under|fewer than|less than|below|no more than|up to)\s+"
                          r"(?:approximately\s+|about\s+|~)?(\d[\d,]*\.?\d*)", re.I)
_APPROX = re.compile(r"(?:~|≈|\babout\b|\bapproximately\b|\bnearly\b|\broughly\b|\bsome\b)\s*"
                     r"(\d[\d,]*\.?\d*)", re.I)


def _bounded_numbers(text: str, nums) -> set:
    """Numbers the model used as a bound/approximation that some tool value satisfies."""
    ok = set()
    for rx, test in (
        (_LOWER_BOUND, lambda v, b: v > b),
        (_UPPER_BOUND, lambda v, b: v < b),
        (_APPROX, lambda v, b: abs(v - b) <= max(abs(b) * 0.15, 1)),
    ):
        for m in rx.finditer(text):
            raw = m.group(1).replace(",", "")
            try:
                b = float(raw)
            except ValueError:
                continue
            if any(test(v, b) for v in nums):
                ok.add(m.group(1))
                ok.add(raw)
    return ok


def _number_supported(tok: str, nums) -> bool:
    """A number is supported only if some tool actually returned that value."""
    if tok in SAFE_NUMBERS:
        return True
    try:
        v = float(tok)
    except ValueError:
        return False
    for b in nums:
        if _close(v, b):
            return True
        # the model may have turned a fraction into a percentage (0.974 -> 97.4)
        if b != 0 and _close(v, b * 100.0):
            return True
    return False


# High-risk QUALITATIVE claims. Numbers are not the only way to fabricate: "approved
# monoclonal antibodies" is a factual claim about the drug landscape, and if no tool said
# it, the model invented it. Each entry is (regex the model wrote, evidence that must be
# present in tool output for it to stand).
QUALITATIVE_CLAIMS = [
    (r"\bmonoclonal antibod\w*\b", r"antibod|mab\b"),
    (r"\bapproved (?:drug|therap|treatment|medication)\w*\b", r"approved|max_phase\D*4|phase.{0,3}4"),
    (r"\bFDA[- ]approved\b", r"approved|max_phase\D*4"),
    (r"\bclinical trial\w*\b", r"trial|phase"),
    (r"\bsmall[- ]molecule\b", r"small.?molecule|inhibitor|SMALL MOLECULE"),
    (r"\bgene therap\w*\b", r"gene therap"),
    (r"\bcolocaliz\w*\b(?!\s*(?:was|is)\s*not)", r"coloc"),
    (r"\bpathogenic variant\w*\b", r"[Pp]athogenic"),
    (r"\bloss[- ]of[- ]function intoleran\w*|LoF[- ]intoleran\w*", r"pLI|LOEUF|intoleran"),
]


# Language that asserts CAUSATION rather than association. Allowed only when the MR tool
# actually returned an estimate for this disease.
CAUSAL_LANGUAGE = re.compile(
    r"\bcausal(?:ly|ity)?\b|\bcauses?\b|\bcausative\b|\bcausal driver\b|"
    r"\bdrives?\s+(?:the\s+)?(?:disease|pathogenesis|risk)\b",
    re.I,
)
# Phrasings that are ABOUT the absence of causal evidence — these must not trip the rule.
# NOTE the `[\w,\s/-]` classes: the first version used `\w+\s+` and so missed
# "no genetic, causal, or pharmacotherapeutic evidence", flagging an honest NO-GO card for
# overclaiming. A rule that punishes correct denials teaches the model to stop denying.
CAUSAL_NEGATED = re.compile(
    r"\bno\b[\w,\s/-]{0,40}?causal|"
    r"\bnot\b[\w,\s/-]{0,30}?causal|"
    # ...and the reverse word order: "causality is NOT established", "causal effect cannot
    # be inferred". The first version only caught negations that preceded the word.
    r"causal\w*[\w,\s/-]{0,40}?\b(?:not|cannot|can't|never|un(?:available|proven|clear))\b|"
    r"causal[\w,\s/-]{0,30}?\b(?:unavailable|absent|missing|lacking)\b|"
    r"\bwithout\b[\w,\s/-]{0,20}?causal|"
    r"\black\w*\b[\w,\s/-]{0,20}?causal|"
    r"\babsence\s+of\b[\w,\s/-]{0,25}?causal|"
    r"\bcannot\b[\w,\s/-]{0,25}?causal|"
    r"\bno\s+(?:MR|mendelian)\b|"
    r"\b(?:MR|mendelian randomi[sz]ation)\s+(?:estimate|evidence|result)s?\s+"
    r"(?:are|is|was|were)?\s*(?:not|un)",
    re.I,
)


def check_evidence_consistency(model_text: str, ledger) -> list:
    """Rules where the model's WORDS must not contradict the tool TABLE.

    The headline rule: an agent whose entire purpose is separating causation from
    association must not call a target 'causal' when its causal-evidence tool returned
    nothing. No number is fabricated in that sentence — which is exactly why the
    token-level checks above cannot see it.
    """
    problems = []
    mr = (ledger.results_by_tool() or {}).get("get_mr_result") or {}
    mr_has_estimate = bool(mr.get("found")) and bool(mr.get("matched_disease_estimates"))

    if not mr_has_estimate:
        hit = CAUSAL_LANGUAGE.search(model_text)
        if hit and not CAUSAL_NEGATED.search(model_text):
            problems.append({
                "kind": "causal-claim-without-mr",
                "token": hit.group(0),
                "detail": ("card asserts causation but get_mr_result returned no estimate "
                           "for this disease"),
            })

    # Claiming this agent performed MR is a standing red line for the project.
    if re.search(r"\b(?:we|this (?:agent|tool)|the (?:agent|tool))\b[^.]{0,60}"
                 r"\b(?:ran|performed|computed|conducted)\b[^.]{0,30}"
                 r"\b(?:MR|mendelian randomi[sz]ation|colocali[sz]ation)\b", model_text, re.I):
        problems.append({"kind": "claims-agent-computed-mr", "token": "performed MR",
                         "detail": "this agent retrieves MR estimates; it never computes them"})
    return problems


def validate(model_text: str, ledger) -> dict:
    """Return {'ok': bool, 'unsupported': [...], 'checked': int} for model-written text."""
    hay = _haystack(ledger)
    unsupported = list(check_evidence_consistency(model_text, ledger))

    for claim_re, evidence_re in QUALITATIVE_CLAIMS:
        m = re.search(claim_re, model_text, re.I)
        if m and not re.search(evidence_re, hay, re.I):
            unsupported.append({"kind": "qualitative-claim", "token": m.group(0)})

    for tok in set(RSID_RE.findall(model_text)):
        if tok.lower() not in hay.lower():
            unsupported.append({"kind": "rsid", "token": tok})

    for tok in set(ACC_RE.findall(model_text)):
        if tok not in hay:
            unsupported.append({"kind": "identifier", "token": tok})

    numbers = set(NUM_RE.findall(model_text))
    hay_nums = _hay_numbers(hay)
    bounded = _bounded_numbers(model_text, hay_nums)
    for tok in numbers:
        if tok in bounded:
            continue
        if not _number_supported(tok, hay_nums):
            unsupported.append({"kind": "number", "token": tok})

    checked = len(numbers) + len(set(RSID_RE.findall(model_text))) + len(set(ACC_RE.findall(model_text)))
    return {"ok": not unsupported, "unsupported": unsupported, "checked": checked}


def format_report(v: dict) -> str:
    if v["ok"]:
        return f"PASS — {v['checked']} claim token(s) checked, all traceable to tool output."
    lines = [f"FAIL — {len(v['unsupported'])} unsupported token(s) of {v['checked']} checked:"]
    for u in v["unsupported"]:
        lines.append(f"    [{u['kind']}] {u['token']}  <- appears nowhere in tool output")
    return "\n".join(lines)
