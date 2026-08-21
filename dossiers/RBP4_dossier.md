# Protein Dossier — RBP4 (Retinol-binding protein 4)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: vitiligo | 1.24 | 0.346 | 3.17e-04 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I80 Phlebitis and thrombophlebitis | 0.52 | 0.155 | 7.83e-04 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K40 Inguinal hernia | 0.237 | 0.0841 | 0.00475 | Wald ratio | 1 | cis | NA |
| Lung cancer | 0.34 | 0.126 | 0.00705 | Wald ratio | 1 | cis | NA |
| Schizophrenia | 0.201 | 0.0816 | 0.014 | Wald ratio | 1 | cis | NA |
| Birth weight | 0.0646 | 0.0265 | 0.0149 | Wald ratio | 1 | cis | NA |
| High grade serous ovarian cancer | -0.279 | 0.118 | 0.0178 | Wald ratio | 1 | cis | NA |
| Ovarian cancer | -0.23 | 0.0993 | 0.0203 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | 0.148 | 0.0666 | 0.0258 | Wald ratio | 1 | cis | NA |
| Diastolic blood pressure  automated reading | -0.0389 | 0.0177 | 0.0279 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | 0.0295 | 0.0142 | 0.0373 | Wald ratio | 1 | cis | NA |
| Amygdala volume | -36.9 | 17.9 | 0.0387 | Wald ratio | 1 | cis | NA |
| _...and 70 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3641_49_4` | RBP | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_9 association rows across 6 traits (7 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Retinol (Vitamin A) levels | 6e-30 | rs10882283 | 3 | GCST90245401 | no MR -> candidate analysis |
| Retinol-binding protein 4 levels | 8e-24 | rs36014035 | 1 | GCST90249256 | no MR -> candidate analysis |
| Triglyceride levels (UKB data field 30870) | 4e-21 | rs76582050 | 1 | GCST90468106 | no MR -> candidate analysis |
| Blood protein levels | 7e-9 | rs36014035 | 2 | GCST006585 | no MR -> candidate analysis |
| Optic disc area | 4e-8 | rs10882283 | 1 | GCST009411 | no MR -> candidate analysis |
| Colorectal cancer x estrogen-progesterone hormone therapy in | 4e-6 | rs7091052 | 1 | GCST90243999 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1215 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| progressive retinal dystrophy due to retinol transport defect | 0.766 | — | established (curated) | no MR -> candidate analysis |
| microphthalmia, isolated, with coloboma 10 | 0.758 | — | established (curated) | no MR -> candidate analysis |
| microphthalmia, isolated, with coloboma | 0.608 | — | established (curated) | no MR -> candidate analysis |
| microphthalmia | 0.657 | — | established (curated) | no MR -> candidate analysis |
| Retinal dystrophy | 0.685 | — | established (curated) | no MR -> candidate analysis |
| coloboma | 0.657 | — | established (curated) | no MR -> candidate analysis |
| Bilateral microphthalmos | 0.669 | — | established (curated) | no MR -> candidate analysis |
| open-angle glaucoma | 0.58 | — | common-variant locus | no MR -> candidate analysis |
| hereditary disease | 0.557 | — | established (curated) | no MR -> candidate analysis |
| diabetic ketoacidosis | 0.465 | — | common-variant locus | no MR -> candidate analysis |
| Anophthalmia | 0.438 | — | established (curated) | no MR -> candidate analysis |
| anterior segment dysgenesis | 0.438 | — | established (curated) | no MR -> candidate analysis |
| Unilateral microphthalmos | 0.438 | — | established (curated) | no MR -> candidate analysis |
| Ocular anterior segment dysgenesis | 0.438 | — | established (curated) | no MR -> candidate analysis |
| Abnormality of the eye | 0.426 | — | established (curated) | no MR -> candidate analysis |

> Of the 15 rows above, **15 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Retinol-binding protein 4) |
| gnomAD constraint | pLI=0.8, LOEUF=0.599 — LoF-tolerant |
| GWAS Catalog | 56 unique SNPs / 112 rows |
| ClinVar | 228 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1215 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'RBP4' and resolved to 'Retinol-binding protein 4' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 228 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 6 of 6 traits by best p-value, aggregated from 9 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P02753 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000138207/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3100/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/RBP4 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/RBP4 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=RBP4%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/RBP4 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:45:59  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
