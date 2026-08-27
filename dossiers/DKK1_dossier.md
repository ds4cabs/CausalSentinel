# Protein Dossier — DKK1 (Dickkopf-related protein 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Eye problems or disorders: Cataract | -0.342 | 0.107 | 0.00138 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: gout | 0.25 | 0.0904 | 0.00562 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Diabetes related eye disease | 0.34 | 0.127 | 0.00742 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R10 Abdominal and pelvic pain | -0.208 | 0.0822 | 0.0116 | Wald ratio | 1 | cis | NA |
| Large vessel disease | 0.508 | 0.208 | 0.0146 | Wald ratio | 1 | cis | NA |
| 2hr glucose | -0.258 | 0.11 | 0.0188 | Wald ratio | 1 | cis | NA |
| Low grade serous ovarian cancer | -0.566 | 0.27 | 0.0358 | Wald ratio | 1 | cis | NA |
| Red blood cell count | -0.0252 | 0.0121 | 0.0365 | Wald ratio | 1 | cis | NA |
| Underlying (primary) cause of death: ICD10: E85.4 Organ-limited amyloidosis | 1.84 | 0.949 | 0.053 | Wald ratio | 1 | cis | NA |
| Thalamus volume | -69.5 | 36.2 | 0.0551 | Wald ratio | 1 | cis | NA |
| Amygdala volume | 25.2 | 13.5 | 0.0629 | Wald ratio | 1 | cis | NA |
| Mean cell haemoglobin | 0.104 | 0.0565 | 0.0665 | Wald ratio | 1 | cis | NA |
| _...and 90 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3535_84_1` | DKK1 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_34 association rows across 28 traits (31 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| DKK1/PDGFA protein level ratio | 2e-196 | rs7093925 | 1 | GCST90314475 | no MR -> candidate analysis |
| DKK1/VEGFC protein level ratio | 1e-195 | rs7093925 | 1 | GCST90314484 | no MR -> candidate analysis |
| APP/DKK1 protein level ratio | 3e-187 | rs7093925 | 1 | GCST90313321 | no MR -> candidate analysis |
| DKK1/SERPINE1 protein level ratio | 9e-173 | rs7093925 | 1 | GCST90314480 | no MR -> candidate analysis |
| DKK1/SPARC protein level ratio | 1e-163 | rs7093925 | 1 | GCST90314481 | no MR -> candidate analysis |
| CCN2/DKK1 protein level ratio | 3e-156 | rs7093925 | 1 | GCST90313710 | no MR -> candidate analysis |
| ANGPT1/DKK1 protein level ratio | 3e-128 | rs7093925 | 1 | GCST90313263 | no MR -> candidate analysis |
| CPXM1/DKK1 protein level ratio | 1e-116 | rs7093925 | 1 | GCST90314218 | no MR -> candidate analysis |
| DKK1/PDGFB protein level ratio | 1e-107 | rs7093925 | 1 | GCST90314476 | no MR -> candidate analysis |
| Circulating DKK1 levels | 1e-91 | rs7097068 | 3 | GCST90859805 | no MR -> candidate analysis |
| DKK1/NID2 protein level ratio | 2e-81 | rs7093925 | 1 | GCST90314474 | no MR -> candidate analysis |
| DKK1/VEGFA protein level ratio | 2e-70 | rs7093925 | 1 | GCST90314483 | no MR -> candidate analysis |
| _...and 16 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 2274 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| alcohol drinking | 0.728 | — | common-variant locus | no MR -> candidate analysis |
| atrial fibrillation | 0.636 | — | common-variant locus | no MR -> candidate analysis |
| Arnold-Chiari malformation type I | 0.608 | — | established (curated) | no MR -> candidate analysis |
| androgenetic alopecia | 0.431 | — | common-variant locus | no MR -> candidate analysis |
| bone fracture | 0.408 | — | common-variant locus | no MR -> candidate analysis |
| malunion fracture | 0.409 | — | common-variant locus | no MR -> candidate analysis |
| radius fracture | 0.306 | — | common-variant locus | no MR -> candidate analysis |
| ulna fracture | 0.306 | — | common-variant locus | no MR -> candidate analysis |
| Pilonidal abscess | 0.295 | — | common-variant locus | no MR -> candidate analysis |
| spermatocele | 0.203 | — | common-variant locus | no MR -> candidate analysis |

> Of the 10 rows above, **10 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 2 known modulators (Dickkopf-related protein 1) |
| gnomAD constraint | pLI=5.3e-05, LOEUF=1.03 — LoF-tolerant |
| GWAS Catalog | 35 unique SNPs / 62 rows |
| ClinVar | 68 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 2274 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'DKK1' and resolved to 'Dickkopf-related protein 1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 68 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 28 traits by best p-value, aggregated from 34 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O94907 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000107984/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL6024/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/DKK1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/DKK1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=DKK1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/DKK1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:17:18  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
