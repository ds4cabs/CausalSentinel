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

# ---------------------------------------------------------------------------------
# WHICH STUDY, ON WHICH ASSAY — and why this is not a cosmetic detail
# ---------------------------------------------------------------------------------
# `rtype=simple` gives the estimate but never says WHERE the exposure GWAS came from.
# `rtype=inst` does: it carries author_exp, sample_exp, effect allele and allele
# frequency. That matters because affinity-based proteomics measures BINDING, and a
# missense variant in the measured protein can change binding without changing
# abundance — the "epitope effect". Published comparisons find a third of proteins
# with cis-pQTLs on two platforms carry a missense variant, and dozens show OPPOSITE
# effect directions between platforms for the same variant.
#
# IL6R is the worked example. Its instrument rs4129267 is a near-perfect proxy
# (r2 ~ 0.96-0.99 in Europeans) for rs2228145 / Asp358Ala, a MISSENSE variant in the
# assayed protein itself. There is independent wet-lab evidence that the 358Ala allele
# genuinely raises soluble IL6R by accelerating ADAM-mediated shedding, so here the
# signal is real biology rather than an artefact — but nothing in the retrieved fields
# lets a reader tell those two apart. Surfacing the study and the platform is what
# makes that judgement possible at all.
#
# MASS SPECTROMETRY IS THE MISSING ARBITER
# ----------------------------------------
# There are three ways to measure a plasma protein, and only two of them are here:
#
#   affinity_aptamer   SomaScan   — a SOMAmer binds the protein
#   affinity_antibody  Olink PEA  — an antibody pair binds the protein
#   mass_spectrometry             — peptides are identified and counted directly
#
# The first two measure BINDING. Mass spectrometry does not, which makes it the natural
# referee for the epitope question: a cis-pQTL that replicates on MS is about abundance,
# one that appears only on affinity platforms is suspect.
#
# Surveyed 2026-08-16 across 25 proteins, the EpiGraphDB pQTL resource draws on exactly
# five exposure studies: Sun (n=3301), Yao (n=6861), Suhre (n~995), Emilsson (n=3200),
# Folkersen (n=3394). Four SomaScan, one Olink. **No mass-spectrometry study is present.**
# So within this resource the epitope question cannot be adjudicated at all — the tool
# should say that rather than let a reader assume "protein level" means abundance.
#
# There are only a handful of European plasma-proteomics resources, so author -> platform
# is a short lookup rather than a research project. (EpiGraphDB spells Folkersen without
# the second "e"; both spellings are mapped.)
APTAMER = "SomaScan — modified-aptamer (SOMAmer) affinity assay"
ANTIBODY = "Olink PEA — antibody-based proximity extension assay"
ASSAY_BY_AUTHOR = {
    "folkerson": ("Folkersen et al. 2017 (PLoS Genet), IMPROVE / CVD-I panel",
                  ANTIBODY, "affinity_antibody"),
    "folkersen": ("Folkersen et al. 2017 (PLoS Genet), IMPROVE / CVD-I panel",
                  ANTIBODY, "affinity_antibody"),
    "sun": ("Sun et al. 2018 (Nature), INTERVAL", APTAMER, "affinity_aptamer"),
    # Suhre's discovery cohort is KORA F4 (n~1000), replicated in QMDiab (n=338). The
    # sample size EpiGraphDB reports (~995) is KORA, not QMDiab — an earlier version of
    # this table named the replication cohort as though it were the source.
    "suhre": ("Suhre et al. 2017 (Nat Commun), KORA F4 (replicated in QMDiab)",
              APTAMER, "affinity_aptamer"),
    "emilsson": ("Emilsson et al. 2018 (Science), AGES-Reykjavik", APTAMER, "affinity_aptamer"),
    "yao": ("Yao et al. 2018 (Nat Commun), Framingham Heart Study", APTAMER, "affinity_aptamer"),
}
_ASSAY_NOTE = ("Aptamer and antibody platforms both measure BINDING, not abundance. If the "
               "instrument is (or proxies) a missense variant in this same protein, the "
               "pQTL may reflect altered reagent binding rather than a real change in "
               "protein level. Mass spectrometry would settle it because it counts peptides "
               "instead of binding them — but NO mass-spectrometry study is in this "
               "resource, so the question cannot be adjudicated here. Check the "
               "instrument's consequence before treating the exposure as 'protein "
               "abundance'.")
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


def get_instrument_provenance(protein: str) -> dict:
    """Which study measured the protein, on which assay, and with what sample size.

    Uses EpiGraphDB's `rtype=inst` view, which `rtype=simple` does not expose. Returns the
    exposure study author, its sample size, the effect/non-effect alleles and allele
    frequency — the fields needed to judge whether a cis-pQTL could be an assay artefact
    rather than a real difference in protein abundance.
    """
    try:
        r = requests.get(PQTL_API,
                         params={"query": protein, "rtype": "inst",
                                 "pvalue": PVALUE_CEILING, "searchflag": "proteins"},
                         headers={"Accept": "application/json"}, timeout=45)
        r.raise_for_status()
        rows = r.json().get("results", []) or []
    except requests.RequestException as e:
        return {"error": f"EpiGraphDB pQTL instrument request failed: {e}"}
    except ValueError as e:
        return {"error": f"EpiGraphDB pQTL instrument view returned non-JSON: {e}"}

    if not rows:
        return {"found": False, "protein": protein,
                "note": f"No instrument provenance for {protein} in the EpiGraphDB pQTL view."}

    seen, insts = set(), []
    for x in rows:
        key = (x.get("rsID"), x.get("author_exp"))
        if key in seen:
            continue
        seen.add(key)
        author = (x.get("author_exp") or "").strip()
        study, assay, pclass = ASSAY_BY_AUTHOR.get(
            author.lower().split()[0] if author else "", (author or None, None, None))
        insts.append({
            "instrument_rsid": x.get("rsID"),
            "cis_or_trans": x.get("trans_cis"),
            "effect_allele": x.get("ea"),
            "other_allele": x.get("nea"),
            "effect_allele_freq": x.get("eaf_exp"),
            "exposure_study_author": author or None,
            "exposure_study": study,
            "assay_platform": assay,
            # affinity_aptamer | affinity_antibody | mass_spectrometry — the last never
            # occurs in this resource, which is itself the finding.
            "platform_class": pclass,
            "measures": ("binding affinity, used as a proxy for abundance"
                         if pclass and pclass.startswith("affinity") else None),
            "exposure_sample_size": x.get("sample_exp"),
        })

    unmapped = [i["exposure_study_author"] for i in insts if not i["assay_platform"]]
    small = [i for i in insts if isinstance(i.get("exposure_sample_size"), (int, float))
             and i["exposure_sample_size"] < 5000]

    note = _ASSAY_NOTE
    if unmapped:
        note += (f" Assay platform NOT resolved for: {sorted(set(unmapped))} — treat the "
                 f"platform as unknown rather than assuming one.")
    if small:
        note += (f" Note the exposure sample size: "
                 f"{sorted({int(i['exposure_sample_size']) for i in small})}. A pQTL GWAS of a "
                 f"few thousand people supports a strong cis signal but little else.")

    classes = sorted({i["platform_class"] for i in insts if i["platform_class"]})
    return {
        "found": True,
        "computed_here": False,
        "protein": protein,
        "n_instruments": len(insts),
        "platform_classes": classes,
        # Stated explicitly rather than left to be inferred from an absence.
        "mass_spectrometry_available": False,
        "instruments": insts[:10],
        "note": note,
        "source_release": _source_release(),
        "url": "https://epigraphdb.org/pqtl/",
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
