# Protein Dossier — RGMA (Repulsive guidance molecule A)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Height | -0.0705 | 0.0132 | 9.64e-08 | Wald ratio | 1 | trans | 0.847 |
| Urate | -0.0838 | 0.0243 | 5.51e-04 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: M17 Gonarthrosis [arthrosis of knee] | -0.00365 | 0.00113 | 0.00119 | Inverse variance weighted | 2 | cis | NA |
| Diagnoses - main ICD10: M17 Gonarthrosis [arthrosis of knee] | -0.00365 | 0.00113 | 0.00119 | Inverse variance weighted | 2 | trans | NA |
| Triglycerides | -0.0683 | 0.022 | 0.00194 | Wald ratio | 1 | trans | NA |
| Weight | -0.0212 | 0.00711 | 0.00287 | Inverse variance weighted | 2 | cis | NA |
| Weight | -0.0212 | 0.00711 | 0.00287 | Inverse variance weighted | 2 | trans | NA |
| Mean cell haemoglobin | 0.128 | 0.045 | 0.00433 | Wald ratio | 1 | trans | NA |
| Mean cell volume | 0.292 | 0.115 | 0.0108 | Wald ratio | 1 | trans | NA |
| Mean cell haemoglobin concentration | 0.037 | 0.0154 | 0.0164 | Wald ratio | 1 | trans | NA |
| Thalamus volume | -50.1 | 22 | 0.0231 | Inverse variance weighted | 2 | cis | NA |
| Thalamus volume | -50.1 | 22 | 0.0231 | Inverse variance weighted | 2 | trans | NA |
| _...and 171 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3833_10_2` | RGMA | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_122 association rows across 71 traits (77 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating RGMA levels | 1e-344 | rs3752102 | 3 | GCST90859669 | no MR -> candidate analysis |
| RGMA protein levels | 5e-307 | rs3752102 | 12 | GCST90470463 | no MR -> candidate analysis |
| RGMA/RGMB protein level ratio | 4e-299 | rs4778090 | 1 | GCST90315769 | no MR -> candidate analysis |
| ART3/RGMA protein level ratio | 3e-56 | rs35864810 | 1 | GCST90313362 | no MR -> candidate analysis |
| Repulsive guidance molecule A levels | 3e-54 | rs4778091 | 6 | GCST90249293 | no MR -> candidate analysis |
| Height | 3e-51 | rs4777828 | 11 | GCST90245848 | MR: beta=-0.0705, p=9.64e-08 (trans) |
| Hemojuvelin levels | 1e-34 | rs4778091 | 1 | GCST90247866 | no MR -> candidate analysis |
| Type 2 diabetes | 1e-23 | rs7167984 | 8 | GCST90492734 | MR: beta=0.0439, p=0.433 (trans) |
| Serum levels of protein RGMA | 2e-17 | rs4778093 | 1 | GCST90089056 | no MR -> candidate analysis |
| Repulsive guidance molecule A levels (RGMA.5483.1.3) | 3e-16 | rs3752102 | 1 | GCST90242629 | no MR -> candidate analysis |
| Heel bone mineral density | 7e-15 | rs4299103 | 3 | GCST007066 | MR: beta=0.0188, p=0.0706 (cis) |
| Neurofibrillary tangles (SNP x SNP interaction) | 2e-14 | rs17651511 x rs1947892 | 3 | GCST010343 | no MR -> candidate analysis |
| _...and 59 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 167 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| diabetes mellitus | 0.658 | — | common-variant locus | no MR -> candidate analysis |
| type 2 diabetes mellitus | 0.655 | — | common-variant locus | no MR -> candidate analysis |
| osteoarthritis, hip | 0.654 | — | common-variant locus | MR: beta=0.13, p=0.276 (trans) |
| placental abruption | 0.561 | — | common-variant locus | no MR -> candidate analysis |
| COVID-19 | 0.524 | — | common-variant locus | no MR -> candidate analysis |
| medical procedure | 0.524 | — | common-variant locus | no MR -> candidate analysis |
| pregnancy disorder | 0.519 | — | common-variant locus | no MR -> candidate analysis |
| DNA methylation | 0.447 | — | common-variant locus | no MR -> candidate analysis |
| stroke disorder | 0.396 | — | common-variant locus | no MR -> candidate analysis |
| ovarian dysfunction | 0.424 | — | common-variant locus | no MR -> candidate analysis |
| opiate dependence | 0.408 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of refraction | 0.409 | — | common-variant locus | no MR -> candidate analysis |
| Parkinson disease | 0.396 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.396 | — | common-variant locus | no MR -> candidate analysis |
| sign or symptom | 0.396 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **14 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 2 known modulators (Repulsive guidance molecule A) |
| gnomAD constraint | pLI=0.2, LOEUF=0.732 — LoF-tolerant |
| GWAS Catalog | 125 unique SNPs / 212 rows |
| ClinVar | 141 records; 4 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 167 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'RGMA' and resolved to 'Repulsive guidance molecule A' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 141 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 71 traits by best p-value, aggregated from 122 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q96B86 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000182175/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4630886/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/RGMA — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/RGMA — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=RGMA%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/RGMA — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:48:59  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
