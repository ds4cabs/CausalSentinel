# Protein Dossier — RAB6B (Ras-related protein Rab-6B)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Transferrin | 0.214 | 0.0507 | 2.44e-05 | Wald ratio | 1 | cis | NA |
| Mean cell haemoglobin | -0.172 | 0.0489 | 4.40e-04 | Wald ratio | 1 | cis | NA |
| Knee osteoarthritis | -0.408 | 0.139 | 0.00334 | Wald ratio | 1 | cis | NA |
| Alzheimer's disease | -0.212 | 0.077 | 0.00583 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypopituitarism | 0.84 | 0.32 | 0.00864 | Wald ratio | 1 | cis | NA |
| Femoral neck bone mineral density | 0.0968 | 0.0372 | 0.00931 | Wald ratio | 1 | cis | NA |
| Mean cell volume | -0.322 | 0.125 | 0.0102 | Wald ratio | 1 | cis | NA |
| Schizophrenia | -0.133 | 0.0522 | 0.0107 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | 0.0374 | 0.0157 | 0.0173 | Wald ratio | 1 | cis | NA |
| Thyroid cancer | -1.02 | 0.432 | 0.0183 | Wald ratio | 1 | cis | NA |
| Lumbar spine bone mineral density | 0.0961 | 0.0433 | 0.0265 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: D12 Benign neoplasm of colon  rectum  anus and anal canal | -0.317 | 0.144 | 0.028 | Wald ratio | 1 | cis | NA |
| _...and 95 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_21 association rows across 15 traits (14 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Ras-related protein Rab-6B levels | 9e-149 | rs10212397 | 1 | GCST90249223 | no MR -> candidate analysis |
| Serum levels of protein RAB6B | 4e-31 | rs9813363 | 1 | GCST90087852 | no MR -> candidate analysis |
| TF protein levels | 2e-27 | rs17376530 | 5 | GCST90470841 | no MR -> candidate analysis |
| Iron status biomarkers (total iron binding capacity) | 3e-20 | rs7637997 | 1 | GCST004571 | no MR -> candidate analysis |
| Iron status biomarkers (transferrin saturation) | 3e-20 | rs7637997 | 1 | GCST004572 | no MR -> candidate analysis |
| Blood protein levels | 1e-17 | rs9813363 | 1 | GCST006585 | no MR -> candidate analysis |
| Mean reticulocyte volume | 2e-12 | rs1525886 | 1 | GCST90002396 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 2e-12 | rs940900 | 1 | GCST90838669 | no MR -> candidate analysis |
| Mean corpuscular hemoglobin | 9e-11 | rs2692685 | 2 | GCST007068 | no MR -> candidate analysis |
| Immune reponse to smallpox (secreted IL-1beta) | 7e-8 | rs9835973 | 1 | GCST001533 | no MR -> candidate analysis |
| Alkenylphosphatidylethanolamine (P-20:1/20:4) levels | 3e-7 | rs779501250 | 1 | GCST90024447 | no MR -> candidate analysis |
| 5-acetylamino-6-amino-3-methyluracil levels in elite athlete | 2e-6 | rs2692681 | 1 | GCST90134187 | no MR -> candidate analysis |
| _...and 3 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 80 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| alcohol drinking | 0.573 | — | common-variant locus | no MR -> candidate analysis |
| major salivary gland cancer | 0.364 | — | common-variant locus | no MR -> candidate analysis |
| bipolar disorder | 0.17 | — | common-variant locus | MR: beta=-0.23, p=0.062 (cis) |
| Abnormality of the immune system | 0.079 | — | common-variant locus | no MR -> candidate analysis |
| colorectal cancer | 0.063 | — | common-variant locus | no MR -> candidate analysis |
| colorectal adenoma | 0.063 | — | common-variant locus | no MR -> candidate analysis |
| hypertension, pregnancy-induced | 0.035 | — | common-variant locus | no MR -> candidate analysis |
| squamous cell carcinoma | 0.031 | — | common-variant locus | no MR -> candidate analysis |

> Of the 8 rows above, **7 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1, LOEUF=0.422 — LoF-INTOLERANT |
| GWAS Catalog | 101 unique SNPs / 206 rows |
| ClinVar | 51 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 80 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'RAB6B'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 51 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 15 of 15 traits by best p-value, aggregated from 21 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9NRW1 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000154917/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/RAB6B — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/RAB6B — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=RAB6B%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/RAB6B — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:44:55  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
