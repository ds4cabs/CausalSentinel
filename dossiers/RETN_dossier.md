# Protein Dossier — RETN (Resistin)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Multiple sclerosis | -0.62 | 0.132 | 2.59e-06 | Wald ratio | 1 | trans | NA |
| Hip osteoarthritis | -0.65 | 0.212 | 0.00213 | Wald ratio | 1 | trans | NA |
| Fasting proinsulin | -0.159 | 0.0559 | 0.00452 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: K80 Cholelithiasis | -0.00309 | 0.00117 | 0.00804 | Inverse variance weighted | 3 | cis | NA |
| Diagnoses - main ICD10: K80 Cholelithiasis | -0.00309 | 0.00117 | 0.00804 | Inverse variance weighted | 3 | trans | NA |
| Diagnoses - main ICD10: K80 Cholelithiasis | -0.00309 | 0.00117 | 0.00804 | Inverse variance weighted | 3 | trans | NA |
| Non-cancer illness code  self-reported: enlarged prostate | -0.00215 | 0.000946 | 0.0229 | Inverse variance weighted | 3 | cis | NA |
| Non-cancer illness code  self-reported: enlarged prostate | -0.00215 | 0.000946 | 0.0229 | Inverse variance weighted | 3 | trans | NA |
| Non-cancer illness code  self-reported: enlarged prostate | -0.00215 | 0.000946 | 0.0229 | Inverse variance weighted | 3 | trans | NA |
| Crohn's disease | -0.208 | 0.0972 | 0.0326 | Wald ratio | 1 | trans | NA |
| Knee and hip osteoarthritis | -0.354 | 0.166 | 0.033 | Wald ratio | 1 | trans | NA |
| Major depressive disorder | 0.343 | 0.165 | 0.0374 | Wald ratio | 1 | trans | NA |
| _...and 193 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3046_31_1` | resistin | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_41 association rows across 15 traits (39 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Resistin levels | 2e-858 | rs3219175 | 20 | GCST003759 | no MR -> candidate analysis |
| Circulating RETN levels | 4e-481 | rs3745368 | 6 | GCST90859950 | no MR -> candidate analysis |
| LCN2/RETN protein level ratio | 2e-437 | rs34124816 | 1 | GCST90315308 | no MR -> candidate analysis |
| COL18A1/RETN protein level ratio | 1e-287 | rs34124816 | 1 | GCST90314170 | no MR -> candidate analysis |
| CST3/RETN protein level ratio | 4e-274 | rs34124816 | 1 | GCST90314297 | no MR -> candidate analysis |
| RETN/RNASET2 protein level ratio | 3e-273 | rs34124816 | 1 | GCST90315768 | no MR -> candidate analysis |
| RETN protein levels | 1e-92 | rs35547567 | 2 | GCST90470457 | no MR -> candidate analysis |
| Resistin levels in overweight individuals | 6e-64 | rs3219175 | 1 | GCST90091185 | no MR -> candidate analysis |
| Resistin levels in type 2 diabetes | 3e-59 | rs3219175 | 1 | GCST90091204 | no MR -> candidate analysis |
| Resistin levels in lean individuals | 2e-50 | rs3219175 | 1 | GCST90091174 | no MR -> candidate analysis |
| Resistin level in Chronic kidney disease with hypertension a | 1e-47 | rs3219175 | 1 | GCST90237214 | no MR -> candidate analysis |
| Cerebrospinal fluid biomarker levels | 6e-39 | rs3219175 | 1 | GCST004000 | no MR -> candidate analysis |
| _...and 3 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 745 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| autism | 0.182 | — | established (curated) | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.018, LOEUF=1.73 — LoF-tolerant |
| GWAS Catalog | 111 unique SNPs / 266 rows |
| ClinVar | 26 records; 5 pathogenic in sample of 26 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 745 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'RETN'.
- **`clinvar`** — Pathogenic count is over the 26 record(s) retrieved, NOT over all 26 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 15 of 15 traits by best p-value, aggregated from 41 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9HD89 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000104918/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/RETN — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/RETN — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=RETN%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/RETN — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:48:22  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
