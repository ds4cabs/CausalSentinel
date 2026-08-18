"""Tool: get_eqtl_instruments — is there an eQTL instrument for this gene, and what would
it actually be measuring?

THE POINT THIS TOOL EXISTS TO MAKE
----------------------------------
It is tempting to treat an eQTL as a stand-in for a missing pQTL. **It is not a
substitute — it is a different exposure.**

    pQTL  instruments PROTEIN abundance     -> "what happens if I change the protein"
    eQTL  instruments TRANSCRIPT abundance  -> "what happens if I change the transcript"

mRNA and protein levels correlate only moderately: post-transcriptional regulation,
protein stability and secretion all break the link. For a drug target the quantity of
interest is usually the protein, so an eQTL-based MR answers a related but distinct
question and must be reported as such, never silently swapped in.

TISSUE IS PART OF THE EXPOSURE, NOT A DETAIL
--------------------------------------------
"No plasma pQTL" is frequently biology rather than a technical failure. PNPLA3 is a
liver lipid-droplet protein that is not secreted into plasma — measuring it in plasma is
asking the wrong compartment. The same trap applies here: the eQTL layer queried below is
predominantly **blood**-derived, so liver-restricted genes come back empty for the same
reason. An empty result therefore means "no instrument in THIS tissue in THIS resource",
not "this gene cannot be studied".

The tissue-resolved alternative is the eQTL Catalogue (GTEx and friends, liver included).
Its REST API returned HTTP 500 on every path tried on 2026-08-15 and again on 2026-08-16.
**GTEx's own API is up and is now wired in** — see `tools/gtex.py`, which
`instrument_availability` below consults so that a blood miss is no longer the last word.

What that upgrade actually bought, measured 2026-08-16: less than expected, and the
measurement is the point. GTEx liver has only n=208 eQTL donors, and PNPLA3, HMGCR and
IL6R all return ZERO significant liver eQTLs while PCSK9 returns 7. The liver query works;
liver is simply underpowered for most genes. So `none_in_these_resources` still fires for
PNPLA3 — but it now means "absent from blood AND from a 49-tissue survey", which is a much
stronger and more honest statement than it was.
"""
import requests

from .gtex import get_gtex_eqtl

EPI = "https://api.epigraphdb.org"
SOURCE = ("EpiGraphDB xQTL layer (predominantly blood-derived eQTL, e.g. eQTLGen); "
          "estimates retrieved, not computed here")


def get_eqtl_instruments(gene_symbol: str, pval_threshold: float = 1e-4) -> dict:
    """Check whether transcript-level (eQTL) instruments exist for a gene, and what
    outcomes have already been tested with them.

    Use this when a protein has no usable plasma pQTL, to see whether the gene can still
    be interrogated at the transcript level. Input is a gene symbol such as HMGCR.

    IMPORTANT: an eQTL instruments TRANSCRIPT abundance, not protein abundance — it is a
    DIFFERENT EXPOSURE, not a substitute for a pQTL, and any downstream statement must say
    which one it rests on. The layer queried is mostly blood, so an empty result means
    "no instrument in this tissue in this resource", never "this gene cannot be studied".
    """
    try:
        r = requests.get(f"{EPI}/xqtl/single-snp-mr",
                         params={"exposure_gene": gene_symbol, "qtl_type": "eQTL",
                                 "pval_threshold": pval_threshold},
                         headers={"Accept": "application/json"}, timeout=45)
        r.raise_for_status()
        rows = r.json().get("results", []) or []
    except requests.RequestException as e:
        return {"error": f"EpiGraphDB xQTL request failed: {e}", "computed_here": False}
    except ValueError as e:
        return {"error": f"EpiGraphDB xQTL returned non-JSON: {e}", "computed_here": False}

    if not rows:
        return {
            "found": False,
            "computed_here": False,
            "gene_symbol": gene_symbol,
            "exposure_if_used": "transcript abundance (eQTL) — NOT protein abundance",
            "note": (f"No eQTL-based MR result for {gene_symbol} in the EpiGraphDB xQTL layer "
                     f"at p<{pval_threshold:g}. That layer is predominantly BLOOD-derived, so "
                     f"tissue-restricted genes (e.g. liver-specific ones) are expected to be "
                     f"absent here for biological reasons, not because the gene is "
                     f"un-instrumentable. A tissue-resolved source such as the eQTL Catalogue "
                     f"would be the right place to look; its REST API was returning HTTP 500 "
                     f"when this tool was written (2026-08-15). ABSENCE HERE IS NOT ABSENCE OF "
                     f"AN INSTRUMENT."),
            "source_release": SOURCE,
            "url": f"https://epigraphdb.org/xqtl/{gene_symbol}",
        }

    slim, outcomes = [], set()
    for x in rows:
        g, gw, res = x.get("gene", {}), x.get("gwas", {}), x.get("r", {})
        outcomes.add(gw.get("trait"))
        slim.append({
            "outcome": gw.get("trait"),
            "outcome_gwas_id": gw.get("id"),
            "beta": res.get("beta"),
            "se": res.get("se"),
            "p_value": res.get("p"),
            "instrument_rsid": res.get("rsid"),
            "ensembl_id": g.get("ensembl_id"),
        })
    slim.sort(key=lambda d: d["p_value"] if d["p_value"] is not None else 1.0)

    return {
        "found": True,
        "computed_here": False,
        "gene_symbol": gene_symbol,
        "exposure_if_used": "transcript abundance (eQTL) — NOT protein abundance",
        "n_results": len(slim),
        "n_distinct_outcomes": len(outcomes),
        "results": slim[:15],
        "note": ("Instruments exist at the TRANSCRIPT level. Any MR built on these estimates "
                 "the effect of changing gene EXPRESSION, which is a different exposure from "
                 "protein abundance and must be reported as such — mRNA and protein correlate "
                 "only moderately. Tissue also matters: this layer is predominantly blood, so "
                 "an effect here is a statement about blood expression unless stated otherwise."),
        "source_release": SOURCE,
        "url": f"https://epigraphdb.org/xqtl/{gene_symbol}",
    }


