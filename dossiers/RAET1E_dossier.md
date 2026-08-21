# Protein Dossier — RAET1E (Retinoic acid early transcript 1E)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: gout | 0.119 | 0.0464 | 0.0104 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | -0.199 | 0.0913 | 0.0289 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: bladder problem (not cancer) | 0.153 | 0.0704 | 0.0296 | Wald ratio | 1 | trans | NA |
| Underlying (primary) cause of death: ICD10: E85.4 Organ-limited amyloidosis | 1.21 | 0.583 | 0.0387 | Wald ratio | 1 | trans | NA |
| Hirschsprung's disease | -0.776 | 0.378 | 0.04 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: G47 Sleep disorders | 0.145 | 0.0706 | 0.0404 | Wald ratio | 1 | trans | NA |
| Body fat | -0.0282 | 0.0139 | 0.042 | Wald ratio | 1 | trans | NA |
| Neo-neuroticism | 0.472 | 0.241 | 0.0504 | Wald ratio | 1 | trans | NA |
| Neo-agreeableness | -0.302 | 0.156 | 0.0526 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: hypertension | 0.0189 | 0.0104 | 0.0692 | Wald ratio | 1 | trans | NA |
| Lung cancer | 0.0869 | 0.048 | 0.0701 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: pernicious anaemia | -0.283 | 0.157 | 0.0707 | Wald ratio | 1 | trans | NA |
| _...and 105 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_15 association rows across 12 traits (12 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Low-density lipoprotein receptor-related protein 11 levels | 2e-1411 | rs9322225 | 1 | GCST90248262 | no MR -> candidate analysis |
| Blood protein levels | 4e-286 | rs9371533 | 1 | GCST006585 | no MR -> candidate analysis |
| LRP11 protein levels | 1e-79 | rs555648964 | 4 | GCST90469796 | no MR -> candidate analysis |
| Circulating LRP11 levels | 1e-24 | rs6557163 | 1 | GCST90860386 | no MR -> candidate analysis |
| Low-density lipoprotein receptor-related protein 11 (analyte | 4e-23 | rs1889471 | 1 | GCST90422684 | no MR -> candidate analysis |
| ULBP2 protein levels | 5e-15 | rs181773431 | 1 | GCST90471008 | no MR -> candidate analysis |
| Low-density lipoprotein receptor-related protein 11 (analyte | 3e-14 | rs1889471 | 1 | GCST90427338 | no MR -> candidate analysis |
| Cerebrospinal fluid protein LRP11 levels | 2e-8 | rs1889471 | 1 | GCST90944405 | no MR -> candidate analysis |
| Height | 4e-8 | rs9969044 | 1 | GCST90245848 | no MR -> candidate analysis |
| Aging (eyeAgeAcceleration) | 8e-8 | rs531479946 | 1 | GCST90274864 | no MR -> candidate analysis |
| Autism spectrum disorder | 2e-7 | rs9383583 | 1 | GCST012816 | no MR -> candidate analysis |
| Lupus nephritis in systemic lupus erythematosus | 5e-6 | rs17079029 | 1 | GCST90728615 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.1e-11, LOEUF=1.76 — LoF-tolerant |
| GWAS Catalog | 85 unique SNPs / 170 rows |
| ClinVar | 64 records; 4 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 80 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'RAET1E'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 64 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 12 of 12 traits by best p-value, aggregated from 15 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q8TD07 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000164520/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/RAET1E — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/RAET1E — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=RAET1E%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/RAET1E — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:45:20  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
