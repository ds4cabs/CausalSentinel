"""Tool: get_uniprot_dossier - protein context from UniProt (REST, no key needed).

Adapted from the workshop notebook (02_gene_lookup_agent) lookup_gene_uniprot():
  - dropped the LangChain @tool decorator (google-genai reads plain functions);
  - returns a dict (easier to assemble into the causal-card JSON);
  - added a timeout and a __main__ test block (always test a tool alone first).

This is tool #2 of the 8 MVP tools. The other 7 follow the same pattern:
swap the URL + swap the fields you parse out of the JSON.
"""
import requests

UNIPROT_SEARCH_URL = "https://rest.uniprot.org/uniprotkb/search"


def get_uniprot_dossier(gene_symbol: str) -> dict:
    """Look up a human protein in UniProt by its gene symbol.

    Use this when you need the protein's function, subcellular location, or known
    disease associations. Input should be a standard human gene symbol such as
    PNPLA3, PCSK9, or TP53. Returns protein name, function, subcellular location,
    disease associations, and a UniProt URL.
    """
    params = {
        # human only (organism_id 9606) and manually reviewed (Swiss-Prot) entries
        "query": f"(gene:{gene_symbol}) AND (organism_id:9606) AND (reviewed:true)",
        "format": "json",
        "size": 1,  # top hit only
        "fields": "accession,gene_names,protein_name,cc_function,"
                  "cc_subcellular_location,cc_disease",
    }
    try:
        resp = requests.get(UNIPROT_SEARCH_URL, params=params, timeout=30)
    except requests.RequestException as e:
        return {"gene_symbol": gene_symbol, "error": f"UniProt request failed: {e}"}
    if resp.status_code != 200:
        return {"gene_symbol": gene_symbol, "error": f"UniProt HTTP {resp.status_code}"}

    results = resp.json().get("results", [])
    if not results:
        return {"gene_symbol": gene_symbol, "found": False,
                "note": f"No reviewed human UniProt entry for '{gene_symbol}'."}

    entry = results[0]
    accession = entry.get("primaryAccession", "N/A")
    protein_name = (
        entry.get("proteinDescription", {})
        .get("recommendedName", {})
        .get("fullName", {})
        .get("value", "N/A")
    )
    gene_names = [g.get("geneName", {}).get("value", "") for g in entry.get("genes", [])]

    # pull function / location / disease out of the "comments" block
    functions, locations, diseases = [], [], []
    for c in entry.get("comments", []):
        ctype = c.get("commentType")
        if ctype == "FUNCTION":
            functions += [t.get("value", "") for t in c.get("texts", [])]
        elif ctype == "SUBCELLULAR LOCATION":
            locations += [
                loc.get("location", {}).get("value", "")
                for loc in c.get("subcellularLocations", [])
            ]
        elif ctype == "DISEASE":
            d = c.get("disease", {}).get("diseaseId")
            if d:
                diseases.append(d)

    return {
        "found": True,
        "gene_symbol": gene_symbol,
        "accession": accession,
        "gene_names": [g for g in gene_names if g],
        "protein_name": protein_name,
        "function": " ".join(functions) or "Not annotated.",
        "subcellular_location": [loc for loc in locations if loc] or ["Not annotated."],
        "diseases": diseases or ["None annotated."],
        "url": f"https://www.uniprot.org/uniprotkb/{accession}",
    }


if __name__ == "__main__":
    # Test this tool alone before wiring it into the agent.
    import json
    print(json.dumps(get_uniprot_dossier("PNPLA3"), indent=2, ensure_ascii=False))
