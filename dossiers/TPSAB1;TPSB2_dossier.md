# Protein Dossier — TPSAB1;TPSB2

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Birth weight | -0.0312 | 0.00793 | 8.61e-05 | Wald ratio | 1 | cis | NA |
| Age at menarche | 0.0464 | 0.0145 | 0.0014 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: pneumothorax | 0.48 | 0.156 | 0.00213 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R35 Polyuria | 0.198 | 0.0661 | 0.00278 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | -0.0129 | 0.00433 | 0.00299 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | 0.136 | 0.0521 | 0.00902 | Wald ratio | 1 | cis | NA |
| HOMA-IR | 0.0329 | 0.0128 | 0.01 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K60 Fissure and fistula of anal and rectal regions | -0.238 | 0.095 | 0.0121 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: vitiligo | 0.479 | 0.196 | 0.0148 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | -0.00965 | 0.00411 | 0.0188 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K29 Gastritis and duodenitis | -0.0764 | 0.035 | 0.029 | Wald ratio | 1 | cis | NA |
| Serum creatinine (eGFRcrea) | 0.00445 | 0.00213 | 0.0365 | Wald ratio | 1 | cis | NA |
| _...and 80 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_42 association rows across 24 traits (41 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating TPSAB1 levels | 1e-3575 | rs71380254 | 3 | GCST90860174 | no MR -> candidate analysis |
| Tryptase beta-2 levels | 4e-2075 | rs143547788 | 7 | GCST90249955 | no MR -> candidate analysis |
| Tryptase beta-2 levels (TPSB2.3403.1.2) | 2e-819 | rs144979264 | 6 | GCST90243128 | no MR -> candidate analysis |
| Tryptase beta-2 (analyte X3403.1) levels | 6e-449 | rs112332886 | 1 | GCST90425745 | no MR -> candidate analysis |
| Tryptase beta-1 levels | 6e-209 | rs112332886 | 3 | GCST90427803 | no MR -> candidate analysis |
| Serum levels of protein TPSB2 | 5e-162 | rs112332886 | 1 | GCST90088366 | no MR -> candidate analysis |
| Serum levels of protein TPSB2;TPSAB1 | 2e-130 | rs9937881 | 1 | GCST90090686 | no MR -> candidate analysis |
| SIGLEC6 protein levels | 2e-93 | rs2745083 | 1 | GCST90470634 | no MR -> candidate analysis |
| Circulating SIGLEC6 levels | 4e-89 | rs2745083 | 1 | GCST90860512 | no MR -> candidate analysis |
| Tryptase beta-2 (analyte X14696.45) levels | 3e-70 | rs2745086 | 1 | GCST90422577 | no MR -> candidate analysis |
| TPSAB1 protein levels | 2e-58 | rs568646476 | 4 | GCST90470951 | no MR -> candidate analysis |
| Heat shock 70 kDa protein 1A protein levels (SomaScan ID:340 | 1e-40 | rs4984779 | 1 | GCST90438628 | no MR -> candidate analysis |
| _...and 12 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Tryptase beta-2) |
| gnomAD constraint | not available |
| GWAS Catalog | no mapped SNPs |
| ClinVar | no records |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`uniprot`** — No reviewed human UniProt entry for 'TPSAB1;TPSB2'.
- **`phenome`** — Could not resolve target 'TPSAB1;TPSB2'.
- **`chembl`** — ChEMBL target matched by text search on 'TPSAB1;TPSB2' and resolved to 'Tryptase beta-2' — confirm this is the intended target.
- **`gnomad`** — No gnomAD constraint data.
- **`gwas`** — No GWAS Catalog SNPs mapped to this gene.
- **`clinvar`** — No ClinVar records.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 24 traits by best p-value, aggregated from 42 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4523196/ — _ChEMBL_37 (released 2026-05-01)_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/TPSAB1;TPSB2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:28:22  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
