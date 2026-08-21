# Protein Dossier — C1QC (Complement C1q subcomponent subunit C)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Platelet count | 5.74 | 2.22 | 0.00979 | Wald ratio | 1 | trans | NA |
| Forced vital capacity (FVC) | 0.0113 | 0.00445 | 0.0107 | Inverse variance weighted | 2 | cis | NA |
| Forced vital capacity (FVC) | 0.0113 | 0.00445 | 0.0107 | Inverse variance weighted | 2 | trans | NA |
| Red blood cell count | 0.0323 | 0.0133 | 0.0152 | Wald ratio | 1 | trans | NA |
| Childhood intelligence | -0.163 | 0.0702 | 0.0201 | Wald ratio | 1 | trans | NA |
| Cough on most days | -0.00862 | 0.00371 | 0.0202 | Inverse variance weighted | 2 | cis | NA |
| Cough on most days | -0.00862 | 0.00371 | 0.0202 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: hiatus hernia | -0.0018 | 0.000809 | 0.0261 | Inverse variance weighted | 2 | cis | NA |
| Non-cancer illness code  self-reported: hiatus hernia | -0.0018 | 0.000809 | 0.0261 | Inverse variance weighted | 2 | trans | NA |
| Hirschsprung's disease | -0.45 | 0.205 | 0.0277 | Wald ratio | 1 | cis | NA |
| Small vessel disease | -0.408 | 0.192 | 0.0337 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: kidney stone or ureter stone or bladder stone | -0.000972 | 0.000477 | 0.0416 | Inverse variance weighted | 2 | cis | NA |
| _...and 141 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_8 association rows across 5 traits (7 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Complement C1q subcomponent subunit C levels | 3e-81 | rs12073436 | 2 | GCST90246762 | no MR -> candidate analysis |
| Serum levels of protein C1QC | 9e-52 | rs12073436 | 3 | GCST90087782 | no MR -> candidate analysis |
| Complement C1q subcomponent subunit C levels (C1QC.14100.63. | 3e-29 | rs12073436 | 1 | GCST90240764 | no MR -> candidate analysis |
| Cerebrospinal fluid protein C1QA levels | 2e-24 | rs292002 | 1 | GCST90943099 | no MR -> candidate analysis |
| S-6-hydroxywarfarin levels | 4e-6 | rs181867891 | 1 | GCST90129565 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 364 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| immunodeficiency due to a classical component pathway complement deficiency | 0.608 | — | established (curated) | no MR -> candidate analysis |
| C1Q deficiency | 0.792 | — | established (curated) | no MR -> candidate analysis |
| C1Q deficiency 3 | 0.733 | — | established (curated) | no MR -> candidate analysis |
| placenta praevia | 0.52 | — | common-variant locus | no MR -> candidate analysis |
| hereditary disease | 0.313 | — | established (curated) | no MR -> candidate analysis |
| smoking initiation | 0.305 | — | common-variant locus | no MR -> candidate analysis |
| benign urinary system neoplasm | 0.122 | — | common-variant locus | no MR -> candidate analysis |

> Of the 7 rows above, **7 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.058, LOEUF=1.55 — LoF-tolerant |
| GWAS Catalog | 51 unique SNPs / 101 rows |
| ClinVar | 191 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 364 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'C1QC'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 191 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 5 of 5 traits by best p-value, aggregated from 8 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P02747 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000159189/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/C1QC — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/C1QC — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=C1QC%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/C1QC — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:20:09  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
