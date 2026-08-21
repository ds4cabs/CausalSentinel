# Protein Dossier — SHBG (Sex hormone-binding globulin)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Body fat | 0.106 | 0.0266 | 7.34e-05 | Wald ratio | 1 | cis | NA |
| HDL cholesterol | 0.0893 | 0.0243 | 2.40e-04 | Wald ratio | 1 | cis | NA |
| Hirschsprung's disease | 2.19 | 0.606 | 2.97e-04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: deep venous thrombosis (dvt) | 0.221 | 0.0646 | 6.33e-04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | 0.0601 | 0.0182 | 9.35e-04 | Wald ratio | 1 | cis | NA |
| Cardioembolic stroke | -0.497 | 0.162 | 0.00212 | Wald ratio | 1 | cis | NA |
| Alcohol intake frequency | -0.0494 | 0.0167 | 0.00314 | Wald ratio | 1 | cis | NA |
| Platelet count | -6.61 | 2.25 | 0.00323 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: H25 Senile cataract | 0.265 | 0.1 | 0.00811 | Wald ratio | 1 | cis | NA |
| Creatinine (enzymatic) in urine | -0.027 | 0.0108 | 0.0125 | Wald ratio | 1 | cis | NA |
| Birth length | 0.128 | 0.0523 | 0.0148 | Wald ratio | 1 | cis | NA |
| Haemoglobin concentration | 0.0715 | 0.0294 | 0.0152 | Wald ratio | 1 | cis | NA |
| _...and 112 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4929_55_1` | SHBG | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_210 association rows across 88 traits (202 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Sex hormone-binding globulin levels | 2e-3373 | rs6258 | 34 | GCST90025958 | no MR -> candidate analysis |
| Sex hormone-binding globulin levels adjusted for BMI | 2e-3229 | rs858519 | 4 | GCST90012110 | no MR -> candidate analysis |
| Total testosterone levels | 1e-758 | rs1799941 | 13 | GCST90239819 | no MR -> candidate analysis |
| Bioavailable testosterone levels | 8e-309 | rs727428 | 8 | GCST90012102 | no MR -> candidate analysis |
| Testosterone levels (UKB data field 30850) | 2e-294 | rs1799941 | 2 | GCST90468103 | no MR -> candidate analysis |
| Diamine acetyltransferase 2 levels | 3e-282 | rs858522 | 3 | GCST90247237 | no MR -> candidate analysis |
| Free testosterone levels | 1e-233 | rs727428 | 4 | GCST90239826 | no MR -> candidate analysis |
| Body fat percentage (adjusted for testosterone and SHBG) | 1e-224 | rs1799941 | 15 | GCST90432179 | no MR -> candidate analysis |
| N6-acetyllysine levels | 9e-176 | rs13894 | 6 | GCST90245307 | no MR -> candidate analysis |
| SAT2 protein levels | 1e-174 | rs148093673 | 5 | GCST90470529 | no MR -> candidate analysis |
| Hypogonadism | 1e-136 | rs1799941 | 4 | GCST90570530 | no MR -> candidate analysis |
| Blood protein levels | 1e-111 | rs858519 | 5 | GCST006585 | no MR -> candidate analysis |
| _...and 76 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 724 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| testicular disorder | 0.726 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.686 | — | common-variant locus | no MR -> candidate analysis |
| type 2 diabetes mellitus | 0.633 | — | common-variant locus | no MR -> candidate analysis |
| smoking cessation | 0.499 | — | common-variant locus | no MR -> candidate analysis |
| hypogonadism | 0.435 | — | common-variant locus | no MR -> candidate analysis |
| aging | 0.463 | — | common-variant locus | no MR -> candidate analysis |
| osteoarthritis, hip | 0.385 | — | common-variant locus | MR: beta=0.0925, p=0.474 (cis) |
| atrial fibrillation | 0.268 | — | common-variant locus | no MR -> candidate analysis |

> Of the 8 rows above, **7 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Sex hormone-binding globulin) |
| gnomAD constraint | pLI=8.2e-12, LOEUF=1.16 — LoF-tolerant |
| GWAS Catalog | 225 unique SNPs / 584 rows |
| ClinVar | 127 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 724 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'SHBG' and resolved to 'Sex hormone-binding globulin' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 127 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 88 traits by best p-value, aggregated from 210 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P04278 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000129214/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3305/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/SHBG — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/SHBG — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=SHBG%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/SHBG — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:04:43  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
