# Protein Dossier — RGMB (Repulsive guidance molecule B)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Creatinine (enzymatic) in urine | -0.0403 | 0.0108 | 1.87e-04 | Wald ratio | 1 | cis | NA |
| Potassium in urine | -0.0354 | 0.0114 | 0.00193 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | -0.0297 | 0.00976 | 0.00231 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | -0.0414 | 0.0146 | 0.00457 | Wald ratio | 1 | cis | NA |
| Neuroticism | -0.037 | 0.0139 | 0.00766 | Wald ratio | 1 | cis | NA |
| Height | -0.0356 | 0.0139 | 0.0103 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: G56 Mononeuropathies of upper limb | 0.184 | 0.0717 | 0.0103 | Wald ratio | 1 | cis | NA |
| Small vessel disease | -0.411 | 0.161 | 0.0106 | Wald ratio | 1 | cis | NA |
| Depressive symptoms | -0.0324 | 0.0139 | 0.0196 | Wald ratio | 1 | cis | NA |
| Myocardial infarction | -0.111 | 0.0486 | 0.0222 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M16 Coxarthrosis [arthrosis of hip] | -0.282 | 0.127 | 0.0262 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: enlarged prostate | 0.177 | 0.0813 | 0.029 | Wald ratio | 1 | cis | NA |
| _...and 115 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3331_8_1` | RGMB | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_16 association rows across 13 traits (15 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| RGMB protein levels | 1e-52 | rs1053451 | 2 | GCST90470464 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 1e-27 | rs79997895 | 2 | GCST90838669 | no MR -> candidate analysis |
| Height | 3e-21 | rs10479243 | 2 | GCST90245848 | MR: beta=-0.0356, p=0.0103 (cis) |
| RGM domain family member B levels | 1e-20 | rs11370451 | 1 | GCST90249294 | no MR -> candidate analysis |
| Forced expiratory volume in 1 second (FEV1) | 2e-14 | rs1508793 | 1 | GCST90705070 | no MR -> candidate analysis |
| Lung function (FEV1) | 2e-13 | rs2249797 | 1 | GCST90244092 | no MR -> candidate analysis |
| Appendicular lean mass | 4e-11 | rs331917 | 1 | GCST90000025 | no MR -> candidate analysis |
| Basophil percentage of granulocytes | 3e-10 | rs111887461 | 1 | GCST004634 | no MR -> candidate analysis |
| Hair color | 3e-9 | rs2617515 | 1 | GCST007082 | no MR -> candidate analysis |
| Depression severity  x hours spent watching television inter | 2e-8 | rs2662263 | 1 | GCST90101750 | no MR -> candidate analysis |
| Forced vital capacity (FVC) | 2e-8 | rs2249797 | 1 | GCST90705071 | MR: beta=-0.0122, p=0.188 (cis) |
| Hip minimal joint space width | 4e-8 | rs2545730 | 1 | GCST90281365 | no MR -> candidate analysis |
| _...and 1 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 140 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Abnormality of the skeletal system | 0.658 | — | common-variant locus | no MR -> candidate analysis |
| carpal tunnel syndrome | 0.586 | — | common-variant locus | no MR -> candidate analysis |
| benign prostatic hyperplasia | 0.536 | — | common-variant locus | no MR -> candidate analysis |
| Peyronie disease | 0.487 | — | common-variant locus | no MR -> candidate analysis |
| osteoarthritis | 0.482 | — | common-variant locus | MR: beta=-0.05, p=0.208 (cis) |
| frozen shoulder | 0.44 | — | common-variant locus | no MR -> candidate analysis |
| glomerulonephritis | 0.44 | — | common-variant locus | no MR -> candidate analysis |
| physical activity | 0.426 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.397 | — | common-variant locus | no MR -> candidate analysis |
| trauma complication | 0.387 | — | common-variant locus | no MR -> candidate analysis |
| cataract | 0.387 | — | common-variant locus | MR: beta=-0.0846, p=0.209 (cis) |
| placental retention | 0.387 | — | common-variant locus | no MR -> candidate analysis |
| Constipation | 0.362 | — | common-variant locus | no MR -> candidate analysis |
| hemorrhoid | 0.358 | — | common-variant locus | no MR -> candidate analysis |
| disorder of ear | 0.354 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **13 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.001, LOEUF=0.904 — LoF-tolerant |
| GWAS Catalog | 22 unique SNPs / 43 rows |
| ClinVar | 107 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 140 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'RGMB'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 107 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 13 of 13 traits by best p-value, aggregated from 16 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q6NW40 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000174136/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/RGMB — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/RGMB — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=RGMB%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/RGMB — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:49:15  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
