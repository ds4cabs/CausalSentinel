"""Tool: get_gwas_catalog - SNP-trait associations mapped to a gene (GWAS Catalog REST)."""
import requests

GWAS_API = "https://www.ebi.ac.uk/gwas/rest/api"
PAGE_SIZE = 200
MAX_PAGES = 25          # hard stop so a pathological gene can never hang the agent


def get_gwas_catalog(gene_symbol: str) -> dict:
    """Query the GWAS Catalog for genome-wide associations mapped to a gene.

    Use this as complementary genetic evidence: how many GWAS SNPs map to the gene
    (a rough signal that the locus is genetically associated with traits). Input
    should be a gene symbol such as PNPLA3. Returns the number of mapped SNPs and a
    few example rsIDs.
    """
    seen, unique, rows_read = set(), [], 0
    total_reported = None
    total_pages = None
    page = 0

    while page < MAX_PAGES:
        try:
            r = requests.get(
                f"{GWAS_API}/singleNucleotidePolymorphisms/search/findByGene",
                params={"geneName": gene_symbol, "size": PAGE_SIZE, "page": page},
                headers={"Accept": "application/json"},
                timeout=30,
            )
            data = r.json()
        except requests.RequestException as e:
            if page == 0:
                return {"error": f"GWAS Catalog request failed: {e}"}
            # partial data: stop here but say so
            break
        except ValueError as e:
            if page == 0:
                return {"error": f"GWAS Catalog returned non-JSON: {e}"}
            break

        snps = data.get("_embedded", {}).get("singleNucleotidePolymorphisms", [])
        page_meta = data.get("page", {}) or {}
        if page == 0:
            total_reported = page_meta.get("totalElements")
            total_pages = page_meta.get("totalPages")

        if not snps:
            break

        rows_read += len(snps)
        for s in snps:
            rs = s.get("rsId")
            if rs and rs not in seen:
                seen.add(rs)
                unique.append(rs)

        page += 1
        if total_pages is not None and page >= total_pages:
            break

    if not unique:
        return {
            "found": False,
            "gene_symbol": gene_symbol,
            "note": "No GWAS Catalog SNPs mapped to this gene.",
            "source_release": "GWAS Catalog REST (live)",
        }

    # Was the sweep complete? Only claim a complete count when it actually is one.
    complete = (
        total_pages is not None
        and page >= total_pages
    ) or (
        total_reported is not None and rows_read >= total_reported
    )

    if complete:
        note = None
    else:
        note = (
            f"INCOMPLETE SWEEP: read {rows_read} of {total_reported} association rows "
            f"({page} of {total_pages} pages) before the page cap; the unique-SNP count "
            f"is a LOWER BOUND."
        )

    return {
        "found": True,
        "gene_symbol": gene_symbol,
        "n_unique_snps": len(unique),
        "n_association_rows": rows_read,
        "total_association_rows_reported": total_reported,
        "sweep_complete": bool(complete),
        "note": note,
        "example_rsids": unique[:15],
        "url": f"https://www.ebi.ac.uk/gwas/genes/{gene_symbol}",
        "source_release": "GWAS Catalog REST (live; release not exposed by this endpoint)",
    }


if __name__ == "__main__":
    import json
    print(json.dumps(get_gwas_catalog("PNPLA3"), indent=2, ensure_ascii=False))
