# Protein Dossier — SPINK2 (Serine protease inhibitor Kazal-type 2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Squamous cell lung cancer | -0.31 | 0.0649 | 1.79e-06 | Inverse variance weighted | 2 | trans | 2.96e-07 |
| Squamous cell lung cancer | -0.31 | 0.0649 | 1.79e-06 | Inverse variance weighted | 2 | cis | 0.834 |
| Diagnoses - main ICD10: I83 Varicose veins of lower extremities | 0.129 | 0.0526 | 0.0141 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: polio  or  poliomyelitis | 0.504 | 0.208 | 0.0152 | Wald ratio | 1 | cis | NA |
| Cough on most days | -0.11 | 0.0483 | 0.0224 | Wald ratio | 1 | cis | NA |
| Primary sclerosing cholangitis  | -0.235 | 0.121 | 0.052 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hiatus hernia | -0.113 | 0.0631 | 0.0722 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hyperthyroidism or thyrotoxicosis | 0.149 | 0.0863 | 0.0842 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K44 Diaphragmatic hernia | -0.135 | 0.0789 | 0.0862 | Wald ratio | 1 | cis | NA |
| Neuroticism | -0.0352 | 0.0205 | 0.0865 | Wald ratio | 1 | trans | NA |
| Depressive symptoms | -0.044 | 0.0264 | 0.0956 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: R10 Abdominal and pelvic pain | -0.0716 | 0.0444 | 0.107 | Wald ratio | 1 | cis | NA |
| _...and 70 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_147 association rows across 95 traits (135 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Serine protease inhibitor Kazal-type 2 levels | 2e-111 | rs781538 | 2 | GCST90422125 | no MR -> candidate analysis |
| Cerebrospinal fluid protein SPINK2 levels | 9e-110 | rs146649464 | 1 | GCST90944595 | no MR -> candidate analysis |
| Height | 1e-109 | rs66790703 | 9 | GCST90662911 | no MR -> candidate analysis |
| Platelet count | 2e-77 | rs7665147 | 9 | GCST90662907 | no MR -> candidate analysis |
| Cerebellar grey matter morphology (MOSTest) | 6e-60 | rs3806746 | 1 | GCST90728589 | no MR -> candidate analysis |
| Serum levels of protein SPINK2 | 1e-57 | rs34393987 | 2 | GCST90087423 | no MR -> candidate analysis |
| CBLN4 protein levels | 9e-53 | rs571492629 | 1 | GCST90468554 | no MR -> candidate analysis |
| SPINK2 protein levels | 5e-50 | rs11133463 | 4 | GCST90470722 | no MR -> candidate analysis |
| Platelet count (UKB data field 30080) | 2e-42 | rs58408429 | 1 | GCST90468095 | no MR -> candidate analysis |
| Mean platelet thrombocyte volume (UKB data field 30100) | 2e-38 | rs55762216 | 1 | GCST90468087 | no MR -> candidate analysis |
| Serine protease inhibitor Kazal-type 2 levels (SPINK2.13405. | 2e-33 | rs11941335 | 1 | GCST90242763 | no MR -> candidate analysis |
| White blood cell count | 3e-31 | rs58408429 | 6 | GCST90002378 | no MR -> candidate analysis |
| _...and 83 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 161 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| spermatogenic failure 29 | 0.596 | — | established (curated) | no MR -> candidate analysis |
| male infertility with azoospermia or oligozoospermia due to single gene mutation | 0.608 | — | established (curated) | no MR -> candidate analysis |
| migraine disorder | 0.417 | — | common-variant locus | no MR -> candidate analysis |
| Pain | 0.319 | — | common-variant locus | MR: beta=-0.0716, p=0.107 (cis) |
| nervous system benign neoplasm | 0.209 | — | common-variant locus | no MR -> candidate analysis |
| risk-taking behaviour | 0.116 | — | common-variant locus | no MR -> candidate analysis |

> Of the 6 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.022, LOEUF=1.07 — LoF-tolerant |
| GWAS Catalog | 118 unique SNPs / 246 rows |
| ClinVar | 47 records; 6 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 161 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'SPINK2'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 47 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 95 traits by best p-value, aggregated from 147 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P20155 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000128040/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/SPINK2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/SPINK2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=SPINK2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/SPINK2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:11:45  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
