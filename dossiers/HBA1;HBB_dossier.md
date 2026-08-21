# Protein Dossier — HBA1;HBB

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| LDL cholesterol | 0.176 | 0.0125 | 2.47e-45 | Wald ratio | 1 | trans | NA |
| Total cholesterol | 0.167 | 0.0119 | 1.13e-44 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: high cholesterol | 0.176 | 0.0189 | 8.14e-21 | Wald ratio | 1 | trans | NA |
| Weight | 0.0326 | 0.00734 | 8.87e-06 | Wald ratio | 1 | trans | NA |
| Triglycerides | 0.0501 | 0.0114 | 1.06e-05 | Wald ratio | 1 | trans | NA |
| Body mass index (BMI) | 0.0338 | 0.00831 | 4.88e-05 | Wald ratio | 1 | trans | NA |
| Myocardial infarction | 0.121 | 0.0329 | 2.50e-04 | Wald ratio | 1 | trans | NA |
| Coronary heart disease | 0.1 | 0.0297 | 7.15e-04 | Wald ratio | 1 | trans | NA |
| Childhood intelligence | -0.142 | 0.0442 | 0.00128 | Wald ratio | 1 | trans | NA |
| Red blood cell count | 0.02 | 0.00732 | 0.00613 | Wald ratio | 1 | trans | NA |
| Eye problems or disorders: Cataract | 0.107 | 0.0409 | 0.00878 | Wald ratio | 1 | trans | NA |
| Transferrin | 0.0889 | 0.0349 | 0.011 | Wald ratio | 1 | trans | NA |
| _...and 101 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_287 association rows across 141 traits (280 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| AHSP/HBQ1 protein level ratio | 5e-434 | rs8061637 | 2 | GCST90313216 | no MR -> candidate analysis |
| Hereditary hemolytic anemias (PheCode 282) | 1e-323 | rs334 | 3 | GCST90475778 | no MR -> candidate analysis |
| mean corpuscular hemoglobin (MCH, minimum, inv-norm transfor | 1e-323 | rs11549407 | 2 | GCST90479674 | no MR -> candidate analysis |
| mean corpuscular hemoglobin (MCH, mean, inv-norm transformed | 1e-323 | rs11549407 | 2 | GCST90479673 | no MR -> candidate analysis |
| mean corpuscular hemoglobin (MCH, maximum, inv-norm transfor | 1e-323 | rs11549407 | 2 | GCST90479672 | no MR -> candidate analysis |
| red cell diameter width (RDW, minimum, inv-norm transformed) | 1e-323 | rs11549407 | 3 | GCST90476365 | no MR -> candidate analysis |
| red blood cell count (RBC, mean, inv-norm transformed) | 1e-323 | rs11549407 | 2 | GCST90476349 | no MR -> candidate analysis |
| red cell diameter width (RDW, mean, inv-norm transformed) | 1e-323 | rs76462751 | 3 | GCST90476360 | no MR -> candidate analysis |
| red blood cell count (RBC, maximum, inv-norm transformed) | 1e-323 | rs11549407 | 2 | GCST90476345 | no MR -> candidate analysis |
| mean corpuscular volume (MCV, minimum, inv-norm transformed) | 1e-323 | rs11549407 | 1 | GCST90475474 | no MR -> candidate analysis |
| mean corpuscular volume (MCV, mean, inv-norm transformed) | 1e-323 | rs11549407 | 1 | GCST90475470 | no MR -> candidate analysis |
| mean corpuscular volume (MCV, maximum, inv-norm transformed) | 1e-323 | rs11549407 | 1 | GCST90475466 | no MR -> candidate analysis |
| _...and 129 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 2 known modulators (Hemoglobin HbA) |
| gnomAD constraint | not available |
| GWAS Catalog | no mapped SNPs |
| ClinVar | no records |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`uniprot`** — No reviewed human UniProt entry for 'HBA1;HBB'.
- **`phenome`** — Could not resolve target 'HBA1;HBB'.
- **`chembl`** — ChEMBL target matched by text search on 'HBA1;HBB' and resolved to 'Hemoglobin HbA' — confirm this is the intended target.
- **`gnomad`** — No gnomAD constraint data.
- **`gwas`** — No GWAS Catalog SNPs mapped to this gene.
- **`clinvar`** — No ClinVar records.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 141 traits by best p-value, aggregated from 287 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2095168/ — _ChEMBL_37 (released 2026-05-01)_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/HBA1;HBB — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:58:25  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
