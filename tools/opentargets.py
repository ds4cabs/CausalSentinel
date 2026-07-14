"""Tool: get_target_disease_evidence — target-disease association from Open Targets (GraphQL).

NOTE: This is the fiddliest tool ('identifier hell') because it must resolve a gene
symbol -> Ensembl id and a disease name -> EFO id before scoring. Test it alone first.
"""
import requests

OT_URL = "https://api.platform.opentargets.org/api/v4/graphql"

_SEARCH = """
query($q: String!, $e: [String!]) {
  search(queryString: $q, entityNames: $e) { hits { id name entity } }
}
"""

_ASSOC = """
query($efo: String!) {
  disease(efoId: $efo) {
    name
    associatedTargets(page: {index: 0, size: 500}) {
      rows { target { id approvedSymbol } score datatypeScores { id score } }
    }
  }
}
"""


def _gql(query: str, variables: dict) -> dict:
    r = requests.post(OT_URL, json={"query": query, "variables": variables}, timeout=30)
    r.raise_for_status()
    return r.json()


def get_target_disease_evidence(gene_symbol: str, disease: str) -> dict:
    """Query Open Targets for how strongly a target is associated with a disease.

    Use this to gauge the overall genetic/experimental association score (0-1) between
    a gene/target and a disease. Inputs: a gene symbol (e.g. PNPLA3) and a disease name
    (e.g. 'MASLD' or 'fatty liver disease'). Returns the association score and the
    contributing data-type scores, plus the resolved Ensembl and EFO ids.
    """
    try:
        tgt_hits = _gql(_SEARCH, {"q": gene_symbol, "e": ["target"]})["data"]["search"]["hits"]
        dis_hits = _gql(_SEARCH, {"q": disease, "e": ["disease"]})["data"]["search"]["hits"]
    except Exception as ex:
        return {"error": f"Open Targets search failed: {ex}"}

    if not tgt_hits or not dis_hits:
        return {"found": False, "note": f"Could not resolve target '{gene_symbol}' or disease '{disease}'."}

    ensembl_id = tgt_hits[0]["id"]
    efo_id = dis_hits[0]["id"]

    try:
        rows = _gql(_ASSOC, {"efo": efo_id})["data"]["disease"]["associatedTargets"]["rows"]
    except Exception as ex:
        return {"error": f"Open Targets association query failed: {ex}",
                "resolved": {"ensembl_id": ensembl_id, "efo_id": efo_id}}

    match = next((row for row in rows if row["target"]["id"] == ensembl_id), None)
    if not match:
        return {"found": False, "resolved": {"ensembl_id": ensembl_id, "efo_id": efo_id},
                "note": "Target not among this disease's top associations."}

    return {
        "found": True,
        "ensembl_id": ensembl_id,
        "efo_id": efo_id,
        "overall_score": round(match["score"], 4),
        "datatype_scores": {d["id"]: round(d["score"], 4) for d in match.get("datatypeScores", [])},
        "url": f"https://platform.opentargets.org/evidence/{ensembl_id}/{efo_id}",
    }


if __name__ == "__main__":
    import json
    print(json.dumps(get_target_disease_evidence("PNPLA3", "fatty liver disease"), indent=2))
