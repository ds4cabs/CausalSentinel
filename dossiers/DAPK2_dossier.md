# Protein Dossier — DAPK2 (Death-associated protein kinase 2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: I30 Acute pericarditis | 0.592 | 0.213 | 0.0055 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: chronic obstructive airways disease or copd | 0.235 | 0.0874 | 0.00714 | Wald ratio | 1 | cis | NA |
| Creatinine (enzymatic) in urine | 0.016 | 0.00613 | 0.00922 | Wald ratio | 1 | cis | NA |
| Packed cell volume | -0.124 | 0.0486 | 0.0105 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: psoriasis | 0.131 | 0.053 | 0.0132 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N92 Excessive  frequent and irregular menstruation | 0.0994 | 0.0404 | 0.0139 | Wald ratio | 1 | cis | NA |
| LDL cholesterol | 0.0337 | 0.0138 | 0.0146 | Wald ratio | 1 | cis | NA |
| Chronic kidney disease | -0.0955 | 0.0398 | 0.0164 | Wald ratio | 1 | cis | NA |
| HDL cholesterol | 0.0303 | 0.0127 | 0.0175 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: G47 Sleep disorders | 0.165 | 0.0711 | 0.02 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K43 Ventral hernia | 0.184 | 0.0805 | 0.0223 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R10 Abdominal and pelvic pain | -0.0736 | 0.0333 | 0.0271 | Wald ratio | 1 | cis | NA |
| _...and 98 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4355_13_1` | DAPK2 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_43 association rows across 32 traits (29 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Death-associated protein kinase 2 levels | 2e-150 | rs4436737 | 3 | GCST90247234 | no MR -> candidate analysis |
| Death-associated protein kinase 1 levels | 2e-117 | rs55986634 | 1 | GCST90247233 | no MR -> candidate analysis |
| DAPK2 protein levels | 5e-109 | rs2414840 | 7 | GCST90468945 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 3e-18 | rs187236774 | 1 | GCST90838669 | no MR -> candidate analysis |
| Height | 3e-15 | rs17788704 | 3 | GCST90245848 | MR: beta=0.00557, p=0.469 (cis) |
| HDL cholesterol levels | 4e-15 | rs34675318 | 1 | GCST010242 | no MR -> candidate analysis |
| Thyroid stimulating hormone levels | 2e-14 | rs1542244 | 1 | GCST90572789 | no MR -> candidate analysis |
| Standing height (UKB data field 50) | 3e-12 | rs145586222 | 1 | GCST90468178 | no MR -> candidate analysis |
| Mean corpuscular volume | 7e-12 | rs72755040 | 1 | GCST90056174 | no MR -> candidate analysis |
| Height (baseline) | 3e-11 | rs17775820 | 1 | GCST90565843 | no MR -> candidate analysis |
| Platelet distribution width | 6e-10 | rs141207816 | 1 | GCST004616 | no MR -> candidate analysis |
| Gut microbial network clusters (Salmon (at 1 year) x Any Bre | 3e-9 | rs72755006 | 1 | GCST90569450 | no MR -> candidate analysis |
| _...and 20 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 124 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| alcohol drinking | 0.536 | — | common-variant locus | no MR -> candidate analysis |
| eye disorder | 0.394 | — | common-variant locus | no MR -> candidate analysis |
| hypothyroidism | 0.106 | — | common-variant locus | no MR -> candidate analysis |
| placental abruption | 0.049 | — | common-variant locus | no MR -> candidate analysis |
| gastric ulcer | 0.045 | — | common-variant locus | no MR -> candidate analysis |
| hemorrhage | 0.045 | — | common-variant locus | no MR -> candidate analysis |
| IgA glomerulonephritis | 0.04 | — | common-variant locus | no MR -> candidate analysis |

> Of the 7 rows above, **7 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Death-associated protein kinase 2) |
| gnomAD constraint | pLI=3.8e-10, LOEUF=1.05 — LoF-tolerant |
| GWAS Catalog | 75 unique SNPs / 146 rows |
| ClinVar | 99 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 124 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'DAPK2' and resolved to 'Death-associated protein kinase 2' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 99 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 32 traits by best p-value, aggregated from 43 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9UIK4 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000035664/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3123/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/DAPK2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/DAPK2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=DAPK2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/DAPK2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:14:51  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
