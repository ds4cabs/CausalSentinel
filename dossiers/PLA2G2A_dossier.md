# Protein Dossier — PLA2G2A (Phospholipase A2, membrane associated)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Cancer code  self-reported: prostate cancer | 0.0829 | 0.0305 | 0.00649 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: vitiligo | 0.333 | 0.125 | 0.00762 | Wald ratio | 1 | cis | NA |
| Fasting glucose | 0.0098 | 0.00382 | 0.0103 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: osteoarthritis | -0.0225 | 0.00968 | 0.0202 | Wald ratio | 1 | cis | NA |
| Percent emphysema | -0.0478 | 0.0208 | 0.0213 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: basal cell carcinoma | 0.0633 | 0.0277 | 0.0224 | Wald ratio | 1 | cis | NA |
| Fractured or broken bones in last 5 years | -0.0194 | 0.009 | 0.031 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: joint disorder | -0.0978 | 0.0456 | 0.0321 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: G47 Sleep disorders | 0.073 | 0.0343 | 0.0334 | Wald ratio | 1 | cis | NA |
| Bipolar disorder | 0.0586 | 0.0294 | 0.0463 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I83 Varicose veins of lower extremities | 0.0375 | 0.019 | 0.0488 | Wald ratio | 1 | cis | NA |
| Height | 0.00706 | 0.00363 | 0.0517 | Wald ratio | 1 | cis | NA |
| _...and 68 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2692_74_2` | NPS-PLA2 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_36 association rows across 17 traits (34 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Phospholipase A2, membrane associated levels | 2e-1000 | rs11573156 | 6 | GCST90248834 | no MR -> candidate analysis |
| Group IIA secretory phospholipase A2 levels in individuals w | 5e-472 | rs11573156 | 3 | GCST008260 | no MR -> candidate analysis |
| Phospholipase A2, membrane associated levels (PLA2G2A.2692.7 | 2e-384 | rs11573156 | 2 | GCST90242257 | no MR -> candidate analysis |
| Serum levels of protein PLA2G2A | 1e-292 | rs11573156 | 2 | GCST90088020 | no MR -> candidate analysis |
| PLA2G2A protein levels | 5e-265 | rs1588050 | 11 | GCST90470247 | no MR -> candidate analysis |
| Blood protein levels | 2e-111 | rs4744 | 1 | GCST006585 | no MR -> candidate analysis |
| A0A3B3IRX2;PA2GA protein level (protein group normalized int | 2e-38 | rs2307246 | 1 | GCST90570761 | no MR -> candidate analysis |
| Protein levels in obesity | 3e-26 | rs10732279 | 1 | GCST010196 | no MR -> candidate analysis |
| Brevican core protein protein levels (SomaScan ID:2692-74) | 4e-23 | rs11573156 | 1 | GCST90440967 | no MR -> candidate analysis |
| CXCL14 protein levels | 3e-17 | rs11573156 | 1 | GCST90468927 | no MR -> candidate analysis |
| Circulating CCDC80 levels | 1e-16 | rs11573156 | 1 | GCST90860352 | no MR -> candidate analysis |
| LECT2 protein levels | 4e-16 | rs11573156 | 1 | GCST90469751 | no MR -> candidate analysis |
| _...and 5 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 400 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| familial colorectal cancer | 0.547 | — | established (curated) | no MR -> candidate analysis |
| ectropion | 0.448 | — | common-variant locus | no MR -> candidate analysis |
| entropion | 0.448 | — | common-variant locus | no MR -> candidate analysis |
| breast adenosis | 0.096 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 2 known modulators (Phospholipase A2, membrane associated) |
| gnomAD constraint | pLI=0.076, LOEUF=1.06 — LoF-tolerant |
| GWAS Catalog | 60 unique SNPs / 116 rows |
| ClinVar | 55 records; 3 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 400 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'PLA2G2A' and resolved to 'Phospholipase A2, membrane associated' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 55 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 17 of 17 traits by best p-value, aggregated from 36 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P14555 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000188257/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3474/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PLA2G2A — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PLA2G2A — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PLA2G2A%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PLA2G2A — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:24:23  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
