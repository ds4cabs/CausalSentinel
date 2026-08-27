# Protein Dossier — CLEC3B (Tetranectin)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Neuroticism | 0.0704 | 0.0188 | 1.77e-04 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | 0.0653 | 0.0176 | 2.13e-04 | Wald ratio | 1 | cis | NA |
| Sodium in urine | 0.045 | 0.0134 | 7.79e-04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: depression | 0.133 | 0.0493 | 0.00693 | Wald ratio | 1 | cis | NA |
| Hirschsprung's disease | 2.98 | 1.12 | 0.0076 | Wald ratio | 1 | cis | NA |
| Vascular or heart problems diagnosed by doctor: Angina | 0.167 | 0.0649 | 0.0101 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | 0.0335 | 0.0136 | 0.0138 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: prostate cancer | 0.296 | 0.121 | 0.0143 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R07 Pain in throat and chest | 0.13 | 0.0535 | 0.0151 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C61 Malignant neoplasm of prostate | 0.301 | 0.126 | 0.0169 | Wald ratio | 1 | cis | NA |
| Hearing difficulty or problems: Yes | -0.0576 | 0.0249 | 0.0208 | Wald ratio | 1 | cis | NA |
| Creatinine (enzymatic) in urine | 0.0297 | 0.013 | 0.0225 | Wald ratio | 1 | cis | NA |
| _...and 94 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_20 association rows across 12 traits (15 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| CLEC3B protein levels | 7e-210 | rs13065490 | 5 | GCST90468770 | no MR -> candidate analysis |
| Tetranectin levels | 5e-66 | rs10514712 | 3 | GCST90249808 | no MR -> candidate analysis |
| Circulating CDCP1 levels | 2e-57 | rs62242502 | 2 | GCST90859836 | no MR -> candidate analysis |
| Exosome complex component RRP43 levels | 1e-47 | rs149457742 | 1 | GCST90249380 | no MR -> candidate analysis |
| CDCP1 protein levels | 4e-45 | rs62242502 | 2 | GCST90468667 | no MR -> candidate analysis |
| Tetranectin plasma levels | 1e-34 | rs8318 | 1 | GCST90085779 | no MR -> candidate analysis |
| Estimated glomerular filtration rate (creatinine, cystatin c | 8e-9 | rs2372857 | 1 | GCST90428446 | no MR -> candidate analysis |
| Estimated glomerular filtration rate (cystatin c) | 6e-8 | rs2372857 | 1 | GCST90428448 | no MR -> candidate analysis |
| Color vision defects (Tritan) | 3e-7 | rs10510745 | 1 | GCST90301671 | no MR -> candidate analysis |
| Estimated glomerular filtration rate (creatinine) | 4e-6 | rs2372857 | 1 | GCST90428447 | no MR -> candidate analysis |
| Alzheimer's disease | 5e-6 | rs7618668 | 1 | GCST012214 | MR: beta=-0.0761, p=0.386 (cis) |
| Stuttering | 8e-6 | rs11922169 | 1 | GCST90707224 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 569 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| macular dystrophy, retinal, 4 | 0.547 | — | established (curated) | no MR -> candidate analysis |
| inborn disorder of amino acid metabolism | 0.406 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.00011, LOEUF=1.34 — LoF-tolerant |
| GWAS Catalog | 50 unique SNPs / 86 rows |
| ClinVar | 37 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 569 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CLEC3B'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 37 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 12 of 12 traits by best p-value, aggregated from 20 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P05452 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000163815/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CLEC3B — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CLEC3B — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CLEC3B%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CLEC3B — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:53:00  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
