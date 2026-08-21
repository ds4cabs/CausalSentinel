# Card archive — v0.3, generated 2026-08-17

The 10 benchmark cards as produced by the round-5 code (PR #14): tissue panels,
instrument provenance, mechanism classes, and the `causal-claim-on-unvalidated-estimate`
validator rule.

**What this version did NOT have** (added in round 6, the version after this one):

- No evidence-concordance classification: nothing said which retrieval sources answered,
  or whether multiple matched estimates agreed — and two validator rules read only the
  FIRST estimate, so their verdicts depended on sort order.
- No clinical development record at all: the card was blind to "has anyone already tried
  this target?" — no drugs, no stages, no why-stopped reasons. The validator's response
  was a blanket ban on all clinical-status wording.
- 33 validator regression cases (round 6 ends at 60).

Known verdicts in this batch: IL6R × coronary heart disease FAILS validation under the
unvalidated-estimate rule (single-instrument Wald ratio, no Steiger/coloc/LD); TREM2 ×
Alzheimer disease FAILS on modality-not-in-chembl. Both failures are the validator doing
its job, kept as exhibits.

Compare with the round-6 regeneration in `cards/` to see what the new tools changed on
identical inputs.
