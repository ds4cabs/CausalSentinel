# Protein Dossier — LYZ (Lysozyme C)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Body mass index (BMI) | 0.0218 | 0.00509 | 1.83e-05 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | 0.0331 | 0.00839 | 7.92e-05 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: high cholesterol | 0.044 | 0.0132 | 8.40e-04 | Wald ratio | 1 | cis | NA |
| Bulimia nervosa | -0.0422 | 0.0148 | 0.00427 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | -0.0117 | 0.00418 | 0.00527 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: osteoarthritis | 0.045 | 0.0163 | 0.00568 | Wald ratio | 1 | cis | NA |
| Sodium in urine | 0.0137 | 0.00501 | 0.00635 | Wald ratio | 1 | cis | NA |
| Height | -0.0169 | 0.00634 | 0.00766 | Wald ratio | 1 | cis | NA |
| Squamous cell lung cancer | 0.144 | 0.0543 | 0.00804 | Wald ratio | 1 | cis | NA |
| Lung cancer | 0.0854 | 0.0362 | 0.0183 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R07 Pain in throat and chest | 0.0508 | 0.0216 | 0.0186 | Wald ratio | 1 | cis | NA |
| Paget's disease | -0.274 | 0.127 | 0.0309 | Wald ratio | 1 | cis | NA |
| _...and 102 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4920_10_1` | Lysozyme | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_157 association rows across 107 traits (150 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Lysozyme C levels | 4e-543 | rs4761234 | 9 | GCST90248359 | no MR -> candidate analysis |
| Serum levels of protein LYZ | 8e-200 | rs4761234 | 1 | GCST90088815 | no MR -> candidate analysis |
| Monocyte count | 2e-187 | rs1800973 | 6 | GCST90002340 | no MR -> candidate analysis |
| Monocyte count (UKB data field 30130) | 8e-173 | rs1800973 | 2 | GCST90468090 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 7e-164 | rs1800973 | 2 | GCST90838669 | no MR -> candidate analysis |
| Monocyte percentage (UKB data field 30190) | 2e-154 | rs1800973 | 1 | GCST90468091 | no MR -> candidate analysis |
| Monocyte side fluorescence | 1e-147 | rs1800973 | 1 | GCST90281241 | no MR -> candidate analysis |
| SSC-A on monocyte | 2e-145 | rs1800973 | 2 | GCST90002073 | no MR -> candidate analysis |
| Monocyte percentage of white cells | 7e-139 | rs1800973 | 2 | GCST90002394 | no MR -> candidate analysis |
| SSC-A on CD14+ monocyte | 3e-114 | rs1800973 | 2 | GCST90002074 | no MR -> candidate analysis |
| Blood protein levels | 3e-104 | rs4761234 | 1 | GCST006585 | no MR -> candidate analysis |
| Lysozyme C levels (LYZ.4920.10.1) | 4e-89 | rs4761234 | 2 | GCST90241848 | no MR -> candidate analysis |
| _...and 95 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1282 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| familial visceral amyloidosis | 0.756 | — | established (curated) | no MR -> candidate analysis |
| Familial renal amyloidosis | 0.756 | — | established (curated) | no MR -> candidate analysis |
| amyloidosis, hereditary systemic 5 | 0.753 | — | established (curated) | no MR -> candidate analysis |
| Oral ulcer | 0.795 | — | common-variant locus | no MR -> candidate analysis |
| hypertensive disorder | 0.749 | — | common-variant locus | no MR -> candidate analysis |
| ALys amyloidosis | 0.608 | — | established (curated) | no MR -> candidate analysis |
| Familial renal amyloidosis due to lysozyme variant | 0.608 | — | established (curated) | no MR -> candidate analysis |
| alcohol drinking | 0.39 | — | common-variant locus | no MR -> candidate analysis |
| seasonal allergic rhinitis | 0.39 | — | common-variant locus | no MR -> candidate analysis |
| drug allergy | 0.378 | — | common-variant locus | no MR -> candidate analysis |
| hereditary disease | 0.3 | — | established (curated) | no MR -> candidate analysis |
| Pain | 0.232 | — | common-variant locus | MR: beta=0.0508, p=0.0186 (cis) |
| cervical carcinoma | 0.115 | — | common-variant locus | no MR -> candidate analysis |

> Of the 13 rows above, **12 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Lysozyme C) |
| gnomAD constraint | pLI=1.5e-07, LOEUF=1.69 — LoF-tolerant |
| GWAS Catalog | 94 unique SNPs / 188 rows |
| ClinVar | 118 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1282 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'LYZ' and resolved to 'Lysozyme C' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 118 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 107 traits by best p-value, aggregated from 157 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P61626 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000090382/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2297/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/LYZ — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/LYZ — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=LYZ%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/LYZ — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:40:31  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
