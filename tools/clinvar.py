"""Tool: get_clinvar_variants - clinically significant variants from ClinVar (NCBI E-utilities)."""
import requests

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"


def get_clinvar_variants(gene_symbol: str) -> dict:
    """Look up clinically significant variants in a gene via ClinVar.

    Use this to see whether a gene has known pathogenic or benign clinical variants.
    Input should be a gene symbol such as PNPLA3. Returns the total number of ClinVar
    records, how many of a sampled set are pathogenic, and a few example variants.
    """
    # 1) esearch -> record ids + total count
    try:
        es = requests.get(
            f"{EUTILS}/esearch.fcgi",
            params={"db": "clinvar", "term": f"{gene_symbol}[gene]", "retmode": "json", "retmax": 30},
            timeout=30,
        ).json()
    except requests.RequestException as e:
        return {"error": f"ClinVar esearch failed: {e}"}
    result = es.get("esearchresult", {})
    ids = result.get("idlist", [])
    total = int(result.get("count", 0))
    if not ids:
        return {"found": False, "gene_symbol": gene_symbol, "note": "No ClinVar records."}

    # 2) esummary -> clinical significance per record
    try:
        summ = requests.get(
            f"{EUTILS}/esummary.fcgi",
            params={"db": "clinvar", "id": ",".join(ids), "retmode": "json"},
            timeout=30,
        ).json().get("result", {})
    except requests.RequestException as e:
        return {"error": f"ClinVar esummary failed: {e}", "total_records": total}

    # NOTE: `pathogenic` is counted over every record we actually retrieved, so the
    # denominator reported below must be that same set — not the length of `examples`,
    # which is capped at 5 purely for display. Reporting "0 of 5" when the count was taken
    # over 30 records is a silently wrong fraction.
    examples, pathogenic, n_scored = [], 0, 0
    for uid in summ.get("uids", []):
        rec = summ.get(uid, {})
        n_scored += 1
        # the clinical-significance field name has changed over time; try the common ones
        sig = ""
        for key in ("germline_classification", "clinical_significance"):
            val = rec.get(key)
            if isinstance(val, dict):
                sig = val.get("description", "") or sig
            elif isinstance(val, str):
                sig = val or sig
        if "pathogenic" in sig.lower():
            pathogenic += 1
        if len(examples) < 5:
            examples.append({"title": rec.get("title", ""), "significance": sig or "N/A"})

    # ClinVar's build id makes the card reproducible; a retrieval date alone does not.
    build = ""
    try:
        info = requests.get(f"{EUTILS}/einfo.fcgi",
                            params={"db": "clinvar", "retmode": "json"}, timeout=20).json()
        dbinfo = info.get("einforesult", {}).get("dbinfo", [])
        if dbinfo:
            build = dbinfo[0].get("dbbuild", "")
    except (requests.RequestException, ValueError):
        build = ""

    return {
        "found": True,
        "gene_symbol": gene_symbol,
        "total_records": total,
        "pathogenic_in_sample": pathogenic,
        "sample_size": n_scored,
        "examples": examples,
        "note": (f"Pathogenic count is over the {n_scored} record(s) retrieved, NOT over all "
                 f"{total} ClinVar records for this gene; it is a sample, not a rate."),
        "url": f"https://www.ncbi.nlm.nih.gov/clinvar/?term={gene_symbol}%5Bgene%5D",
        "source_release": f"ClinVar build {build}" if build else "ClinVar (build not reported)",
    }


if __name__ == "__main__":
    import json
    print(json.dumps(get_clinvar_variants("PNPLA3"), indent=2, ensure_ascii=False))
