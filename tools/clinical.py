"""Tool: get_clinical_evidence — what the CLINIC already knows about this target,
from Open Targets' drug and clinical-candidate records (ChEMBL + trial registries).

WHY THIS EXISTS
---------------
The card answered "should this target be pursued?" while being structurally blind to the
question every reader asks next: has anyone already TRIED? This tool closes that gap with
retrieved facts: which drugs exist against the target, the maximum clinical stage each
reached (up to APPROVAL), and per-trial records including status and — where registries
state it — why a trial stopped.

THE ONE READING RULE THAT MATTERS
---------------------------------
**Phase and status say that trials EXIST, not that they worked.** A COMPLETED phase-3
trial can be a failed one: ziltivekimab's ZEUS completed in 2026 and missed its primary
endpoint. Failure information lives only in why-stopped fields (often blank) and in the
absence of an approval; success information lives only in approval itself, which carries
a regulator's efficacy judgement. Nothing here licenses the word "efficacy" — the
validator enforces that.

Registries also lag reality: results announced by press release can take a data release
or more to appear here. An up-to-date-looking record is still a snapshot.
"""
import requests

try:
    from .opentargets import OT_URL, _SEARCH, _gql, _release
    from .mr import _disease_match, _norm
except ImportError:                        # running standalone: python tools/clinical.py
    from opentargets import OT_URL, _SEARCH, _gql, _release
    from mr import _disease_match, _norm

# Clinical registries name diseases differently from GWAS outcome strings ("high
# cholesterol" arrives as "Hypercholesterolemia" or "hyperlipidemia"). These probes
# SUPPLEMENT mr.py's matcher locally instead of editing its ALIASES, because widening
# that table would silently change which MR estimates every existing card matches —
# a behaviour change this tool has no business smuggling in.
_CLINICAL_PROBES = {
    "high cholesterol": ["hypercholesterolemia", "hyperlipidemia", "dyslipidemia"],
    "hypercholesterolemia": ["hyperlipidemia", "dyslipidemia"],
    "coronary heart disease": ["coronary artery", "cardiovascular", "myocardial",
                               "atheroscler", "ischemic heart", "ischaemic heart"],
    "coronary artery disease": ["cardiovascular", "atheroscler"],
    "masld": ["nonalcoholic fatty liver", "steatohepatitis", "nash", "steatotic liver"],
    "nafld": ["steatohepatitis", "nash", "steatotic liver"],
}
# mr.py's ALIASES include bare tokens like "liver" — harmless against GWAS outcome
# strings, but against registry disease names they match the wrong ETIOLOGY: a review
# caught MASLD scoring 0.90 against "alcoholic liver disease", "liver cirrhosis" and
# "liver neoplasm". These veto a match unless a specific positive probe also hit.
_CLINICAL_EXCLUDES = {
    "masld": ["alcoholic", "cirrhosis", "neoplasm", "carcinoma", "cancer",
              "hepatitis b", "hepatitis c", "biliary"],
    "nafld": ["alcoholic", "cirrhosis", "neoplasm", "carcinoma", "cancer",
              "hepatitis b", "hepatitis c", "biliary"],
}


def _clinical_match(disease: str, name: str) -> float:
    """Symmetric match plus registry-vocabulary probes, minus wrong-etiology vetoes."""
    if not name:
        return 0.0
    score = max(_disease_match(disease, name), _disease_match(name, disease))
    n = _norm(name)
    d = _norm(disease)
    probe_hit = False
    for probe in _CLINICAL_PROBES.get(d, []):
        if _norm(probe) in n:
            score = max(score, 0.85)
            probe_hit = True
    if not probe_hit:
        for veto in _CLINICAL_EXCLUDES.get(d, []):
            # "nonalcoholic fatty liver disease" contains "alcoholic"; the positive
            # probe catches the nonalcoholic form first, so a veto here is genuine.
            if _norm(veto) in n:
                return min(score, 0.4)
    return score

_CANDIDATES = """
query($ensemblId: String!) {
  target(ensemblId: $ensemblId) {
    approvedSymbol
    drugAndClinicalCandidates {
      count
      rows {
        maxClinicalStage
        drug { id name }
        diseases { disease { id name } }
        clinicalReports {
          clinicalStage trialOverallStatus trialWhyStopped trialStopReasonCategories year
          diseases { disease { name } }
        }
      }
    }
  }
}
"""

