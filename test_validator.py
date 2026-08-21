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

# Negative beta: higher protein goes with LESS disease, so a benefit claim must be about
# RAISING the target. Taken from the real IL6R x coronary heart disease row.
MR_NEG = FakeLedger({
    "get_mr_result": {"found": True, "protein": "IL6R",
                      "matched_disease_estimates": [
                          {"beta": -0.0441899892357374, "se": 0.00853, "p_value": 2.21e-07,
                           "instrument_rsid": "rs4129267", "cis_or_trans": "cis", "n_snp": 1,
                           # Passing validation fields ON PURPOSE: these fixtures test the
                           # DIRECTION rule, and leaving them empty would fire the
                           # unvalidated-estimate rule too, so every direction case would
                           # be testing two rules at once. The real IL6R row, whose Steiger
                           # genuinely is NA, is MR_UNVALIDATED above.
                           "steiger_direction_ok": "TRUE", "ld_check": 1.0}]},
    "get_chembl_modulators": {"found": True, "modulators": [{"action": "RNAI INHIBITOR"}]},
})

# Positive beta: higher protein goes with MORE disease — the LPA x CHD row, same outcome,
# opposite sign. Both conventions must be handled by one rule.
MR_POS = FakeLedger({
    "get_mr_result": {"found": True, "protein": "LPA",
                      "matched_disease_estimates": [
                          {"beta": 0.252303585657371, "se": 0.0181, "p_value": 1e-40,
                           "instrument_rsid": "rs10455872", "cis_or_trans": "cis", "n_snp": 1,
                           "steiger_direction_ok": "TRUE", "ld_check": 1.0}]},
    "get_chembl_modulators": {"found": True, "modulators": [{"action": "RNAI INHIBITOR"}]},
})

# The real IL6R x CHD row: an estimate EXISTS, so the "no MR" rule does not fire, but
# every check that would separate a causal effect from LD confounding or reverse causation
# is missing. Causal wording on this is unearned.
MR_UNVALIDATED = FakeLedger({
    "get_mr_result": {"found": True, "protein": "IL6R",
                      "matched_disease_estimates": [
                          {"beta": -0.0441899892357374, "se": 0.00853005023322569,
                           "p_value": 2.21283026387414e-07, "method": "Wald ratio", "n_snp": 1,
                           "instrument_rsid": "rs4129267", "cis_or_trans": "cis",
                           "steiger_direction_ok": "NA", "steiger_p": None,
                           "coloc_prob": None, "ld_check": None}]},
})

# The LPA x CHD row from the same batch: same outcome, same tool, same single instrument —
# but Steiger passed and the LD check is 1.0. Causal wording here IS earned, and the rule
# must not fire, or it would punish the better-evidenced card equally.
MR_VALIDATED = FakeLedger({
    "get_mr_result": {"found": True, "protein": "LPA",
                      "matched_disease_estimates": [
                          {"beta": 0.252303585657371, "se": 0.0193149800796813,
                           "p_value": 5.38664852468177e-39, "method": "Wald ratio", "n_snp": 1,
                           "instrument_rsid": "rs55730499", "cis_or_trans": "cis",
                           "steiger_direction_ok": "TRUE", "steiger_p": 0.0,
                           "coloc_prob": None, "ld_check": 1.0}]},
})

# Two estimates for one pair, OPPOSITE signs, both validated (so only the direction rule
# is under test). This shape exists in the resource: every multi-estimate protein draws
# its rows from one study, often as different molecular forms (C3 fragments, PROC zymogen
# vs activated), where sign conflicts are fragment biology before they are artefacts.
MR_CONFLICTING = FakeLedger({
    "get_mr_result": {"found": True, "protein": "C3",
                      "matched_disease_estimates": [
                          {"beta": 0.11, "se": 0.02, "p_value": 1e-8, "n_snp": 1,
                           "outcome_gwas_id": "101", "instrument_rsid": "rs1000001",
                           "steiger_direction_ok": "TRUE", "ld_check": 1.0},
                          {"beta": -0.09, "se": 0.02, "p_value": 1e-6, "n_snp": 1,
                           "outcome_gwas_id": "101", "instrument_rsid": "rs1000002",
                           "steiger_direction_ok": "TRUE", "ld_check": 1.0}]},
    "get_chembl_modulators": {"found": True, "modulators": [{"action": "RNAI INHIBITOR"}]},
})

# est[0] unvalidated, est[1] validated. The old causal rule read ONLY est[0] and failed
# this ledger — a verdict decided by sort order. The fix judges the best estimate.
MR_SECOND_VALIDATED = FakeLedger({
    "get_mr_result": {"found": True, "protein": "LPA",
                      "matched_disease_estimates": [
                          {"beta": 0.21, "se": 0.03, "p_value": 1e-12, "n_snp": 1,
                           "instrument_rsid": "rs10455872",
                           "steiger_direction_ok": "NA", "coloc_prob": None, "ld_check": None},
                          {"beta": 0.252303585657371, "se": 0.0193, "p_value": 5.39e-39,
                           "n_snp": 1, "instrument_rsid": "rs55730499",
                           "steiger_direction_ok": "TRUE", "steiger_p": 0.0,
                           "ld_check": 1.0}]},
})

