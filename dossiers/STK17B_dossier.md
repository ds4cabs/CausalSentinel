# Protein Dossier — STK17B (Serine/threonine-protein kinase 17B)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Myocardial infarction | -0.155 | 0.0444 | 4.76e-04 | Wald ratio | 1 | trans | NA |
| Coronary heart disease | -0.134 | 0.0403 | 8.64e-04 | Wald ratio | 1 | trans | NA |
| Amyotrophic lateral sclerosis | -0.237 | 0.0729 | 0.00113 | Wald ratio | 1 | trans | NA |
| Eczema | 0.214 | 0.0713 | 0.00266 | Wald ratio | 1 | trans | NA |
| Years of schooling | -0.0476 | 0.0159 | 0.0027 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: N92 Excessive  frequent and irregular menstruation | 0.168 | 0.0565 | 0.00295 | Wald ratio | 1 | trans | NA |
| Chronic kidney disease | 0.174 | 0.0634 | 0.00596 | Wald ratio | 1 | trans | NA |
| Forced vital capacity (FVC) | -0.0214 | 0.00785 | 0.00649 | Wald ratio | 1 | trans | NA |
| LDL cholesterol | -0.0598 | 0.0222 | 0.00701 | Wald ratio | 1 | trans | NA |
| Sodium in urine | 0.0238 | 0.00941 | 0.0115 | Wald ratio | 1 | trans | NA |
| Heel bone mineral density (BMD) T-score  automated | 0.0303 | 0.0124 | 0.0143 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: deep venous thrombosis (dvt) | -0.203 | 0.0837 | 0.0155 | Wald ratio | 1 | trans | NA |
| _...and 99 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5249_31_3` | DRAK2 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_36 association rows across 24 traits (31 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Vertex-wise sulcal depth | 9e-33 | rs1054537 | 1 | GCST90095129 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 2e-32 | rs4514889 | 2 | GCST90838669 | no MR -> candidate analysis |
| Mean reticulocyte volume (UKB data field 30260) | 2e-16 | rs539299744 | 1 | GCST90468088 | no MR -> candidate analysis |
| Mean sphered cell volume (UKB data field 30270) | 5e-16 | rs75229287 | 1 | GCST90468089 | no MR -> candidate analysis |
| Vertex-wise cortical thickness | 1e-15 | rs1519602 | 1 | GCST90095131 | no MR -> candidate analysis |
| Cortical thickness | 4e-15 | rs1519602 | 1 | GCST90091061 | no MR -> candidate analysis |
| Mean corpuscular volume | 6e-15 | rs76005009 | 4 | GCST90002338 | no MR -> candidate analysis |
| Mean spheric corpuscular volume | 3e-14 | rs539299744 | 1 | GCST90002397 | no MR -> candidate analysis |
| Mean corpuscular hemoglobin | 3e-13 | rs17302154 | 3 | GCST007068 | no MR -> candidate analysis |
| Eosinophill percentage (UKB data field 30210) | 5e-13 | rs539299744 | 1 | GCST90468069 | no MR -> candidate analysis |
| Eosinophil percentage of white cells | 3e-12 | rs539299744 | 1 | GCST90002382 | no MR -> candidate analysis |
| Brain morphology (MOSTest) | 3e-12 | rs1519602 | 1 | GCST90239729 | no MR -> candidate analysis |
| _...and 12 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 123 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| frozen shoulder | 0.5 | — | common-variant locus | no MR -> candidate analysis |
| placental retention | 0.484 | — | common-variant locus | no MR -> candidate analysis |
| type 2 diabetes mellitus | 0.3 | — | common-variant locus | no MR -> candidate analysis |
| smoking initiation | 0.297 | — | common-variant locus | no MR -> candidate analysis |
| depressive disorder | 0.215 | — | common-variant locus | no MR -> candidate analysis |
| anxiety disorder | 0.212 | — | common-variant locus | no MR -> candidate analysis |
| hypothyroidism | 0.203 | — | common-variant locus | MR: beta=-0.0405, p=0.361 (trans) |
| mood disorder | 0.176 | — | common-variant locus | no MR -> candidate analysis |
| ulcerative colitis | 0.176 | — | common-variant locus | no MR -> candidate analysis |
| generalized dystonia | 0.173 | — | common-variant locus | no MR -> candidate analysis |
| hypertrophic cardiomyopathy | 0.103 | — | common-variant locus | no MR -> candidate analysis |
| mental disorder | 0.055 | — | common-variant locus | no MR -> candidate analysis |
| upper extremity fracture | 0.041 | — | common-variant locus | no MR -> candidate analysis |
| ovarian dysfunction | 0.041 | — | common-variant locus | no MR -> candidate analysis |

> Of the 14 rows above, **13 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Serine/threonine-protein kinase 17B) |
| gnomAD constraint | pLI=0.0042, LOEUF=0.72 — LoF-tolerant |
| GWAS Catalog | 36 unique SNPs / 71 rows |
| ClinVar | 75 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 123 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'STK17B' and resolved to 'Serine/threonine-protein kinase 17B' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 75 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 24 traits by best p-value, aggregated from 36 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O94768 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000081320/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3980/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/STK17B — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/STK17B — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=STK17B%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/STK17B — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:15:29  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
