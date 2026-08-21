# Verdict benchmark — 20 resolved pairs from Minikel et al. 2024

The first external scoring of this agent's GO / NO-GO verdicts. The labels are history's:
each pair either **launched** (a regulator said yes) or **died at phase II/III with no
active programme** (the industry tried seriously and walked away).

## Where the pairs come from

[Minikel, Painter, Dong & Nelson 2024](https://github.com/ericminikel/genetic_support)
(*Nature* 629:624-629, CC-BY-4.0): 29,476 Pharmaprojects target–indication pairs with
per-phase outcomes. Sampling (seed 20260821, `benchmark/minikel20_pairs.txt`, one pair
per gene, this repo's worked-example proteins excluded):

- **10 SUCCESS** — historical category "Launched".
- **10 FAILURE** — reached Phase II/III, failed that transition, never launched, no
  active programme today. Preclinical/Phase-I stops are excluded: those often die for
  portfolio reasons, which would poison the NO-GO label.

Labels live in `minikel20_labels.tsv`, which the agent never sees.

## The leakage rule

The run **withholds `get_clinical_evidence`** (`--exclude-tool get_clinical_evidence`):
that tool shows launched drugs as APPROVAL stages, which IS the answer. Residual leakage
remains — Open Targets' association score includes a `known_drug` datatype, and the
model's own training data knows famous drugs — so the scorer prints the known_drug score
per pair instead of pretending the leak is zero, and rule 7 of the system prompt
("do not import what you already know") is the model-side control.

## How to read the score

Perfect accuracy is not the expectation and would itself be suspicious: most launched
drugs have **no** genetic support for their indication — the entire point of the
genetic-support literature is that support merely ~2.6×'s the odds (Nelson 2015, King
2019, Minikel 2024). The informative readouts are:

1. **Precision of GO** — when the genetics-first verdict says GO, how often did history
   agree?
2. **Failure rejection** — how many of the 10 failures the agent declined to endorse.
3. **Honesty under absence** — whether the model invents support where retrieval has
   none, which the validator scores independently of this benchmark.

## Reproduce

```
python agent.py --batch benchmark/minikel20_pairs.txt \
    --exclude-tool get_clinical_evidence --allow-unvalidated \
    --out-dir benchmark/cards_genetic_only
python benchmark/score_minikel20.py
```

## Results — first run, 2026-08-21 (v0.4 agent, genetic-only mode)

|                | GO | NO-GO | INSUFFICIENT |
|----------------|----|-------|--------------|
| SUCCESS (10)   | 4  | 0     | 6            |
| FAILURE (10)   | 0  | 0     | 10           |

- **Precision of GO: 4/4** — every genetics-first GO (VDR-psoriasis, JAK3-ulcerative
  colitis, ROCK2-GvHD, SLC5A2-CKD) is a launched drug.
- **Failure rejection: 10/10** — no failed programme was endorsed. The agent also never
  said NO-GO: absence of evidence stays "insufficient", never "no effect".
- **The 6 INSUFFICIENT successes are the expected asymmetry**, not a defect: those pairs
  (TNF-seborrheic dermatitis, SCN9A-postherpetic neuralgia, ...) launched without
  genetic support for the indication — exactly the population Nelson/Minikel showed
  dominates approved drugs.
- **The leakage audit earned its keep, twice.** (1) The model tried to smuggle training
  knowledge past the withheld clinical tool — SLC5A2's card claims "multiple approved
  inhibitors" and FAILS validation on `clinical-status-not-retrievable`; the run is
  scored on retrieval, and the violation is visible instead of silent. (2) The three
  clean GO calls all carry Open Targets `clinical` datatype scores of 0.91-0.99 — a
  datatype derived from known drugs — so part of the GO precision rides on residual
  clinical signal inside the association score, not on genetics alone. A stricter
  iteration would strip that datatype too; the current run reports it per pair rather
  than pretending it is zero.
- 18/20 cards passed validation; both failures are the validator catching real
  overreach (the SLC5A2 case above, and a "small-molecule" claim without ChEMBL
  support on NR3C1).

Verdict-level takeaway, phrased the only honest way: **on 20 externally-labelled pairs,
the agent never endorsed a historical failure and never rejected a historical success —
its errors are all abstentions, and its confident calls were all right, partly aided by
residual clinical signal that the audit makes visible.**
