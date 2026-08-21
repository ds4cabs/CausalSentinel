# Protein Dossier — LEAP2 (Liver-expressed antimicrobial peptide 2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Heel bone mineral density (BMD) T-score  automated | 0.0736 | 0.0139 | 1.24e-07 | Wald ratio | 1 | cis | NA |
| Alcohol intake frequency | 0.0812 | 0.0159 | 3.38e-07 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: pneumothorax | 0.947 | 0.216 | 1.21e-05 | Wald ratio | 1 | cis | NA |
| Birth weight | 0.0653 | 0.0163 | 6.33e-05 | Wald ratio | 1 | cis | NA |
| Serum creatinine (eGFRcrea) | -0.0153 | 0.004 | 1.26e-04 | Wald ratio | 1 | cis | NA |
| ER-positive Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.117 | 0.0337 | 5.30e-04 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | -0.0295 | 0.00884 | 8.58e-04 | Wald ratio | 1 | cis | NA |
| Age at menarche | 0.0833 | 0.0253 | 0.001 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | -0.0304 | 0.00932 | 0.00111 | Wald ratio | 1 | cis | NA |
| Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0867 | 0.028 | 0.00197 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M72 Fibroblastic disorders | 0.319 | 0.108 | 0.00308 | Wald ratio | 1 | cis | NA |
| Diastolic blood pressure  automated reading | -0.0324 | 0.011 | 0.00327 | Wald ratio | 1 | cis | NA |
| _...and 102 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_5 association rows across 4 traits (4 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| DEFA1_DEFA1B/LCN2 protein level ratio | 3e-23 | rs803223 | 1 | GCST90314454 | no MR -> candidate analysis |
| LCN2/PGLYRP1 protein level ratio | 6e-23 | rs803223 | 1 | GCST90315306 | no MR -> candidate analysis |
| Blood protein levels | 4e-19 | rs57880964 | 1 | GCST006585 | no MR -> candidate analysis |
| Core binding factor acute myeloid leukemia | 2e-14 | rs803222; rs2525485; rs10038027; rs3798128; rs739863; rs10479013; rs12653694; rs17691584 | 2 | GCST008413 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=2.5e-06, LOEUF=2.21 — LoF-tolerant |
| GWAS Catalog | 50 unique SNPs / 100 rows |
| ClinVar | 34 records; 11 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 110 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'LEAP2'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 34 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 4 of 4 traits by best p-value, aggregated from 5 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q969E1 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000164406/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/LEAP2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/LEAP2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=LEAP2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/LEAP2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:29:21  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
