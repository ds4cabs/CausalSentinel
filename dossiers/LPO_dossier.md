# Protein Dossier — LPO (Lactoperoxidase)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: high cholesterol | 0.107 | 0.0308 | 4.85e-04 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | 0.315 | 0.112 | 0.00482 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: migraine | -0.258 | 0.0957 | 0.00708 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: M54 Dorsalgia | 0.206 | 0.0806 | 0.0106 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: K80 Cholelithiasis | 0.175 | 0.0745 | 0.0189 | Wald ratio | 1 | trans | NA |
| Cancer code  self-reported: small intestine or small bowel cancer | 0.737 | 0.323 | 0.0224 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: psoriasis | 0.218 | 0.0969 | 0.0248 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: iron deficiency anaemia | 0.296 | 0.132 | 0.0249 | Wald ratio | 1 | trans | NA |
| Hearing difficulty or problems: Yes | -0.0493 | 0.023 | 0.0319 | Wald ratio | 1 | trans | NA |
| Fractured or broken bones in last 5 years | 0.0685 | 0.0369 | 0.0636 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: uterine fibroids | 0.163 | 0.0877 | 0.0638 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: S66 Injury of muscle and tendon at wrist and hand level | 0.405 | 0.225 | 0.071 | Wald ratio | 1 | trans | NA |
| _...and 66 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4801_13_3` | PERL | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_37 association rows across 24 traits (26 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| LPO protein levels | 4e-101 | rs368901060 | 3 | GCST90469789 | no MR -> candidate analysis |
| Lactoperoxidase levels | 4e-62 | rs8178290 | 3 | GCST90248228 | no MR -> candidate analysis |
| Serum levels of protein LPO | 9e-38 | rs62083746 | 1 | GCST90088774 | no MR -> candidate analysis |
| Cerebrospinal fluid protein LPO levels | 3e-33 | rs7219860 | 1 | GCST90943593 | no MR -> candidate analysis |
| Eosinophil count | 5e-31 | rs536070968 | 3 | GCST90018733 | no MR -> candidate analysis |
| Basophil count | 4e-28 | rs546552332 | 1 | GCST90002379 | no MR -> candidate analysis |
| Monocyte percentage of white cells | 3e-19 | rs8178414 | 1 | GCST90002394 | no MR -> candidate analysis |
| Basophil percentage of white cells | 4e-18 | rs546552332 | 1 | GCST90002380 | no MR -> candidate analysis |
| Lactoperoxidase levels (LPO.4801.13.3) | 5e-18 | rs11337012 | 1 | GCST90241730 | no MR -> candidate analysis |
| TNFRSF10C protein levels | 5e-16 | rs8178414 | 1 | GCST90470901 | no MR -> candidate analysis |
| Basophil percentage of white cells variance | 2e-12 | rs546552332 | 1 | GCST90565688 | no MR -> candidate analysis |
| Chromodomain Y-like protein 2 levels | 5e-12 | rs8178340 | 1 | GCST90246969 | no MR -> candidate analysis |
| _...and 12 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 2235 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Joubert syndrome | 0.901 | — | established (curated) | no MR -> candidate analysis |
| Meckel syndrome | 0.9 | — | established (curated) | no MR -> candidate analysis |
| Meckel syndrome, type 1 | 0.83 | — | established (curated) | no MR -> candidate analysis |
| Bardet-Biedl syndrome 13 | 0.819 | — | established (curated) | no MR -> candidate analysis |
| Joubert syndrome 28 | 0.67 | — | established (curated) | no MR -> candidate analysis |
| hereditary disease | 0.3 | — | established (curated) | no MR -> candidate analysis |
| Retinal dystrophy | 0.195 | — | established (curated) | no MR -> candidate analysis |

> Of the 7 rows above, **7 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Lactoperoxidase) |
| gnomAD constraint | pLI=8.6e-25, LOEUF=1.25 — LoF-tolerant |
| GWAS Catalog | 102 unique SNPs / 212 rows |
| ClinVar | 139 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 2235 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'LPO' and resolved to 'Lactoperoxidase' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 139 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 24 traits by best p-value, aggregated from 37 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P22079 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000167419/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL5898/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/LPO — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/LPO — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=LPO%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/LPO — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:36:44  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
