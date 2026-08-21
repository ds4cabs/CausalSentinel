# Protein Dossier — IL18R1 (Interleukin-18 receptor 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Crohn's disease | 0.114 | 0.0156 | 2.25e-13 | Wald ratio | 1 | cis | 4.67e-07 |
| Inflammatory bowel disease | 0.0862 | 0.013 | 2.84e-11 | Wald ratio | 1 | cis | 1.55e-07 |
| Eczema | 0.13 | 0.0218 | 2.78e-09 | Wald ratio | 1 | cis | 0.931 |
| Platelet count | -1.69 | 0.53 | 0.00146 | Wald ratio | 1 | cis | NA |
| Glioma | -0.175 | 0.0566 | 0.00197 | Wald ratio | 1 | cis | NA |
| Urinary albumin-to-creatinine ratio | -0.022 | 0.00782 | 0.00485 | Wald ratio | 1 | cis | NA |
| Ulcerative colitis | 0.0418 | 0.0164 | 0.0107 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M72 Fibroblastic disorders | 0.0997 | 0.0393 | 0.0111 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R07 Pain in throat and chest | 0.0344 | 0.0137 | 0.0122 | Wald ratio | 1 | cis | NA |
| Mean cell volume | 0.0804 | 0.0324 | 0.013 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: G47 Sleep disorders | -0.115 | 0.0467 | 0.0138 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: vitiligo | 0.342 | 0.14 | 0.0148 | Wald ratio | 1 | cis | NA |
| _...and 89 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3446_7_2` | IL-18 Ra | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_284 association rows across 121 traits (273 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating IL18R1 levels | 1e-4635 | rs12712145 | 5 | GCST90859873 | no MR -> candidate analysis |
| Circulating IL1RL1 levels | 9e-1796 | rs13029918 | 4 | GCST90859979 | no MR -> candidate analysis |
| ST2 protein levels | 7e-1635 | rs13020553 | 5 | GCST90012040 | no MR -> candidate analysis |
| interleukin-18 receptor 1 levels | 6e-996 | rs2270297 | 8 | GCST90274804 | no MR -> candidate analysis |
| Interleukin-18 receptor 1 (analyte X3446.7) levels | 5e-611 | rs12712135 | 1 | GCST90425769 | no MR -> candidate analysis |
| Interleukin-18 receptor 1 (analyte X14079.14) levels | 1e-576 | rs12712135 | 1 | GCST90422451 | no MR -> candidate analysis |
| Cerebrospinal fluid protein IL18R1 levels | 5e-367 | rs12996505 | 1 | GCST90943509 | no MR -> candidate analysis |
| Eosinophil count | 6e-305 | rs9807989 | 17 | GCST90002302 | no MR -> candidate analysis |
| Serum levels of protein IL1RL1 | 1e-296 | rs11676124 | 2 | GCST90088634 | no MR -> candidate analysis |
| Eosinophill percentage (UKB data field 30210) | 9e-285 | rs9807989 | 1 | GCST90468069 | no MR -> candidate analysis |
| eosinophil (fraction, mean, inv-norm transformed) | 2e-269 | rs13019081 | 3 | GCST90475300 | no MR -> candidate analysis |
| Interleukin-1 receptor-like 1 levels | 3e-257 | rs13029918 | 10 | GCST90248051 | no MR -> candidate analysis |
| _...and 109 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 438 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Ascending aortic dissection | 0.827 | — | established (curated) | no MR -> candidate analysis |
| Wheezing | 0.781 | — | common-variant locus | no MR -> candidate analysis |
| Behcet disease | 0.761 | — | established (curated) | no MR -> candidate analysis |
| asthma | 0.732 | — | common-variant locus | no MR -> candidate analysis |
| Eczematoid dermatitis | 0.687 | — | common-variant locus | no MR -> candidate analysis |
| atopic eczema | 0.695 | — | common-variant locus | no MR -> candidate analysis |
| ulcerative colitis | 0.652 | — | common-variant locus | MR: beta=0.0418, p=0.0107 (cis) |
| Crohn disease | 0.594 | — | common-variant locus | no MR -> candidate analysis |
| dermatitis | 0.571 | — | common-variant locus | no MR -> candidate analysis |
| inflammatory bowel disease | 0.559 | — | common-variant locus | MR: beta=0.0862, p=2.84e-11 (cis) |
| chronic obstructive pulmonary disease | 0.541 | — | common-variant locus | no MR -> candidate analysis |
| celiac disease | 0.56 | — | common-variant locus | no MR -> candidate analysis |
| lower respiratory tract disorder | 0.557 | — | common-variant locus | no MR -> candidate analysis |
| psoriasis | 0.522 | — | common-variant locus | MR: beta=-0.039, p=0.211 (cis) |
| nasal cavity polyp | 0.539 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **12 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 1 known modulators (IL18 Receptor) |
| gnomAD constraint | pLI=6.9e-12, LOEUF=1.07 — LoF-tolerant |
| GWAS Catalog | 215 unique SNPs / 545 rows |
| ClinVar | 83 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 438 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'IL18R1' and resolved to 'IL18 Receptor' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 83 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 121 traits by best p-value, aggregated from 284 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q13478 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000115604/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4804253/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/IL18R1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/IL18R1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=IL18R1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/IL18R1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:12:59  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
