"""Tool: get_gwas_catalog - SNP-trait associations mapped to a gene (GWAS Catalog REST)."""
import requests

GWAS_API = "https://www.ebi.ac.uk/gwas/rest/api"


def get_gwas_catalog(gene_symbol: str) -> dict:
    """Query the GWAS Catalog for genome-wide associations mapped to a gene.

    Use this as complementary genetic evidence: how many GWAS SNPs map to the gene
    (a rough signal that the locus is genetically associated with traits). Input
    should be a gene symbol such as PNPLA3. Returns the number of mapped SNPs and a
    few example rsIDs.
    """
    try:
        r = requests.get(
            f"{GWAS_API}/singleNucleotidePolymorphisms/search/findByGene",
            params={"geneName": gene_symbol, "size": 100},
            headers={"Accept": "application/json"},
            timeout=30,
        )
        data = r.json()
    except requests.RequestException as e:
        return {"error": f"GWAS Catalog request failed: {e}"}

    snps = data.get("_embedded", {}).get("singleNucleotidePolymorphisms", [])
    if not snps:
        return {"found": False, "gene_symbol": gene_symbol, "note": "No GWAS Catalog SNPs mapped."}

    # de-duplicate rsIDs (the endpoint returns one row per SNP-association mapping)
    seen, unique = set(), []
    for s in snps:
        rs = s.get("rsId")
        if rs and rs not in seen:
            seen.add(rs)
            unique.append(rs)
    capped = len(snps) >= 100
    return {
        "found": True,
        "gene_symbol": gene_symbol,
        "n_unique_snps": len(unique),
        "note": "SNP count capped at 100; may be higher." if capped else None,
        "example_rsids": unique[:15],
        "url": f"https://www.ebi.ac.uk/gwas/genes/{gene_symbol}",
    }


if __name__ == "__main__":
    import json
    print(json.dumps(get_gwas_catalog("PNPLA3"), indent=2, ensure_ascii=False))
