# Protein Dossier — SMIM9 (Small integral membrane protein 9)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Vascular or heart problems diagnosed by doctor: Angina | 0.133 | 0.0391 | 6.54e-04 | Wald ratio | 1 | trans | NA |
| Depressive symptoms | 0.0394 | 0.0121 | 0.00115 | Wald ratio | 1 | trans | NA |
| Schizophrenia | 0.103 | 0.0352 | 0.00328 | Wald ratio | 1 | trans | NA |
| Forced vital capacity (FVC) | -0.0187 | 0.00653 | 0.00414 | Wald ratio | 1 | trans | NA |
| Forced expiratory volume in 1-second (FEV1) | -0.019 | 0.00689 | 0.00577 | Wald ratio | 1 | trans | NA |
| Happiness | 0.026 | 0.00986 | 0.00834 | Wald ratio | 1 | trans | NA |
| Microalbuminuria | 0.164 | 0.0698 | 0.0189 | Wald ratio | 1 | trans | NA |
| Alcohol intake frequency | 0.0272 | 0.0118 | 0.0207 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: osteoarthritis | 0.0566 | 0.0252 | 0.0247 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: N81 Female genital prolapse | 0.13 | 0.0586 | 0.0263 | Wald ratio | 1 | trans | NA |
| Diastolic blood pressure  automated reading | 0.0177 | 0.00815 | 0.0298 | Wald ratio | 1 | trans | NA |
| Heel bone mineral density (BMD) T-score  automated | 0.0217 | 0.0103 | 0.0355 | Wald ratio | 1 | trans | NA |
| _...and 102 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_1 association rows across 1 traits (1 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Hemoglobin | 4e-8 | rs201920434 | 1 | GCST90278631 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.00069, LOEUF=1.99 — LoF-tolerant |
| GWAS Catalog | 8 unique SNPs / 16 rows |
| ClinVar | 235 records; 18 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 4 of 4 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'SMIM9'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 235 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 1 of 1 traits by best p-value, aggregated from 1 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/A6NGZ8 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000203870/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/SMIM9 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/SMIM9 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=SMIM9%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/SMIM9 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:09:07  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
