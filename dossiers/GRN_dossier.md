# Protein Dossier — GRN (Progranulin)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Serum cystatin C (eGFRcys) | 0.0217 | 0.00721 | 0.00268 | Inverse variance weighted | 2 | cis | NA |
| Serum cystatin C (eGFRcys) | 0.0217 | 0.00721 | 0.00268 | Inverse variance weighted | 2 | trans | NA |
| Parkinson's disease | -0.697 | 0.252 | 0.00571 | Wald ratio | 1 | trans | NA |
| Age at menarche | -0.058 | 0.0214 | 0.0066 | Inverse variance weighted | 2 | cis | NA |
| Age at menarche | -0.058 | 0.0214 | 0.0066 | Inverse variance weighted | 2 | trans | NA |
| Lumbar spine bone mineral density | -0.129 | 0.0517 | 0.0129 | Wald ratio | 1 | trans | NA |
| Schizophrenia | 0.0865 | 0.0356 | 0.015 | Inverse variance weighted | 2 | cis | NA |
| Schizophrenia | 0.0865 | 0.0356 | 0.015 | Inverse variance weighted | 2 | trans | NA |
| Alzheimer's disease | -0.145 | 0.06 | 0.0158 | Inverse variance weighted | 2 | cis | NA |
| Alzheimer's disease | -0.145 | 0.06 | 0.0158 | Inverse variance weighted | 2 | trans | NA |
| Birth length | 0.0753 | 0.032 | 0.0185 | Inverse variance weighted | 2 | cis | NA |
| Birth length | 0.0753 | 0.032 | 0.0185 | Inverse variance weighted | 2 | trans | NA |
| _...and 194 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4992_49_1` | GRN | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_32 association rows across 25 traits (28 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating GRN levels | 8e-463 | rs5848 | 1 | GCST90859928 | no MR -> candidate analysis |
| Circulating CEACAM8 levels | 6e-162 | rs114641762 | 1 | GCST90859796 | no MR -> candidate analysis |
| CEACAM8 protein levels | 5e-125 | rs114641762 | 1 | GCST90468698 | no MR -> candidate analysis |
| Granulins levels | 7e-60 | rs5848 | 4 | GCST90247801 | no MR -> candidate analysis |
| Complement C1q tumor necrosis factor-related protein 1 level | 3e-59 | rs5848 | 1 | GCST90246766 | no MR -> candidate analysis |
| SEMA3G protein levels | 2e-46 | rs5848 | 1 | GCST90470571 | no MR -> candidate analysis |
| Cerebrospinal fluid protein GRN levels | 3e-44 | rs5848 | 1 | GCST90944774 | no MR -> candidate analysis |
| LRRC37A2 protein levels | 5e-29 | rs9895894 | 1 | GCST90469802 | no MR -> candidate analysis |
| Cerebrospinal fluid protein SEMA3G levels | 2e-27 | rs5848 | 1 | GCST90944562 | no MR -> candidate analysis |
| Eosinophil side fluorescence | 1e-23 | rs114641762 | 1 | GCST90281231 | no MR -> candidate analysis |
| Granulins levels (GRN.4992.49.1) | 8e-23 | rs5848 | 1 | GCST90241317 | no MR -> candidate analysis |
| Eosinophil side scatter | 1e-22 | rs114641762 | 1 | GCST90281230 | no MR -> candidate analysis |
| _...and 13 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1815 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| neuronal ceroid lipofuscinosis 11 | 0.915 | — | established (curated) | no MR -> candidate analysis |
| GRN-related frontotemporal lobar degeneration with Tdp43 inclusions | 0.848 | — | established (curated) | no MR -> candidate analysis |
| CLN11 disease | 0.608 | — | established (curated) | no MR -> candidate analysis |
| frontotemporal dementia | 0.887 | — | established (curated) | no MR -> candidate analysis |
| Alzheimer disease | 0.713 | — | established (curated) | no MR -> candidate analysis |
| dementia | 0.675 | 0.563 | multi-layer: burden+GWAS (allelic-series candidate) | no MR -> candidate analysis |
| hereditary disease | 0.801 | — | established (curated) | no MR -> candidate analysis |
| amyotrophic lateral sclerosis | 0.608 | — | established (curated) | MR: beta=-0.129, p=0.118 (cis) |
| primary progressive aphasia | 0.596 | — | established (curated) | no MR -> candidate analysis |
| frontotemporal dementia and/or amyotrophic lateral sclerosis | 0.195 | — | established (curated) | no MR -> candidate analysis |
| frontotemporal dementia with motor neuron disease | 0.608 | — | established (curated) | no MR -> candidate analysis |
| neurodegenerative disease | 0.485 | — | common-variant locus | no MR -> candidate analysis |
| Parkinson disease | 0.547 | — | established (curated) | no MR -> candidate analysis |
| Cognitive impairment | 0.559 | — | established (curated) | no MR -> candidate analysis |
| mental disorder | 0.558 | 0.558 | exploratory rare-variant signal | no MR -> candidate analysis |

> Of the 15 rows above, **14 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 1 exploratory rare-variant signal(s), 1 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Sortilin/Progranulin) |
| gnomAD constraint | pLI=0.015, LOEUF=0.61 — LoF-tolerant |
| GWAS Catalog | 66 unique SNPs / 132 rows |
| ClinVar | 844 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1815 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'GRN' and resolved to 'Sortilin/Progranulin' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 844 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 25 traits by best p-value, aggregated from 32 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P28799 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000030582/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4680051/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/GRN — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/GRN — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=GRN%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/GRN — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:54:33  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
