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


SEARCH_API = "https://www.ebi.ac.uk/gwas/api/search/advancefilter"
_FL = ("traitName_s,pValueMantissa,pValueExponent,rsId,accessionId,pubmedId,"
       "betaNum,betaDirection,orPerCopyNum,author_s")


def get_gwas_associations(gene_symbol: str, max_traits: int = 20) -> dict:
    """List the TRAITS this gene's locus is associated with in the GWAS Catalog — the
    actual GWAS results (trait, best p-value, lead SNP, study), not just a SNP count.

    Use this to see which phenotypes have GWAS signal at this gene: the locus table a
    researcher scans for comorbidity structure and for what upstream evidence exists.
    Input is a gene symbol such as PNPLA3. ASSOCIATIONS ARE LOCI, NOT CAUSAL CLAIMS.
    """
    try:
        r = requests.get(
            SEARCH_API,
            params={"q": f"ensemblMappedGenes:{gene_symbol}",
                    "facet": "association", "fl": _FL, "max": 1},
            headers={"Accept": "application/json"},
            timeout=60,
        )
        r.raise_for_status()
        groups = r.json().get("grouped", {}).get("resourcename", {}).get("groups", [])
    except requests.RequestException as e:
        return {"error": f"GWAS Catalog search failed: {e}"}
    except ValueError as e:
        return {"error": f"GWAS Catalog search returned non-JSON: {e}"}

    docs = []
    for g in groups:
        if g.get("groupValue") == "association":
            docs = g.get("doclist", {}).get("docs", [])
            break
    if not docs:
        return {"found": False, "gene_symbol": gene_symbol,
                "note": "No GWAS Catalog associations mapped to this gene.",
                "source_release": "GWAS Catalog search API (live)"}

    # Aggregate association rows -> one line per trait, keeping the strongest hit.
    # p-values in the catalog go far below float range (10^-467): compare and DISPLAY via
    # (mantissa, exponent) so "p=0.0e+00" never reaches a reader.
    traits = {}
    n_gwsig = 0
    for doc in docs:
        name = doc.get("traitName_s") or ", ".join(doc.get("traitName", [])[:1]) or "?"
        try:
            mant = float(doc.get("pValueMantissa"))
            expo = int(doc.get("pValueExponent"))
            key = (expo, mant)                      # smaller exponent = stronger
        except (TypeError, ValueError):
            mant, expo, key = None, None, None
        if key is not None and (expo < -8 or (expo == -8 and mant < 5)):
            n_gwsig += 1
        t = traits.setdefault(name, {"trait": name, "n_associations": 0,
                                     "best_p": None, "_key": None, "lead_snp": None,
                                     "study": None, "pubmed": None})
        t["n_associations"] += 1
        if key is not None and (t["_key"] is None or key < t["_key"]):
            t["_key"] = key
            t["best_p"] = f"{mant:g}e{expo}"
            rs = doc.get("rsId") or []
            t["lead_snp"] = rs[0] if isinstance(rs, list) and rs else rs or None
            t["study"] = doc.get("accessionId")
            t["pubmed"] = doc.get("pubmedId")

    ranked = sorted(traits.values(),
                    key=lambda t: t["_key"] if t["_key"] is not None else (999, 9.9))
    for t in ranked:
        t.pop("_key", None)
    return {
        "found": True,
        "gene_symbol": gene_symbol,
        "n_associations_total": len(docs),
        "n_traits_total": len(traits),
        "n_genome_wide_significant": n_gwsig,
        "top_traits": ranked[:max_traits],
        "note": (f"Top {min(max_traits, len(ranked))} of {len(traits)} traits by best "
                 f"p-value, aggregated from {len(docs)} association rows. These are GWAS "
                 f"ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are "
                 f"not necessarily the effector gene."),
        "url": f"https://www.ebi.ac.uk/gwas/genes/{gene_symbol}",
        "source_release": "GWAS Catalog search API (live; release not exposed)",
    }


if __name__ == "__main__":
    import json
    print(json.dumps(get_gwas_catalog("PNPLA3"), indent=2, ensure_ascii=False))
    print(json.dumps(get_gwas_associations("PNPLA3", max_traits=8), indent=2,
                     ensure_ascii=False))
