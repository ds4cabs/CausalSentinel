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


_META = "query { meta { dataVersion { year month iteration } apiVersion { x y z } } }"


def _gql(query: str, variables: dict = None) -> dict:
    r = requests.post(OT_URL, json={"query": query, "variables": variables or {}}, timeout=30)
    r.raise_for_status()
    return r.json()


def _release() -> str:
    """Open Targets publishes its data release; record it so the card is reproducible."""
    try:
        m = _gql(_META)["data"]["meta"]
        dv = m.get("dataVersion") or {}
        parts = [str(dv.get(k)) for k in ("year", "month", "iteration") if dv.get(k) is not None]
        return "Open Targets data release " + ".".join(parts) if parts else \
               "Open Targets (release not reported)"
    except Exception:
        return "Open Targets (release not reported)"


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
    tgt_name = tgt_hits[0].get("name")
    dis_name = dis_hits[0].get("name")

    # The free-text disease string is silently resolved to ONE ontology term. If the caller
    # asked about "high cholesterol" and this resolved to an HPO phenotype rather than the
    # disease they meant, every downstream score is about a different question. Say so.
    resolution_note = (f"Free-text inputs were resolved to ontology terms: "
                       f"'{gene_symbol}' -> {ensembl_id} ({tgt_name}); "
                       f"'{disease}' -> {efo_id} ({dis_name}). "
                       f"Scores below describe THAT term, not the free-text phrase.")

    try:
        rows = _gql(_ASSOC, {"efo": efo_id})["data"]["disease"]["associatedTargets"]["rows"]
    except Exception as ex:
        return {"error": f"Open Targets association query failed: {ex}",
                "resolved": {"ensembl_id": ensembl_id, "efo_id": efo_id}}

    match = next((row for row in rows if row["target"]["id"] == ensembl_id), None)
    if not match:
        return {"found": False,
                "resolved": {"ensembl_id": ensembl_id, "efo_id": efo_id,
                             "target_name": tgt_name, "disease_name": dis_name},
                "note": (f"{gene_symbol} is not among the top 500 associated targets for "
                         f"{efo_id} ({dis_name}). This is a TRUNCATED LOOKUP, not proof of no "
                         f"association. " + resolution_note),
                "source_release": _release()}

    return {
        "found": True,
        "ensembl_id": ensembl_id,
        "efo_id": efo_id,
        "resolved_target_name": tgt_name,
        "resolved_disease_name": dis_name,
        "overall_score": round(match["score"], 4),
        "datatype_scores": {d["id"]: round(d["score"], 4) for d in match.get("datatypeScores", [])},
        "note": resolution_note,
        "url": f"https://platform.opentargets.org/evidence/{ensembl_id}/{efo_id}",
        "source_release": _release(),
    }


_PHENOME = """
query($e: String!, $size: Int!) {
  target(ensemblId: $e) {
    approvedSymbol
    associatedDiseases(page: {index: 0, size: $size}) {
      count
      rows { disease { id name } score
             datatypeScores { id score }
             datasourceScores { id score } }
    }
  }
}
"""


def get_gene_phenome(gene_symbol: str, size: int = 30) -> dict:
    """List the phenotypes/diseases this gene is genetically associated with (Open Targets).

    Use this to see WHERE this gene is a genetic locus across the phenome — the disease
    table a researcher scans to spot comorbidity structure and un-run MR analyses. The
    genetic_association score aggregates common-variant (GWAS) and rare-variant evidence.
    ASSOCIATION IS NOT CAUSATION: rows here are loci, not causal claims.
    """
    try:
        hits = _gql(_SEARCH, {"q": gene_symbol, "e": ["target"]})["data"]["search"]["hits"]
    except Exception as ex:
        return {"error": f"Open Targets search failed: {ex}"}
    if not hits:
        return {"found": False, "note": f"Could not resolve target '{gene_symbol}'."}
    ensembl_id = hits[0]["id"]

    try:
        t = _gql(_PHENOME, {"e": ensembl_id, "size": size})["data"]["target"]
        ad = t["associatedDiseases"]
    except Exception as ex:
        return {"error": f"Open Targets phenome query failed: {ex}",
                "resolved": {"ensembl_id": ensembl_id}}

    # Curated clinical/Mendelian assertion sources. Presence means SOMEONE has curated a
    # gene-disease claim (any validity level) — it does NOT mean ClinGen "Definitive".
    CURATED = {"clingen", "gene2phenotype", "genomics_england", "orphanet", "eva",
               "uniprot_variants"}

    rows = []
    for row in ad.get("rows", []):
        ga = next((x["score"] for x in row.get("datatypeScores", [])
                   if x["id"] == "genetic_association"), None)
        ds = {x["id"]: x["score"] for x in row.get("datasourceScores", [])}
        # gene_burden = ExWAS burden evidence (Genebass / AZ PheWAS via Open Targets):
        # rare-variant carrier contrasts — a "nature's knockout" design (cf. PCSK9,
        # Cohen 2006). Estimand differs from two-sample MR: carrier-vs-noncarrier,
        # not per-SD of protein.
        gb = ds.get("gene_burden")
        gwas = ds.get("gwas_credible_sets")            # renamed from ot_genetics_portal
        curated = sorted(k for k in ds if k in CURATED)

        # Four-state causal triage per gene-disease pair. The owner's insight: "no MR"
        # rows are not one thing — an established Mendelian relationship needs no MR,
        # while a burden signal WITHOUT curation is a candidate new gene-disease
        # relationship that ExWAS/MR exploration could establish.
        if curated:
            status = "established (curated)"
        elif gb is not None and gwas is not None:
            status = "multi-layer: burden+GWAS (allelic-series candidate)"
        elif gb is not None:
            status = "exploratory rare-variant signal"
        elif gwas is not None:
            status = "common-variant locus"
        else:
            status = "other evidence only"

        rows.append({
            "disease": row["disease"]["name"],
            "disease_id": row["disease"]["id"],
            "overall_score": round(row["score"], 3),
            "genetic_association": None if ga is None else round(ga, 3),
            "gene_burden_exwas": None if gb is None else round(gb, 3),
            "gwas_common": None if gwas is None else round(gwas, 3),
            "curated_sources": ";".join(curated) if curated else None,
            "causal_status": status,
        })

    return {
        "found": True,
        "gene_symbol": gene_symbol,
        "ensembl_id": ensembl_id,
        "n_associated_diseases_total": ad.get("count"),
        "top_diseases": rows,
        "note": (f"Top {len(rows)} of {ad.get('count')} associated diseases by overall score. "
                 f"genetic_association aggregates GWAS common-variant AND rare-variant "
                 f"evidence. These are ASSOCIATIONS (loci), not causal claims."),
        "url": f"https://platform.opentargets.org/target/{ensembl_id}/associations",
        "source_release": _release(),
    }


if __name__ == "__main__":
    import json
    print(json.dumps(get_target_disease_evidence("PNPLA3", "fatty liver disease"), indent=2))
