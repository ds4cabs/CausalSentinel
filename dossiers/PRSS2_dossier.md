# Protein Dossier — PRSS2 (Trypsin-2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Multiple sclerosis | -0.338 | 0.088 | 1.24e-04 | Wald ratio | 1 | trans | NA |
| Ulcerative colitis | -0.242 | 0.0678 | 3.55e-04 | Wald ratio | 1 | trans | NA |
| Age at menopause | -0.358 | 0.107 | 8.58e-04 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: K43 Ventral hernia | 0.307 | 0.0952 | 0.00127 | Inverse variance weighted | 2 | trans | NA |
| Diagnoses - main ICD10: K43 Ventral hernia | 0.307 | 0.0952 | 0.00127 | Inverse variance weighted | 2 | trans | NA |
| Myocardial infarction | 0.128 | 0.0413 | 0.00201 | Inverse variance weighted | 2 | trans | NA |
| Myocardial infarction | 0.128 | 0.0413 | 0.00201 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: psoriasis | -0.335 | 0.114 | 0.00332 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: psoriasis | -0.335 | 0.114 | 0.00332 | Inverse variance weighted | 2 | trans | NA |
| Neo-openness to experience | -1.12 | 0.389 | 0.00403 | Wald ratio | 1 | trans | NA |
| Neuroblastoma | -0.616 | 0.224 | 0.00588 | Wald ratio | 1 | trans | NA |
| Birth length | -0.12 | 0.0436 | 0.00603 | Wald ratio | 1 | trans | NA |
| _...and 153 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5034_79_1` | Trypsin 2 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_43 association rows across 16 traits (39 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| CTRB1/PRSS2 protein level ratio | 3e-340 | rs10952532 | 1 | GCST90314308 | no MR -> candidate analysis |
| CPB1/PRSS2 protein level ratio | 6e-339 | rs10952532 | 1 | GCST90314211 | no MR -> candidate analysis |
| PLA2G1B/PRSS2 protein level ratio | 4e-152 | rs10952532 | 1 | GCST90315665 | no MR -> candidate analysis |
| PRSS2 protein levels | 2e-106 | rs3752404 | 1 | GCST90470343 | no MR -> candidate analysis |
| Circulating PRSS2 levels | 2e-101 | rs4726588 | 1 | GCST90860437 | no MR -> candidate analysis |
| Alcoholic chronic pancreatitis | 5e-40 | rs2855983 | 26 | GCST004860 | no MR -> candidate analysis |
| CTRB1 protein levels | 3e-21 | rs1969595 | 1 | GCST90468905 | no MR -> candidate analysis |
| Trypsin-2 levels (PRSS2.5034.79.1) | 3e-20 | rs13229701 | 1 | GCST90243126 | no MR -> candidate analysis |
| Chronic pancreatitis (PheCode 577.2) | 5e-17 | rs2855972 | 2 | GCST90480358 | no MR -> candidate analysis |
| Serum levels of protein PRSS2 | 5e-14 | rs10258394 | 1 | GCST90088888 | no MR -> candidate analysis |
| Trypsin-2 levels | 3e-12 | rs28706856 | 2 | GCST90137836 | no MR -> candidate analysis |
| Diseases of pancreas (PheCode 577) | 3e-12 | rs2855972 | 1 | GCST90480360 | no MR -> candidate analysis |
| _...and 4 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 246 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| alcoholic pancreatitis | 0.697 | — | common-variant locus | no MR -> candidate analysis |
| acute pancreatitis | 0.503 | — | common-variant locus | no MR -> candidate analysis |
| chronic pancreatitis | 0.505 | — | common-variant locus | no MR -> candidate analysis |
| pancreatitis | 0.057 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Trypsin-2) |
| gnomAD constraint | pLI=3.2e-07, LOEUF=1.45 — LoF-tolerant |
| GWAS Catalog | 105 unique SNPs / 209 rows |
| ClinVar | 31 records; 22 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 246 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'PRSS2' and resolved to 'Trypsin-2' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 31 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 16 of 16 traits by best p-value, aggregated from 43 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P07478 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000275896/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3159/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PRSS2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PRSS2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PRSS2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PRSS2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:37:51  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
