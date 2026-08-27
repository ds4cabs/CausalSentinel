# Protein Dossier — ISG15 (Ubiquitin-like protein ISG15)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Alcohol intake frequency | -0.0636 | 0.014 | 5.85e-06 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: psoriasis | 0.227 | 0.0717 | 0.00154 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hyperthyroidism or thyrotoxicosis | 0.243 | 0.0874 | 0.00545 | Wald ratio | 1 | cis | NA |
| Coronary heart disease | -0.139 | 0.0518 | 0.00709 | Wald ratio | 1 | cis | NA |
| Myocardial infarction | -0.145 | 0.0598 | 0.0154 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: L03 Cellulitis | 0.202 | 0.0871 | 0.0201 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N81 Female genital prolapse | 0.147 | 0.0689 | 0.0333 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | -0.0357 | 0.0168 | 0.0336 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: pernicious anaemia | 0.286 | 0.134 | 0.0336 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: H25 Senile cataract | 0.185 | 0.0909 | 0.0421 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | 0.0787 | 0.0391 | 0.044 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K80 Cholelithiasis | -0.156 | 0.0779 | 0.0449 | Wald ratio | 1 | cis | NA |
| _...and 73 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_17 association rows across 13 traits (17 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Ubiquitin-like protein ISG15 levels | 1e-277 | rs4615788 | 5 | GCST90250090 | no MR -> candidate analysis |
| Ubiquitin-like protein ISG15 (analyte X14151.4) levels | 4e-60 | rs1921 | 1 | GCST90422504 | no MR -> candidate analysis |
| Ubiquitin-like protein ISG15 (analyte X14148.2) levels | 5e-42 | rs1921 | 1 | GCST90422501 | no MR -> candidate analysis |
| Ubiquitin-like protein ISG15 levels (ISG15.14151.4.3) | 1e-24 | rs1891906 | 1 | GCST90243248 | no MR -> candidate analysis |
| AGRN protein levels | 5e-24 | rs139816136 | 1 | GCST90468255 | no MR -> candidate analysis |
| Serum levels of protein ISG15 | 4e-20 | rs13303172 | 1 | GCST90087821 | no MR -> candidate analysis |
| BST2 protein levels | 2e-13 | rs3128116 | 1 | GCST90468475 | no MR -> candidate analysis |
| Alanine levels | 5e-13 | rs3121569 | 1 | GCST90301943 | no MR -> candidate analysis |
| Blood protein levels | 2e-12 | rs3121567 | 1 | GCST006585 | no MR -> candidate analysis |
| Circulating BST2 levels | 4e-12 | rs3128116 | 1 | GCST90860689 | no MR -> candidate analysis |
| Alcohol consumption | 7e-10 | rs59239970 | 1 | GCST90133003 | no MR -> candidate analysis |
| High-density lipoprotein levels | 2e-9 | rs9331223 | 1 | GCST90662894 | no MR -> candidate analysis |
| _...and 1 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Ubl carboxyl-terminal hydrolase 18) |
| gnomAD constraint | pLI=0.11, LOEUF=2.57 — LoF-tolerant |
| GWAS Catalog | 81 unique SNPs / 160 rows |
| ClinVar | 306 records; 4 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 570 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'ISG15' and resolved to 'Ubl carboxyl-terminal hydrolase 18' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 306 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 13 of 13 traits by best p-value, aggregated from 17 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P05161 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000187608/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3407317/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/ISG15 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/ISG15 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=ISG15%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/ISG15 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:18:10  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
