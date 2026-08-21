# Protein Dossier — FTL;FTH1

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Total cholesterol | -0.109 | 0.00897 | 4.48e-34 | Wald ratio | 1 | trans | 1 |
| LDL cholesterol | -0.104 | 0.00935 | 7.76e-29 | Wald ratio | 1 | trans | 1 |
| Non-cancer illness code  self-reported: high cholesterol | -0.123 | 0.0177 | 3.97e-12 | Wald ratio | 1 | trans | 0.997 |
| Height | 0.0458 | 0.00725 | 2.69e-10 | Wald ratio | 1 | trans | 0.999 |
| Transferrin | -0.0817 | 0.0242 | 7.51e-04 | Wald ratio | 1 | trans | NA |
| Triglycerides | -0.0282 | 0.0084 | 7.69e-04 | Wald ratio | 1 | trans | NA |
| Forced vital capacity (FVC) | 0.015 | 0.00476 | 0.00159 | Wald ratio | 1 | trans | NA |
| Forced expiratory volume in 1-second (FEV1) | 0.0153 | 0.00502 | 0.00231 | Wald ratio | 1 | trans | NA |
| HDL cholesterol | -0.0242 | 0.00859 | 0.00477 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: K80 Cholelithiasis | -0.125 | 0.0458 | 0.00648 | Wald ratio | 1 | trans | NA |
| Rheumatoid arthritis | -0.0779 | 0.0304 | 0.0105 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: N81 Female genital prolapse | 0.11 | 0.0435 | 0.0111 | Wald ratio | 1 | trans | NA |
| _...and 103 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_897 association rows across 109 traits (873 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Omega-3 fatty acids to total fatty acids percentage | 3e-70 | rs11230850 | 121 | GCST90502082 | no MR -> candidate analysis |
| Pallidum iron levels (R2* MRI) | 3e-64 | rs10736716 | 1 | GCST90551868 | no MR -> candidate analysis |
| Omega-3 fatty acids to Omega-6 fatty acids ratio | 6e-60 | rs760405491 | 111 | GCST90502069 | no MR -> candidate analysis |
| Degree of unsaturation | 1e-59 | rs4343027 | 114 | GCST90502225 | no MR -> candidate analysis |
| Omega-3 fatty acid levels | 3e-56 | rs259874 | 97 | GCST90502064 | no MR -> candidate analysis |
| Docosahexaenoic acid levels | 5e-39 | rs4534592 | 71 | GCST90501978 | no MR -> candidate analysis |
| Docosahexaenoic acid to total fatty acids percentage | 3e-33 | rs11230850 | 62 | GCST90501991 | no MR -> candidate analysis |
| Caudate iron levels (R2* MRI) | 4e-33 | rs6591679 | 1 | GCST90551864 | no MR -> candidate analysis |
| Pallidum iron levels (quantitative susceptibility mapping) | 7e-33 | rs12786452 | 1 | GCST90551867 | no MR -> candidate analysis |
| Linoleic acid levels | 9e-33 | rs56215258 | 19 | GCST90502311 | no MR -> candidate analysis |
| Thalamus iron levels (quantitative susceptibility mapping) | 2e-30 | rs12793372 | 1 | GCST90551873 | no MR -> candidate analysis |
| Putamen iron levels (R2* MRI) | 2e-29 | rs56215258 | 1 | GCST90551870 | no MR -> candidate analysis |
| _...and 97 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Ferritin heavy chain) |
| gnomAD constraint | not available |
| GWAS Catalog | no mapped SNPs |
| ClinVar | no records |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`uniprot`** — No reviewed human UniProt entry for 'FTL;FTH1'.
- **`phenome`** — Could not resolve target 'FTL;FTH1'.
- **`chembl`** — ChEMBL target matched by text search on 'FTL;FTH1' and resolved to 'Ferritin heavy chain' — confirm this is the intended target.
- **`gnomad`** — No gnomAD constraint data.
- **`gwas`** — No GWAS Catalog SNPs mapped to this gene.
- **`clinvar`** — No ClinVar records.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 109 traits by best p-value, aggregated from 897 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL6066220/ — _ChEMBL_37 (released 2026-05-01)_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/FTL;FTH1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:44:06  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
