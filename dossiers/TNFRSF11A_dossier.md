# Protein Dossier — TNFRSF11A (Tumor necrosis factor receptor superfamily member 11A)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Paget's disease | 2.15 | 0.297 | 4.72e-13 | Wald ratio | 1 | cis | 0.99 |
| Heel bone mineral density (BMD) T-score  automated | -0.111 | 0.0161 | 6.61e-12 | Wald ratio | 1 | cis | 1 |
| Lumbar spine bone mineral density | -0.278 | 0.0457 | 1.12e-09 | Wald ratio | 1 | cis | NA |
| Femoral neck bone mineral density | -0.189 | 0.0394 | 1.60e-06 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: osteoporosis | 0.27 | 0.0767 | 4.31e-04 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Wrist | 0.229 | 0.071 | 0.00127 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M17 Gonarthrosis [arthrosis of knee] | -0.472 | 0.148 | 0.00138 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | -0.0362 | 0.0124 | 0.00361 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: vaginal prolapse or uterine prolapse | 0.349 | 0.121 | 0.00393 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | 0.0279 | 0.0102 | 0.00621 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M16 Coxarthrosis [arthrosis of hip] | -0.375 | 0.155 | 0.0158 | Wald ratio | 1 | cis | NA |
| Fasting insulin | -0.0371 | 0.0161 | 0.0211 | Wald ratio | 1 | cis | NA |
| _...and 104 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5424_55_3` | RANK | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_120 association rows across 71 traits (109 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| TNFRSF11A/TNFRSF1A protein level ratio | 1e-1835 | rs74938001 | 1 | GCST90315928 | no MR -> candidate analysis |
| Circulating TNFRSF11A levels | 2e-1622 | rs62098352 | 3 | GCST90859756 | no MR -> candidate analysis |
| TNFRSF11A/TNFRSF1B protein level ratio | 2e-1447 | rs74938001 | 1 | GCST90315929 | no MR -> candidate analysis |
| Tumor necrosis factor receptor superfamily member 11A levels | 9e-101 | rs80067526 | 3 | GCST90179450 | no MR -> candidate analysis |
| Cerebrospinal fluid protein TNFRSF11A levels | 2e-79 | rs35211496 | 1 | GCST90943993 | no MR -> candidate analysis |
| Alkaline phosphatase (UKB data field 30610) | 3e-73 | rs884205 | 1 | GCST90468060 | no MR -> candidate analysis |
| Serum alkaline phosphatase levels | 3e-65 | rs884205 | 7 | GCST90018942 | no MR -> candidate analysis |
| TNFRSF11A protein levels | 9e-47 | rs141434942 | 10 | GCST90470902 | no MR -> candidate analysis |
| Heel bone mineral density | 6e-38 | rs884205 | 7 | GCST006979 | MR: beta=-0.111, p=6.61e-12 (cis) |
| Estimated bone mineral density | 3e-35 | rs884205 | 2 | GCST90726625 | no MR -> candidate analysis |
| Height | 5e-28 | rs884205 | 2 | GCST90245848 | MR: beta=0.0183, p=0.228 (cis) |
| Circulating COL1A1 levels | 4e-27 | rs2957126 | 1 | GCST90859986 | no MR -> candidate analysis |
| _...and 59 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1431 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Osteopetrosis - hypogammaglobulinemia | 0.847 | — | established (curated) | no MR -> candidate analysis |
| autosomal recessive osteopetrosis 7 | 0.829 | — | established (curated) | no MR -> candidate analysis |
| familial expansile osteolysis | 0.738 | — | established (curated) | no MR -> candidate analysis |
| bone Paget disease | 0.531 | — | established (curated) | no MR -> candidate analysis |
| osteoporosis | 0.839 | — | common-variant locus | MR: beta=0.27, p=4.31e-04 (cis) |
| bone disorder | 0.582 | — | established (curated) | MR: beta=0.177, p=0.458 (cis) |
| asthma | 0.69 | — | common-variant locus | no MR -> candidate analysis |
| hypothyroidism | 0.715 | — | common-variant locus | MR: beta=-0.143, p=0.0261 (cis) |
| allergic rhinitis | 0.696 | — | common-variant locus | MR: beta=-0.0945, p=0.0941 (cis) |
| Eczematoid dermatitis | 0.664 | — | common-variant locus | no MR -> candidate analysis |
| childhood onset asthma | 0.656 | — | common-variant locus | no MR -> candidate analysis |
| myasthenia gravis | 0.629 | — | common-variant locus | no MR -> candidate analysis |
| dysosteosclerosis | 0.608 | — | established (curated) | no MR -> candidate analysis |
| osteoarthritis, hip | 0.609 | — | common-variant locus | MR: beta=-0.183, p=0.0864 (cis) |
| myxedema | 0.604 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **10 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Tumor necrosis factor ligand superfamily member 11/11A) |
| gnomAD constraint | pLI=5.4e-06, LOEUF=0.772 — LoF-tolerant |
| GWAS Catalog | 73 unique SNPs / 146 rows |
| ClinVar | 891 records; 5 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 2 clinical annotations across 6 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1431 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'TNFRSF11A' and resolved to 'Tumor necrosis factor ligand superfamily member 11/11A' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 891 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 20 of 71 traits by best p-value, aggregated from 120 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9Y6Q6 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000141655/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4296079/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/TNFRSF11A — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/TNFRSF11A — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=TNFRSF11A%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=TNFRSF11A — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/TNFRSF11A — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:25:58  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
