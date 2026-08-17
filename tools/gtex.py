"""Tool: get_gtex_eqtl — tissue-resolved eQTL instruments from the GTEx Portal API v2.

WHY THIS EXISTS
---------------
`tools/eqtl.py` queries EpiGraphDB's xQTL layer, which is predominantly BLOOD. That leaves
tissue-restricted genes looking un-instrumentable when they are merely being asked about in
the wrong compartment. The eQTL Catalogue was the intended fix; its REST API was returning
HTTP 500 on every path tried on 2026-08-15 and again on 2026-08-16. GTEx's own API is up,
needs no key, and covers 49 tissues including liver — so it fills the gap directly.

THE FINDING THAT MADE THIS TOOL WORTH WRITING
---------------------------------------------
The obvious expectation was that GTEx liver would rescue PNPLA3 — the canonical liver gene
of MASLD genetics. It does not. Measured live on 2026-08-16:

    PNPLA3, GTEx v8, ALL tissues : 511 significant eQTLs
    PNPLA3, GTEx v8, Liver       :   0
    (skin 266, spleen 101, lung 68, cultured fibroblasts 67, thyroid 3, heart 3, ...)

So "no plasma pQTL, therefore try liver eQTL" **still returns nothing for PNPLA3**, and the
naive reading — "PNPLA3 expression is not genetically regulated in liver" — is exactly the
wrong conclusion to draw. GTEx liver has n=208 eQTL donors, among its smallest tissues; a
null there is weak evidence of absence, not evidence of a null.

That is the whole design requirement for this tool: **an empty tissue result must arrive
with the sample size and eGene count attached**, so that "underpowered" is distinguishable
from "genuinely no signal". A bare zero is the same silent-truncation failure mode as the
GWAS pagination bug, wearing a different hat.

WHAT AN eQTL IS AND IS NOT (repeated here on purpose)
-----------------------------------------------------
An eQTL instruments TRANSCRIPT abundance in a NAMED TISSUE. It is not a stand-in for a
plasma pQTL — it is a different exposure, and the tissue is part of that exposure, not a
footnote. Any downstream MR statement must say which one it rests on.

NOT COMPUTED HERE
-----------------
These are GTEx's own published cis-eQTL associations, retrieved. No MR, no colocalization
and no fine-mapping happens in this file. `nes` is GTEx's normalised effect size (effect of
the ALT allele on expression), not an MR estimate.
"""
import requests

API = "https://gtexportal.org/api/v2"
DATASET = "gtex_v8"          # the dataset the v2 association endpoints serve
PAGE = 250                   # API max; anything less silently truncates
SOURCE = (f"GTEx Portal API v2, dataset {DATASET} (GENCODE v26 / GRCh38); "
          "published cis-eQTL associations retrieved, not computed here")

_TISSUE_CACHE: dict | None = None


def _tissue_table() -> dict:
    """Tissue -> {donors, eGenes}. Fetched once; this is what turns a bare 0 into a
    statement a reader can weigh."""
    global _TISSUE_CACHE
    if _TISSUE_CACHE is not None:
        return _TISSUE_CACHE
    try:
        r = requests.get(f"{API}/dataset/tissueSiteDetail",
                         params={"itemsPerPage": 100},
                         headers={"Accept": "application/json"}, timeout=30)
        r.raise_for_status()
        rows = r.json().get("data", []) or []
    except (requests.RequestException, ValueError):
        _TISSUE_CACHE = {}
        return _TISSUE_CACHE
    _TISSUE_CACHE = {
        t["tissueSiteDetailId"]: {
            "donors": (t.get("eqtlSampleSummary") or {}).get("totalCount"),
            "egenes": t.get("eGeneCount"),
            "label": t.get("tissueSiteDetail"),
        }
        for t in rows if t.get("tissueSiteDetailId")
    }
    return _TISSUE_CACHE