def instrument_availability(gene_symbol: str, pqtl_found: bool,
                            tissue: str = "") -> dict:
    """Classify what KIND of instrument exists, replacing the old 'Tier C = cannot do MR'.

    The old tiering conflated "no plasma pQTL" with "no MR possible", which is wrong twice
    over: a gene may be instrumentable at the transcript level, and a plasma miss is often
    just the wrong compartment. This returns the instrument class and, crucially, the
    exposure that class implies.

    Two eQTL sources are consulted before the negative class is allowed to fire: the
    EpiGraphDB xQTL layer (mostly blood) and GTEx (49 tissues). `tissue` optionally pins
    the GTEx query to one tissue, e.g. "Liver" for a hepatocyte gene — but read the power
    caveat that comes back with it, because GTEx's small tissues produce zeros easily.
    """
    e = get_eqtl_instruments(gene_symbol)
    g = get_gtex_eqtl(gene_symbol, tissue=tissue)
    g_found = bool(g.get("found"))

    if pqtl_found:
        cls, exposure = "plasma_pQTL", "plasma protein abundance"
        detail = "Plasma pQTL instruments available; MR estimates the effect of protein level."
    elif e.get("found") or g_found:
        cls = "eQTL_only"
        if g_found:
            best = (g.get("tissues") or [{}])[0]
            exposure = (f"transcript abundance (eQTL); strongest tissue in GTEx: "
                        f"{best.get('tissue')} ({best.get('n_eqtls')} eQTLs)")
            detail = (f"No plasma pQTL, but GTEx has {g.get('n_significant_eqtls')} "
                      f"significant cis-eQTLs across {g.get('n_tissues_with_signal')} "
                      f"tissue(s). MR is possible, but it answers a DIFFERENT question "
                      f"from a pQTL MR, and the tissue you instrument in is part of the "
                      f"exposure — an effect in fibroblasts is not an effect in liver.")
        else:
            exposure = "transcript abundance (eQTL, predominantly blood)"
            detail = ("No plasma pQTL, but blood transcript-level instruments exist. MR is "
                      "possible, but it answers a DIFFERENT question from a pQTL MR.")
    else:
        cls, exposure = "none_in_these_resources", "not instrumentable with the sources queried"
        # When the GTEx query was pinned to one tissue, saying "no GTEx eQTL" would be a
        # false absence claim: the gene may be strongly instrumented elsewhere. Re-query
        # unpinned and say which it is. This is the exact error class this project exists
        # to catch, so the tool must not commit it in its own prose.
        elsewhere = get_gtex_eqtl(gene_symbol) if tissue else g
        power = ""
        if tissue:
            n_here = f"n={g['tissue_donors']} donors" if g.get("tissue_donors") else "unknown n"
            power = (f" The GTEx query was PINNED TO {tissue} ({n_here}); a zero in a small "
                     f"tissue is weak evidence of absence, not evidence of a null.")
            if elsewhere.get("found"):
                best = (elsewhere.get("tissues") or [{}])[0]
                power += (f" UNPINNED, GTEx has {elsewhere['n_significant_eqtls']} cis-eQTLs "
                          f"for this gene across {elsewhere['n_tissues_with_signal']} other "
                          f"tissue(s) (strongest: {best.get('tissue')}). The gene IS "
                          f"genetically regulated — just not detectably in {tissue}. Do not "
                          f"report this as 'no eQTL'.")
                cls = "eQTL_other_tissue_only"
                exposure = (f"transcript abundance, but only outside {tissue} "
                            f"(strongest: {best.get('tissue')}) — a tissue mismatch for this "
                            f"gene's biology")
        detail = (f"No plasma pQTL and no blood eQTL in EpiGraphDB."
                  f"{' No GTEx cis-eQTL in any tissue.' if not elsewhere.get('found') else ''}"
                  f" This is a statement about the resources queried, not about the gene."
                  + power)

    return {
        "gene_symbol": gene_symbol,
        "instrument_class": cls,
        "exposure_if_used": exposure,
        "detail": detail,
        "sources_checked": ["EpiGraphDB xQTL (blood)", f"GTEx {tissue or 'all tissues'}"],
        "eqtl": e,
        "gtex": g,
    }


if __name__ == "__main__":
    import json
    import sys
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    print("=== EpiGraphDB xQTL layer (blood) ===")
    for g in ["HMGCR", "IL6R", "CFH", "PNPLA3"]:
        r = get_eqtl_instruments(g)
        print(f"{g:8s} found={str(r.get('found')):5s} "
              f"n={r.get('n_results', 0)} outcomes={r.get('n_distinct_outcomes', 0)}")
        if r.get("found"):
            top = r["results"][0]
            print(f"         top: {str(top['outcome'])[:48]:48s} "
                  f"beta={top['beta']:.3g} p={top['p_value']:.2e} {top['instrument_rsid']}")

    print("\n=== instrument_availability, now with GTEx behind it ===")
    for g, has_pqtl in [("IL6R", True), ("HMGCR", False), ("PNPLA3", False)]:
        a = instrument_availability(g, pqtl_found=has_pqtl, tissue="Liver")
        print(f"{g:8s} pqtl={str(has_pqtl):5s} -> {a['instrument_class']}")
        print(f"         exposure: {a['exposure_if_used']}")
