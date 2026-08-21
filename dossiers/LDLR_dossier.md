# Protein Dossier — LDLR (Low-density lipoprotein receptor)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: high cholesterol | -0.174 | 0.0363 | 1.57e-06 | Wald ratio | 1 | trans | NA |
| Forced expiratory volume in 1-second (FEV1) | 0.0378 | 0.00974 | 1.04e-04 | Wald ratio | 1 | trans | NA |
| Forced vital capacity (FVC) | 0.033 | 0.00923 | 3.57e-04 | Wald ratio | 1 | trans | NA |
| Systolic blood pressure  automated reading | -0.0378 | 0.0115 | 0.00102 | Wald ratio | 1 | trans | NA |
| Body mass index (BMI) | -0.0332 | 0.0113 | 0.00313 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: R10 Abdominal and pelvic pain | -0.161 | 0.0642 | 0.0122 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: hypertension | -0.0506 | 0.0202 | 0.0122 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: I48 Atrial fibrillation and flutter | 0.212 | 0.087 | 0.0151 | Wald ratio | 1 | trans | NA |
| Bulimia nervosa | -0.0787 | 0.0324 | 0.0152 | Wald ratio | 1 | trans | NA |
| Endometrioid ovarian cancer | -0.336 | 0.139 | 0.0158 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: emphysema or chronic bronchitis | -0.311 | 0.136 | 0.0222 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: C50 Malignant neoplasm of breast | -0.258 | 0.116 | 0.0258 | Wald ratio | 1 | trans | NA |
| _...and 65 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_1403 association rows across 670 traits (1363 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Low density lipoprotein cholesterol levels | 9e-2305 | rs73015024 | 49 | GCST90239655 | no MR -> candidate analysis |
| Total cholesterol levels | 2e-1793 | rs73015024 | 61 | GCST90239673 | no MR -> candidate analysis |
| Non-HDL cholesterol levels | 8e-1498 | rs73015024 | 7 | GCST90239667 | no MR -> candidate analysis |
| Apolipoprotein B levels | 9e-830 | rs6511720 | 25 | GCST90019496 | no MR -> candidate analysis |
| LDL cholesterol | 2e-522 | rs147985405 | 13 | GCST90018961 | no MR -> candidate analysis |
| Low-density lipoprotein levels | 5e-380 | rs17242381 | 2 | GCST90662892 | no MR -> candidate analysis |
| Cholesteryl Esters in Medium VLDL | 3e-340 | rs12151108 | 3 | GCST90501208 | no MR -> candidate analysis |
| Phospholipids in IDL | 2e-327 | rs12151108 | 4 | GCST90501129 | no MR -> candidate analysis |
| Free cholesterol in IDL | 6e-321 | rs12151108 | 3 | GCST90501125 | no MR -> candidate analysis |
| High cholesterol | 1e-320 | rs12151108 | 6 | GCST90475205 | MR: beta=-0.174, p=1.57e-06 (trans) |
| Concentration of IDL particles | 5e-319 | rs12151108 | 8 | GCST90501128 | no MR -> candidate analysis |
| Free cholesterol in small LDL | 7e-311 | rs73015024 | 4 | GCST90501250 | no MR -> candidate analysis |
| _...and 658 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1670 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| hypercholesterolemia, familial, 1 | 0.991 | — | established (curated) | no MR -> candidate analysis |
| Hypercholesterolemia | 0.974 | 0.987 | established (curated) | MR: beta=-0.174, p=1.57e-06 (trans) |
| familial hypercholesterolemia | 0.941 | 0.953 | established (curated) | no MR -> candidate analysis |
| homozygous familial hypercholesterolemia | 0.868 | — | established (curated) | no MR -> candidate analysis |
| coronary artery disorder | 0.973 | 0.978 | multi-layer: burden+GWAS (allelic-series candidate) | no MR -> candidate analysis |
| metabolic disease | 0.977 | 0.983 | multi-layer: burden+GWAS (allelic-series candidate) | no MR -> candidate analysis |
| heart disorder | 0.936 | 0.951 | multi-layer: burden+GWAS (allelic-series candidate) | no MR -> candidate analysis |
| hyperlipidemia | 0.853 | 0.615 | established (curated) | no MR -> candidate analysis |
| angina pectoris | 0.907 | 0.842 | multi-layer: burden+GWAS (allelic-series candidate) | no MR -> candidate analysis |
| Disorder of lipid metabolism | 0.905 | 0.936 | multi-layer: burden+GWAS (allelic-series candidate) | no MR -> candidate analysis |
| metabolic syndrome | 0.89 | — | established (curated) | no MR -> candidate analysis |
| myocardial infarction | 0.9 | 0.731 | multi-layer: burden+GWAS (allelic-series candidate) | MR: beta=-0.04, p=0.41 (trans) |
| cardiovascular disorder | 0.796 | 0.257 | multi-layer: burden+GWAS (allelic-series candidate) | no MR -> candidate analysis |
| coronary atherosclerosis | 0.921 | — | common-variant locus | no MR -> candidate analysis |
| Other metabolic disease | 0.93 | 0.93 | exploratory rare-variant signal | no MR -> candidate analysis |

> Of the 15 rows above, **13 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 4 exploratory rare-variant signal(s), 8 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Low-density lipoprotein receptor) |
| gnomAD constraint | pLI=1.3e-32, LOEUF=1.12 — LoF-tolerant |
| GWAS Catalog | 203 unique SNPs / 528 rows |
| ClinVar | 4921 records; 15 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 6 clinical annotations across 6 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1670 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'LDLR' and resolved to 'Low-density lipoprotein receptor' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 4921 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 20 of 670 traits by best p-value, aggregated from 1403 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P01130 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000130164/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3311/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/LDLR — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/LDLR — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=LDLR%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=LDLR — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/LDLR — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:28:53  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
