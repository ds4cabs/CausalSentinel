# Protein Dossier — IL1R1 (Interleukin-1 receptor type 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: asthma | 0.242 | 0.0356 | 1.01e-11 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hayfever or allergic rhinitis | 0.185 | 0.0555 | 8.79e-04 | Wald ratio | 1 | cis | NA |
| Internalizing problems | 0.46 | 0.151 | 0.00233 | Wald ratio | 1 | cis | NA |
| Schizophrenia | -0.215 | 0.0706 | 0.00234 | Wald ratio | 1 | cis | NA |
| Childhood intelligence | -0.253 | 0.0871 | 0.00371 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Glaucoma | 0.265 | 0.105 | 0.0115 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | 0.0314 | 0.0133 | 0.0181 | Wald ratio | 1 | cis | NA |
| Mean cell volume | 0.391 | 0.168 | 0.0201 | Wald ratio | 1 | cis | NA |
| Eczema | 0.261 | 0.113 | 0.0211 | Wald ratio | 1 | cis | NA |
| Mean cell haemoglobin | 0.145 | 0.0663 | 0.0282 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: G56 Mononeuropathies of upper limb | 0.216 | 0.1 | 0.0308 | Wald ratio | 1 | cis | NA |
| Knee and hip osteoarthritis | -0.315 | 0.148 | 0.033 | Wald ratio | 1 | cis | NA |
| _...and 106 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2991_9_2` | IL-1 sRI | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_121 association rows across 68 traits (105 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating IL1RL2 levels | 3e-1790 | rs3917265 | 2 | GCST90859762 | no MR -> candidate analysis |
| Circulating IL1R1 levels | 2e-207 | rs956730 | 8 | GCST90859959 | no MR -> candidate analysis |
| IL1R1 protein levels | 1e-176 | rs3917238 | 4 | GCST90469571 | no MR -> candidate analysis |
| Circulating IL1R2 levels | 4e-124 | rs115860741 | 2 | GCST90859972 | no MR -> candidate analysis |
| IL1RL1 protein levels | 3e-106 | rs10203724 | 2 | GCST90469574 | no MR -> candidate analysis |
| IL1R2 protein levels | 2e-103 | rs11883987 | 9 | GCST90469572 | no MR -> candidate analysis |
| Interleukin-1 receptor-like 2 levels | 9e-82 | rs3917265 | 4 | GCST90248052 | no MR -> candidate analysis |
| Interleukin-1 receptor type 1 levels | 9e-64 | rs7587167 | 4 | GCST90425563 | no MR -> candidate analysis |
| Serum levels of protein IL1RL2 | 7e-60 | rs3917265 | 2 | GCST90088174 | no MR -> candidate analysis |
| IL1RL2 protein levels | 2e-55 | rs41294844 | 2 | GCST90469575 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 4e-48 | rs67985128 | 1 | GCST90838669 | no MR -> candidate analysis |
| Cerebrospinal fluid protein IL1R1 levels | 5e-42 | rs11685537 | 1 | GCST90944793 | no MR -> candidate analysis |
| _...and 56 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1305 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Ascending aortic dissection | 0.745 | — | established (curated) | no MR -> candidate analysis |
| asthma | 0.635 | — | common-variant locus | MR: beta=0.242, p=1.01e-11 (cis) |
| inflammatory bowel disease | 0.665 | — | common-variant locus | MR: beta=-0.0575, p=0.394 (cis) |
| gout | 0.532 | — | common-variant locus | no MR -> candidate analysis |
| chronic recurrent multifocal osteomyelitis 3 | 0.547 | — | established (curated) | no MR -> candidate analysis |
| ulcerative colitis | 0.505 | — | common-variant locus | MR: beta=-0.141, p=0.0965 (cis) |
| coronary artery disorder | 0.443 | — | common-variant locus | no MR -> candidate analysis |
| intestinal obstruction | 0.448 | — | common-variant locus | no MR -> candidate analysis |
| ischemic stroke | 0.443 | — | common-variant locus | MR: beta=0.0908, p=0.4 (cis) |

> Of the 9 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 3 known modulators (Interleukin-1 receptor type 1) |
| gnomAD constraint | pLI=0.07, LOEUF=0.626 — LoF-tolerant |
| GWAS Catalog | 151 unique SNPs / 370 rows |
| ClinVar | 81 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1305 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'IL1R1' and resolved to 'Interleukin-1 receptor type 1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 81 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 68 traits by best p-value, aggregated from 121 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P14778 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000115594/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL1959/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/IL1R1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/IL1R1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=IL1R1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/IL1R1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:13:43  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