# Concordance classifier present: two estimates agree in sign but share one study — the
# only kind of multiplicity this resource actually contains.
CONC_AGREE_NONINDEP = FakeLedger({
    "get_mr_result": {"found": True, "protein": "C5",
                      "matched_disease_estimates": [
                          {"beta": 0.12, "n_snp": 1, "steiger_direction_ok": "TRUE",
                           "ld_check": 1.0},
                          {"beta": 0.10, "n_snp": 1, "steiger_direction_ok": "TRUE",
                           "ld_check": 1.0}]},
    "classify_evidence_concordance": {
        "estimate_concordance": {"n_estimates_compared": 2, "direction": "agree",
                                 "independence": "non_independent",
                                 "label": "sign_consistent_non_independent",
                                 "cross_platform": False}},
})

CONC_CONFLICT = FakeLedger({
    "get_mr_result": {"found": True, "protein": "C3", "matched_disease_estimates": [
        {"beta": 0.11, "n_snp": 1, "steiger_direction_ok": "TRUE", "ld_check": 1.0},
        {"beta": -0.09, "n_snp": 1, "steiger_direction_ok": "TRUE", "ld_check": 1.0}]},
    "classify_evidence_concordance": {
        "estimate_concordance": {"n_estimates_compared": 2, "direction": "conflict",
                                 "independence": "non_independent",
                                 "cross_platform": False}},
})

# (name, ledger, text, expect_ok)
CASES = [
    # --- conflicting estimates license NO intervention direction ------------------
    ("conflicting signs forbid a drug-direction claim", MR_CONFLICTING,
     "MR evidence suggests C3 inhibition would be therapeutic.", False),
    ("conflicting signs described neutrally are fine", MR_CONFLICTING,
     "The retrieved estimates for C3 disagree in sign; no direction is asserted.", True),
    # --- the est[0] bug: causal wording judged on the BEST estimate, not the first --
    ("causal wording earned by the second, validated estimate", MR_SECOND_VALIDATED,
     "Mendelian randomization evidence supports a causal effect of LPA on coronary heart "
     "disease risk.", True),
    # --- replication wording must be earned by the concordance classifier -----------
    ("replication claim with no classifier in the run", MR_VALIDATED,
     "This causal effect of LPA has been replicated across studies.", False),
    ("bare 'consistent with' is not a replication claim", MR_VALIDATED,
     "The verdict is consistent with the retrieved causal estimate for LPA.", True),
    ("denying replication is not claiming it", MR_VALIDATED,
     "This causal LPA estimate has not been replicated across studies.", True),
    ("sign consistency may be stated when classified", CONC_AGREE_NONINDEP,
     "The two retrieved estimates are concordant across datasets in sign.", True),
    ("but not sold as independent replication", CONC_AGREE_NONINDEP,
     "The association is independently confirmed by two estimates.", False),
    ("nor as cross-platform agreement", CONC_AGREE_NONINDEP,
     "The association shows cross-platform agreement.", False),
    ("agreement wording on conflicting estimates fails", CONC_CONFLICT,
     "The estimates are concordant across datasets.", False),
    # --- causal wording must be earned by the validation fields, not just by existence --
    ("unvalidated single-SNP estimate cannot carry causal wording", MR_UNVALIDATED,
     "Mendelian randomization evidence supports a causal role of IL6R in coronary heart "
     "disease.", False),
    ("same estimate is fine described as an association", MR_UNVALIDATED,
     "Genetically-predicted higher plasma IL6R is associated with lower coronary heart "
     "disease risk. Steiger direction, colocalization and the LD check are unavailable "
     "for this estimate.", True),
    ("stating the causal limitation is not a causal claim", MR_UNVALIDATED,
     "A causal interpretation is not supported: this is a single-instrument Wald ratio "
     "with no Steiger direction test and no colocalization.", True),
    ("validated estimate may carry causal wording", MR_VALIDATED,
     "Mendelian randomization evidence supports a causal effect of LPA on coronary heart "
     "disease risk.", True),
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
    # --- clinical status: never retrievable from this tool panel --------------
    ("approval claim",                MR_PRESENT, "Approved therapies already exist for this target.", False),
    ("clinical trial claim",          MR_PRESENT, "Clinical trials have validated this mechanism.", False),
    ("proof-of-efficacy claim",       MR_PRESENT, "The clinical legacy provides definitive proof of efficacy.", False),
    ("modality absent from ChEMBL",   MR_PRESENT, "Biologic modulators of this target exist.", False),
    ("modality present in ChEMBL",    MR_PRESENT, "RNAi modulators of this target are listed.", True),
    # --- direction: the sign of beta licenses exactly one intervention --------
    # Motivating failure: a card quoted beta = -0.0442 correctly and then recommended the
    # opposite intervention, because the model was reciting a remembered conclusion.
    ("beta<0: inhibition is backwards", MR_NEG,   "MR supports a protective effect of IL6R inhibition in disease.", False),
    ("beta<0: activation is licensed",  MR_NEG,   "Causal evidence suggests IL6R activation could be therapeutic.", True),
    ("beta<0: outcome wording is fine", MR_NEG,   "Higher IL6R protein is associated with lower disease risk.", True),
    ("beta>0: inhibition is licensed",  MR_POS,   "MR supports that LPA inhibition would be therapeutic.", True),
    ("beta>0: activation is backwards", MR_POS,   "MR supports that LPA activation would be therapeutic.", False),
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
