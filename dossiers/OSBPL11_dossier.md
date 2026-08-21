# Protein Dossier — OSBPL11 (Oxysterol-binding protein-related protein 11)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: muscle or soft tissue injuries | 0.348 | 0.119 | 0.00356 | Wald ratio | 1 | trans | NA |
| Sodium in urine | 0.0333 | 0.0138 | 0.0161 | Wald ratio | 1 | trans | NA |
| Systolic blood pressure  automated reading | 0.033 | 0.0144 | 0.0222 | Wald ratio | 1 | trans | NA |
| Clear cell ovarian cancer | 0.5 | 0.231 | 0.0302 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: M23 Internal derangement of knee | -0.261 | 0.125 | 0.037 | Wald ratio | 1 | trans | NA |
| Cigarettes smoked per day | 1.93 | 0.953 | 0.0432 | Wald ratio | 1 | trans | NA |
| Autism | 0.393 | 0.21 | 0.0619 | Wald ratio | 1 | trans | NA |
| Endometrioid ovarian cancer | 0.314 | 0.171 | 0.0654 | Wald ratio | 1 | trans | NA |
| Birth weight | -0.0465 | 0.0255 | 0.0686 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: M16 Coxarthrosis [arthrosis of hip] | -0.288 | 0.161 | 0.0739 | Wald ratio | 1 | trans | NA |
| Hearing difficulty or problems: Yes | -0.0391 | 0.0252 | 0.121 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: N81 Female genital prolapse | -0.231 | 0.152 | 0.129 | Wald ratio | 1 | trans | NA |
| _...and 43 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_14 association rows across 9 traits (6 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Severe COVID-19 infection | 1e-16 | rs2979382 | 2 | GCST90255357 | no MR -> candidate analysis |
| Neurofibrillary tangles (SNP x SNP interaction) | 3e-13 | rs4899207 x rs2979307 | 1 | GCST010343 | no MR -> candidate analysis |
| Height | 2e-12 | rs529963700 | 1 | GCST90018959 | no MR -> candidate analysis |
| Core binding factor acute myeloid leukemia | 2e-10 | rs11717181; rs6799729; rs2979312; rs10755079; rs6784346; rs17273670; rs13058844; rs9968159; rs2001665; rs2979322; rs2976720; rs2979342; rs2971306 | 2 | GCST008413 | no MR -> candidate analysis |
| Body mass index | 2e-8 | rs143348557 | 2 | GCST90662912 | MR: beta=0.0205, p=0.144 (trans) |
| Gut microbial network clusters (Tan (at 3 months) x Summer B | 6e-8 | rs11717250 | 1 | GCST90569246 | no MR -> candidate analysis |
| Astrocytoma (high-grade) | 4e-7 | rs192322845 | 2 | GCST90296468 | no MR -> candidate analysis |
| Glioma (high-grade) | 6e-7 | rs184687927 | 2 | GCST90296475 | no MR -> candidate analysis |
| Hair curvature (quantitative) | 3e-6 | rs62270208 | 1 | GCST011641 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 72 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| severe acute respiratory syndrome | 0.481 | — | common-variant locus | no MR -> candidate analysis |
| COVID-19 | 0.481 | — | common-variant locus | no MR -> candidate analysis |
| ovarian neoplasm | 0.284 | — | common-variant locus | no MR -> candidate analysis |
| circadian rhythm sleep disorder | 0.279 | — | common-variant locus | no MR -> candidate analysis |
| seborrheic keratosis | 0.091 | — | common-variant locus | no MR -> candidate analysis |
| bone remodeling disease | 0.056 | — | common-variant locus | no MR -> candidate analysis |

> Of the 6 rows above, **6 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.72, LOEUF=0.523 — LoF-tolerant |
| GWAS Catalog | 33 unique SNPs / 66 rows |
| ClinVar | 128 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 72 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'OSBPL11'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 128 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 9 of 9 traits by best p-value, aggregated from 14 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9BXB4 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000144909/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/OSBPL11 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/OSBPL11 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=OSBPL11%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/OSBPL11 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:09:48  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
