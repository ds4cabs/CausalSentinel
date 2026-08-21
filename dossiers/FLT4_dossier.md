# Protein Dossier — FLT4 (Vascular endothelial growth factor receptor 3)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| HbA1C | -0.0158 | 0.00508 | 0.00184 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: H25 Senile cataract | 0.00093 | 0.000299 | 0.00187 | Inverse variance weighted | 2 | trans | NA |
| Diagnoses - main ICD10: H25 Senile cataract | 0.00093 | 0.000299 | 0.00187 | Inverse variance weighted | 2 | cis | NA |
| Hirschsprung's disease | -0.577 | 0.196 | 0.00319 | Wald ratio | 1 | trans | NA |
| Thalamus volume | 24.8 | 9.26 | 0.00733 | Wald ratio | 1 | trans | NA |
| Type 2 diabetes | -0.057 | 0.0214 | 0.00772 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: G47 Sleep disorders | -0.000676 | 0.000261 | 0.00969 | Inverse variance weighted | 2 | trans | NA |
| Diagnoses - main ICD10: G47 Sleep disorders | -0.000676 | 0.000261 | 0.00969 | Inverse variance weighted | 2 | cis | NA |
| Diagnoses - main ICD10: Z09 Follow-up examination after treatment for conditions other than malignant neoplasms | -0.00107 | 0.000416 | 0.00998 | Inverse variance weighted | 2 | trans | NA |
| Diagnoses - main ICD10: Z09 Follow-up examination after treatment for conditions other than malignant neoplasms | -0.00107 | 0.000416 | 0.00998 | Inverse variance weighted | 2 | cis | NA |
| Age at menopause | -0.0726 | 0.0291 | 0.0124 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: vitiligo | 0.000141 | 5.69e-05 | 0.0129 | Inverse variance weighted | 2 | trans | NA |
| _...and 148 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2358_19_2` | VEGF sR3 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_37 association rows across 24 traits (31 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating FLT4 levels | 3e-608 | rs34221241 | 4 | GCST90860081 | no MR -> candidate analysis |
| FLT4/ICAM2 protein level ratio | 3e-516 | rs34221241 | 1 | GCST90314860 | no MR -> candidate analysis |
| FLT4/KDR protein level ratio | 3e-498 | rs34221241 | 1 | GCST90314861 | no MR -> candidate analysis |
| FLT4 protein levels | 7e-73 | rs307813 | 7 | GCST90469252 | no MR -> candidate analysis |
| SCGB3A1 protein levels | 5e-71 | rs307802 | 2 | GCST90470542 | no MR -> candidate analysis |
| Serum levels of protein FLT4 | 5e-33 | rs34221241 | 1 | GCST90087934 | no MR -> candidate analysis |
| Secretoglobin family 3A member 1 levels | 1e-24 | rs307802 | 1 | GCST90249510 | no MR -> candidate analysis |
| Vascular endothelial growth factor receptor 3 levels (FLT4.2 | 2e-19 | rs34221241 | 1 | GCST90243324 | no MR -> candidate analysis |
| Vascular endothelial growth factor receptor 3 levels | 1e-17 | rs34221241 | 2 | GCST90161351 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 6e-16 | rs10065018 | 1 | GCST90838669 | no MR -> candidate analysis |
| Platelet count | 3e-13 | rs10065018 | 2 | GCST90002357 | MR: beta=-0.725, p=0.239 (trans) |
| Albumin levels | 6e-11 | rs62407083 | 1 | GCST90662901 | no MR -> candidate analysis |
| _...and 12 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 980 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| lymphatic malformation 1 | 0.951 | — | established (curated) | no MR -> candidate analysis |
| congenital heart defects, multiple types, 7 | 0.891 | — | established (curated) | no MR -> candidate analysis |
| Milroy disease | 0.852 | — | established (curated) | no MR -> candidate analysis |
| capillary infantile hemangioma | 0.715 | — | established (curated) | no MR -> candidate analysis |
| neoplasm | 0.195 | — | established (curated) | MR: beta=-0.00107, p=0.00998 (trans) |
| colorectal cancer | 0.012 | — | established (curated) | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.834 | — | common-variant locus | no MR -> candidate analysis |
| hereditary disease | 0.83 | — | established (curated) | no MR -> candidate analysis |

> Of the 8 rows above, **7 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 1 known modulators (Vascular endothelial growth factor C) |
| gnomAD constraint | pLI=1, LOEUF=0.249 — LoF-INTOLERANT |
| GWAS Catalog | 41 unique SNPs / 82 rows |
| ClinVar | 657 records; 8 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 2 clinical annotations across 1 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 980 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'FLT4' and resolved to 'Vascular endothelial growth factor C' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 657 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 20 of 24 traits by best p-value, aggregated from 37 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P35916 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000037280/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3714157/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/FLT4 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/FLT4 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=FLT4%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=FLT4 — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/FLT4 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:41:54  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
