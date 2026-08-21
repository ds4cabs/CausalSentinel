# Protein Dossier — PPP3CA;PPP3R1

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Inflammatory bowel disease | 0.167 | 0.0293 | 1.18e-08 | Wald ratio | 1 | cis | NA |
| Crohn's disease | 0.185 | 0.0354 | 1.88e-07 | Wald ratio | 1 | cis | NA |
| Ulcerative colitis | 0.144 | 0.0369 | 9.24e-05 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | 0.0222 | 0.00696 | 0.00144 | Wald ratio | 1 | cis | NA |
| Diastolic blood pressure  automated reading | -0.0227 | 0.00713 | 0.00146 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K40 Inguinal hernia | 0.117 | 0.0379 | 0.00194 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: H25 Senile cataract | 0.196 | 0.0655 | 0.00278 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: osteoarthritis | 0.064 | 0.0219 | 0.00339 | Wald ratio | 1 | cis | NA |
| Body fat | 0.0459 | 0.0158 | 0.00357 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N40 Hyperplasia of prostate | 0.173 | 0.0612 | 0.00481 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | -0.0949 | 0.0341 | 0.00534 | Wald ratio | 1 | cis | NA |
| Rheumatoid arthritis | -0.107 | 0.04 | 0.00772 | Wald ratio | 1 | cis | NA |
| _...and 115 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_154 association rows across 108 traits (122 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Bone mineral density mean | 1e-300 | rs147187441 | 1 | GCST90321120 | no MR -> candidate analysis |
| CB1 cannabinoid receptor-interacting protein 1 levels | 3e-243 | rs7578047 | 2 | GCST90247079 | no MR -> candidate analysis |
| Height | 5e-140 | rs6733029 | 7 | GCST90245848 | MR: beta=-0.00869, p=0.302 (cis) |
| Varicose veins | 4e-36 | rs7569914 | 4 | GCST90018939 | MR: beta=-0.0697, p=0.182 (cis) |
| Diastolic blood pressure | 1e-24 | rs1527351 | 7 | GCST90310295 | MR: beta=-0.0227, p=0.00146 (cis) |
| Platelet distribution width | 3e-22 | rs13033725 | 1 | GCST90002401 | no MR -> candidate analysis |
| Height (baseline) | 6e-22 | rs75483778 | 2 | GCST90565843 | no MR -> candidate analysis |
| Height (maximum, inv-normal transformed) | 2e-21 | rs58916116 | 1 | GCST90479634 | no MR -> candidate analysis |
| height (mean, inv-normal transformed) | 2e-21 | rs58916116 | 1 | GCST90479635 | no MR -> candidate analysis |
| CD5L protein levels | 1e-19 | rs865020 | 1 | GCST90468640 | no MR -> candidate analysis |
| height (minimum, inv-normal transformed) | 4e-19 | rs58916116 | 1 | GCST90479636 | no MR -> candidate analysis |
| Physical function (baseline) | 4e-18 | rs75483778 | 1 | GCST90565837 | no MR -> candidate analysis |
| _...and 96 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Calcineurin subunit B type 1) |
| gnomAD constraint | not available |
| GWAS Catalog | no mapped SNPs |
| ClinVar | no records |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`uniprot`** — No reviewed human UniProt entry for 'PPP3CA;PPP3R1'.
- **`phenome`** — Could not resolve target 'PPP3CA;PPP3R1'.
- **`chembl`** — ChEMBL target matched by text search on 'PPP3CA;PPP3R1' and resolved to 'Calcineurin subunit B type 1' — confirm this is the intended target.
- **`gnomad`** — No gnomAD constraint data.
- **`gwas`** — No GWAS Catalog SNPs mapped to this gene.
- **`clinvar`** — No ClinVar records.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 108 traits by best p-value, aggregated from 154 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2082/ — _ChEMBL_37 (released 2026-05-01)_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PPP3CA;PPP3R1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:34:55  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
