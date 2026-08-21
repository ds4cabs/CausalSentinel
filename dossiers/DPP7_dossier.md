# Protein Dossier — DPP7 (Dipeptidyl peptidase 2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: hypertension | -0.0433 | 0.0135 | 0.00132 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R10 Abdominal and pelvic pain | -0.107 | 0.0408 | 0.00891 | Wald ratio | 1 | cis | NA |
| Clear cell ovarian cancer | 0.305 | 0.137 | 0.0261 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: J33 Nasal polyp | 0.194 | 0.0915 | 0.0339 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: arthritis (nos) | 0.156 | 0.0751 | 0.0376 | Wald ratio | 1 | cis | NA |
| Hirschsprung's disease | -0.962 | 0.473 | 0.042 | Wald ratio | 1 | cis | NA |
| Eczema | -0.125 | 0.0623 | 0.0444 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K80 Cholelithiasis | -0.119 | 0.0597 | 0.0461 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: psoriasis | -0.163 | 0.0847 | 0.0542 | Wald ratio | 1 | cis | NA |
| Birth weight | -0.0228 | 0.0121 | 0.0592 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: vaginal prolapse or uterine prolapse | 0.165 | 0.0879 | 0.0606 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: asthma | -0.0401 | 0.0221 | 0.0699 | Wald ratio | 1 | cis | NA |
| _...and 57 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3608_12_1` | DPP2 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_23 association rows across 19 traits (23 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| DPP7/SIAE protein level ratio | 1e-1546 | rs10747049 | 1 | GCST90314549 | no MR -> candidate analysis |
| DPP7/TPP1 protein level ratio | 7e-1468 | rs10747049 | 1 | GCST90314550 | no MR -> candidate analysis |
| DPP7/MCFD2 protein level ratio | 3e-1460 | rs10747049 | 1 | GCST90314547 | no MR -> candidate analysis |
| DPP7/GLB1 protein level ratio | 9e-1338 | rs10747049 | 1 | GCST90314545 | no MR -> candidate analysis |
| ARSA/DPP7 protein level ratio | 3e-1288 | rs10747049 | 1 | GCST90313353 | no MR -> candidate analysis |
| ARSB/DPP7 protein level ratio | 3e-1277 | rs10747049 | 1 | GCST90313358 | no MR -> candidate analysis |
| CREG1/DPP7 protein level ratio | 6e-1263 | rs10747049 | 1 | GCST90314248 | no MR -> candidate analysis |
| DPP7/PLA2G15 protein level ratio | 1e-1249 | rs10747049 | 1 | GCST90314548 | no MR -> candidate analysis |
| CANT1/DPP7 protein level ratio | 3e-1168 | rs10747049 | 1 | GCST90313614 | no MR -> candidate analysis |
| DPP7/LGMN protein level ratio | 7e-1110 | rs10747049 | 1 | GCST90314546 | no MR -> candidate analysis |
| DPP7/VSIR protein level ratio | 2e-1071 | rs10747049 | 1 | GCST90314551 | no MR -> candidate analysis |
| Dipeptidyl peptidase 2 levels | 3e-513 | rs10747049 | 5 | GCST90247349 | no MR -> candidate analysis |
| _...and 7 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 115 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Abnormality of the skeletal system | 0.067 | — | common-variant locus | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Dipeptidyl peptidase 2) |
| gnomAD constraint | pLI=8.5e-31, LOEUF=1.53 — LoF-tolerant |
| GWAS Catalog | 71 unique SNPs / 142 rows |
| ClinVar | 278 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 115 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'DPP7' and resolved to 'Dipeptidyl peptidase 2' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 278 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 19 of 19 traits by best p-value, aggregated from 23 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9UHL4 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000176978/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3976/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/DPP7 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/DPP7 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=DPP7%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/DPP7 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:20:03  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
