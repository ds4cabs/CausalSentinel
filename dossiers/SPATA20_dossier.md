# Protein Dossier — SPATA20 (Spermatogenesis-associated protein 20)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Birth weight | -0.0648 | 0.015 | 1.59e-05 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | 0.0528 | 0.0127 | 3.32e-05 | Wald ratio | 1 | cis | NA |
| Systolic blood pressure  automated reading | 0.04 | 0.0101 | 6.87e-05 | Wald ratio | 1 | cis | NA |
| Diastolic blood pressure  automated reading | 0.0346 | 0.0101 | 5.79e-04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | 0.0479 | 0.016 | 0.00269 | Wald ratio | 1 | cis | NA |
| Mean cell haemoglobin | -0.151 | 0.0513 | 0.00322 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K60 Fissure and fistula of anal and rectal regions | 0.31 | 0.108 | 0.00414 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: L03 Cellulitis | 0.246 | 0.0863 | 0.00428 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: pernicious anaemia | 0.351 | 0.13 | 0.00706 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: gastro-oesophageal reflux (gord)  or  gastric reflux | -0.138 | 0.0545 | 0.0113 | Wald ratio | 1 | cis | NA |
| Lumbar spine bone mineral density | 0.0902 | 0.036 | 0.0123 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: enlarged prostate | -0.276 | 0.112 | 0.014 | Wald ratio | 1 | cis | NA |
| _...and 106 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_37 association rows across 34 traits (35 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Spermatogenesis-associated protein 20 levels | 3e-926 | rs8076632 | 2 | GCST90249648 | no MR -> candidate analysis |
| Bone mineral density mean | 1e-300 | rs117351904 | 1 | GCST90321120 | no MR -> candidate analysis |
| Serum levels of protein SPATA20 | 8e-149 | rs8076632 | 1 | GCST90086548 | no MR -> candidate analysis |
| Height | 1e-39 | rs878619 | 1 | GCST90245848 | MR: beta=-0.0284, p=0.0455 (cis) |
| Spermatogenesis-associated protein 20 levels (SPATA20.11117. | 9e-24 | rs9890200 | 1 | GCST90242879 | no MR -> candidate analysis |
| Sex hormone-binding globulin levels adjusted for BMI and hee | 3e-18 | rs8076628 | 1 | GCST90399398 | no MR -> candidate analysis |
| Sex hormone-binding globulin levels and heel estimated bone  | 5e-18 | rs8077323 | 1 | GCST90399396 | no MR -> candidate analysis |
| Regulator of G-protein signaling 7 protein levels (SomaScan  | 6e-18 | rs9890200 | 1 | GCST90441189 | no MR -> candidate analysis |
| Glycine levels | 7e-13 | rs9890200 | 1 | GCST90501110 | no MR -> candidate analysis |
| Heel bone mineral density | 2e-11 | rs916978 | 1 | GCST007066 | MR: beta=0.0528, p=3.32e-05 (cis) |
| Estimated glomerular filtration rate (creatinine, cystatin c | 2e-11 | rs1809284 | 1 | GCST90428446 | no MR -> candidate analysis |
| Estimated glomerular filtration rate (creatinine) | 2e-11 | rs1809284 | 1 | GCST90428447 | no MR -> candidate analysis |
| _...and 22 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 174 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| risk-taking behaviour | 0.555 | — | common-variant locus | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=5.3e-19, LOEUF=0.908 — LoF-tolerant |
| GWAS Catalog | 52 unique SNPs / 104 rows |
| ClinVar | 182 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 174 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'SPATA20'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 182 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 34 traits by best p-value, aggregated from 37 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q8TB22 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000006282/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/SPATA20 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/SPATA20 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=SPATA20%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/SPATA20 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:11:10  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
