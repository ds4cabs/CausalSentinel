# Protein Dossier — NRCAM (Neuronal cell adhesion molecule)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: high cholesterol | -0.216 | 0.0503 | 1.70e-05 | Wald ratio | 1 | trans | NA |
| Platelet count | -9.43 | 2.54 | 2.00e-04 | Wald ratio | 1 | trans | NA |
| Forced vital capacity (FVC) | 0.0432 | 0.0122 | 4.21e-04 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: hypertension | -0.0991 | 0.0281 | 4.25e-04 | Wald ratio | 1 | trans | NA |
| Rheumatoid arthritis | -0.36 | 0.105 | 5.79e-04 | Wald ratio | 1 | trans | NA |
| Systolic blood pressure  automated reading | -0.0504 | 0.0153 | 9.59e-04 | Wald ratio | 1 | trans | NA |
| Forced expiratory volume in 1-second (FEV1) | 0.0418 | 0.0129 | 0.0012 | Wald ratio | 1 | trans | NA |
| Schizophrenia | 0.204 | 0.0667 | 0.00225 | Wald ratio | 1 | trans | NA |
| Alcohol intake frequency | -0.0655 | 0.0221 | 0.00299 | Wald ratio | 1 | trans | NA |
| Body mass index (BMI) | -0.0427 | 0.0149 | 0.00421 | Wald ratio | 1 | trans | NA |
| Ischemic stroke | -0.278 | 0.101 | 0.00596 | Wald ratio | 1 | trans | NA |
| Diastolic blood pressure  automated reading | -0.0384 | 0.0153 | 0.0121 | Wald ratio | 1 | trans | NA |
| _...and 94 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5109_24_3` | Nr-CAM | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_63 association rows across 27 traits (49 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| IL6ST/NRCAM protein level ratio | 7e-493 | rs10953562 | 1 | GCST90315168 | no MR -> candidate analysis |
| Circulating NRCAM levels | 4e-467 | rs12056165 | 8 | GCST90859739 | no MR -> candidate analysis |
| NRCAM/NTRK2 protein level ratio | 5e-450 | rs10953562 | 1 | GCST90315552 | no MR -> candidate analysis |
| LAMB1 protein levels | 5e-167 | rs111638202 | 15 | GCST90469732 | no MR -> candidate analysis |
| NRCAM protein levels | 1e-36 | rs368131 | 11 | GCST90470082 | no MR -> candidate analysis |
| Somatostatin-28 levels | 3e-19 | rs3833683 | 1 | GCST90162478 | no MR -> candidate analysis |
| Blood protein levels | 6e-14 | rs10487851 | 2 | GCST010104 | no MR -> candidate analysis |
| Diastolic blood pressure | 2e-11 | rs1269663 | 2 | GCST90132904 | MR: beta=-0.0384, p=0.0121 (trans) |
| Protein quantitative trait loci (liver) | 6e-10 | rs117789043 | 1 | GCST011427 | no MR -> candidate analysis |
| Height | 7e-10 | rs12333431 | 1 | GCST90245848 | MR: beta=0.0191, p=0.301 (trans) |
| Weight | 2e-9 | rs73201511 | 2 | GCST90662910 | MR: beta=-0.0202, p=0.126 (trans) |
| Diastolic blood pressure (MTAG) | 2e-9 | rs12536606 | 1 | GCST90449057 | no MR -> candidate analysis |
| _...and 15 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1366 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| neurodevelopmental disorder with neuromuscular and skeletal abnormalities | 0.915 | — | established (curated) | no MR -> candidate analysis |
| complex neurodevelopmental disorder | 0.608 | — | established (curated) | no MR -> candidate analysis |
| stroke disorder | 0.468 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.468 | — | common-variant locus | no MR -> candidate analysis |
| ovarian neoplasm | 0.468 | — | common-variant locus | no MR -> candidate analysis |
| Raynaud disease | 0.425 | — | common-variant locus | no MR -> candidate analysis |
| liver disorder | 0.425 | — | common-variant locus | no MR -> candidate analysis |
| hereditary disease | 0.319 | — | established (curated) | no MR -> candidate analysis |
| ocular hypotension | 0.295 | — | common-variant locus | no MR -> candidate analysis |
| myopia | 0.156 | — | established (curated) | no MR -> candidate analysis |
| pathological myopia | 0.182 | — | established (curated) | no MR -> candidate analysis |

> Of the 11 rows above, **11 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=2.6e-11, LOEUF=0.636 — LoF-tolerant |
| GWAS Catalog | 78 unique SNPs / 156 rows |
| ClinVar | 288 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1366 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'NRCAM'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 288 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 27 traits by best p-value, aggregated from 63 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q92823 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000091129/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/NRCAM — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/NRCAM — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=NRCAM%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/NRCAM — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:04:20  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
