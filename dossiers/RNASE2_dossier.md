# Protein Dossier — RNASE2 (Non-secretory ribonuclease)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Underlying (primary) cause of death: ICD10: E85.4 Organ-limited amyloidosis | 1.82 | 0.463 | 8.40e-05 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: D25 Leiomyoma of uterus | -0.273 | 0.12 | 0.0231 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M16 Coxarthrosis [arthrosis of hip] | -0.241 | 0.11 | 0.0277 | Wald ratio | 1 | cis | NA |
| Fracture resulting from simple fall | -0.0619 | 0.0286 | 0.0304 | Wald ratio | 1 | cis | NA |
| Alzheimer's disease | 0.139 | 0.0664 | 0.0367 | Wald ratio | 1 | cis | NA |
| Hippocampus volume | -40.9 | 19.6 | 0.0371 | Wald ratio | 1 | cis | NA |
| Schizophrenia | 0.0879 | 0.0448 | 0.0497 | Wald ratio | 1 | cis | NA |
| Femoral neck bone mineral density | 0.061 | 0.0318 | 0.0554 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R11 Nausea and vomiting | 0.245 | 0.13 | 0.0587 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hayfever or allergic rhinitis | 0.071 | 0.0391 | 0.0697 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C61 Malignant neoplasm of prostate | -0.308 | 0.177 | 0.0813 | Wald ratio | 1 | cis | NA |
| Sleep duration | 0.0136 | 0.00796 | 0.0872 | Wald ratio | 1 | cis | NA |
| _...and 56 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_28 association rows across 20 traits (28 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| MNDA/RNASE3 protein level ratio | 5e-386 | rs7141958 | 1 | GCST90315474 | no MR -> candidate analysis |
| MPO/RNASE3 protein level ratio | 2e-382 | rs7141958 | 1 | GCST90315493 | no MR -> candidate analysis |
| CLC/RNASE3 protein level ratio | 4e-341 | rs7141958 | 1 | GCST90314077 | no MR -> candidate analysis |
| CEACAM8/RNASE3 protein level ratio | 1e-335 | rs7141958 | 1 | GCST90314004 | no MR -> candidate analysis |
| Eosinophil cationic protein (analyte X5741.55) levels | 4e-154 | rs871408 | 1 | GCST90426491 | no MR -> candidate analysis |
| Monocyte side fluorescence | 5e-153 | rs2771358 | 3 | GCST90281241 | no MR -> candidate analysis |
| Cerebrospinal fluid protein RNASE3 levels | 1e-109 | rs871408 | 1 | GCST90944542 | no MR -> candidate analysis |
| Circulating RNASE3 levels | 8e-80 | rs117643813 | 2 | GCST90860416 | no MR -> candidate analysis |
| RNASE3 protein levels | 7e-65 | rs79867878 | 5 | GCST90470477 | no MR -> candidate analysis |
| Neutrophil side fluorescence | 5e-42 | rs2771312 | 1 | GCST90281223 | no MR -> candidate analysis |
| Monocyte side fluorescence distribution width | 6e-31 | rs2771359 | 1 | GCST90281244 | no MR -> candidate analysis |
| Serum levels of protein RNASE3 | 2e-22 | rs55633173 | 2 | GCST90089186 | no MR -> candidate analysis |
| _...and 8 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 343 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| alcohol drinking | 0.133 | — | common-variant locus | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Non-secretory ribonuclease) |
| gnomAD constraint | not available |
| GWAS Catalog | 65 unique SNPs / 130 rows |
| ClinVar | 54 records; 8 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 343 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'RNASE2' and resolved to 'Non-secretory ribonuclease' — confirm this is the intended target.
- **`gnomad`** — No gnomAD constraint data.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 54 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 20 traits by best p-value, aggregated from 28 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P10153 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000169385/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL5120/ — _ChEMBL_37 (released 2026-05-01)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/RNASE2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=RNASE2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/RNASE2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:50:19  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
