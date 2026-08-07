"""Regression tests for the claim validator.

Run: python test_validator.py

Every case here came from a real failure. The validator's own first version passed a
fabricated p-value of 1.2e-45, because formatting it to one decimal gives "0.0", which
occurs as a substring of "0.029369372" — so numbers are now compared numerically, and
this file exists to keep them that way.
"""
import sys

from validate_card import validate


class FakeLedger:
    def __init__(self, d):
        self.d = d

    def results_by_tool(self):
        return self.d


MR_PRESENT = FakeLedger({
    "get_mr_result": {"found": True, "matched_disease_estimates": [
        {"beta": 0.277233958, "se": 0.029369372, "p_value": 3.74e-21,
         "instrument_rsid": "rs191448950", "cis_or_trans": "cis"}]},
    "get_chembl_modulators": {"found": True, "n_modulators": 2,
                              "modulators": [{"action": "RNAI INHIBITOR"}]},
    "get_gnomad_constraint": {"pLI": 2.8e-18, "LOEUF": 1.1407805},
    "get_gwas_catalog": {"n_unique_snps": 109, "n_association_rows": 246},
})

MR_ABSENT = FakeLedger({
    "get_mr_result": {"found": False, "note": "no estimate"},
    "get_gwas_catalog": {"n_unique_snps": 108, "n_association_rows": 256},
})

# (name, ledger, text, expect_ok)
CASES = [
    # --- numbers -------------------------------------------------------------
    ("qualitative only",              MR_PRESENT, "Strong cis-instrument support and RNAi modulators.", True),
    ("real numbers, rounded",         MR_PRESENT, "beta=0.277 (se=0.0294, p=3.74e-21) via rs191448950; LOEUF=1.14.", True),
    ("fabricated p-value",            MR_PRESENT, "The effect was overwhelming (p=1.2e-45).", False),
    ("fabricated rsID",               MR_PRESENT, "The lead instrument rs99999999 drives it.", False),
    ("fabricated count",              MR_PRESENT, "We found 512 unique SNPs.", False),
    ("subtly altered beta",           MR_PRESENT, "The causal estimate was beta=0.412.", False),
    # --- bounds and approximations ------------------------------------------
    ("lower bound that holds",        MR_ABSENT,  "Over 250 GWAS associations are mapped.", True),
    ("lower bound that fails",        MR_ABSENT,  "Over 400 GWAS associations are mapped.", False),
    ("approximation that holds",      MR_ABSENT,  "Nearly 110 unique SNPs were found.", True),
    # --- qualitative claims --------------------------------------------------
    ("invented monoclonal antibody",  MR_PRESENT, "Approved monoclonal antibodies target this protein.", False),
    ("invented approval",             MR_PRESENT, "FDA-approved therapies already exist.", False),
    # --- causal consistency --------------------------------------------------
    ("asserts causal without MR",     MR_ABSENT,  "PNPLA3 is a primary causal target for MASLD.", False),
    ("asserts causes without MR",     MR_ABSENT,  "This protein causes the disease.", False),
    ("honest NO-GO denial",           MR_ABSENT,  "There is no genetic, causal, or pharmacotherapeutic evidence here.", True),
    ("causality not established",     MR_ABSENT,  "Causality is not established without an MR estimate.", True),
    ("causal cannot be inferred",     MR_ABSENT,  "A causal effect cannot be inferred from these data.", True),
    ("MR unavailable phrasing",       MR_ABSENT,  "No Mendelian randomization estimates are available.", True),
    ("causal WITH MR is fine",        MR_PRESENT, "MR supports a causal role for this target.", True),
    ("claims the agent ran MR",       MR_PRESENT, "We performed Mendelian randomization for this target.", False),
]


def main() -> int:
    failed = 0
    for name, ledger, text, expect_ok in CASES:
        got = validate(text, ledger)["ok"]
        if got != expect_ok:
            failed += 1
            print(f"FAIL  {name}: expected ok={expect_ok}, got ok={got}")
        else:
            print(f"pass  {name}")
    print(f"\n{len(CASES) - failed}/{len(CASES)} passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