# The LIVE Open Targets enum, verified against the API 2026-08-21 — an earlier draft
# guessed "PHASE_1_EARLY" (real value: EARLY_PHASE_1) and omitted the combined stages,
# so PHASE_1_2 / PHASE_2_3 / PREAPPROVAL all ranked below everything. Combined stages
# rank between their components; APPROVAL outranks all. Keep in sync with the copy in
# validate_card.py (_VSTAGES).
_STAGE_ORDER = ["PRECLINICAL", "EARLY_PHASE_1", "PHASE_1", "PHASE_1_2", "PHASE_2",
                "PHASE_2_3", "PHASE_3", "PREAPPROVAL", "PHASE_4", "APPROVAL"]


def _stage_rank(stage) -> int:
    try:
        return _STAGE_ORDER.index(str(stage))
    except ValueError:
        return -1


def _summarise_reports(reports: list, disease: str) -> dict:
    """Counts, not a dump — and stage attribution at the REPORT level.

    The first version reported the DRUG's maxClinicalStage next to a disease-level match,
    which let tocilizumab (approved for rheumatoid arthritis, trialled for cardiovascular
    safety) read as "APPROVAL for coronary heart disease". A drug's stage for THIS
    disease may only come from trial reports that are actually about this disease.
    """
    reports = reports or []
    stopped = [r for r in reports if r.get("trialWhyStopped") or
               r.get("trialStopReasonCategories")]
    cats = {}
    for r in stopped:
        for c in (r.get("trialStopReasonCategories") or []):
            cats[c] = cats.get(c, 0) + 1
    years = [r.get("year") for r in reports if r.get("year")]
    example = next((r.get("trialWhyStopped") for r in stopped if r.get("trialWhyStopped")),
                   None)

    this_disease = [
        r for r in reports
        if any(_clinical_match(disease, ((d or {}).get("disease") or {}).get("name") or "")
               >= 0.6 for d in (r.get("diseases") or []))
    ]
    stages_here = [r.get("clinicalStage") for r in this_disease if r.get("clinicalStage")]
    stopped_here = [r for r in this_disease if r.get("trialWhyStopped") or
                    r.get("trialStopReasonCategories")]
    cats_here = {}
    for r in stopped_here:
        for c in (r.get("trialStopReasonCategories") or []):
            cats_here[c] = cats_here.get(c, 0) + 1
    example_here = next((r.get("trialWhyStopped") for r in stopped_here
                         if r.get("trialWhyStopped")), None)
    # Two denominators, named so they cannot be mixed: a review caught the card showing
    # "5 trial reports, 52 with a stop reason" for tocilizumab x CHD — 5 was this-disease,
    # 52 was all 427 all-indication reports. Every count says which universe it counts.
    return {
        "n_reports_this_disease": len(this_disease),
        "max_stage_this_disease": (max(stages_here, key=_stage_rank)
                                   if stages_here else None),
        "n_stop_this_disease": len(stopped_here),
        "stop_reason_categories_this_disease": cats_here or None,
        "example_why_stopped_this_disease": (str(example_here)[:160]
                                             if example_here else None),
        "n_reports_any_disease": len(reports),
        "n_stop_any_disease": len(stopped),
        "stop_reason_categories_any_disease": cats or None,
        "example_why_stopped_any_disease": (str(example)[:160] if example else None),
        "latest_report_year_any_disease": max(years) if years else None,
    }


