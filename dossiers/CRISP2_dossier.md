# Protein Dossier — CRISP2 (Cysteine-rich secretory protein 2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Underlying (primary) cause of death: ICD10: E85.4 Organ-limited amyloidosis | 1.34 | 0.272 | 9.33e-07 | Wald ratio | 1 | cis | NA |
| Diastolic blood pressure  automated reading | -0.0114 | 0.00433 | 0.00848 | Wald ratio | 1 | cis | NA |
| Squamous cell lung cancer | -0.114 | 0.0452 | 0.0113 | Wald ratio | 1 | cis | NA |
| Lung cancer | -0.0746 | 0.0301 | 0.0131 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code self-reported: pulmonary embolism (with or without) dvt | -0.118 | 0.0529 | 0.0257 | Wald ratio | 1 | cis | NA |
| Hip osteoarthritis | -0.102 | 0.0463 | 0.0271 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C50 Malignant neoplasm of breast | 0.0663 | 0.0309 | 0.032 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K29 Gastritis and duodenitis | 0.0552 | 0.0259 | 0.033 | Wald ratio | 1 | cis | NA |
| Alzheimer's disease | -0.0529 | 0.0272 | 0.0521 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Glaucoma | 0.0634 | 0.0331 | 0.0557 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Injury or trauma resulting in loss of vision | 0.0906 | 0.0505 | 0.0725 | Wald ratio | 1 | cis | NA |
| Anorexia nervosa | 0.0888 | 0.0497 | 0.0741 | Wald ratio | 1 | cis | NA |
| _...and 75 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_26 association rows across 18 traits (23 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating CRISP2 levels | 8e-1000 | rs113140471 | 3 | GCST90860530 | no MR -> candidate analysis |
| Cysteine-rich secretory protein 2 levels | 2e-246 | rs112840264 | 2 | GCST90247160 | no MR -> candidate analysis |
| CRISP3 protein levels | 2e-216 | rs765003308 | 5 | GCST90468866 | no MR -> candidate analysis |
| Cysteine-rich secretory protein 2 levels (CRISP2.9282.12.3) | 2e-82 | rs36069724 | 1 | GCST90240840 | no MR -> candidate analysis |
| Cerebrospinal fluid protein CRISP2 levels | 6e-44 | rs112840264 | 1 | GCST90943230 | no MR -> candidate analysis |
| Mean spheric corpuscular volume | 4e-28 | rs188522023 | 1 | GCST90002397 | no MR -> candidate analysis |
| Cysteine-rich secretory protein 2 level in Chronic kidney di | 3e-17 | rs360541 | 1 | GCST90239289 | no MR -> candidate analysis |
| CRISP2 protein levels | 3e-15 | rs143650014 | 1 | GCST90468865 | no MR -> candidate analysis |
| Mean corpuscular hemoglobin concentration | 1e-14 | rs188522023 | 2 | GCST90002391 | no MR -> candidate analysis |
| Reticulocyte fraction of red cells | 4e-13 | rs188522023 | 1 | GCST90002406 | no MR -> candidate analysis |
| Reticulocyte count | 5e-13 | rs188522023 | 1 | GCST90002405 | no MR -> candidate analysis |
| Mean reticulocyte volume | 4e-12 | rs188522023 | 1 | GCST90002396 | no MR -> candidate analysis |
| _...and 6 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 118 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Aganglionic megacolon | 0.195 | — | established (curated) | no MR -> candidate analysis |
| carotid artery disorder | 0.145 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=8.5e-10, LOEUF=1.25 — LoF-tolerant |
| GWAS Catalog | 50 unique SNPs / 96 rows |
| ClinVar | 54 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 118 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CRISP2'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 54 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 18 of 18 traits by best p-value, aggregated from 26 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P16562 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000124490/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CRISP2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CRISP2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CRISP2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CRISP2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:03:29  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
