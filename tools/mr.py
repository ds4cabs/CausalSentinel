"""Tool: get_mr_result — retrieve PUBLISHED Mendelian randomization estimates for a
protein's effect on disease outcomes, from EpiGraphDB's pQTL resource.

WHAT THIS IS, PRECISELY
-----------------------
This tool **retrieves** two-sample MR estimates that were computed by others and
published (Zheng et al., *Nature Genetics* 2020; served by EpiGraphDB). It does
**NOT** run Mendelian randomization here — no instrument selection, no harmonisation,
no colocalization is performed by this agent. Every returned estimate carries
`computed_here: False` so a card can never imply otherwise.

COVERAGE IS PARTIAL AND THAT MATTERS
------------------------------------
The resource only covers proteins that had usable plasma pQTL instruments in the
source datasets. Many genes — PNPLA3, HMGCR, APOE, TNF, SORT1 among them — have
**no** entry. For those the tool returns `found: False`, which the card must print as
"not available". An absent estimate is not a null effect.
"""
import difflib
import requests

PQTL_API = "https://api.epigraphdb.org/pqtl/"
BUILDS_API = "https://api.epigraphdb.org/builds"
_SOURCE_BASE = ("EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; "
                "retrieved, not computed by this agent")


def _source_release() -> str:
    """Pin the EpiGraphDB build so the estimate can be traced to a version, not a date."""
    try:
        b = requests.get(BUILDS_API, timeout=15).json()
        return (f"{_SOURCE_BASE}; EpiGraphDB build {b.get('epigraphdb', {}).get('overall')}, "
                f"pQTL dataset v{b.get('pqtl')}")
    except Exception:
        return _SOURCE_BASE


SOURCE = _SOURCE_BASE
# Loosened from the API default (0.5) so we can see and report non-significant results too;
# the card is expected to weigh the p-values, not to be handed a pre-filtered rosy subset.
PVALUE_CEILING = 0.5


def _norm(s: str) -> str:
    return "".join(ch.lower() for ch in (s or "") if ch.isalnum() or ch.isspace()).strip()


# Common disease aliases so "MASLD" can match "fatty liver disease" style trait strings.
ALIASES = {
    "masld": ["fatty liver", "nafld", "steatotic liver", "steatosis", "liver"],
    "nafld": ["fatty liver", "masld", "steatotic liver", "steatosis", "liver"],
    "cad": ["coronary", "heart disease", "myocardial", "ischaemic heart", "ischemic heart"],
    "chd": ["coronary", "heart disease"],
    "coronary artery disease": ["coronary", "heart disease", "myocardial"],
    "t2d": ["type 2 diabetes", "diabetes"],
    "type 2 diabetes": ["diabetes"],
    "ibd": ["inflammatory bowel", "crohn", "colitis"],
    "ra": ["rheumatoid"],
    "ldl": ["ldl", "cholesterol", "lipid"],
    "hypercholesterolemia": ["cholesterol", "lipid"],
    "obesity": ["body mass index", "bmi", "body fat", "obesity"],
    "alzheimer": ["alzheimer", "dementia"],
    "asthma": ["asthma"],
}


def _disease_match(disease: str, out_id: str) -> float:
    """0..1 crude relevance of a returned outcome trait to the requested disease."""
    d, o = _norm(disease), _norm(out_id)
    if not d or not o:
        return 0.0
    if d in o:
        return 1.0
    for alias in ALIASES.get(d, []):
        if _norm(alias) in o:
            return 0.9
    # token overlap
    dt, ot = set(d.split()), set(o.split())
    if dt and dt <= ot:
        return 0.85
    overlap = len(dt & ot) / max(1, len(dt))
    fuzzy = difflib.SequenceMatcher(None, d, o).ratio()
    return max(overlap * 0.7, fuzzy * 0.6)


def _slim(row: dict) -> dict:
    """Keep the fields a causal claim actually rests on."""
    return {
        "outcome": row.get("outID"),
        "outcome_gwas_id": row.get("outID_mrbase"),
        "beta": row.get("beta"),
        "se": row.get("se"),
        "p_value": row.get("pvalue"),
        "method": row.get("method"),
        "n_snp": row.get("nsnp"),
        "instrument_rsid": row.get("rsID"),
        "cis_or_trans": row.get("trans_cis"),
        "steiger_direction_ok": row.get("direction"),
        "steiger_p": row.get("steiger_pvalue"),
        "coloc_prob": row.get("coloc_prob"),
        "heterogeneity_q_p": row.get("q_pvalue"),
        "ld_check": row.get("ld_check"),
    }


