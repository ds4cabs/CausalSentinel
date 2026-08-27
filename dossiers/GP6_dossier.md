# Protein Dossier — GP6 (Platelet glycoprotein VI)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Platelet count | -3.22 | 0.869 | 2.12e-04 | Wald ratio | 1 | cis | NA |
| Mean platelet volume | 0.00746 | 0.00213 | 4.65e-04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertrophic cardiomyopathy (hcm  or  hocm) | 0.624 | 0.19 | 0.00101 | Wald ratio | 1 | cis | NA |
| Gallbladder cancer | -2.43 | 0.925 | 0.00847 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | -0.0219 | 0.00845 | 0.00969 | Wald ratio | 1 | cis | NA |
| Alzheimer's disease | 0.0789 | 0.0349 | 0.0237 | Wald ratio | 1 | cis | NA |
| Systemic lupus erythematosus | -0.208 | 0.092 | 0.0241 | Wald ratio | 1 | cis | NA |
| Systolic blood pressure  automated reading | -0.011 | 0.00496 | 0.026 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: deep venous thrombosis (dvt) | 0.0701 | 0.0321 | 0.029 | Wald ratio | 1 | cis | NA |
| Putamen volume | -25.7 | 12.1 | 0.0342 | Wald ratio | 1 | cis | NA |
| Invasive mucinous ovarian cancer | 0.18 | 0.0857 | 0.0356 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: Z09 Follow-up examination after treatment for conditions other than malignant neoplasms | -0.0907 | 0.0433 | 0.0362 | Wald ratio | 1 | cis | NA |
| _...and 95 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3194_36_2` | GPVI | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_405 association rows across 351 traits (400 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| GP6/HPCAL1 protein level ratio | 4e-1824 | rs1613662 | 1 | GCST90314963 | no MR -> candidate analysis |
| GP6/SERPINB1 protein level ratio | 1e-1477 | rs1613662 | 1 | GCST90314972 | no MR -> candidate analysis |
| GP6/MPIG6B protein level ratio | 2e-1277 | rs1613662 | 1 | GCST90314968 | no MR -> candidate analysis |
| F2R/GP6 protein level ratio | 1e-1252 | rs1613662 | 1 | GCST90314730 | no MR -> candidate analysis |
| GP6/MIF protein level ratio | 2e-1234 | rs1613662 | 1 | GCST90314967 | no MR -> candidate analysis |
| GP6/TMSB10 protein level ratio | 2e-1190 | rs1613662 | 1 | GCST90314975 | no MR -> candidate analysis |
| DAG1/GP6 protein level ratio | 7e-1066 | rs1613662 | 1 | GCST90314375 | no MR -> candidate analysis |
| GP6/LGALS8 protein level ratio | 6e-1039 | rs1613662 | 1 | GCST90314964 | no MR -> candidate analysis |
| FYB1/GP6 protein level ratio | 7e-934 | rs1613662 | 1 | GCST90314909 | no MR -> candidate analysis |
| GP6/MANF protein level ratio | 2e-899 | rs1613662 | 1 | GCST90314965 | no MR -> candidate analysis |
| GP6/STIP1 protein level ratio | 6e-800 | rs1613662 | 1 | GCST90314974 | no MR -> candidate analysis |
| GP6/MESD protein level ratio | 5e-798 | rs1613662 | 1 | GCST90314966 | no MR -> candidate analysis |
| _...and 339 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 553 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| platelet-type bleeding disorder 11 | 0.825 | — | established (curated) | no MR -> candidate analysis |
| Bleeding diathesis due to glycoprotein VI deficiency | 0.73 | — | established (curated) | no MR -> candidate analysis |
| venous thromboembolism | 0.807 | — | common-variant locus | no MR -> candidate analysis |
| Thromboembolism | 0.725 | — | common-variant locus | no MR -> candidate analysis |
| platelet aggregation | 0.715 | — | common-variant locus | no MR -> candidate analysis |
| deep vein thrombosis | 0.6 | — | common-variant locus | no MR -> candidate analysis |
| hereditary disease | 0.318 | — | established (curated) | no MR -> candidate analysis |
| Abnormal bleeding | 0.24 | — | established (curated) | no MR -> candidate analysis |
| Thrombocytopenia | 0.182 | — | established (curated) | no MR -> candidate analysis |

> Of the 9 rows above, **9 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 1 known modulators (Platelet glycoprotein VI) |
| gnomAD constraint | pLI=2.2e-18, LOEUF=1.55 — LoF-tolerant |
| GWAS Catalog | 85 unique SNPs / 170 rows |
| ClinVar | 382 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 1 clinical annotations across 1 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 553 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'GP6' and resolved to 'Platelet glycoprotein VI' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 382 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 20 of 351 traits by best p-value, aggregated from 405 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9HCN6 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000088053/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3308912/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/GP6 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/GP6 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=GP6%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=GP6 — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/GP6 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:52:33  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