def _resolve_gencode_id(gene_symbol: str) -> tuple[str | None, str | None]:
    """Gene symbol -> versioned GENCODE id, which is what the association endpoints require.

    Returns (gencode_id, error). A plain symbol is NOT accepted by the eQTL endpoints, and
    passing one yields an empty result rather than an error — another silent-zero trap.
    """
    try:
        r = requests.get(f"{API}/reference/gene", params={"geneId": gene_symbol},
                         headers={"Accept": "application/json"}, timeout=30)
        r.raise_for_status()
        hits = r.json().get("data", []) or []
    except requests.RequestException as e:
        return None, f"GTEx gene lookup failed: {e}"
    except ValueError as e:
        return None, f"GTEx gene lookup returned non-JSON: {e}"

    if not hits:
        return None, f"No GTEx gene record for '{gene_symbol}'."
    # Prefer an exact symbol match on a protein-coding gene; GTEx can return paralogs
    # and retired symbols for the same query.
    exact = [h for h in hits if (h.get("geneSymbolUpper") or "").upper() == gene_symbol.upper()]
    coding = [h for h in (exact or hits) if h.get("geneType") == "protein coding"]
    return (coding or exact or hits)[0].get("gencodeId"), None


def get_gtex_eqtl(gene_symbol: str, tissue: str = "") -> dict:
    """Retrieve GTEx significant cis-eQTLs for a gene, optionally restricted to one tissue.

    Use this when a gene has no plasma pQTL instrument, to ask whether it is instrumentable
    at the TRANSCRIPT level in a SPECIFIC TISSUE — for example a liver gene that is not
    secreted into plasma. Input is a gene symbol such as PNPLA3; `tissue` is an optional
    GTEx tissue id such as "Liver" or "Adipose_Subcutaneous".

    IMPORTANT: an eQTL instruments transcript abundance in the tissue queried, which is a
    DIFFERENT EXPOSURE from plasma protein abundance — never report one as the other. An
    empty result for a tissue is returned together with that tissue's donor count and total
    eGene count, because GTEx's smaller tissues (liver n=208) are underpowered and a zero
    there is weak evidence of absence, not evidence of absence.
    """
    gencode_id, err = _resolve_gencode_id(gene_symbol)
    if err:
        return {"error": err, "computed_here": False, "gene_symbol": gene_symbol}

    params = {"gencodeId": gencode_id, "datasetId": DATASET, "itemsPerPage": PAGE}
    if tissue:
        params["tissueSiteDetailId"] = tissue

    rows, page, pages = [], 0, 1
    try:
        while page < pages:
            params["page"] = page
            r = requests.get(f"{API}/association/singleTissueEqtl", params=params,
                             headers={"Accept": "application/json"}, timeout=60)
            r.raise_for_status()
            body = r.json()
            rows.extend(body.get("data", []) or [])
            pages = (body.get("paging_info") or {}).get("numberOfPages", 1) or 1
            page += 1
    except requests.RequestException as e:
        return {"error": f"GTEx eQTL request failed: {e}", "computed_here": False,
                "gene_symbol": gene_symbol, "gencode_id": gencode_id}
    except ValueError as e:
        return {"error": f"GTEx eQTL returned non-JSON: {e}", "computed_here": False,
                "gene_symbol": gene_symbol, "gencode_id": gencode_id}

    tt = _tissue_table()
    human_url = f"https://gtexportal.org/home/gene/{gene_symbol}"
    exposure = ("transcript abundance (cis-eQTL) in the tissue named — NOT plasma protein "
                "abundance")

    if not rows:
        ctx = tt.get(tissue, {}) if tissue else {}
        where = f"GTEx {DATASET} {tissue}" if tissue else f"GTEx {DATASET} (any tissue)"
        power = ""
        if tissue and ctx.get("donors"):
            power = (f" That tissue has n={ctx['donors']} eQTL donors and {ctx['egenes']} "
                     f"eGenes in total, so an absent signal here may reflect POWER rather "
                     f"than the absence of genetic regulation.")
        elif tissue:
            power = (f" '{tissue}' returned no rows and is not in the tissue table — check "
                     f"the id against /dataset/tissueSiteDetail before reading this as a "
                     f"biological null.")
        return {
            "found": False,
            "computed_here": False,
            "gene_symbol": gene_symbol,
            "gencode_id": gencode_id,
            "tissue_queried": tissue or "all",
            "exposure_if_used": exposure,
            "tissue_donors": ctx.get("donors"),
            "tissue_egenes": ctx.get("egenes"),
            "note": (f"No significant cis-eQTL for {gene_symbol} in {where}.{power} "
                     f"GTEx reports only gene-level significant eQTLs, so this is a "
                     f"thresholded absence, not raw evidence of no association. ABSENCE "
                     f"HERE IS NOT ABSENCE OF AN INSTRUMENT."),
            "source_release": SOURCE,
            "url": human_url,
        }

    by_tissue: dict[str, int] = {}
    for x in rows:
        t = x.get("tissueSiteDetailId")
        by_tissue[t] = by_tissue.get(t, 0) + 1

    tissues = sorted(
        ({"tissue": t, "n_eqtls": n,
          "tissue_donors": tt.get(t, {}).get("donors"),
          "tissue_egenes": tt.get(t, {}).get("egenes")} for t, n in by_tissue.items()),
        key=lambda d: -d["n_eqtls"])

    def _p(x):
        try:
            return float(x.get("pValue"))
        except (TypeError, ValueError):
            return 1.0

    top = [{
        "rsid": x.get("snpId"),
        "variant_id": x.get("variantId"),
        "tissue": x.get("tissueSiteDetailId"),
        "p_value": x.get("pValue"),
        "nes": x.get("nes"),          # GTEx normalised effect size, ALT allele on expression
    } for x in sorted(rows, key=_p)[:15]]

    # A tissue the user asked about that has no signal is the single most misreadable
    # result this tool can produce, so name it explicitly rather than leaving a gap.
    missing_note = ""
    if not tissue:
        for t in ("Liver", "Whole_Blood"):
            if t not in by_tissue and t in tt:
                missing_note += (f" No significant eQTL in {t} (n={tt[t]['donors']} donors) "
                                 f"despite signal elsewhere — likely power, not biology.")

    return {
        "found": True,
        "computed_here": False,
        "gene_symbol": gene_symbol,
        "gencode_id": gencode_id,
        "tissue_queried": tissue or "all",
        "exposure_if_used": exposure,
        "n_significant_eqtls": len(rows),
        "n_tissues_with_signal": len(by_tissue),
        "tissues": tissues,
        "top_associations": top,
        "note": (f"{len(rows)} significant cis-eQTLs across {len(by_tissue)} tissue(s). "
                 f"`nes` is GTEx's normalised effect size of the ALT allele on EXPRESSION — "
                 f"it is not an MR estimate and says nothing about disease. Tissue is part "
                 f"of the exposure: an effect in fibroblasts is not an effect in liver."
                 f"{missing_note}"),
        "source_release": SOURCE,
        "url": human_url,
    }