def get_mr_result(protein: str, disease: str) -> dict:
    """Retrieve published Mendelian randomization (MR) estimates for a protein's causal
    effect on disease outcomes, from the EpiGraphDB pQTL resource.

    Use this to judge whether the protein has evidence of a CAUSAL effect on the disease
    rather than a mere correlation. Inputs: protein (gene symbol, e.g. PCSK9 or IL6R) and
    disease name (e.g. 'coronary heart disease').

    IMPORTANT: these estimates are RETRIEVED from published work, not computed here. Many
    proteins have no pQTL instrument in this resource and will return found=false — that
    means "no estimate available", NOT "no effect".
    """
    try:
        r = requests.get(
            PQTL_API,
            params={"query": protein, "rtype": "simple",
                    "pvalue": PVALUE_CEILING, "searchflag": "proteins"},
            headers={"Accept": "application/json"},
            timeout=45,
        )
        r.raise_for_status()
        rows = r.json().get("results", []) or []
    except requests.RequestException as e:
        return {"error": f"EpiGraphDB pQTL request failed: {e}", "computed_here": False}
    except ValueError as e:
        return {"error": f"EpiGraphDB pQTL returned non-JSON: {e}", "computed_here": False}

    if not rows:
        return {
            "found": False,
            "computed_here": False,
            "protein": protein,
            "disease": disease,
            "note": (f"No pQTL-based MR estimate for {protein} in the EpiGraphDB pQTL resource. "
                     f"This resource only covers proteins with usable plasma pQTL instruments. "
                     f"ABSENCE OF AN ESTIMATE IS NOT EVIDENCE OF NO EFFECT."),
            "source_release": _source_release(),
            "url": "https://epigraphdb.org/pqtl/",
        }

    scored = sorted(
        ({**_slim(x), "_match": _disease_match(disease, x.get("outID", ""))} for x in rows),
        key=lambda d: (-d["_match"], d["p_value"] if d["p_value"] is not None else 1.0),
    )
    matched = [dict(d) for d in scored if d["_match"] >= 0.6]
    for d in scored:
        d.pop("_match", None)

    out = {
        "found": bool(matched),
        "computed_here": False,
        "protein": protein,
        "disease": disease,
        "n_outcomes_available": len(rows),
        "matched_disease_estimates": [{k: v for k, v in m.items() if k != "_match"} for m in matched],
        "other_outcomes_for_this_protein": scored[: 12 if matched else 8],
        "source_release": _source_release(),
        "url": "https://epigraphdb.org/pqtl/",
    }
    if matched:
        out["note"] = ("Estimates RETRIEVED from published pQTL MR, not computed by this agent. "
                       "Check cis_or_trans (cis instruments are less pleiotropy-prone), "
                       "steiger_direction_ok, and coloc_prob before treating this as causal; "
                       "coloc_prob=null means colocalization was not available for this pair.")
    else:
        out["note"] = (f"{protein} HAS pQTL MR estimates in this resource, but NONE matched the "
                       f"requested disease '{disease}'. The other outcomes are listed for context "
                       f"only — do not present them as evidence about '{disease}'.")
    return out


def get_mr_outcomes(protein: str) -> dict:
    """Retrieve ALL published pQTL-MR outcomes for a protein (no disease filter).

    Library entry point for proteome-wide sweeps: returns every outcome with an estimate,
    sorted by p-value. Same source and same honesty rules as get_mr_result — retrieved,
    never computed here.
    """
    try:
        r = requests.get(
            PQTL_API,
            params={"query": protein, "rtype": "simple",
                    "pvalue": PVALUE_CEILING, "searchflag": "proteins"},
            headers={"Accept": "application/json"},
            timeout=45,
        )
        r.raise_for_status()
        rows = r.json().get("results", []) or []
    except requests.RequestException as e:
        return {"error": f"EpiGraphDB pQTL request failed: {e}", "computed_here": False}
    except ValueError as e:
        return {"error": f"EpiGraphDB pQTL returned non-JSON: {e}", "computed_here": False}

    slim = sorted((_slim(x) for x in rows),
                  key=lambda d: d["p_value"] if d["p_value"] is not None else 1.0)
    return {
        "found": bool(slim),
        "computed_here": False,
        "protein": protein,
        "n_outcomes": len(slim),
        "outcomes": slim,
        "note": (None if slim else
                 f"No pQTL MR estimates for {protein} in this resource. "
                 f"ABSENCE OF AN ESTIMATE IS NOT EVIDENCE OF NO EFFECT."),
        "source_release": _source_release(),
        "url": "https://epigraphdb.org/pqtl/",
    }


if __name__ == "__main__":
    import json
    for prot, dis in [("PCSK9", "high cholesterol"), ("IL6R", "coronary heart disease"),
                      ("PNPLA3", "MASLD")]:
        print("=" * 70)
        print(json.dumps(get_mr_result(prot, dis), indent=2, ensure_ascii=False)[:1200])
