# Protein Dossier — SPINT2 (Kunitz-type protease inhibitor 2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: C61 Malignant neoplasm of prostate | 0.106 | 0.0308 | 5.99e-04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: bladder problem (not cancer) | 0.0936 | 0.0333 | 0.00489 | Wald ratio | 1 | cis | NA |
| Platelet count | -1.29 | 0.466 | 0.00555 | Wald ratio | 1 | cis | NA |
| Mean platelet volume | 0.00333 | 0.00121 | 0.00596 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K57 Diverticular disease of intestine | 0.0506 | 0.0186 | 0.00659 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: prostate cancer | 0.0666 | 0.0305 | 0.029 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R35 Polyuria | 0.0881 | 0.0409 | 0.0311 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: deep venous thrombosis (dvt) | 0.0394 | 0.019 | 0.0379 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | 0.00971 | 0.0047 | 0.0388 | Wald ratio | 1 | cis | NA |
| Systolic blood pressure  automated reading | 0.00582 | 0.00285 | 0.0412 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N40 Hyperplasia of prostate | 0.0549 | 0.0274 | 0.0456 | Wald ratio | 1 | cis | NA |
| Vascular or heart problems diagnosed by doctor: Angina | -0.0322 | 0.0161 | 0.046 | Wald ratio | 1 | cis | NA |
| _...and 106 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2843_13_2` | SPINT2 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_91 association rows across 50 traits (77 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Bone mineral density mean | 1e-300 | rs73037316 | 2 | GCST90321120 | no MR -> candidate analysis |
| CDSN protein levels | 2e-156 | rs7253823 | 1 | GCST90468688 | no MR -> candidate analysis |
| Serum levels of protein SPINT2 | 7e-143 | rs11548457 | 1 | GCST90088100 | no MR -> candidate analysis |
| WFDC12 protein levels | 3e-93 | rs7251987 | 1 | GCST90471073 | no MR -> candidate analysis |
| Prostate cancer | 5e-79 | rs12976534 | 21 | GCST90274713 | MR: beta=0.0666, p=0.029 (cis) |
| PYDC1 protein levels | 8e-61 | rs761061860 | 1 | GCST90470397 | no MR -> candidate analysis |
| Circulating PRSS8 levels | 9e-46 | rs57822461 | 2 | GCST90859807 | no MR -> candidate analysis |
| Cancer of prostate (PheCode 185) | 3e-43 | rs12610267 | 2 | GCST90475591 | no MR -> candidate analysis |
| Circulating CDSN levels | 2e-36 | rs58711382 | 1 | GCST90860191 | no MR -> candidate analysis |
| Kunitz-type protease inhibitor 2 levels | 4e-34 | rs11548457 | 5 | GCST90161509 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 4e-32 | rs4802324 | 1 | GCST90838669 | no MR -> candidate analysis |
| PRSS8 protein levels | 2e-31 | rs58560372 | 1 | GCST90470345 | no MR -> candidate analysis |
| _...and 38 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 169 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| congenital sodium diarrhea | 0.871 | — | established (curated) | no MR -> candidate analysis |
| syndromic congenital sodium diarrhea | 0.608 | — | established (curated) | no MR -> candidate analysis |
| prostate carcinoma | 0.725 | — | common-variant locus | no MR -> candidate analysis |
| abdominal abscess | 0.456 | — | common-variant locus | no MR -> candidate analysis |
| digestive system disorder | 0.456 | — | common-variant locus | no MR -> candidate analysis |
| hereditary disease | 0.313 | — | established (curated) | no MR -> candidate analysis |
| prostate cancer | 0.144 | — | common-variant locus | MR: beta=0.0666, p=0.029 (cis) |
| diverticular disease | 0.135 | — | common-variant locus | MR: beta=0.0506, p=0.00659 (cis) |
| intestinal disorder | 0.116 | — | common-variant locus | no MR -> candidate analysis |
| cancer | 0.091 | — | common-variant locus | MR: beta=0.0936, p=0.00489 (cis) |

> Of the 10 rows above, **7 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Kunitz-type protease inhibitor 2) |
| gnomAD constraint | pLI=0.00044, LOEUF=0.886 — LoF-tolerant |
| GWAS Catalog | 95 unique SNPs / 189 rows |
| ClinVar | 226 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 169 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'SPINT2' and resolved to 'Kunitz-type protease inhibitor 2' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 226 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 50 traits by best p-value, aggregated from 91 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O43291 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000167642/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL6066288/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/SPINT2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/SPINT2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=SPINT2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/SPINT2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:12:52  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
