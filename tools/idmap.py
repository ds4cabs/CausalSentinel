"""Tool: resolve_ids — one place that turns a gene symbol or a disease name into every
identifier the rest of the pipeline needs.

WHY THIS IS ITS OWN MODULE
--------------------------
"Identifier hell" was named as a core challenge of this project on day one, and until now
each tool solved it privately: UniProt accessions inside `uniprot.py`, Ensembl and EFO
inside `opentargets.py`, protein-panel trait names inside `mr.py`. Same problem, three
answers, none reusable. This module is the shared answer.

THE PART THAT ACTUALLY BITES
----------------------------
Free-text resolution is silent. `"high cholesterol"` resolves to `HP_0003124`
(Hypercholesterolemia, a phenotype) rather than to a disease term, and every score
downstream then answers a question nobody asked. So `resolve_disease` always returns what
it matched **and** the runners-up, and the caller is expected to show that to the reader
rather than quietly proceed.

The protein side has its own trap: pQTL panels store assay names, not gene symbols —
IL6R is filed as "IL-6 sRa" and HMGCR as "HMGR". Matching on symbol silently returns
nothing, which reads as "this protein has no data" when it means "you asked with the
wrong key". `resolve_gene` therefore returns the UniProt accession, which is what those
panels can actually be matched on.
"""
import requests

UNIPROT = "https://rest.uniprot.org/uniprotkb/search"
OT_GQL = "https://api.platform.opentargets.org/api/v4/graphql"

_SEARCH = """
query($q: String!, $e: [String!]) {
  search(queryString: $q, entityNames: $e) { hits { id name entity description } }
}
"""


def resolve_gene(gene_symbol: str) -> dict:
    """Resolve a human gene symbol to UniProt accession, Ensembl id and known aliases.

    Use this before querying any resource keyed on something other than the gene symbol.
    Returns accession (the key pQTL panels can be matched on), ensembl_id, and the alias
    list to use for literature search.
    """
    out = {"query": gene_symbol, "found": False}

    try:
        r = requests.get(UNIPROT, params={
            "query": f"(gene:{gene_symbol}) AND (organism_id:9606) AND (reviewed:true)",
            "format": "json", "size": 1,
            "fields": "accession,gene_names,protein_name,gene_primary",
        }, timeout=30)
        r.raise_for_status()
        res = r.json().get("results", [])
        out["uniprot_release"] = r.headers.get("X-UniProt-Release")
    except (requests.RequestException, ValueError) as e:
        return {**out, "error": f"UniProt lookup failed: {e}"}

    if res:
        entry = res[0]
        genes = entry.get("genes", []) or []
        primary = (genes[0].get("geneName", {}) or {}).get("value") if genes else None
        synonyms = [s.get("value") for g in genes for s in (g.get("synonyms") or [])
                    if s.get("value")]
        pname = ((entry.get("proteinDescription", {}) or {}).get("recommendedName", {})
                 .get("fullName", {}) or {}).get("value")
        seen, aliases = set(), []
        for a in [gene_symbol, primary, pname, *synonyms]:
            if a and a.lower() not in seen:
                seen.add(a.lower())
                aliases.append(a)
        out.update({
            "found": True,
            "accession": entry.get("primaryAccession"),
            "gene_primary": primary or gene_symbol,
            "protein_name": pname,
            "aliases": aliases,
        })

    try:
        hits = requests.post(OT_GQL, json={"query": _SEARCH,
                                           "variables": {"q": gene_symbol, "e": ["target"]}},
                             timeout=30).json()["data"]["search"]["hits"]
        if hits:
            out["ensembl_id"] = hits[0]["id"]
            out["ensembl_matched_name"] = hits[0].get("name")
    except Exception:
        pass

    if not out["found"] and "ensembl_id" not in out:
        out["note"] = (f"'{gene_symbol}' resolved to nothing in UniProt (reviewed human) or "
                       f"Open Targets. Check the symbol — a withdrawn or non-human symbol "
                       f"fails silently everywhere downstream.")
    elif out.get("accession"):
        out["note"] = (f"Use accession {out['accession']} when matching pQTL panels: they "
                       f"store assay names (IL6R is filed as 'IL-6 sRa', HMGCR as 'HMGR'), "
                       f"so symbol matching returns nothing and reads as 'no data'.")
    return out


def resolve_disease(disease: str, n_alternatives: int = 4) -> dict:
    """Resolve a free-text disease name to an ontology term, and show what else it could
    have matched.

    Use this before interpreting any disease-keyed score. The match is returned WITH its
    runners-up because free-text resolution is silent and frequently wrong in a way that
    changes the question: 'high cholesterol' resolves to a phenotype term, not a disease.
    """
    try:
        hits = requests.post(OT_GQL, json={"query": _SEARCH,
                                           "variables": {"q": disease, "e": ["disease"]}},
                             timeout=30).json()["data"]["search"]["hits"]
    except Exception as e:
        return {"query": disease, "found": False, "error": f"Open Targets search failed: {e}"}

    if not hits:
        return {"query": disease, "found": False,
                "note": f"No ontology term matched '{disease}'."}

    top = hits[0]
    alts = [{"id": h["id"], "name": h.get("name")} for h in hits[1:1 + n_alternatives]]
    ontology = top["id"].split("_")[0] if "_" in top["id"] else "unknown"
    return {
        "query": disease,
        "found": True,
        "id": top["id"],
        "name": top.get("name"),
        "ontology": ontology,
        "alternatives": alts,
        "note": (f"'{disease}' was resolved to {top['id']} ({top.get('name')}). "
                 f"Everything keyed on this term describes THAT concept, not the phrase you "
                 f"typed. " + (f"Other candidates were: "
                               f"{', '.join(a['id'] + ' (' + str(a['name']) + ')' for a in alts)}."
                               if alts else "No close alternatives were offered.")
                 + (" Note this is an HPO phenotype term rather than a disease term."
                    if ontology == "HP" else "")),
    }


def resolve_pair(gene_symbol: str, disease: str) -> dict:
    """Resolve both sides of a (protein, disease) question in one call."""
    return {"gene": resolve_gene(gene_symbol), "disease": resolve_disease(disease)}


if __name__ == "__main__":
    import json
    import sys
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    for g in ["IL6R", "HMGCR", "PNPLA3"]:
        r = resolve_gene(g)
        print(f"{g:8s} acc={r.get('accession')} ensembl={r.get('ensembl_id')} "
              f"aliases={r.get('aliases', [])[:4]}")
    print()
    for d in ["high cholesterol", "MASLD", "coronary heart disease"]:
        r = resolve_disease(d)
        print(f"{d:24s} -> {r.get('id')} ({r.get('name')})  [{r.get('ontology')}]")
        for a in r.get("alternatives", [])[:2]:
            print(f"{'':24s}    alt: {a['id']} ({a['name']})")
