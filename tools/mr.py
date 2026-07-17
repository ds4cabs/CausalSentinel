"""Tool: get_mr_result — Mendelian randomization causal estimate.

ROUND 1 = STUB. Real MR is slow (R + TwoSampleMR + coloc), so we pre-compute it into
DuckDB in Round 3 and swap this stub for a real DuckDB read. Returning a clearly-labelled
placeholder now lets the whole agent loop run end-to-end today.
"""


def get_mr_result(protein: str, disease: str) -> dict:
    """Return the pre-computed Mendelian randomization (MR) causal estimate for a
    protein's effect on a disease.

    Use this to judge whether the protein has a CAUSAL effect on the disease (not just
    a correlation). Inputs: protein (gene symbol) and disease name.

    NOTE: this is currently a PLACEHOLDER (stub: true) — real MR/colocalization results
    from DuckDB replace it in Round 3. Treat the numbers as not-yet-available.
    """
    return {
        "stub": True,
        "protein": protein,
        "disease": disease,
        "method": "two-sample MR (PLACEHOLDER — not real)",
        "beta": None,
        "se": None,
        "p_value": None,
        "note": "Placeholder. Real MR + colocalization from DuckDB will replace this in Round 3.",
    }


if __name__ == "__main__":
    import json
    print(json.dumps(get_mr_result("PNPLA3", "MASLD"), indent=2))
