# Protein Dossier — PRRG1 (Transmembrane gamma-carboxyglutamic acid protein 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Systolic blood pressure  automated reading | 0.0521 | 0.0146 | 3.60e-04 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: R07 Pain in throat and chest | 0.184 | 0.0532 | 5.54e-04 | Wald ratio | 1 | trans | NA |
| Hearing difficulty or problems: Yes | 0.0695 | 0.023 | 0.00254 | Wald ratio | 1 | trans | NA |
| Primary sclerosing cholangitis  | -0.453 | 0.154 | 0.00335 | Wald ratio | 1 | trans | NA |
| Hippocampus volume | -66.9 | 24.8 | 0.00703 | Wald ratio | 1 | trans | NA |
| Hip osteoarthritis | 0.44 | 0.171 | 0.00986 | Wald ratio | 1 | trans | NA |
| Eye problems or disorders: Glaucoma | 0.24 | 0.0945 | 0.0111 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: high cholesterol | 0.0869 | 0.0355 | 0.0144 | Wald ratio | 1 | trans | NA |
| Microalbuminuria | 0.298 | 0.122 | 0.0145 | Wald ratio | 1 | trans | NA |
| Vascular or heart problems diagnosed by doctor: Angina | 0.166 | 0.0683 | 0.0148 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: B37 Candidiasis | 0.812 | 0.347 | 0.0194 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: diverticular disease or diverticulitis | 0.246 | 0.107 | 0.0215 | Wald ratio | 1 | trans | NA |
| _...and 106 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_1 association rows across 1 traits (0 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Cognitive performance (attention) (longitudinal) | 1e-6 | rs7891774 | 1 | GCST90104685 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.28, LOEUF=0.888 — LoF-tolerant |
| GWAS Catalog | 2 unique SNPs / 4 rows |
| ClinVar | 211 records; 4 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 33 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'PRRG1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 211 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 1 of 1 traits by best p-value, aggregated from 1 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O14668 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000130962/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PRRG1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PRRG1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PRRG1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PRRG1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:37:26  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
