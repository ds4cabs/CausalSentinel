# Protein Dossier — GNMT (Glycine N-methyltransferase)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Creatinine (enzymatic) in urine | 0.0182 | 0.00578 | 0.00159 | Wald ratio | 1 | cis | NA |
| Sodium in urine | 0.0182 | 0.00594 | 0.00216 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I80 Phlebitis and thrombophlebitis | 0.195 | 0.0731 | 0.00774 | Wald ratio | 1 | cis | NA |
| ER-positive Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.0478 | 0.0185 | 0.00985 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K20 Oesophagitis | 0.134 | 0.0535 | 0.0124 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K80 Cholelithiasis | 0.0949 | 0.0383 | 0.0131 | Wald ratio | 1 | cis | NA |
| Coronary heart disease | 0.0532 | 0.0234 | 0.0233 | Wald ratio | 1 | cis | NA |
| Birth weight | -0.0205 | 0.00925 | 0.0267 | Wald ratio | 1 | cis | NA |
| Hearing difficulty or problems: Yes | 0.0221 | 0.0102 | 0.0303 | Wald ratio | 1 | cis | NA |
| Pulse rate | -0.0229 | 0.0107 | 0.032 | Wald ratio | 1 | cis | NA |
| Lung adenocarcinoma | 0.151 | 0.0732 | 0.0389 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R10 Abdominal and pelvic pain | 0.0546 | 0.0276 | 0.048 | Wald ratio | 1 | cis | NA |
| _...and 70 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_22 association rows across 20 traits (22 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Total lipids in small HDL | 1e-43 | rs10948059 | 1 | GCST90501240 | no MR -> candidate analysis |
| Cholesterol in Small HDL | 6e-31 | rs10948059 | 1 | GCST90501234 | no MR -> candidate analysis |
| Concentration of small HDL particles | 6e-30 | rs10948059 | 1 | GCST90501241 | no MR -> candidate analysis |
| X-11564 levels | 3e-25 | rs4987173 | 1 | GCST90245508 | no MR -> candidate analysis |
| Sarcosine (N-Methylglycine) levels | 3e-21 | rs575786265 | 1 | GCST90245410 | no MR -> candidate analysis |
| Free cholesterol in small HDL | 8e-21 | rs10948059 | 2 | GCST90501238 | no MR -> candidate analysis |
| Phospholipids in small HDL | 3e-18 | rs2296804 | 1 | GCST90302087 | no MR -> candidate analysis |
| Concentration of medium HDL particles | 7e-16 | rs2296804 | 1 | GCST90302038 | no MR -> candidate analysis |
| Total lipids in medium HDL | 9e-16 | rs2296804 | 1 | GCST90302037 | no MR -> candidate analysis |
| Cholesterol esters in medium HDL | 3e-15 | rs2296804 | 1 | GCST90302033 | no MR -> candidate analysis |
| Phospholipids in medium HDL | 5e-15 | rs2296804 | 1 | GCST90302039 | no MR -> candidate analysis |
| Degree of unsaturation | 5e-15 | rs2296805 | 1 | GCST90502233 | no MR -> candidate analysis |
| _...and 8 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 613 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| glycine N-methyltransferase deficiency | 0.798 | — | established (curated) | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Glycine N-methyltransferase) |
| gnomAD constraint | not available |
| GWAS Catalog | 79 unique SNPs / 158 rows |
| ClinVar | 158 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 1 clinical annotations across 1 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 613 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'GNMT' and resolved to 'Glycine N-methyltransferase' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 158 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 20 of 20 traits by best p-value, aggregated from 22 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q14749 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000124713/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4523295/ — _ChEMBL_37 (released 2026-05-01)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/GNMT — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=GNMT%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=GNMT — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/GNMT — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:51:01  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: gnomad
