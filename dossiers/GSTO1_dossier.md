# Protein Dossier — GSTO1 (Glutathione S-transferase omega-1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Happiness | 0.0124 | 0.00341 | 2.80e-04 | Wald ratio | 1 | cis | NA |
| Ischemic stroke | 0.0597 | 0.0184 | 0.0012 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | -0.00748 | 0.00238 | 0.0017 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R07 Pain in throat and chest | 0.037 | 0.0118 | 0.00175 | Wald ratio | 1 | cis | NA |
| Depressive symptoms | 0.0132 | 0.00439 | 0.0027 | Wald ratio | 1 | cis | NA |
| Schizophrenia | 0.0338 | 0.0121 | 0.00511 | Wald ratio | 1 | cis | NA |
| Mean platelet volume | 0.00439 | 0.00165 | 0.00766 | Wald ratio | 1 | cis | NA |
| Subjective well being | -0.00878 | 0.00329 | 0.00766 | Wald ratio | 1 | cis | NA |
| Lung adenocarcinoma | -0.0867 | 0.0335 | 0.00962 | Wald ratio | 1 | cis | NA |
| Bulimia nervosa | 0.022 | 0.00878 | 0.0124 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R10 Abdominal and pelvic pain | 0.0308 | 0.0129 | 0.0168 | Wald ratio | 1 | cis | NA |
| Age at menarche | -0.0154 | 0.00671 | 0.022 | Wald ratio | 1 | cis | NA |
| _...and 103 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_15 association rows across 14 traits (14 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Glutathione S-transferase omega-1 levels (GSTO1.12436.84.3) | 2e-437 | rs2282326 | 2 | GCST90241286 | no MR -> candidate analysis |
| Serum levels of protein GSTO1 | 4e-265 | rs2282326 | 1 | GCST90086982 | no MR -> candidate analysis |
| Blood protein levels | 3e-139 | rs1147611 | 1 | GCST006585 | no MR -> candidate analysis |
| Cerebrospinal fluid metabolite X-25855 levels | 9e-45 | rs34521730 | 1 | GCST90318336 | no MR -> candidate analysis |
| Type 2 diabetes | 1e-23 | rs2164624 | 1 | GCST90134620 | no MR -> candidate analysis |
| Glutathione S-transferase omega-1 level in Chronic kidney di | 4e-22 | rs634013 | 1 | GCST90233458 | no MR -> candidate analysis |
| Spermatogenesis-associated protein 24 protein levels (SomaSc | 9e-19 | rs2282326 | 1 | GCST90438390 | no MR -> candidate analysis |
| Brain metabolite X-25855 levels | 6e-17 | rs17885241 | 1 | GCST90319110 | no MR -> candidate analysis |
| GSTO1 protein levels | 2e-16 | rs11191968 | 1 | GCST90453259 | no MR -> candidate analysis |
| Protein quantitative trait loci (liver) | 4e-13 | rs71473516 | 1 | GCST011427 | no MR -> candidate analysis |
| Uterine fibroids | 4e-9 | rs145973216 | 1 | GCST90461959 | MR: beta=-0.0349, p=0.13 (cis) |
| Diastolic blood pressure (MTAG) | 3e-8 | rs628480 | 1 | GCST90449057 | no MR -> candidate analysis |
| _...and 2 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 227 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| type 2 diabetes mellitus | 0.42 | — | common-variant locus | no MR -> candidate analysis |
| female genital tract polyp | 0.066 | — | common-variant locus | no MR -> candidate analysis |
| thyroid gland carcinoma | 0.055 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Glutathione S-transferase omega-1) |
| gnomAD constraint | pLI=7.9e-11, LOEUF=1.56 — LoF-tolerant |
| GWAS Catalog | 37 unique SNPs / 73 rows |
| ClinVar | 61 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 227 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'GSTO1' and resolved to 'Glutathione S-transferase omega-1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 61 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 14 of 14 traits by best p-value, aggregated from 15 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P78417 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000148834/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3174/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/GSTO1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/GSTO1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=GSTO1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/GSTO1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:56:00  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
