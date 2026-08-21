# Protein Dossier — CCL23 (C-C motif chemokine 23)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: bladder problem (not cancer) | 0.168 | 0.0545 | 0.00208 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C61 Malignant neoplasm of prostate | 0.136 | 0.0526 | 0.00978 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | 0.129 | 0.0514 | 0.0121 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: gastro-oesophageal reflux (gord)  or  gastric reflux | -0.0588 | 0.025 | 0.0189 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: vitiligo | 0.458 | 0.196 | 0.0198 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | 0.0186 | 0.0082 | 0.0232 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | -0.00904 | 0.00402 | 0.0246 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: bone disorder | 0.19 | 0.0871 | 0.0288 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I30 Acute pericarditis | 0.415 | 0.193 | 0.0317 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: L03 Cellulitis | 0.102 | 0.0494 | 0.0389 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I48 Atrial fibrillation and flutter | 0.0864 | 0.0426 | 0.0426 | Wald ratio | 1 | cis | NA |
| Intracranial volume | 7.81e+03 | 3.88e+03 | 0.0444 | Wald ratio | 1 | cis | NA |
| _...and 79 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2913_1_2` | MPIF-1 | Suhre K | 2019 |
| `prot-c-3028_36_2` | Ck-b-8-1 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_145 association rows across 61 traits (139 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating CCL18 levels | 9e-1471 | rs2015086 | 2 | GCST90860473 | no MR -> candidate analysis |
| C-C motif chemokine 15 levels | 3e-1432 | rs854628 | 6 | GCST90246903 | no MR -> candidate analysis |
| ANG/CCL18 protein level ratio | 7e-1018 | rs56683451 | 1 | GCST90313258 | no MR -> candidate analysis |
| CCL18/RARRES2 protein level ratio | 2e-1001 | rs56683451 | 1 | GCST90313690 | no MR -> candidate analysis |
| CCL18/TFPI protein level ratio | 4e-986 | rs56683451 | 1 | GCST90313691 | no MR -> candidate analysis |
| C-C motif chemokine 14 levels | 2e-763 | rs7222922 | 7 | GCST90246902 | no MR -> candidate analysis |
| C-C motif chemokine 18 levels | 2e-635 | rs2015086 | 9 | GCST90246906 | no MR -> candidate analysis |
| Circulating CCL23 levels (id: OID00530_OID20693) | 3e-360 | rs712046 | 2 | GCST90859884 | no MR -> candidate analysis |
| C-C motif chemokine 3 levels | 2e-314 | rs2015086 | 5 | GCST90246917 | no MR -> candidate analysis |
| CCL16 protein levels | 1e-299 | rs117259529 | 1 | GCST90468568 | no MR -> candidate analysis |
| Circulating CCL14 levels | 4e-296 | rs854466 | 2 | GCST90860489 | no MR -> candidate analysis |
| Serum levels of protein CCL15 | 3e-293 | rs41508645 | 1 | GCST90088428 | no MR -> candidate analysis |
| _...and 49 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 287 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| septic shock | 0.255 | — | common-variant locus | no MR -> candidate analysis |
| immune system disorder | 0.255 | — | common-variant locus | no MR -> candidate analysis |
| pernicious anemia | 0.082 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.00071, LOEUF=1.43 — LoF-tolerant |
| GWAS Catalog | 171 unique SNPs / 418 rows |
| ClinVar | 43 records; 4 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 287 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CCL23'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 43 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 20 of 61 traits by best p-value, aggregated from 145 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P55773 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000274736/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CCL23 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CCL23 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CCL23%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CCL23 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:36:00  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: pharmgkb
