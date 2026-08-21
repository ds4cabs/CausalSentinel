# Protein Dossier — PGLYRP2 (N-acetylmuramoyl-L-alanine amidase)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Eye problems or disorders: Diabetes related eye disease | -0.264 | 0.113 | 0.0198 | Wald ratio | 1 | cis | NA |
| Forearm bone mineral density | 0.0983 | 0.0428 | 0.0217 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I83 Varicose veins of lower extremities | -0.114 | 0.0524 | 0.0294 | Wald ratio | 1 | cis | NA |
| Potassium in urine | 0.0147 | 0.00678 | 0.03 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: migraine | 0.0756 | 0.0358 | 0.0349 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | 0.0231 | 0.0111 | 0.0375 | Wald ratio | 1 | cis | NA |
| Systolic blood pressure  automated reading | 0.014 | 0.00683 | 0.0406 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Glaucoma | 0.103 | 0.0505 | 0.041 | Wald ratio | 1 | cis | NA |
| Vascular or heart problems diagnosed by doctor: Angina | 0.0703 | 0.0349 | 0.0443 | Wald ratio | 1 | cis | NA |
| ER-negative Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0681 | 0.0342 | 0.0462 | Wald ratio | 1 | cis | NA |
| Pulse rate | -0.0224 | 0.0118 | 0.0579 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M54 Dorsalgia | 0.0894 | 0.0475 | 0.0599 | Wald ratio | 1 | cis | NA |
| _...and 69 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_48 association rows across 36 traits (47 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| V(D)J recombination-activating protein 1 levels | 5e-461 | rs34440547 | 1 | GCST90250190 | no MR -> candidate analysis |
| N-acetylmuramoyl-L-alanine amidase levels | 6e-195 | rs10164310 | 3 | GCST90248594 | no MR -> candidate analysis |
| Serum levels of protein PACSIN1 | 2e-173 | rs12610560 | 1 | GCST90087144 | no MR -> candidate analysis |
| Ribosomal protein S6 kinase beta-1 levels | 1e-159 | rs919791 | 1 | GCST90248213 | no MR -> candidate analysis |
| Macrophage scavenger receptor types I and II levels | 2e-127 | rs2304200 | 1 | GCST90248385 | no MR -> candidate analysis |
| Serum levels of protein ITGB6 | 1e-106 | rs36020076 | 1 | GCST90089794 | no MR -> candidate analysis |
| Serum levels of protein TREML1 | 7e-106 | rs36020076 | 1 | GCST90086569 | no MR -> candidate analysis |
| Protein LDOC1 levels | 3e-97 | rs34440547 | 1 | GCST90248268 | no MR -> candidate analysis |
| Serum levels of protein RPS6KB1 | 7e-87 | rs919791 | 1 | GCST90090412 | no MR -> candidate analysis |
| Submaxillary gland androgen-regulated protein 3A levels (SMR | 1e-84 | rs36020076 | 1 | GCST90242908 | no MR -> candidate analysis |
| Glycoprotein hormone alpha-2 levels (GPHA2.6395.58.3) | 3e-82 | rs4638719 | 1 | GCST90241299 | no MR -> candidate analysis |
| Serum levels of protein PGLYRP2 | 3e-76 | rs55866012 | 3 | GCST90089084 | no MR -> candidate analysis |
| _...and 24 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=2.5e-11, LOEUF=1.08 — LoF-tolerant |
| GWAS Catalog | 78 unique SNPs / 154 rows |
| ClinVar | 94 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 229 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'PGLYRP2'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 94 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 36 traits by best p-value, aggregated from 48 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q96PD5 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000161031/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PGLYRP2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PGLYRP2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PGLYRP2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PGLYRP2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:19:16  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