def tissue_ids(substring: str = "") -> dict:
    """List GTEx tissue ids with their eQTL donor counts, optionally filtered by substring.

    Use this to get the exact `tissue` string for get_gtex_eqtl — a wrong id returns zero
    rows rather than an error, which reads like a biological null.
    """
    tt = _tissue_table()
    if not tt:
        return {"error": "GTEx tissue table unavailable."}
    s = substring.lower()
    hits = sorted(
        ({"tissue": k, "label": v["label"], "donors": v["donors"], "egenes": v["egenes"]}
         for k, v in tt.items() if s in k.lower()),
        key=lambda d: -(d["donors"] or 0))
    return {"found": bool(hits), "n": len(hits), "tissues": hits,
            "source_release": SOURCE, "url": "https://gtexportal.org/home/tissueSummaryPage"}


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    print("=== the case this tool was written for ===")
    r = get_gtex_eqtl("PNPLA3", tissue="Liver")
    print(f"PNPLA3 x Liver -> found={r.get('found')}")
    print(f"  {r.get('note')}\n")

    r = get_gtex_eqtl("PNPLA3")
    print(f"PNPLA3 x all tissues -> {r.get('n_significant_eqtls')} eQTLs in "
          f"{r.get('n_tissues_with_signal')} tissues")
    for t in (r.get("tissues") or [])[:6]:
        print(f"    {t['tissue']:34s} {t['n_eqtls']:4d}  (n={t['tissue_donors']})")
    print()

    print("=== controls ===")
    for g in ["HMGCR", "IL6R", "PCSK9"]:
        a = get_gtex_eqtl(g)
        liv = get_gtex_eqtl(g, tissue="Liver")
        print(f"{g:8s} all={a.get('n_significant_eqtls', 0):5d} in "
              f"{a.get('n_tissues_with_signal', 0):2d} tissues | "
              f"Liver={liv.get('n_significant_eqtls', 0)}")
