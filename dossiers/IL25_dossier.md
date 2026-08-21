# Protein Dossier — IL25 (Interleukin-25)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Weight | -0.0112 | 0.00322 | 4.85e-04 | Wald ratio | 1 | trans | NA |
| Body mass index (BMI) | -0.0121 | 0.00365 | 9.35e-04 | Wald ratio | 1 | trans | NA |
| High grade serous ovarian cancer | 0.0702 | 0.0238 | 0.00324 | Wald ratio | 1 | trans | NA |
| Thyroid cancer | -0.405 | 0.138 | 0.00333 | Wald ratio | 1 | trans | NA |
| Diastolic blood pressure  automated reading | 0.0108 | 0.00373 | 0.00377 | Wald ratio | 1 | trans | NA |
| Ovarian cancer | 0.0548 | 0.0201 | 0.00636 | Wald ratio | 1 | trans | NA |
| Hirschsprung's disease | -0.619 | 0.238 | 0.00935 | Wald ratio | 1 | trans | NA |
| Depressive symptoms | 0.0146 | 0.0061 | 0.0164 | Wald ratio | 1 | trans | NA |
| Systolic blood pressure  automated reading | 0.00891 | 0.00373 | 0.017 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: gout | -0.075 | 0.033 | 0.0231 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: M17 Gonarthrosis [arthrosis of knee] | -0.0605 | 0.0279 | 0.0303 | Wald ratio | 1 | trans | NA |
| Schizophrenia | 0.0351 | 0.0162 | 0.0304 | Wald ratio | 1 | trans | NA |
| _...and 91 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4137_57_2` | IL-17E | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_6 association rows across 6 traits (4 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Embryonal Fyn-associated substrate levels | 2e-12 | rs10137082 | 1 | GCST90247405 | no MR -> candidate analysis |
| Height (baseline) | 1e-11 | rs3759609 | 1 | GCST90565843 | no MR -> candidate analysis |
| PR interval | 7e-10 | rs11465506 | 1 | GCST007045 | no MR -> candidate analysis |
| Blood pressure (pleiotropy model 1 DBP adjusted for estimate | 3e-8 | rs146602111 | 1 | GCST90239828 | no MR -> candidate analysis |
| Type 1 diabetes | 6e-6 | rs10137082 | 1 | GCST001255 | no MR -> candidate analysis |
| Blood pressure (pleiotropy model 2 SBP adjusted for estimate | 8e-6 | rs146602111 | 1 | GCST90239829 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1020 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| atrial fibrillation | 0.053 | — | common-variant locus | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.0015, LOEUF=1.29 — LoF-tolerant |
| GWAS Catalog | 72 unique SNPs / 144 rows |
| ClinVar | 57 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1020 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'IL25'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 57 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 6 of 6 traits by best p-value, aggregated from 6 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9H293 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000166090/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/IL25 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/IL25 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=IL25%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/IL25 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:15:21  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
