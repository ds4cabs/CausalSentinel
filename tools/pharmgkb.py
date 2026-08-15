"""Tool: get_pharmgkb_drug_gene - drug-gene pharmacogenomics from PharmGKB / ClinPGx.

NOTE ON THE ENDPOINT: PharmGKB's old `api.pharmgkb.org` host no longer resolves — the
resource now serves its public API as **ClinPGx** at `api.clinpgx.org`, with the same
`/v1/data/clinicalAnnotation` shape. We try the current host first and keep the legacy
host as a fallback so the tool still works if the redirect is ever restored.
"""
import requests

PRIMARY_API = "https://api.clinpgx.org/v1/data"     # current host (PharmGKB -> ClinPGx)
LEGACY_API = "https://api.pharmgkb.org/v1/data"     # retired host, kept as fallback


def _fetch(base: str, gene_symbol: str):
    r = requests.get(
        f"{base}/clinicalAnnotation",
        params={"location.genes.symbol": gene_symbol, "view": "min"},
        headers={"Accept": "application/json"},
        timeout=30,
    )
    # ClinPGx answers "this gene has no annotations" with 404, not an empty 200. That is a
    # legitimate NEGATIVE RESULT, not a tool failure — returning [] here makes the card say
    # "not available" instead of "tool error".
    if r.status_code == 404:
        return []
    r.raise_for_status()
    return r.json().get("data", [])


def get_pharmgkb_drug_gene(gene_symbol: str) -> dict:
    """Query PharmGKB/ClinPGx for drug-gene pharmacogenomic annotations for a gene.

    Use this to see which drugs have documented pharmacogenomic relationships with the
    gene (relevant to repurposing and dosing). Input should be a gene symbol such as
    VKORC1, CYP2C19, or PNPLA3. Returns the number of clinical annotations, the drugs
    involved, and a few example annotations with their level of evidence.
    """
    annotations, host_used, errors = None, None, []
    for base in (PRIMARY_API, LEGACY_API):
        try:
            annotations = _fetch(base, gene_symbol)
            host_used = base
            break
        except Exception as e:                      # network, DNS, HTTP, or JSON
            errors.append(f"{base}: {type(e).__name__}")

    if annotations is None:
        return {"error": "PharmGKB/ClinPGx request failed on all hosts (" + "; ".join(errors) + ")"}

    if not isinstance(annotations, list) or not annotations:
        return {
            "found": False,
            "gene_symbol": gene_symbol,
            "note": "No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).",
            "source_release": f"ClinPGx clinicalAnnotation via {host_used}",
        }

    drug_set, examples, levels = set(), [], {}
    for ca in annotations:
        drugs = [c.get("name") for c in ca.get("relatedChemicals", []) if c.get("name")]
        drug_set.update(drugs)
        lvl = (ca.get("levelOfEvidence") or {}).get("term")
        if lvl:
            levels[lvl] = levels.get(lvl, 0) + 1
        if len(examples) < 8:
            examples.append({
                "drugs": drugs,
                "level_of_evidence": lvl,
                "annotation": ca.get("name"),
            })

    return {
        "found": True,
        "gene_symbol": gene_symbol,
        "n_clinical_annotations": len(annotations),
        "evidence_level_counts": dict(sorted(levels.items())),
        "drugs": sorted(drug_set)[:20],
        "n_drugs": len(drug_set),
        "examples": examples,
        "url": f"https://www.pharmgkb.org/search?query={gene_symbol}",
        "source_release": f"ClinPGx clinicalAnnotation via {host_used}",
    }


if __name__ == "__main__":
    import json
    # VKORC1 is a classic pharmacogene (warfarin) - good for testing.
    print(json.dumps(get_pharmgkb_drug_gene("VKORC1"), indent=2, ensure_ascii=False))
