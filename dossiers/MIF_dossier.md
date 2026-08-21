# Protein Dossier — MIF (Anti-Muellerian hormone)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: gout | 0.143 | 0.0553 | 0.00957 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: bladder problem (not cancer) | 0.184 | 0.0835 | 0.0276 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | -0.249 | 0.118 | 0.0345 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: G47 Sleep disorders | 0.174 | 0.0839 | 0.0381 | Wald ratio | 1 | trans | NA |
| Hirschsprung's disease | -0.947 | 0.461 | 0.04 | Wald ratio | 1 | trans | NA |
| Body fat | -0.0344 | 0.0169 | 0.042 | Wald ratio | 1 | trans | NA |
| Underlying (primary) cause of death: ICD10: E85.4 Organ-limited amyloidosis | 1.35 | 0.664 | 0.0421 | Wald ratio | 1 | trans | NA |
| Neo-neuroticism | 0.576 | 0.294 | 0.0504 | Wald ratio | 1 | trans | NA |
| Neo-agreeableness | -0.368 | 0.19 | 0.0526 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: hypertension | 0.023 | 0.0127 | 0.0687 | Wald ratio | 1 | trans | NA |
| Lung cancer | 0.106 | 0.0586 | 0.0701 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: R14 Flatulence and related conditions | 0.4 | 0.225 | 0.0752 | Wald ratio | 1 | trans | NA |
| _...and 105 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4923_79_1` | MIS | Suhre K | 2019 |
| `prot-c-5356_2_3` | MIF | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_114 association rows across 70 traits (110 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Glutathione S-transferase theta-2B levels | 2e-447 | rs5751777 | 1 | GCST90247824 | no MR -> candidate analysis |
| Cerebrospinal fluid protein GSTT2B levels | 2e-445 | rs5751777 | 1 | GCST90943447 | no MR -> candidate analysis |
| MIF/PARK7 protein level ratio | 1e-391 | rs4822455 | 1 | GCST90315447 | no MR -> candidate analysis |
| MIF/STIP1 protein level ratio | 1e-338 | rs4822455 | 1 | GCST90315451 | no MR -> candidate analysis |
| Glutathione S-transferase theta-1 levels | 2e-330 | rs2000468 | 1 | GCST90423466 | no MR -> candidate analysis |
| MIF/PEBP1 protein level ratio | 3e-298 | rs4822455 | 1 | GCST90315448 | no MR -> candidate analysis |
| HARS1/MIF protein level ratio | 6e-281 | rs4822455 | 1 | GCST90315024 | no MR -> candidate analysis |
| FHIT/MIF protein level ratio | 2e-255 | rs4822455 | 1 | GCST90314819 | no MR -> candidate analysis |
| MIF/S100A4 protein level ratio | 2e-242 | rs4822455 | 1 | GCST90315449 | no MR -> candidate analysis |
| X-16071 levels | 8e-241 | rs5751777 | 1 | GCST90245605 | no MR -> candidate analysis |
| GLOD4/MIF protein level ratio | 1e-184 | rs4822455 | 1 | GCST90314939 | no MR -> candidate analysis |
| MIF/SERPINB1 protein level ratio | 1e-176 | rs4822455 | 1 | GCST90315450 | no MR -> candidate analysis |
| _...and 58 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1390 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| systemic-onset juvenile idiopathic arthritis | 0.304 | — | established (curated) | no MR -> candidate analysis |
| cystic fibrosis | 0.608 | — | established (curated) | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 2 known modulators (Macrophage migration inhibitory factor) |
| gnomAD constraint | pLI=1.2e-07, LOEUF=2.16 — LoF-tolerant |
| GWAS Catalog | 112 unique SNPs / 276 rows |
| ClinVar | 162 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1390 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'MIF' and resolved to 'Macrophage migration inhibitory factor' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 162 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 70 traits by best p-value, aggregated from 114 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P03971 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000240972/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2085/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/MIF — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/MIF — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=MIF%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/MIF — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:48:23  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
