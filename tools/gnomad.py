"""Tool: get_gnomad_constraint - gene constraint metrics from gnomAD (GraphQL, no key)."""
import requests

GNOMAD_API = "https://gnomad.broadinstitute.org/api"

_QUERY = """
query Constraint($symbol: String!) {
  gene(gene_symbol: $symbol, reference_genome: GRCh38) {
    symbol
    gnomad_constraint { pli oe_lof oe_lof_upper mis_z lof_z syn_z }
  }
}
"""


def get_gnomad_constraint(gene_symbol: str) -> dict:
    """Fetch gnomAD gene-constraint metrics (pLI, LOEUF, missense z) for a gene.

    Use this to judge loss-of-function (LoF) tolerance, which is key for target safety:
    a gene that is intolerant to LoF (high pLI, low LOEUF) may be a riskier drug target.
    Input should be a gene symbol such as PNPLA3. Returns pLI, LOEUF (oe_lof_upper),
    and z-scores, with a short interpretation.
    """
    try:
        r = requests.post(
            GNOMAD_API,
            json={"query": _QUERY, "variables": {"symbol": gene_symbol}},
            timeout=30,
        )
        data = r.json()
    except requests.RequestException as e:
        return {"error": f"gnomAD request failed: {e}"}

    gene = (data.get("data") or {}).get("gene")
    if not gene or not gene.get("gnomad_constraint"):
        return {"found": False, "gene_symbol": gene_symbol, "note": "No gnomAD constraint data."}

    c = gene["gnomad_constraint"]
    return {
        "found": True,
        "gene_symbol": gene_symbol,
        "pLI": c.get("pli"),
        "LOEUF": c.get("oe_lof_upper"),
        "oe_lof": c.get("oe_lof"),
        "mis_z": c.get("mis_z"),
        "lof_z": c.get("lof_z"),
        "interpretation": "High pLI (>0.9) or low LOEUF (<0.35) = LoF-intolerant (handle as a target with care).",
        "url": f"https://gnomad.broadinstitute.org/gene/{gene_symbol}",
    }


if __name__ == "__main__":
    import json
    print(json.dumps(get_gnomad_constraint("PNPLA3"), indent=2, ensure_ascii=False))
