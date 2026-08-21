# Protein Dossier — SMR3A (Submaxillary gland androgen-regulated protein 3A)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: R11 Nausea and vomiting | -0.328 | 0.115 | 0.00434 | Wald ratio | 1 | trans | NA |
| Alcohol intake frequency | -0.0173 | 0.00757 | 0.0223 | Wald ratio | 1 | trans | NA |
| Sodium in urine | -0.011 | 0.00504 | 0.029 | Wald ratio | 1 | trans | NA |
| Primary sclerosing cholangitis  | -0.161 | 0.0739 | 0.0291 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: C61 Malignant neoplasm of prostate | -0.15 | 0.0735 | 0.0408 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: sleep apnoea | 0.162 | 0.0791 | 0.0408 | Wald ratio | 1 | trans | NA |
| Cancer code  self-reported: prostate cancer | -0.141 | 0.0693 | 0.0424 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: N92 Excessive  frequent and irregular menstruation | -0.0762 | 0.0385 | 0.0479 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: G47 Sleep disorders | 0.116 | 0.0597 | 0.0519 | Wald ratio | 1 | trans | NA |
| Systolic blood pressure  automated reading | 0.0101 | 0.00524 | 0.0545 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: bladder problem (not cancer) | -0.148 | 0.0784 | 0.0592 | Wald ratio | 1 | trans | NA |
| Squamous cell lung cancer | -0.119 | 0.065 | 0.0666 | Wald ratio | 1 | trans | NA |
| _...and 66 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_4 association rows across 3 traits (2 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| CST5 protein levels | 2e-19 | rs1842475 | 1 | GCST90468895 | no MR -> candidate analysis |
| Clinical endometriosis | 4e-8 | rs11930506 | 1 | GCST90841386 | no MR -> candidate analysis |
| Endometriosis | 5e-7 | rs11930506 | 2 | GCST90841381 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=NA, LOEUF=NA — Constraint metrics missing; LoF tolerance cannot be judged. |
| GWAS Catalog | 11 unique SNPs / 22 rows |
| ClinVar | 59 records; 6 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 18 of 18 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'SMR3A'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 59 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 3 of 3 traits by best p-value, aggregated from 4 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q99954 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000109208/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/SMR3A — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/SMR3A — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=SMR3A%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/SMR3A — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:10:00  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
