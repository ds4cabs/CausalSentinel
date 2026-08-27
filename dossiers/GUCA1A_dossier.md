# Protein Dossier — GUCA1A (Guanylyl cyclase-activating protein 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Systolic blood pressure  automated reading | 0.0206 | 0.00652 | 0.00161 | Wald ratio | 1 | trans | NA |
| Eye problems or disorders: Glaucoma | 0.145 | 0.046 | 0.00168 | Wald ratio | 1 | trans | NA |
| Fractured bone site(s): Wrist | 0.112 | 0.0407 | 0.00605 | Wald ratio | 1 | trans | NA |
| Cough on most days | 0.0811 | 0.0302 | 0.00717 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: R11 Nausea and vomiting | -0.389 | 0.154 | 0.0116 | Wald ratio | 1 | trans | NA |
| Eye problems or disorders: Diabetes related eye disease | -0.247 | 0.106 | 0.0193 | Wald ratio | 1 | trans | NA |
| ER-negative Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0764 | 0.0328 | 0.0198 | Wald ratio | 1 | trans | NA |
| Small vessel disease | -0.222 | 0.0965 | 0.0215 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: G47 Sleep disorders | 0.151 | 0.0719 | 0.0362 | Wald ratio | 1 | trans | NA |
| Forearm bone mineral density | 0.0858 | 0.0413 | 0.0379 | Wald ratio | 1 | trans | NA |
| Fractured bone site(s): Ankle | -0.128 | 0.0621 | 0.0395 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: M54 Dorsalgia | 0.0923 | 0.0452 | 0.0411 | Wald ratio | 1 | trans | NA |
| _...and 80 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_3 association rows across 2 traits (2 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Femur bone mineral density x serum urate levels interaction | 2e-13 | rs11752636 | 2 | GCST012490 | no MR -> candidate analysis |
| Spatial processing | 5e-6 | rs13203733 | 1 | GCST009306 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 436 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| cone dystrophy 3 | 0.958 | — | established (curated) | no MR -> candidate analysis |
| Cone rod dystrophy | 0.853 | — | established (curated) | no MR -> candidate analysis |
| Progressive cone dystrophy | 0.847 | — | established (curated) | no MR -> candidate analysis |
| cone-rod dystrophy | 0.72 | — | established (curated) | no MR -> candidate analysis |
| cone-rod dystrophy 14 | 0.745 | — | established (curated) | no MR -> candidate analysis |
| Retinal dystrophy | 0.888 | — | established (curated) | no MR -> candidate analysis |
| Macular dystrophy | 0.654 | — | established (curated) | no MR -> candidate analysis |
| Rod-cone dystrophy | 0.486 | — | established (curated) | no MR -> candidate analysis |
| central areolar choroidal dystrophy | 0.608 | — | established (curated) | no MR -> candidate analysis |
| retinitis pigmentosa | 0.544 | — | established (curated) | no MR -> candidate analysis |
| Usher syndrome | 0.547 | — | established (curated) | no MR -> candidate analysis |
| retinal disorder | 0.559 | — | established (curated) | no MR -> candidate analysis |
| isolated macular dystrophy | 0.559 | — | established (curated) | no MR -> candidate analysis |
| hereditary disease | 0.307 | — | established (curated) | no MR -> candidate analysis |

> Of the 14 rows above, **14 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.00016, LOEUF=1.18 — LoF-tolerant |
| GWAS Catalog | 20 unique SNPs / 40 rows |
| ClinVar | 297 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 436 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'GUCA1A'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 297 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 2 of 2 traits by best p-value, aggregated from 3 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P43080 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000048545/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/GUCA1A — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/GUCA1A — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=GUCA1A%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/GUCA1A — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:56:31  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
