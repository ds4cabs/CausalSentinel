# Protein Dossier — SCARF1 (Scavenger receptor class F member 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Depressive symptoms | 0.0187 | 0.00678 | 0.00596 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: muscle or soft tissue injuries | 0.139 | 0.0522 | 0.00761 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Other bones | 0.0528 | 0.0209 | 0.0115 | Wald ratio | 1 | cis | NA |
| Serum cystatin C (eGFRcys) | 0.00933 | 0.0039 | 0.0168 | Wald ratio | 1 | cis | NA |
| Squamous cell lung cancer | -0.123 | 0.0524 | 0.0186 | Wald ratio | 1 | cis | NA |
| Fractured or broken bones in last 5 years | 0.0349 | 0.0153 | 0.0224 | Wald ratio | 1 | cis | NA |
| Glioma | 0.201 | 0.0917 | 0.0285 | Wald ratio | 1 | cis | NA |
| Eczema | -0.0763 | 0.0349 | 0.0288 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | 0.0177 | 0.00849 | 0.0373 | Wald ratio | 1 | cis | NA |
| Alzheimer's disease | -0.067 | 0.0322 | 0.0376 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K60 Fissure and fistula of anal and rectal regions | -0.184 | 0.0911 | 0.0429 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N81 Female genital prolapse | 0.0781 | 0.0392 | 0.0464 | Wald ratio | 1 | cis | NA |
| _...and 96 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5129_12_3` | SREC-I | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_32 association rows across 22 traits (32 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| DAG1/SCARF1 protein level ratio | 8e-1454 | rs2272011 | 1 | GCST90314381 | no MR -> candidate analysis |
| SCARF1/TNFRSF14 protein level ratio | 3e-1355 | rs2272011 | 1 | GCST90315812 | no MR -> candidate analysis |
| ESAM/SCARF1 protein level ratio | 2e-1310 | rs2272011 | 1 | GCST90314715 | no MR -> candidate analysis |
| PEAR1/SCARF1 protein level ratio | 9e-1003 | rs2272011 | 1 | GCST90315642 | no MR -> candidate analysis |
| SCARF1/SUSD1 protein level ratio | 9e-973 | rs2272011 | 1 | GCST90315811 | no MR -> candidate analysis |
| Circulating SCARF1 levels | 1e-841 | rs2272011 | 5 | GCST90860642 | no MR -> candidate analysis |
| Scavenger receptor class F member 1 levels | 3e-118 | rs2272011 | 5 | GCST90249444 | no MR -> candidate analysis |
| Cerebrospinal fluid protein SCARF1 levels | 4e-99 | rs76081968 | 1 | GCST90944886 | no MR -> candidate analysis |
| Serum levels of protein SCARF1 | 4e-93 | rs2272011 | 1 | GCST90088945 | no MR -> candidate analysis |
| SCARF1 protein levels | 2e-39 | rs186669865 | 2 | GCST90470536 | no MR -> candidate analysis |
| Mean platelet thrombocyte volume (UKB data field 30100) | 7e-28 | rs113487086 | 1 | GCST90468087 | no MR -> candidate analysis |
| Scavenger receptor class F member 1 level in Chronic kidney  | 8e-24 | rs2272011 | 1 | GCST90237863 | no MR -> candidate analysis |
| _...and 10 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 440 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| brain aneurysm | 0.511 | — | common-variant locus | no MR -> candidate analysis |
| rhabdomyolysis | 0.325 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.4e-10, LOEUF=0.814 — LoF-tolerant |
| GWAS Catalog | 103 unique SNPs / 218 rows |
| ClinVar | 270 records; 4 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 440 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'SCARF1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 270 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 22 traits by best p-value, aggregated from 32 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q14162 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000074660/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/SCARF1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/SCARF1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=SCARF1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/SCARF1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:55:52  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
