# Protein Dossier — PROC (Vitamin K-dependent protein C)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: deep venous thrombosis (dvt) | 0.191 | 0.0297 | 1.27e-10 | Wald ratio | 1 | trans | NA |
| Height | 0.0334 | 0.00585 | 1.10e-08 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: I80 Phlebitis and thrombophlebitis | 0.249 | 0.0581 | 1.84e-05 | Wald ratio | 1 | trans | NA |
| Coronary heart disease | -0.0725 | 0.0173 | 2.92e-05 | Wald ratio | 1 | trans | NA |
| Myocardial infarction | -0.0739 | 0.0192 | 1.13e-04 | Wald ratio | 1 | trans | NA |
| Creatinine (enzymatic) in urine | -0.0186 | 0.00485 | 1.27e-04 | Wald ratio | 1 | trans | NA |
| Body mass index (BMI) | -0.0193 | 0.00507 | 1.37e-04 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code self-reported: pulmonary embolism (with or without) dvt | 0.171 | 0.0474 | 3.03e-04 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: M72 Fibroblastic disorders | 0.194 | 0.057 | 6.86e-04 | Wald ratio | 1 | trans | NA |
| Heel bone mineral density (BMD) T-score  automated | -0.0222 | 0.00657 | 7.19e-04 | Wald ratio | 1 | trans | NA |
| Sodium in urine | -0.0135 | 0.00499 | 0.00669 | Wald ratio | 1 | trans | NA |
| Potassium in urine | -0.0138 | 0.00515 | 0.00737 | Wald ratio | 1 | trans | NA |
| _...and 114 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2961_1_2` | Protein C | Suhre K | 2019 |
| `prot-c-3758_68_3` | Activated Protein C | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_27 association rows across 13 traits (26 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating PROC levels | 1e-254 | rs1799809 | 4 | GCST90860431 | no MR -> candidate analysis |
| PROC protein levels | 1e-245 | rs1799810 | 5 | GCST90470335 | no MR -> candidate analysis |
| F9/PROC protein level ratio | 2e-231 | rs1799810 | 1 | GCST90314748 | no MR -> candidate analysis |
| Protein C levels | 2e-42 | rs1799810 | 2 | GCST006119 | no MR -> candidate analysis |
| Height | 4e-41 | rs7599210 | 1 | GCST90245848 | MR: beta=0.0334, p=1.10e-08 (trans) |
| Vitamin K-dependent protein C levels | 8e-32 | rs1799810 | 3 | GCST90250174 | no MR -> candidate analysis |
| Venous thromboembolism | 7e-29 | rs1158867 | 2 | GCST90244158 | no MR -> candidate analysis |
| Serum levels of protein PROC | 2e-22 | rs1799809 | 2 | GCST90088150 | no MR -> candidate analysis |
| Encounter for long-term (current) use of anticoagulants (Phe | 4e-19 | rs200045749 | 2 | GCST90479975 | no MR -> candidate analysis |
| Blood protein levels | 5e-13 | rs2069901 | 2 | GCST006585 | no MR -> candidate analysis |
| Coagulation defects (PheCode 286) | 2e-11 | rs200045749 | 1 | GCST90479980 | no MR -> candidate analysis |
| Takes medication for blood clot/ pulmonary embolism/ deep ve | 3e-11 | rs200045749 | 1 | GCST90479548 | no MR -> candidate analysis |
| _...and 1 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 423 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| hereditary thrombophilia due to congenital protein C deficiency | 0.929 | — | established (curated) | no MR -> candidate analysis |
| venous thromboembolism | 0.921 | 0.938 | multi-layer: burden+GWAS (allelic-series candidate) | no MR -> candidate analysis |
| deep vein thrombosis | 0.937 | 0.97 | multi-layer: burden+GWAS (allelic-series candidate) | no MR -> candidate analysis |
| thrombophilia due to protein C deficiency, autosomal dominant | 0.943 | — | established (curated) | no MR -> candidate analysis |
| protein c deficiency | 0.813 | — | established (curated) | no MR -> candidate analysis |
| thrombophilia due to protein C deficiency, autosomal recessive | 0.919 | — | established (curated) | no MR -> candidate analysis |
| phlebitis | 0.855 | 0.978 | multi-layer: burden+GWAS (allelic-series candidate) | MR: beta=0.249, p=1.84e-05 (trans) |
| Thrombophlebitis | 0.85 | 0.971 | multi-layer: burden+GWAS (allelic-series candidate) | MR: beta=0.249, p=1.84e-05 (trans) |
| Abnormal thrombosis | 0.829 | 0.896 | established (curated) | no MR -> candidate analysis |
| thrombophilia | 0.829 | 0.829 | exploratory rare-variant signal | no MR -> candidate analysis |
| blood coagulation disease | 0.667 | 0.628 | multi-layer: burden+GWAS (allelic-series candidate) | no MR -> candidate analysis |
| Portal vein thrombosis | 0.883 | 0.883 | exploratory rare-variant signal | no MR -> candidate analysis |
| Thromboembolism | 0.675 | — | established (curated) | no MR -> candidate analysis |
| hereditary disease | 0.759 | — | established (curated) | no MR -> candidate analysis |
| heart disorder | 0.709 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **13 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 6 exploratory rare-variant signal(s), 6 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 2 known modulators (Vitamin K-dependent protein C) |
| gnomAD constraint | pLI=7.3e-05, LOEUF=0.865 — LoF-tolerant |
| GWAS Catalog | 31 unique SNPs / 62 rows |
| ClinVar | 510 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 1 clinical annotations across 1 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 423 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'PROC' and resolved to 'Vitamin K-dependent protein C' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 510 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 13 of 13 traits by best p-value, aggregated from 27 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P04070 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000115718/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4444/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PROC — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PROC — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PROC%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=PROC — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PROC — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:36:55  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
