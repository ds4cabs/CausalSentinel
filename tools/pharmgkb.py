"""Tool: get_pharmgkb_drug_gene - drug-gene pharmacogenomics from PharmGKB (public API)."""
import requests

PGKB_API = "https://api.pharmgkb.org/v1/data"


def get_pharmgkb_drug_gene(gene_symbol: str) -> dict:
    """Query PharmGKB for drug-gene pharmacogenomic annotations for a gene.

    Use this to see which drugs have documented pharmacogenomic relationships with the
    gene (relevant to repurposing and dosing). Input should be a gene symbol such as
    VKORC1, CYP2C19, or PNPLA3. Returns the number of clinical annotations, the drugs
    involved, and a few example annotations with their level of evidence.
    """
    # 1) clinical annotations for this gene (each links drugs <-> variants)
    try:
        r = requests.get(
            f"{PGKB_API}/clinicalAnnotation",
            params={"location.genes.symbol": gene_symbol, "view": "min"},
            timeout=30,
        )
        annotations = r.json().get("data", [])
    except requests.RequestException as e:
        return {"error": f"PharmGKB request failed: {e}"}

    if not isinstance(annotations, list) or not annotations:
        return {"found": False, "gene_symbol": gene_symbol,
                "note": "No PharmGKB clinical annotations (gene may not be a pharmacogene)."}

    drug_set, examples = set(), []
    for ca in annotations:
        drugs = [c.get("name") for c in ca.get("relatedChemicals", []) if c.get("name")]
        drug_set.update(drugs)
        if len(examples) < 8:
            examples.append({
                "drugs": drugs,
                "level_of_evidence": (ca.get("levelOfEvidence") or {}).get("term"),
                "annotation": ca.get("name"),
            })

    return {
        "found": True,
        "gene_symbol": gene_symbol,
        "n_clinical_annotations": len(annotations),
        "drugs": sorted(drug_set)[:20],
        "examples": examples,
        "url": f"https://www.pharmgkb.org/search?query={gene_symbol}",
    }


if __name__ == "__main__":
    import json
    # VKORC1 is a classic pharmacogene (warfarin) - good for testing.
    print(json.dumps(get_pharmgkb_drug_gene("VKORC1"), indent=2, ensure_ascii=False))
