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


# No tool in this panel returns a development phase, an approval status, or an indication.
# ChEMBL modulator objects carry {drug, action, moa} and nothing else. So ANY sentence about
# clinical status is unearned by construction — no proximity heuristic can rescue it, and a
# hand-written phrase list was walked around every time.
CLINICAL_STATUS = re.compile(
    r"\b(?:approved?|approval|licen[cs]ed|marketed|registrational|standard of care|"
    r"in clinical (?:practice|use)|in the clinic|clinical[- ]stage|late[- ]stage|"
    r"phase\s*(?:i{1,3}v?|[1-4])\b|clinical trials?|efficacy|proven|definitive proof|"
    r"clinically (?:validated|established|proven)|therapeutic legacy|legacy of)\b",
    re.I,
)
# Modality words are allowed only when a ChEMBL action/moa actually says so.
MODALITY = {
    "monoclonal": r"antibod|mab\b", "antibody": r"antibod|mab\b", "biologic": r"antibod|biologic|protein therap",
    "small-molecule": r"small.?molecule|INHIBITOR", "small molecule": r"small.?molecule|INHIBITOR",
    "antisense": r"antisense|ASO", "siRNA": r"rnai|sirna", "RNAi": r"rnai|sirna",
    "gene therapy": r"gene therap", "PROTAC": r"protac", "peptide": r"peptide",
}
# Words that assert a pharmacological ACTION ON THE TARGET.
#
# Deliberately excludes higher/lower/increase/decrease/elevate: in these cards those almost
# always describe the OUTCOME ("higher protein is associated with lower disease risk"), not
# an intervention. An earlier version included them and failed that correct sentence — a
# rule that punishes an accurate description teaches the writer to be vaguer, which is the
# opposite of what this project wants.
DIRECTION_WORDS = re.compile(
    r"\b(inhibit\w*|blockade|blocking|antagoni\w*|suppress\w*|knockdown|silenc\w*|"
    r"agonis\w*|activat\w*|augment\w*|potentiat\w*|stimulat\w*)\b", re.I)
_LOWERING = re.compile(r"^(inhibit|block|antagoni|suppress|knockdown|silenc)", re.I)


def check_direction(model_text: str, ledger) -> list:
    """The sign of beta licenses exactly one direction of pharmacological claim.

    The card that motivated this rule quoted beta = -0.0442 correctly and then recommended
    the opposite intervention, because the model was reciting a remembered conclusion. The
    numbers all checked out; only the biology was backwards.
    """
    mr = (ledger.results_by_tool() or {}).get("get_mr_result") or {}
    ms = mr.get("matched_disease_estimates") or []
    if not ms:
        return []
    # ALL matched estimates, not ms[0]. The first version read only the first row, so when
    # two estimates disagreed in sign the verdict depended on sort order — an arbitrary
    # outcome dressed as a check. With conflicting signs NO drug direction is licensed.
    signs = {(1 if b > 0 else -1) for b in
             (e.get("beta") for e in ms) if isinstance(b, (int, float)) and b != 0}
    if not signs:
        return []
    protein = str(mr.get("protein") or "")
    conflicted = len(signs) > 1
    beta = next(e.get("beta") for e in ms
                if isinstance(e.get("beta"), (int, float)) and e.get("beta") != 0)
    problems = []
    for sent in re.split(r"(?<=[.;])\s+", model_text):
        # Only judge sentences that tie an intervention to a benefit claim about THIS target.
        if not re.search(r"\bMR\b|mendelian|causal|protectiv|therapeutic|benefit", sent, re.I):
            continue
        if protein and protein.lower() not in sent.lower():
            continue
        for m in DIRECTION_WORDS.finditer(sent):
            word = m.group(0)
            if conflicted:
                problems.append({
                    "kind": "direction-claim-on-conflicting-estimates",
                    "token": word,
                    "detail": (f"the matched estimates for {mr.get('protein')} disagree in "
                               f"sign, so NO intervention direction is licensed by this "
                               f"retrieval. Report the conflict itself — and check whether "
                               f"the estimates even measure the same molecular form before "
                               f"explaining it."),
                })
                break
            says_lower = bool(_LOWERING.match(word))
            # beta<0: higher protein -> less disease, so a BENEFIT claim needs RAISING it.
            # beta>0: higher protein -> more disease, so a benefit claim needs LOWERING it.
            licensed_lower = beta > 0
            if says_lower != licensed_lower:
                problems.append({
                    "kind": "direction-contradicts-beta",
                    "token": word,
                    # Worded as PROVENANCE, not biology. IL6R is the reason: its instrument
                    # rs4129267 proxies the Asp358Ala missense variant, which raises shed
                    # soluble receptor while IMPAIRING classical signalling — so "higher
                    # plasma IL6R" and "IL-6R blockade" really are the same direction, and
                    # the card's "inhibition is protective" was pharmacologically right.
                    # It was still unearned: nothing in the retrieved fields carries the
                    # shedding mechanism, so the model supplied it from memory and merely
                    # happened to be correct. This rule must say "your retrieval does not
                    # support this", never "your biology is backwards".
                    "detail": (f"beta={beta:+.4g} describes {mr.get('protein')} PROTEIN "
                               f"ABUNDANCE, and higher abundance goes with "
                               f"{'more' if beta > 0 else 'less'} disease. A claim about "
                               f"'{word}' is a claim about DRUG ACTION, which no retrieved "
                               f"field covers — abundance and pathway activity can even run "
                               f"opposite when the instrument alters shedding, cleavage or "
                               f"receptor decoy behaviour. State the abundance-outcome "
                               f"direction, not a therapeutic one."),
                })
                break
        if problems:
            break
    return problems


