# v0.1 — 2026-07-13 · the model wrote the whole card

Eight tools were wired up, but **`get_mr_result` returned a placeholder**
(`{"stub": true, "beta": null}`) and **every part of the card was written by the model**,
including the evidence table and the source list.

Kept because this is the only record of what the system says with no guardrails.

## What it got wrong, and where each was fixed

| On the card | Why it is wrong | Fixed in |
|---|---|---|
| `Causal effect (MR) … Stub: Placeholder results` — **and the verdict is still GO** | A placeholder is not evidence; nothing should have been concluded from it | v0.2 |
| `51 unique GWAS SNPs` | The tool read page 1 of 3. True count is **114** from 256/256 rows | v0.2 |
| `216 records, no pathogenic identified in sampled set` | Reads as 0/216. It was 0 out of a sample of 30 | v0.2 |
| No statement of what "MASLD" resolved to | Every downstream score answers a question the reader cannot see | v0.2 |
| *"high tolerance to LoF … suggests that inhibiting the protein is likely to be safe"* | Constraint read as a licence. LoF tolerance is **not** evidence that inhibition works | v0.2 wording, v0.3 printed on the figure itself |
| Sources are bare links, no database release | Timestamped, not reproducible | v0.2 |

Same input under a later version: `../v0.2_2026-08-14/PNPLA3_MASLD_evidence_card.md`
and, for the current version, `../../PNPLA3_MASLD_evidence_card.md`.
