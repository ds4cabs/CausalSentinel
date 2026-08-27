# Protein Dossier — CGA;CGB3;CGB7

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: N92 Excessive  frequent and irregular menstruation | 0.162 | 0.0557 | 0.00358 | Wald ratio | 1 | trans | NA |
| Eye problems or disorders: Glaucoma | 0.175 | 0.066 | 0.00813 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: bone disorder | 0.344 | 0.145 | 0.0178 | Wald ratio | 1 | trans | NA |
| Pancreatic cancer | 0.439 | 0.186 | 0.0181 | Wald ratio | 1 | trans | NA |
| Neo-agreeableness | -0.601 | 0.272 | 0.0273 | Wald ratio | 1 | trans | NA |
| Happiness | -0.0246 | 0.0116 | 0.0341 | Wald ratio | 1 | trans | NA |
| Nucleus accumbens volume | 8.97 | 4.36 | 0.0399 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: C50 Malignant neoplasm of breast | -0.181 | 0.0886 | 0.0412 | Wald ratio | 1 | trans | NA |
| Age at menopause | 0.156 | 0.0781 | 0.0455 | Wald ratio | 1 | trans | NA |
| Mean platelet volume | 0.00859 | 0.0043 | 0.0455 | Wald ratio | 1 | trans | NA |
| Subjective well being | 0.0234 | 0.0117 | 0.0455 | Wald ratio | 1 | trans | NA |
| Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.052 | 0.0262 | 0.0471 | Wald ratio | 1 | trans | NA |
| _...and 91 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_30 association rows across 22 traits (29 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Thyroid stimulating hormone levels | 5e-78 | rs1998615 | 4 | GCST90572789 | no MR -> candidate analysis |
| HSD17B14 protein levels | 3e-30 | rs10407858 | 1 | GCST90469483 | no MR -> candidate analysis |
| DKKL1 protein levels | 8e-24 | rs117421182 | 2 | GCST90469000 | no MR -> candidate analysis |
| Thyroid-stimulating hormone levels | 3e-22 | rs2031365 | 1 | GCST90662868 | no MR -> candidate analysis |
| White blood cell count | 2e-20 | rs4574603 | 2 | GCST90002378 | no MR -> candidate analysis |
| Circulating CGA levels | 2e-18 | rs2031367 | 1 | GCST90860633 | no MR -> candidate analysis |
| Neutrophil percentage of granulocytes | 6e-18 | rs67614146 | 1 | GCST004623 | no MR -> candidate analysis |
| CGA protein levels | 4e-17 | rs2031367 | 1 | GCST90468732 | no MR -> candidate analysis |
| FSHB protein levels | 4e-15 | rs779759288 | 1 | GCST90469270 | no MR -> candidate analysis |
| Eosinophil percentage of granulocytes | 5e-15 | rs67614146 | 1 | GCST004617 | no MR -> candidate analysis |
| Free thyroxine levels within normal range in pregnancy | 1e-13 | rs9362387 | 1 | GCST90435196 | no MR -> candidate analysis |
| Neutrophil-to-lymphocyte ratio | 8e-13 | rs981087 | 3 | GCST90866310 | no MR -> candidate analysis |
| _...and 10 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Glycoprotein hormones alpha chain) |
| gnomAD constraint | not available |
| GWAS Catalog | no mapped SNPs |
| ClinVar | no records |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`uniprot`** — No reviewed human UniProt entry for 'CGA;CGB3;CGB7'.
- **`phenome`** — Could not resolve target 'CGA;CGB3;CGB7'.
- **`chembl`** — ChEMBL target matched by text search on 'CGA;CGB3;CGB7' and resolved to 'Glycoprotein hormones alpha chain' — confirm this is the intended target.
- **`gnomad`** — No gnomAD constraint data.
- **`gwas`** — No GWAS Catalog SNPs mapped to this gene.
- **`clinvar`** — No ClinVar records.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 22 traits by best p-value, aggregated from 30 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2146305/ — _ChEMBL_37 (released 2026-05-01)_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CGA;CGB3;CGB7 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:49:20  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
