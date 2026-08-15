# Changelog

All notable changes to CausalSentinel, newest first. Where a claim is measurable, the
same-input before/after evidence is quoted — the objective yardstick for every upgrade
is *identical input, compared output*. Any older version's full output can be
reconstructed from git (see "Comparing versions" at the bottom).

## v0.3 — 2026-08-14 · The proteome resource (branch `round3-real-mr-and-validation`)

**Added**
- `proteome_sweep.py`: protein-centric **dossiers for the whole searchable universe** —
  no LLM, no API key, every cell rendered mechanically. 991 dossiers +
  `dossiers/master_index.csv`. Totals: 101,543 retrieved MR estimate rows, 50,730
  aggregated GWAS Catalog traits, 7,524 genetically-supported disease rows with no MR
  estimate.
- Per-gene **GWAS Catalog trait tables** (`get_gwas_associations`): trait, best p
  (kept as mantissa/exponent so p < 1e-308 never prints as 0), lead SNP, study accession.
- **Four-state causal triage** per gene-disease pair, derived from Open Targets
  datasource scores: *established (curated)* / *exploratory rare-variant signal* /
  *common-variant locus* / *multi-layer (allelic-series candidate)*. Across 991
  proteins: 417 / 25 / 17 respectively. ExWAS burden scores (Genebass/AZ PheWAS via
  the `gene_burden` datasource) shown per disease.
- Tier-B instrument probe: prot-* pQTL GWAS datasets matched by UniProt accession.

**Notes**
- The four-state triage exists because the project owner (a statistical geneticist)
  corrected the first two-state version twice in one night: Mendelian genes can still
  anchor complex-trait claims via ExWAS burden, and a burden signal without curation is
  a candidate NEW gene-disease relationship. The screen finds candidates; the
  geneticist judges.

## v0.2 — 2026-08-07 · Real MR retrieval + mechanical rendering + validator

**Changed — the MR slot is no longer a stub.** `get_mr_result` now **retrieves**
published two-sample MR estimates (EpiGraphDB pQTL resource; Zheng et al.,
*Nat Genet* 2020). It still computes nothing, and says so in every result
(`computed_here: false`).

Same-input evidence (PCSK9 × high cholesterol):

| | v0.1 stub | v0.2 retrieval |
|---|---|---|
| beta / se / p | null / null / null | **+0.277 / 0.029 / 3.7e-21** |
| instrument | — | rs191448950, **cis**, Wald ratio, n_snp=1 |
| causal-credibility fields | — | Steiger TRUE (p=4.4e-16) · ld_check 1.0 · coloc explicitly "not available" |
| context / provenance | — | 64 outcomes for this protein · pQTL dataset v3.0 · URL |

And the honest-absence case (PNPLA3 × MASLD): v0.1 said "placeholder, not built"
(a statement about the tool); v0.2 says "no plasma pQTL instrument for this protein;
absence of an estimate is not evidence of no effect" (a statement about the world,
actionable: liver eQTL instruments would be needed).

**Added**
- `ledger.py`: captures every tool call's arguments and verbatim return (Gemini's
  automatic function calling otherwise executes tools inside the SDK and the results
  vanish — the card was previously written from the model's memory of them).
- `render.py`: evidence table, caveats, sources, provenance and the **MR-direction
  sentence** rendered mechanically. The model writes only a verdict line and one
  reasoning paragraph.
- `validate_card.py` + `test_validator.py` (29 regression cases): fails the run on
  unsupported numbers/rsIDs/accessions (compared numerically, tolerant of honest
  rounding and "over N" bounds), unearned qualitative and clinical-status claims,
  causal language without a matching MR estimate, and any therapeutic-direction claim
  contradicting sign(beta).
- `--batch` mode and a **claim-density metric** printed alongside pass rate (a model
  that stops making checkable claims can pass everything; density exposes that).

**Fixed** (each found by running, not by reading)
- GWAS Catalog tool read page 1 of 3: PNPLA3 reported 52 unique SNPs, truth is
  **114 from 256/256 rows**; `sweep_complete` now states whether a count is total or
  a lower bound.
- `api.pharmgkb.org` no longer resolves at all — the resource now serves as ClinPGx;
  migrated, and a 404 there is treated as a negative result, not a failure.
- ClinVar pathogenic count was taken over 30 records but reported over a denominator
  of 5; both now come from the same set.
- The validator's own first version accepted a fabricated p=1.2e-45 (substring
  matching); numbers are now compared numerically.

**Audit.** An adversarial audit (41 agents; every allegation re-checked by an
independent skeptic) confirmed 18 defects the token-level validator missed (recall
0/18), the worst being a sign inversion: the IL6R × CHD card quoted beta = −0.0442
correctly and recommended the opposite intervention. The direction sentence is now
mechanical and a direction lock rejects contradicting runs.

## v0.1 — 2026-07-13 · Round 1+2 (merged to `main`, PR #7)

- Gemini tool-calling agent (`google-genai`, automatic function calling) + 8 tools:
  UniProt, Open Targets, ChEMBL, ClinVar, gnomAD, GWAS Catalog, PharmGKB, and a
  **declared MR stub** (`{"stub": true}` — labelled placeholder, never presented as
  real). One generated card (PNPLA3 × MASLD). The model wrote the entire card.
- Known limitations, all addressed in v0.2: model-written numbers could drift
  (the card said "51 unique GWAS SNPs" — the tool had returned 52, and the true count
  was 114), tool-declared caveats could be dropped, no validation of model prose.

---

### Comparing versions (the objective yardstick)

Git keeps every prior version — old results need no manual archiving:

```bash
git show main:tools/mr.py            # the v0.1 stub, verbatim
git show main:cards/PNPLA3_MASLD_causal_card.md   # the v0.1 card
git log --oneline --all              # the full version story
```

To reproduce a comparison: check out any two versions of a tool, run both on the same
input, and diff the outputs. Upgrades in this project are judged by that diff, not by
intent.