# Language that asserts REPLICATION or cross-study agreement. Bare "consistent with X" is
# deliberately NOT here: "consistent with the retrieved estimate" is an honest sentence
# about one estimate, and a rule that fires on it teaches the model to stop comparing its
# words to the data — the CAUSAL_NEGATED lesson again. What needs earning is the claim
# that MULTIPLE studies agree.
REPLICATION_LANGUAGE = re.compile(
    r"\breplicat\w*\b|"
    r"\bindependent(?:ly)?\s+(?:confirm|support|validat|verif)\w*|"
    r"\b(?:consistent|concordant|convergent|converging)\s+across\b|"
    r"\bacross\s+(?:multiple\s+)?(?:studies|cohorts|platforms|datasets)\b|"
    r"\bmultiple\s+(?:independent\s+)?studies\s+(?:agree|show|support|confirm)\w*",
    re.I,
)
REPLICATION_NEGATED = re.compile(
    r"\b(?:not|never|no|cannot|can't|un)\W{0,3}(?:\w+\W{1,3}){0,3}"
    r"(?:replicat|independent|confirm|concordan)|"
    r"\breplicat\w*[\w,\s/-]{0,30}?\b(?:not|cannot|unavailable|absent|missing|lacking|failed)\b",
    re.I,
)
CROSS_PLATFORM_LANGUAGE = re.compile(
    r"\bcross[- ]platform\b|\borthogonal\s+platform\w*|\b(?:both|two)\s+platforms\b", re.I)


def check_concordance(model_text: str, ledger) -> list:
    """Cross-study agreement wording must be earned by the concordance classifier.

    Base rates make the temptation concrete: of 101,543 estimate rows in this resource,
    well under 0.4% carry any of the three validation checks, and every multi-estimate
    protein draws its estimates from ONE study (often as different molecular forms of the
    same gene product). So "replicated across studies" is almost never true here — and a
    model that says it anyway is reciting the literature, not the retrieval.
    """
    problems = []
    hit = REPLICATION_LANGUAGE.search(model_text)
    if hit and not REPLICATION_NEGATED.search(model_text):
        conc = (ledger.results_by_tool() or {}).get("classify_evidence_concordance") or {}
        ec = conc.get("estimate_concordance") or {}
        if not conc:
            problems.append({
                "kind": "concordance-not-in-ledger", "token": hit.group(0),
                "detail": ("the text claims cross-study agreement but no concordance "
                           "classification is in this run — nothing retrieved here "
                           "compares two studies"),
            })
        elif ec.get("direction") == "conflict":
            problems.append({
                "kind": "concordance-contradicts-ledger", "token": hit.group(0),
                "detail": "the classified estimates DISAGREE in sign",
            })
        elif ec.get("direction") != "agree" or (ec.get("n_estimates_compared") or 0) < 2:
            problems.append({
                "kind": "concordance-not-in-ledger", "token": hit.group(0),
                "detail": (f"the classifier found "
                           f"{ec.get('n_estimates_compared', 0)} comparable estimate(s) "
                           f"(direction={ec.get('direction')}) — there is no agreement "
                           f"to report"),
            })
        elif re.search(r"\bindependent", hit.group(0), re.I) and \
                ec.get("independence") != "independent":
            problems.append({
                "kind": "independence-claim-unsupported", "token": hit.group(0),
                "detail": (f"the estimates agree in sign but share a study and/or outcome "
                           f"GWAS (independence={ec.get('independence')}) — sign "
                           f"consistency is not independent replication"),
            })
    m = CROSS_PLATFORM_LANGUAGE.search(model_text)
    if m:
        conc = (ledger.results_by_tool() or {}).get("classify_evidence_concordance") or {}
        if not (conc.get("estimate_concordance") or {}).get("cross_platform"):
            problems.append({
                "kind": "cross-platform-claim-unsupported", "token": m.group(0),
                "detail": ("no two platform classes among the matched estimates — this "
                           "resource is four SomaScan studies and one Olink, so genuinely "
                           "cross-platform agreement is almost never observable in it"),
            })
    return problems