def get_clinical_evidence(protein: str, disease: str) -> dict:
    """Retrieve the clinical development record for drugs against this protein target:
    which drugs exist, the maximum clinical stage each reached (up to approval), and
    per-trial counts including why-stopped reasons where registries state them.

    Use this to answer "has the clinic already tried this target, and how far did it
    get?" for the given disease. Inputs: protein (gene symbol) and disease name.

    IMPORTANT: phase and trial status mean trials EXIST, not that they succeeded — a
    completed phase-3 trial can be a failed one. Stages reached for OTHER diseases are
    context about the drug, not evidence about this disease.
    """
    try:
        hits = _gql(_SEARCH, {"q": protein, "e": ["target"]})["data"]["search"]["hits"]
    except (requests.RequestException, ValueError, KeyError) as e:
        return {"error": f"Open Targets search failed: {e}", "computed_here": False}
    if not hits:
        return {"found": False, "protein": protein, "computed_here": False,
                "note": f"Could not resolve target '{protein}' in Open Targets."}
    ensembl_id = hits[0]["id"]

    try:
        data = _gql(_CANDIDATES, {"ensemblId": ensembl_id})["data"]["target"]
    except (requests.RequestException, ValueError, KeyError, TypeError) as e:
        return {"error": f"Open Targets clinical-candidates query failed: {e}",
                "computed_here": False}
    if not data:
        return {"found": False, "protein": protein, "computed_here": False,
                "note": f"No Open Targets record for {ensembl_id}."}

    rows = (data.get("drugAndClinicalCandidates") or {}).get("rows") or []
    matched, others = [], []
    for row in rows:
        names = [((d or {}).get("disease") or {}).get("name") or ""
                 for d in (row.get("diseases") or [])]
        best = max((_clinical_match(disease, n) for n in names), default=0.0)
        summary = _summarise_reports(row.get("clinicalReports"), disease)
        entry = {
            "drug": (row.get("drug") or {}).get("name"),
            "chembl_id": (row.get("drug") or {}).get("id"),
            # The drug's ceiling across ALL its indications — context, not evidence
            # about the asked disease. The per-disease stage lives in the summary.
            "max_stage_any_disease": row.get("maxClinicalStage"),
            "diseases": [n for n in names if n][:6],
            **summary,
        }
        # A drug counts for THIS disease only if a report about this disease exists or
        # the row-level indication list names it.
        if best >= 0.6 or summary["n_reports_this_disease"]:
            matched.append(entry)
        else:
            others.append(entry)
    matched.sort(key=lambda m: (_stage_rank(m.get("max_stage_this_disease")),
                                m.get("n_reports_this_disease", 0)), reverse=True)
    others.sort(key=lambda m: _stage_rank(m.get("max_stage_any_disease")), reverse=True)

    if not rows:
        return {
            "found": False,
            "computed_here": False,
            "protein": protein,
            "disease": disease,
            "ensembl_id": ensembl_id,
            "note": (f"No drug or clinical candidate against {protein} in Open Targets. "
                     f"An empty clinical record means the clinic has not filed results "
                     f"against this target — NOT that the target is bad, and not that "
                     f"nothing was ever tried outside registries."),
            "url": f"https://platform.opentargets.org/target/{ensembl_id}",
            "source_release": _release(),
        }

    stages = [r.get("maxClinicalStage") for r in rows]
    max_any = max(stages, key=_stage_rank, default=None)
    max_matched = max((m.get("max_stage_this_disease") for m in matched),
                      key=_stage_rank, default=None)

    note = ("Phase and trial status mean trials EXIST, not that they worked — a "
            "COMPLETED phase-3 trial can be a failed one; only why-stopped fields carry "
            "failure information, and only approval carries a regulator's efficacy "
            "judgement. Registries lag press releases by a data release or more.")
    if others and not matched:
        note += (f" All {len(others)} drug programme(s) target OTHER diseases — their "
                 f"clinical stages are context about the drugs, not evidence "
                 f"about '{disease}'.")

    return {
        "found": True,
        "computed_here": False,
        "protein": protein,
        "disease": disease,
        "ensembl_id": ensembl_id,
        "n_drug_programmes": (data.get("drugAndClinicalCandidates") or {}).get("count"),
        "max_stage_any_disease": max_any,
        "max_stage_this_disease": max_matched,
        "drugs_for_this_disease": matched[:8],
        "drugs_other_diseases_context_only": others[:6],
        "note": note,
        "url": f"https://platform.opentargets.org/target/{ensembl_id}",
        "source_release": (_release() + "; drugAndClinicalCandidates "
                           "(ChEMBL + trial registries via Open Targets)"),
    }


if __name__ == "__main__":
    import json
    import sys
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    # Three deliberately different shapes:
    #   PCSK9 x high cholesterol   should reach APPROVAL for the matched disease
    #   IL6R  x coronary heart d.  drugs exist, but the matched-disease stage is the story
    #   PNPLA3 x MASLD             expect an honest empty record
    for prot, dis in [("PCSK9", "high cholesterol"),
                      ("IL6R", "coronary heart disease"),
                      ("PNPLA3", "MASLD")]:
        r = get_clinical_evidence(prot, dis)
        slim = {k: v for k, v in r.items()
                if k in ("protein", "disease", "found", "n_drug_programmes",
                         "max_stage_any_disease", "max_stage_this_disease", "note")}
        slim["drugs_for_this_disease"] = [
            {kk: d[kk] for kk in ("drug", "max_stage_this_disease", "max_stage_any_disease",
                                  "n_reports_this_disease", "n_stop_this_disease")}
            for d in (r.get("drugs_for_this_disease") or [])[:4]]
        print("=" * 70)
        print(json.dumps(slim, indent=2, ensure_ascii=False)[:1400])
