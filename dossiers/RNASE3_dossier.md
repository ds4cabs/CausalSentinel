# Protein Dossier — RNASE3 (Eosinophil cationic protein)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| ER-positive Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.129 | 0.0444 | 0.00379 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: pneumothorax | 0.823 | 0.316 | 0.00915 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: D25 Leiomyoma of uterus | -0.495 | 0.199 | 0.0127 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | -0.0398 | 0.0169 | 0.0186 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: kidney stone or ureter stone or bladder stone | 0.238 | 0.118 | 0.0445 | Wald ratio | 1 | cis | NA |
| Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.0734 | 0.0369 | 0.0469 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K80 Cholelithiasis | 0.152 | 0.0789 | 0.0546 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: gastro-oesophageal reflux (gord)  or  gastric reflux | 0.109 | 0.0567 | 0.0551 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | 0.0383 | 0.0215 | 0.0742 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: G56 Mononeuropathies of upper limb | 0.15 | 0.0864 | 0.0817 | Wald ratio | 1 | cis | NA |
| Schizophrenia | 0.1 | 0.0593 | 0.0905 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I80 Phlebitis and thrombophlebitis | 0.254 | 0.153 | 0.0967 | Wald ratio | 1 | cis | NA |
| _...and 59 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_37 association rows across 28 traits (32 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| AZU1/RNASE3 protein level ratio | 1e-422 | rs112539509 | 1 | GCST90313428 | no MR -> candidate analysis |
| Circulating RNASE3 levels | 2e-409 | rs1763559 | 1 | GCST90860416 | no MR -> candidate analysis |
| RNASE1 protein levels | 2e-208 | rs12885981 | 3 | GCST90470476 | no MR -> candidate analysis |
| Eosinophil cationic protein (analyte X15576.158) levels | 6e-164 | rs4982376 | 1 | GCST90422739 | no MR -> candidate analysis |
| Non-secretory ribonuclease levels | 9e-126 | rs2233859 | 1 | GCST90248708 | no MR -> candidate analysis |
| Monocyte side fluorescence | 1e-59 | rs6571511 | 2 | GCST90281241 | no MR -> candidate analysis |
| Ribonuclease pancreatic levels | 8e-53 | rs17254387 | 2 | GCST90249353 | no MR -> candidate analysis |
| RNASE3 protein levels | 3e-51 | rs117558322 | 2 | GCST90470477 | no MR -> candidate analysis |
| Serum levels of protein RNASE2 | 1e-35 | rs2233859 | 1 | GCST90090180 | no MR -> candidate analysis |
| Serum levels of protein RNASE1 | 2e-35 | rs17254387 | 2 | GCST90089740 | no MR -> candidate analysis |
| Circulating CTRC levels | 8e-29 | rs35775091 | 1 | GCST90859776 | no MR -> candidate analysis |
| Blood protein levels | 3e-25 | rs12885981 | 1 | GCST006585 | no MR -> candidate analysis |
| _...and 16 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=NA, LOEUF=NA — Constraint metrics missing; LoF tolerance cannot be judged. |
| GWAS Catalog | 65 unique SNPs / 130 rows |
| ClinVar | 60 records; 3 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 558 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'RNASE3'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 60 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 28 traits by best p-value, aggregated from 37 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P12724 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000169397/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/RNASE3 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/RNASE3 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=RNASE3%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/RNASE3 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:50:32  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
