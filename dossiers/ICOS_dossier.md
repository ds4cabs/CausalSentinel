# Protein Dossier — ICOS (Inducible T-cell costimulator)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Systolic blood pressure  automated reading | 0.058 | 0.012 | 1.46e-06 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: hypertension | 0.0837 | 0.0184 | 5.69e-06 | Wald ratio | 1 | trans | NA |
| Weight | 0.0387 | 0.0104 | 1.95e-04 | Wald ratio | 1 | trans | NA |
| Diastolic blood pressure  automated reading | 0.0446 | 0.012 | 2.12e-04 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: I48 Atrial fibrillation and flutter | 0.292 | 0.0837 | 4.79e-04 | Wald ratio | 1 | trans | NA |
| Sleep duration | 0.0312 | 0.00918 | 6.66e-04 | Wald ratio | 1 | trans | NA |
| Schizophrenia | -0.166 | 0.0506 | 0.00107 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code self-reported: pulmonary embolism (with or without) dvt | 0.297 | 0.098 | 0.00247 | Wald ratio | 1 | trans | NA |
| Eczema | -0.25 | 0.0862 | 0.00373 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: K80 Cholelithiasis | 0.187 | 0.0683 | 0.0062 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: high cholesterol | 0.0734 | 0.0296 | 0.013 | Wald ratio | 1 | trans | NA |
| Forced expiratory volume in 1-second (FEV1) | 0.0246 | 0.0102 | 0.0156 | Wald ratio | 1 | trans | NA |
| _...and 107 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_153 association rows across 78 traits (129 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Autoimmune hypothyroidism | 3e-251 | rs11571297 | 1 | GCST90837324 | no MR -> candidate analysis |
| Hypothyroidism | 5e-226 | rs11571297 | 12 | GCST90627750 | MR: beta=0.0405, p=0.421 (trans) |
| Hypothyroidism NOS (PheCode 244.4) | 3e-107 | rs3087243 | 2 | GCST90475653 | no MR -> candidate analysis |
| Hypothyroidism (PheCode 244) | 8e-107 | rs3087243 | 2 | GCST90475647 | no MR -> candidate analysis |
| Hypothyroidism or rheumatoid arthritis (pleiotropy) | 2e-90 | rs17268364 | 1 | GCST90428109 | no MR -> candidate analysis |
| Medication use (thyroid preparations) | 4e-88 | rs3087243 | 2 | GCST90018990 | no MR -> candidate analysis |
| Takes medication for Thyroid problems? | 2e-64 | rs3087243 | 2 | GCST90475277 | no MR -> candidate analysis |
| Thyroid problems | 1e-56 | rs3087243 | 2 | GCST90475276 | no MR -> candidate analysis |
| Basal cell carcinoma (MTAG) | 2e-49 | rs1427676 | 1 | GCST90137411 | no MR -> candidate analysis |
| Autoimmune traits | 7e-49 | rs3087243 | 1 | GCST007071 | no MR -> candidate analysis |
| Lymphocytic thyroiditis | 5e-43 | rs11571302 | 2 | GCST90627755 | no MR -> candidate analysis |
| Graves' disease | 1e-37 | rs3087243 | 2 | GCST90627744 | no MR -> candidate analysis |
| _...and 66 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 829 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| immunodeficiency, common variable, 1 | 0.832 | — | established (curated) | no MR -> candidate analysis |
| hypothyroidism | 0.794 | — | common-variant locus | MR: beta=0.0405, p=0.421 (trans) |
| basal cell carcinoma | 0.672 | — | common-variant locus | MR: beta=0.0784, p=0.496 (trans) |
| myxedema | 0.661 | — | common-variant locus | no MR -> candidate analysis |
| skin neoplasm | 0.641 | — | common-variant locus | no MR -> candidate analysis |
| rheumatoid arthritis | 0.537 | — | common-variant locus | MR: beta=-0.0701, p=0.323 (trans) |
| immunodeficiency disease | 0.547 | — | established (curated) | no MR -> candidate analysis |
| asthma | 0.527 | — | common-variant locus | no MR -> candidate analysis |
| skin cancer | 0.504 | — | common-variant locus | no MR -> candidate analysis |
| thyroid cancer | 0.463 | — | common-variant locus | no MR -> candidate analysis |
| Graves disease | 0.386 | — | common-variant locus | no MR -> candidate analysis |
| Hashimoto thyroiditis | 0.38 | — | common-variant locus | no MR -> candidate analysis |
| cutaneous melanoma | 0.371 | — | common-variant locus | no MR -> candidate analysis |
| thyroid gland disorder | 0.368 | — | common-variant locus | no MR -> candidate analysis |
| diabetes mellitus | 0.337 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **12 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 1 known modulators (ICOS ligand) |
| gnomAD constraint | pLI=0.0011, LOEUF=0.94 — LoF-tolerant |
| GWAS Catalog | 72 unique SNPs / 114 rows |
| ClinVar | 238 records; 3 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 829 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'ICOS' and resolved to 'ICOS ligand' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 238 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 78 traits by best p-value, aggregated from 153 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9Y6W8 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000163600/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3712949/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/ICOS — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/ICOS — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=ICOS%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/ICOS — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:04:55  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
