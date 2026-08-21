# Protein Dossier — LGALS9 (Galectin-9)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Crohn's disease | -0.34 | 0.0685 | 7.01e-07 | Wald ratio | 1 | cis | NA |
| Inflammatory bowel disease | -0.267 | 0.0569 | 2.78e-06 | Wald ratio | 1 | cis | NA |
| Ulcerative colitis | -0.202 | 0.0717 | 0.00474 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M16 Coxarthrosis [arthrosis of hip] | 0.253 | 0.09 | 0.00502 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: joint disorder | 0.381 | 0.141 | 0.00676 | Wald ratio | 1 | cis | NA |
| Rheumatoid arthritis | 0.193 | 0.0725 | 0.00772 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | 0.0452 | 0.0178 | 0.0113 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M54 Dorsalgia | 0.209 | 0.0877 | 0.0174 | Wald ratio | 1 | cis | NA |
| Invasive mucinous ovarian cancer | 0.539 | 0.233 | 0.0207 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Ankle | 0.197 | 0.0978 | 0.0445 | Wald ratio | 1 | cis | NA |
| Lumbar spine bone mineral density | 0.1 | 0.0505 | 0.0465 | Wald ratio | 1 | cis | NA |
| Type 2 diabetes | -0.146 | 0.0732 | 0.0468 | Wald ratio | 1 | cis | NA |
| _...and 103 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_15 association rows across 10 traits (10 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating LGALS9 levels (id: OID00406_OID20781) | 2e-1395 | rs74321993 | 2 | GCST90859768 | no MR -> candidate analysis |
| Circulating LGALS9 levels (id: OID00779_OID20781) | 1e-1161 | rs74321993 | 1 | GCST90860112 | no MR -> candidate analysis |
| Galectin-9 levels | 1e-75 | rs4794974 | 4 | GCST90179305 | no MR -> candidate analysis |
| Cerebrospinal fluid protein LGALS9 levels | 3e-69 | rs4239242 | 1 | GCST90944399 | no MR -> candidate analysis |
| Serum levels of protein LGALS9 | 5e-20 | rs4239242 | 1 | GCST90090548 | no MR -> candidate analysis |
| Blood protein levels | 8e-12 | rs62055780 | 1 | GCST006585 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 2e-11 | rs3751091 | 1 | GCST90838669 | no MR -> candidate analysis |
| Oligodendroglioma | 2e-6 | rs146432592 | 2 | GCST90296482 | no MR -> candidate analysis |
| Stuttering | 3e-6 | rs113887266 | 1 | GCST90707226 | no MR -> candidate analysis |
| Squamous cell lung carcinoma | 1e-5 | rs142539114 | 1 | GCST90652535 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 708 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Hemoptysis | 0.45 | — | common-variant locus | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Galectin-9) |
| gnomAD constraint | pLI=4.1e-07, LOEUF=1.01 — LoF-tolerant |
| GWAS Catalog | 51 unique SNPs / 102 rows |
| ClinVar | 114 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 708 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'LGALS9' and resolved to 'Galectin-9' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 114 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 10 of 10 traits by best p-value, aggregated from 15 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O00182 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000168961/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL5474/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/LGALS9 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/LGALS9 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=LGALS9%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/LGALS9 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:31:35  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