def check_unearned_attributes(model_text: str, ledger) -> list:
    """Clinical status is never retrievable here; modality only if ChEMBL said so."""
    hay = _haystack(ledger)
    out = []
    m = CLINICAL_STATUS.search(model_text)
    if m:
        out.append({"kind": "clinical-status-not-retrievable", "token": m.group(0),
                    "detail": "no tool in this panel returns phase, approval or indication"})
    chembl = json.dumps((ledger.results_by_tool() or {}).get("get_chembl_modulators", {}),
                        default=str)
    for word, evidence in MODALITY.items():
        if re.search(r"\b" + re.escape(word) + r"\b", model_text, re.I) and \
                not re.search(evidence, chembl, re.I):
            out.append({"kind": "modality-not-in-chembl", "token": word,
                        "detail": "no ChEMBL action/moa in this run supports that modality"})
    return out


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

    # An estimate EXISTING is not the same as an estimate being VALIDATED. The IL6R x CHD
    # card asserted "supports a causal ... role" from a single-instrument Wald ratio whose
    # Steiger direction test, LD check and colocalization were all absent — while the LPA
    # card in the same batch, same outcome, same tool, carried steiger=TRUE and ld_check=1.0
    # and got exactly the same strength of wording. The check above cannot see this: MR
    # DID return an estimate, so causal language passed.
    #
    # A one-SNP Wald ratio with no Steiger, no LD check and no coloc cannot distinguish a
    # causal effect from confounding by LD with a neighbouring gene, or from reverse
    # causation. Causal wording on it is unearned, so the run fails and the card must fall
    # back to associational language.
    if mr_has_estimate:
        def _blank(v):
            return v is None or (isinstance(v, str) and v.strip().upper() in {"", "NA", "NAN", "NULL"})
        def _unvalidated(e):
            return (_blank(e.get("steiger_direction_ok"))
                    and _blank(e.get("coloc_prob"))
                    and _blank(e.get("ld_check"))
                    and e.get("n_snp") in (1, "1", 1.0))
        ests = mr.get("matched_disease_estimates") or [{}]
        # Judge the BEST estimate, not the first. The first version read only est[0], so a
        # pair whose second estimate carried Steiger + an LD check was punished as if it
        # had none — the rule fired on sort order, not on evidence.
        if all(_unvalidated(e) for e in ests):
            est = ests[0]
            hit = CAUSAL_LANGUAGE.search(model_text)
            if hit and not CAUSAL_NEGATED.search(model_text):
                problems.append({
                    "kind": "causal-claim-on-unvalidated-estimate",
                    "token": hit.group(0),
                    "detail": (f"every retrieved estimate ({len(ests)}) is a "
                               f"single-instrument Wald ratio with steiger="
                               f"{est.get('steiger_direction_ok')}, coloc="
                               f"{est.get('coloc_prob')}, ld_check={est.get('ld_check')} — "
                               f"none of the three sanity checks that separate a causal "
                               f"effect from LD confounding or reverse causation is "
                               f"available, so causal wording is unearned. Say "
                               f"'associated with' and state which checks are missing."),
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
    unsupported += check_direction(model_text, ledger)
    unsupported += check_concordance(model_text, ledger)
    unsupported += check_unearned_attributes(model_text, ledger)

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
