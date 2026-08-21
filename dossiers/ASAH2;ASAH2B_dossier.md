# Protein Dossier — ASAH2;ASAH2B

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Ovarian cancer | -0.062 | 0.0253 | 0.0141 | Wald ratio | 1 | cis | NA |
| Birth weight | 0.0147 | 0.0069 | 0.0331 | Wald ratio | 1 | cis | NA |
| Alzheimer's disease | -0.0561 | 0.0294 | 0.0564 | Wald ratio | 1 | cis | NA |
| Hippocampus volume | -17 | 9.02 | 0.0599 | Wald ratio | 1 | cis | NA |
| Depressive symptoms | -0.0135 | 0.0075 | 0.0719 | Wald ratio | 1 | cis | NA |
| ER-negative Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.035 | 0.0224 | 0.118 | Wald ratio | 1 | cis | NA |
| Thalamus volume | -18.7 | 12 | 0.121 | Wald ratio | 1 | cis | NA |
| High grade serous ovarian cancer | -0.0457 | 0.0299 | 0.127 | Wald ratio | 1 | cis | NA |
| Nucleus accumbens volume | -3 | 2.09 | 0.15 | Wald ratio | 1 | cis | NA |
| Schizophrenia | -0.0273 | 0.0194 | 0.158 | Wald ratio | 1 | cis | NA |
| Lung adenocarcinoma | -0.0688 | 0.053 | 0.195 | Wald ratio | 1 | cis | NA |
| Low grade serous ovarian cancer | -0.114 | 0.0913 | 0.21 | Wald ratio | 1 | cis | NA |
| _...and 8 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_142 association rows across 80 traits (127 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating ASAH2 levels | 1e-1649 | rs2574935 | 5 | GCST90859724 | no MR -> candidate analysis |
| Neutral ceramidase levels | 7e-362 | rs2842126 | 12 | GCST90248650 | no MR -> candidate analysis |
| ASAH2 protein levels | 1e-310 | rs116049719 | 7 | GCST90468374 | no MR -> candidate analysis |
| Serum levels of protein ASAH2 | 2e-126 | rs7071083 | 2 | GCST90088273 | no MR -> candidate analysis |
| Neutral ceramidase levels (ASAH2.3212.30.3) | 2e-124 | rs10740617 | 3 | GCST90242098 | no MR -> candidate analysis |
| Blood protein levels | 5e-73 | rs2813297 | 1 | GCST006585 | no MR -> candidate analysis |
| Cerebrospinal fluid protein ASAH2 levels | 8e-73 | rs202183815 | 1 | GCST90943054 | no MR -> candidate analysis |
| Neutral ceramidase level in Chronic kidney disease with hype | 6e-55 | rs11004802 | 1 | GCST90237277 | no MR -> candidate analysis |
| Urate levels | 3e-35 | rs10821826 | 1 | GCST90019524 | no MR -> candidate analysis |
| Triglyceride levels | 1e-32 | rs41274050 | 8 | GCST90662893 | no MR -> candidate analysis |
| Neurological blood protein biomarker levels | 1e-29 | rs1898198 | 3 | GCST008478 | no MR -> candidate analysis |
| Triglyceride levels (UKB data field 30870) | 6e-28 | rs41274050 | 1 | GCST90468106 | no MR -> candidate analysis |
| _...and 68 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Neutral ceramidase) |
| gnomAD constraint | not available |
| GWAS Catalog | no mapped SNPs |
| ClinVar | no records |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`uniprot`** — No reviewed human UniProt entry for 'ASAH2;ASAH2B'.
- **`phenome`** — Could not resolve target 'ASAH2;ASAH2B'.
- **`chembl`** — ChEMBL target matched by text search on 'ASAH2;ASAH2B' and resolved to 'Neutral ceramidase' — confirm this is the intended target.
- **`gnomad`** — No gnomAD constraint data.
- **`gwas`** — No GWAS Catalog SNPs mapped to this gene.
- **`clinvar`** — No ClinVar records.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 80 traits by best p-value, aggregated from 142 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2021754/ — _ChEMBL_37 (released 2026-05-01)_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/ASAH2;ASAH2B — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:10:21  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
