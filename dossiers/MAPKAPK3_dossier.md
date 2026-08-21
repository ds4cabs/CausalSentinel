# Protein Dossier — MAPKAPK3 (MAP kinase-activated protein kinase 3)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: gout | 0.0475 | 0.0192 | 0.0131 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | -0.0722 | 0.0307 | 0.0186 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: bladder problem (not cancer) | 0.0618 | 0.0295 | 0.0366 | Wald ratio | 1 | trans | NA |
| Hirschsprung's disease | -0.299 | 0.146 | 0.04 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: pernicious anaemia | -0.0998 | 0.0489 | 0.0411 | Wald ratio | 1 | trans | NA |
| Body fat | -0.0109 | 0.00534 | 0.042 | Wald ratio | 1 | trans | NA |
| Underlying (primary) cause of death: ICD10: E85.4 Organ-limited amyloidosis | 0.643 | 0.317 | 0.0425 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: G47 Sleep disorders | 0.0582 | 0.0295 | 0.0483 | Wald ratio | 1 | trans | NA |
| Neo-neuroticism | 0.182 | 0.0929 | 0.0504 | Wald ratio | 1 | trans | NA |
| Neo-agreeableness | -0.116 | 0.06 | 0.0526 | Wald ratio | 1 | trans | NA |
| Lung cancer | 0.0335 | 0.0185 | 0.0701 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: hypertension | 0.00733 | 0.00405 | 0.0708 | Wald ratio | 1 | trans | NA |
| _...and 105 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3822_54_2` | MAPKAPK3 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_24 association rows across 22 traits (22 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Hematological traits (multi-trait analysis) | 8e-31 | rs34492910 | 1 | GCST90838669 | no MR -> candidate analysis |
| MME/NT5E protein level ratio | 6e-25 | rs112256201 | 1 | GCST90315460 | no MR -> candidate analysis |
| BAIAP2/MME protein level ratio | 3e-23 | rs112256201 | 1 | GCST90313453 | no MR -> candidate analysis |
| BST2/MME protein level ratio | 3e-23 | rs112256201 | 1 | GCST90313539 | no MR -> candidate analysis |
| SPINK8 protein levels | 4e-19 | rs74422202 | 2 | GCST90470726 | no MR -> candidate analysis |
| eosinophil (absolute count, maximum, inv-norm transformed) | 5e-17 | rs809451 | 1 | GCST90479601 | no MR -> candidate analysis |
| Reticulocyte percentage (UKB data field 30240) | 7e-17 | rs114292886 | 1 | GCST90468101 | no MR -> candidate analysis |
| Reticulocyte count (UKB data field 30250) | 3e-16 | rs114292886 | 1 | GCST90468100 | no MR -> candidate analysis |
| Educational attainment (MTAG) | 2e-15 | rs11716398 | 1 | GCST006571 | no MR -> candidate analysis |
| Educational attainment (years of education) | 2e-14 | rs11716398 | 1 | GCST006442 | no MR -> candidate analysis |
| Educational attainment | 3e-14 | rs4261877 | 1 | GCST90105038 | no MR -> candidate analysis |
| Total cholesterol levels | 2e-9 | rs41308269 | 1 | GCST90239676 | no MR -> candidate analysis |
| _...and 10 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 133 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| patterned macular dystrophy 3 | 0.615 | — | established (curated) | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.312 | — | common-variant locus | no MR -> candidate analysis |
| Retinal dystrophy | 0.182 | — | established (curated) | no MR -> candidate analysis |
| Alzheimer disease | 0.179 | — | common-variant locus | no MR -> candidate analysis |
| placental abruption | 0.117 | — | common-variant locus | no MR -> candidate analysis |
| schizophrenia | 0.115 | — | common-variant locus | MR: beta=-0.00924, p=0.383 (trans) |
| cystitis | 0.106 | — | common-variant locus | no MR -> candidate analysis |
| breast cancer | 0.068 | — | common-variant locus | MR: beta=0.00562, p=0.369 (trans) |
| mathematical ability | 0.066 | — | common-variant locus | no MR -> candidate analysis |

> Of the 9 rows above, **7 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (MAP kinase-activated protein kinase 3) |
| gnomAD constraint | pLI=5.3e-09, LOEUF=0.943 — LoF-tolerant |
| GWAS Catalog | 58 unique SNPs / 116 rows |
| ClinVar | 335 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 133 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'MAPKAPK3' and resolved to 'MAP kinase-activated protein kinase 3' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 335 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 22 traits by best p-value, aggregated from 24 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q16644 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000114738/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4670/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/MAPKAPK3 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/MAPKAPK3 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=MAPKAPK3%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/MAPKAPK3 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:44:28  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
