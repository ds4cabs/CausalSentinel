# Protein Dossier — ANG (Angiogenin)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: B37 Candidiasis | 0.485 | 0.14 | 5.53e-04 | Wald ratio | 1 | cis | NA |
| Microalbuminuria | 0.124 | 0.0397 | 0.00178 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: polio  or  poliomyelitis | 0.358 | 0.127 | 0.00484 | Wald ratio | 1 | cis | NA |
| Serum cystatin C (eGFRcys) | -0.00967 | 0.00372 | 0.00932 | Wald ratio | 1 | cis | NA |
| Potassium in urine | -0.0123 | 0.00474 | 0.0095 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: vitiligo | 0.471 | 0.184 | 0.0105 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Glaucoma | 0.088 | 0.0357 | 0.0136 | Wald ratio | 1 | cis | NA |
| Hip osteoarthritis | 0.118 | 0.0545 | 0.0302 | Wald ratio | 1 | cis | NA |
| Systemic lupus erythematosus | -0.183 | 0.0884 | 0.0381 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R07 Pain in throat and chest | -0.0438 | 0.0218 | 0.0443 | Wald ratio | 1 | cis | NA |
| Neo-extraversion | -0.297 | 0.155 | 0.0555 | Wald ratio | 1 | cis | NA |
| Vascular or heart problems diagnosed by doctor: Angina | -0.0528 | 0.0276 | 0.0562 | Wald ratio | 1 | cis | NA |
| _...and 100 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4874_3_1` | Angiogenin | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_38 association rows across 15 traits (34 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating ANG levels | 1e-1158 | rs10220701 | 5 | GCST90860430 | no MR -> candidate analysis |
| ANG/F9 protein level ratio | 6e-1118 | rs17114671 | 1 | GCST90313259 | no MR -> candidate analysis |
| Angiogenin levels | 3e-452 | rs11851044 | 11 | GCST90246501 | no MR -> candidate analysis |
| Serum levels of protein ANG | 2e-86 | rs36071889 | 2 | GCST90088789 | no MR -> candidate analysis |
| ANG protein levels | 1e-69 | rs552960263 | 4 | GCST90468307 | no MR -> candidate analysis |
| RNASE4 protein levels | 1e-63 | rs780392419 | 3 | GCST90470478 | no MR -> candidate analysis |
| Ribonuclease 4 levels | 8e-45 | rs4470055 | 3 | GCST90426424 | no MR -> candidate analysis |
| Ribonuclease 4 levels (RNASE4.5644.60.3) | 1e-36 | rs184297073 | 2 | GCST90242666 | no MR -> candidate analysis |
| Blood protein levels | 1e-18 | rs1888560 | 1 | GCST006585 | no MR -> candidate analysis |
| Protein quantitative trait loci | 1e-17 | rs34121942 | 1 | GCST010900 | no MR -> candidate analysis |
| Ribonuclease 4 level in Chronic kidney disease with hyperten | 4e-15 | rs944438 | 1 | GCST90238008 | no MR -> candidate analysis |
| Tyrosine-protein phosphatase non-receptor type substrate 1 p | 9e-9 | rs17516133 | 1 | GCST90439340 | no MR -> candidate analysis |
| _...and 3 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 643 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| amyotrophic lateral sclerosis | 0.917 | — | established (curated) | no MR -> candidate analysis |
| frontotemporal dementia | 0.426 | — | established (curated) | no MR -> candidate analysis |
| hereditary disease | 0.306 | — | established (curated) | no MR -> candidate analysis |
| frontotemporal dementia with motor neuron disease | 0.195 | — | established (curated) | no MR -> candidate analysis |
| schizophrenia | 0.116 | — | common-variant locus | MR: beta=0.0187, p=0.366 (cis) |

> Of the 5 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 8 known modulators (Angiopoietin-2) |
| gnomAD constraint | pLI=NA, LOEUF=NA — Constraint metrics missing; LoF tolerance cannot be judged. |
| GWAS Catalog | 108 unique SNPs / 225 rows |
| ClinVar | 158 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 643 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'ANG' and resolved to 'Angiopoietin-2' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 158 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 15 of 15 traits by best p-value, aggregated from 38 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P03950 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000214274/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3580489/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/ANG — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/ANG — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=ANG%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/ANG — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:03:16  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
