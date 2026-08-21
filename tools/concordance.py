"""Tool: classify_evidence_concordance — classify what the retrieval sources returned
for one protein-disease pair, and whether multiple estimates actually agree.

WHY THIS EXISTS
---------------
A mentor question, 2026-08-20: the project retrieves MR evidence from three places —
EpiGraphDB's structured estimates, Europe PMC, Semantic Scholar (plus MR-KG inside
litcheck). Sometimes a pair shows up in all of them, sometimes in one, and sometimes one
pair has several estimates that agree in direction, disagree, or differ in how much
validation (Steiger / colocalization / LD) each carries. The card needs to CLASSIFY that
instead of leaving the reader to reconstruct it.

WHAT THE REAL DATA FORCED (censused 2026-08-20 over all 991 dossier caches)
---------------------------------------------------------------------------
1. Literature hits carry NO effect direction. Europe PMC / Semantic Scholar hits are
   pmid + title + year + a topical verdict; MR-KG's structured pair is the only
   direction-shaped literature object and it is not yet surfaced per-paper with betas.
   So cross-source direction agreement is NOT computable, and this module never claims
   it — axis 2 is EpiGraphDB-internal only, and `literature_direction` is always None.
2. Multiplicity inside EpiGraphDB is not replication. Every protein with >=2 exposure
   datasets (16 proteins, 41 datasets) draws them from ONE study (Suhre 2019), usually as
   different molecular forms of the same gene product: C3 -> C3/C3a/C3b/C3d/iC3b;
   PROC -> zymogen vs activated; CGA -> four hormones sharing one subunit. Two such
   estimates agreeing is not two studies agreeing, and their conflicting is fragment
   biology before it is a platform artefact. Hence the independence gate and the
   analyte-identity note below.
3. Validation is vanishingly rare: of 101,543 estimate rows, coloc_prob is non-null on
   0.19%, steiger_p on 0.35%, ld_check on 0.16%. "Validated" is therefore a per-estimate
   ANNOTATION here (depth 0-4), not a class most pairs could ever join.

The classification is computed here, by fixed rules, with no model anywhere in the path.
The MR estimates it reads remain retrieved, never computed — same as everywhere else.
"""
try:
    from .mr import get_instrument_provenance, get_mr_result
except ImportError:                       # running standalone: python tools/concordance.py
    from mr import get_instrument_provenance, get_mr_result

_BLANKS = {"", "NA", "NAN", "NULL", "NONE"}


def _blank(v) -> bool:
    return v is None or (isinstance(v, str) and v.strip().upper() in _BLANKS)


def _sign(beta):
    if beta is None:
        return None
    try:
        b = float(beta)
    except (TypeError, ValueError):
        return None
    return 0 if b == 0 else (1 if b > 0 else -1)


def _validation_depth(est: dict) -> dict:
    """Per-estimate annotation: which of the four validation signals are present."""
    signals = {
        "multi_snp": not _blank(est.get("n_snp")) and est.get("n_snp") not in (1, "1", 1.0),
        "steiger": not _blank(est.get("steiger_direction_ok")) or not _blank(est.get("steiger_p")),
        "coloc": not _blank(est.get("coloc_prob")),
        "ld_check": not _blank(est.get("ld_check")),
    }
    return {**signals, "depth": sum(signals.values())}


def _coverage_state(published, count) -> str:
    """present / queried_empty / not_checked for one literature source."""
    if not isinstance(published, dict) or published.get("error"):
        return "not_checked"
    if count is None:
        return "not_checked"
    return "present" if count else "queried_empty"


