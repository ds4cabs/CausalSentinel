# Protein Dossier — MXRA7 (Matrix-remodeling-associated protein 7)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Pulse rate | -0.0822 | 0.0188 | 1.22e-05 | Wald ratio | 1 | cis | NA |
| ER-negative Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.174 | 0.0502 | 5.21e-04 | Wald ratio | 1 | cis | NA |
| Sodium in urine | 0.0342 | 0.0105 | 0.00114 | Wald ratio | 1 | cis | NA |
| Coronary heart disease | -0.133 | 0.0418 | 0.00141 | Wald ratio | 1 | cis | NA |
| Serum cystatin C (eGFRcys) | 0.0249 | 0.0083 | 0.0027 | Wald ratio | 1 | cis | NA |
| Systolic blood pressure  automated reading | 0.0284 | 0.0109 | 0.00924 | Wald ratio | 1 | cis | NA |
| Caudate volume | -52.4 | 21.6 | 0.0155 | Wald ratio | 1 | cis | NA |
| Serum creatinine (eGFRcrea) | 0.00961 | 0.00402 | 0.0168 | Wald ratio | 1 | cis | NA |
| Myocardial infarction | -0.111 | 0.0465 | 0.0173 | Wald ratio | 1 | cis | NA |
| Age at menarche | 0.0568 | 0.0252 | 0.024 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | -0.0206 | 0.00924 | 0.0258 | Wald ratio | 1 | cis | NA |
| Diastolic blood pressure  automated reading | -0.024 | 0.0109 | 0.0278 | Wald ratio | 1 | cis | NA |
| _...and 98 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_33 association rows across 22 traits (30 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Bone mineral density mean | 1e-300 | rs111262383 | 1 | GCST90321120 | no MR -> candidate analysis |
| Matrix-remodeling-associated protein 7 levels | 3e-205 | rs4789346 | 4 | GCST90248545 | no MR -> candidate analysis |
| Serum levels of protein MXRA7 | 5e-53 | rs1558251 | 1 | GCST90089979 | no MR -> candidate analysis |
| Blood protein levels | 1e-36 | rs1558251 | 1 | GCST006585 | no MR -> candidate analysis |
| heart rate (HR, mean, inv-normal transformed) | 3e-25 | rs2286589 | 1 | GCST90480666 | no MR -> candidate analysis |
| Matrix-remodeling-associated protein 7 levels (MXRA7.8005.1. | 2e-20 | rs9900613 | 1 | GCST90241895 | no MR -> candidate analysis |
| Corneal resistance factor (MTAG) | 2e-19 | rs2286586 | 3 | GCST90102517 | no MR -> candidate analysis |
| Central corneal thickness (MTAG) | 6e-16 | rs11077857 | 2 | GCST90102518 | no MR -> candidate analysis |
| Corneal resistance factor | 3e-15 | rs11077857 | 2 | GCST90100568 | no MR -> candidate analysis |
| heart rate (HR, maximum, inv-normal transformed) | 2e-14 | rs2286589 | 1 | GCST90480665 | no MR -> candidate analysis |
| Matrix-remodeling-associated protein 7 level in Chronic kidn | 9e-14 | rs751463433 | 1 | GCST90238760 | no MR -> candidate analysis |
| Pulse rate (UKB data field 102) | 1e-13 | rs720782 | 1 | GCST90468177 | no MR -> candidate analysis |
| _...and 10 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 347 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| COVID-19 | 0.421 | — | common-variant locus | no MR -> candidate analysis |
| severe acute respiratory syndrome | 0.421 | — | common-variant locus | no MR -> candidate analysis |
| Age-related cataract | 0.409 | — | common-variant locus | no MR -> candidate analysis |
| systemic lupus erythematosus | 0.131 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=4.3e-07, LOEUF=1.53 — LoF-tolerant |
| GWAS Catalog | 59 unique SNPs / 118 rows |
| ClinVar | 62 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 347 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'MXRA7'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 62 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 22 traits by best p-value, aggregated from 33 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P84157 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000182534/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/MXRA7 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/MXRA7 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=MXRA7%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/MXRA7 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:53:42  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
