# v0.2 — 2026-08-14 · the model stops writing the card

Merged in PR #11. The model now writes **exactly two things** — a one-line verdict and a
reasoning paragraph. The evidence table, caveat block, sources and provenance footer are
rendered mechanically from the tool ledger, and `validate_card.py` fails the run when the
prose outruns what the tools returned.

`get_mr_result` also stopped being a stub: it **retrieves published** two-sample MR
estimates (Zheng et al., *Nat Genet* 2020, via EpiGraphDB). It still computes nothing.

## Why these four cards are frozen here

| Card | What it is the exhibit for |
|---|---|
| `PNPLA3_MASLD` | The three-version lineage. v0.1 has the same pair, so v0.1 → v0.2 → current is directly readable |
| `IL6R_coronary-heart-disease` | **Passed** validation here saying "genetic and **causal** evidence support IL6R". In v0.3 the same claim **fails** — the estimate is a single-instrument Wald ratio with `steiger=NA`, `coloc=null`, `ld_check=null` |
| `HMGCR_high-cholesterol` | **Failed** here on `clinical-status: clinically proven`, and passes in v0.3. Also the gene whose constraint verdict the v0.3 figure fix corrects |
| `TREM2_Alzheimer-disease` | Failed here on `clinical-status: approved`; fails in v0.3 for a **different** reason (`modality-not-in-chembl: peptide`) |

`_batch_summary.json` is the run record: **8/10 passed, 3 checkable tokens across 915
words of reasoning (0.33 per 100 words)**.

> An earlier run of the same benchmark, before the clinical-status rule was tightened,
> passed **10/10 — also with 3 checkable tokens**. The pass rate fell because the check
> got stricter. That is what the claim-density metric exists to expose: a pass rate on
> its own measures caution, not accuracy.

## What was still broken here, fixed in v0.3

- The constraint **figure re-derived the verdict from LOEUF alone** while the tool used
  `pLI > 0.9 OR LOEUF < 0.35`. HMGCR fell in the gap: the card said LoF-INTOLERANT and the
  figure drew the statin target in the green "tolerant" zone.
- Causal wording did not depend on whether the estimate had been **validated**.
- The direction rule argued the biology was backwards. It is not — see the v0.3 note.
- No record of **which study measured the protein, on which assay platform**.
- No tissue layer.