def classify_evidence_concordance(protein: str,
                                  disease: str,
                                  mr_result: dict | None = None,
                                  provenance: dict | None = None,
                                  published: dict | None = None) -> dict:
    """Classify retrieval coverage (axis 1) and estimate concordance (axis 2) for a pair.

    Pass the dicts already captured in a ledger to reuse them; leave mr_result/provenance
    as None to fetch live. `published` (get_published_mr output) is NEVER fetched here —
    it costs tens of seconds and a stack of model calls, so the caller decides. When it
    is absent every literature source is honestly reported as "not_checked".
    """
    if mr_result is None:
        mr_result = get_mr_result(protein, disease)

    # ---- axis 1: what did each source return for this pair? ----------------------
    if not isinstance(mr_result, dict) or mr_result.get("error"):
        epi_state = "error"
    elif mr_result.get("found") and mr_result.get("matched_disease_estimates"):
        epi_state = "pair_matched"
    elif mr_result.get("n_outcomes_available"):
        # TREM2 x Alzheimer's is the worked example: 51 outcomes, none of them the asked
        # disease. Epistemically different from "no instrument" — this is a coverage gap,
        # not a negative probe — so it gets its own state instead of collapsing into one.
        epi_state = "instrument_exists_disease_unmatched"
    else:
        epi_state = "no_instrument"

    coverage = {
        "epigraphdb": epi_state,
        "europe_pmc": _coverage_state(published,
                                      (published or {}).get("n_epmc_reported_total")),
        "semantic_scholar": _coverage_state(published,
                                            (published or {}).get("n_semantic_scholar_extra")),
        "mr_kg": _coverage_state(published,
                                 (published or {}).get("n_mrkg_studies_seen")),
        # Stated outright rather than left to be inferred: literature hits carry no betas,
        # so no direction can be read from them today.
        "literature_direction": None,
    }

    ests = (mr_result.get("matched_disease_estimates") or []) if isinstance(mr_result, dict) else []
    depths = [_validation_depth(e) for e in ests]
    notes = []

    # ---- axis 2: do the matched estimates agree? (EpiGraphDB-internal ONLY) -------
    signs = [s for s in (_sign(e.get("beta")) for e in ests) if s is not None]
    if len(ests) == 0:
        direction = "no_estimate"
    elif len(ests) == 1:
        direction = "single_estimate"
    elif len(set(signs)) <= 1:
        direction = "agree"
    else:
        direction = "conflict"

    # Independence gate: agreement between two estimates only means something if they do
    # not share their exposure study AND their outcome GWAS. In the current resource the
    # multiplicity that exists never clears this bar, and the label must say so.
    independence = "not_assessable"
    cross_platform = False
    if len(ests) >= 2:
        if provenance is None:
            provenance = get_instrument_provenance(protein)
        author_by_rsid, class_by_rsid = {}, {}
        if isinstance(provenance, dict) and provenance.get("found"):
            for inst in provenance.get("instruments") or []:
                rsid = inst.get("instrument_rsid")
                author_by_rsid.setdefault(rsid, set()).add(inst.get("exposure_study_author"))
                if inst.get("platform_class"):
                    class_by_rsid.setdefault(rsid, set()).add(inst.get("platform_class"))
        authors, outcomes, classes = [], set(), set()
        for e in ests:
            rsid = e.get("instrument_rsid")
            authors.append(author_by_rsid.get(rsid, set()))
            outcomes.add(e.get("outcome_gwas_id"))
            classes |= class_by_rsid.get(rsid, set())
        cross_platform = len(classes) >= 2
        if any(not a for a in authors):
            independence = "not_assessable"
            notes.append("Exposure-study identity could not be resolved for every "
                         "instrument, so independence between estimates is not assessable.")
        else:
            distinct_authors = set().union(*authors)
            if len(distinct_authors) >= 2 and len(outcomes) >= 2:
                independence = "independent"
            else:
                independence = "non_independent"
                notes.append("The matched estimates share an exposure study and/or an "
                             "outcome GWAS — agreement between them is NOT independent "
                             "replication. Do not describe it as such.")
        # Analyte-identity lens BEFORE any platform/epitope story: in this resource,
        # same-study multiplicity usually means different molecular forms of the protein.
        notes.append(f"Multiple estimates from one study may measure different molecular "
                     f"forms of {protein} (cleavage fragments, activation states, shared "
                     f"subunits). Check the analyte names before calling this replication "
                     f"— or, if signs conflict, before calling it a platform artefact.")

    label = direction
    if direction == "agree" and independence != "independent":
        label = "sign_consistent_non_independent"

    if direction == "conflict":
        notes.append("Estimate signs CONFLICT. First ask whether the two analytes are the "
                     "same molecule at all; only then consider platform or epitope "
                     "explanations (see classify_exposure_mechanism).")
    if not cross_platform and len(ests) >= 2:
        notes.append("All matched estimates come from the same platform class — this "
                     "resource holds four SomaScan studies and one Olink, so genuinely "
                     "cross-platform agreement is almost never observable in it.")

    note = " ".join(notes) if notes else (
        "Nothing to compare: fewer than two matched estimates." if len(ests) < 2 else None)

    return {
        "found": epi_state == "pair_matched" or coverage["europe_pmc"] == "present",
        # The CLASSIFICATION is computed here by fixed rules, with no model in the path.
        # The MR estimates it reads remain retrieved, never computed by this agent.
        "computed_here": True,
        "classifier": "rule-based; no LLM anywhere in this path",
        "protein": protein,
        "disease": disease,
        "retrieval_coverage": coverage,
        "estimate_concordance": {
            "n_estimates_compared": len(ests),
            "direction": direction,
            "independence": independence,
            "label": label,
            "cross_platform": cross_platform,
            "validation_depth_per_estimate": [d["depth"] for d in depths],
            "best_validation_depth": max((d["depth"] for d in depths), default=0),
            "validation_signals": depths,
        },
        "note": note,
        "url": "https://epigraphdb.org/pqtl/",
        "source_release": mr_result.get("source_release") if isinstance(mr_result, dict) else None,
    }


if __name__ == "__main__":
    import json
    import sys
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    # Four pairs, four different classifications:
    #   LPA x CHD        pair_matched, single estimate, depth 2 (steiger + ld_check)
    #   IL6R x CHD       pair_matched, single estimate, depth 0 (the unvalidated exemplar)
    #   TREM2 x AD       instrument_exists_disease_unmatched (51 outcomes, none AD)
    #   PNPLA3 x MASLD   no_instrument (the honest empty probe)
    for prot, dis in [("LPA", "coronary heart disease"),
                      ("IL6R", "coronary heart disease"),
                      ("TREM2", "Alzheimer disease"),
                      ("PNPLA3", "MASLD")]:
        r = classify_evidence_concordance(prot, dis)
        keep = {k: r[k] for k in ("protein", "disease", "retrieval_coverage",
                                  "estimate_concordance", "note")}
        print("=" * 70)
        print(json.dumps(keep, indent=2, ensure_ascii=False)[:1500])
