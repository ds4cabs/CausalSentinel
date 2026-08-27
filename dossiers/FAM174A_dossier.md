# Protein Dossier — FAM174A (Membrane protein FAM174A)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Squamous cell lung cancer | 0.129 | 0.0513 | 0.0118 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: L03 Cellulitis | -0.16 | 0.0645 | 0.0132 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: C50 Malignant neoplasm of breast | -0.0981 | 0.0425 | 0.0209 | Wald ratio | 1 | trans | NA |
| ER-negative Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0547 | 0.0242 | 0.0236 | Wald ratio | 1 | trans | NA |
| Serum cystatin C (eGFRcys) | 0.00866 | 0.00399 | 0.0299 | Wald ratio | 1 | trans | NA |
| Lung adenocarcinoma | 0.108 | 0.0515 | 0.0364 | Wald ratio | 1 | trans | NA |
| Lung cancer | 0.0688 | 0.0352 | 0.0508 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: high cholesterol | -0.0264 | 0.0137 | 0.0538 | Wald ratio | 1 | trans | NA |
| Chronic kidney disease | -0.0593 | 0.0308 | 0.0541 | Wald ratio | 1 | trans | NA |
| Sodium in urine | 0.00932 | 0.00484 | 0.0543 | Wald ratio | 1 | trans | NA |
| Forearm bone mineral density | -0.0594 | 0.0318 | 0.0619 | Wald ratio | 1 | trans | NA |
| Myocardial infarction | 0.0417 | 0.0228 | 0.0677 | Wald ratio | 1 | trans | NA |
| _...and 77 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_33 association rows across 22 traits (26 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Hematological traits (multi-trait analysis) | 7e-50 | rs62387563 | 2 | GCST90838669 | no MR -> candidate analysis |
| Bone mineral density mean | 1e-42 | rs72776654 | 1 | GCST90321120 | no MR -> candidate analysis |
| Estimated bone mineral density | 5e-19 | rs34187381 | 1 | GCST90726625 | no MR -> candidate analysis |
| Heel bone mineral density | 1e-17 | rs10515269 | 3 | GCST006979 | no MR -> candidate analysis |
| Smoking initiation | 3e-16 | rs766693 | 5 | GCST90243985 | no MR -> candidate analysis |
| White blood cell count | 1e-14 | rs62387565 | 2 | GCST90002374 | no MR -> candidate analysis |
| Core binding factor acute myeloid leukemia | 4e-14 | rs32282; rs10491363; rs282072 | 2 | GCST008413 | no MR -> candidate analysis |
| Neutrophil count | 1e-13 | rs1445171 | 2 | GCST90002351 | no MR -> candidate analysis |
| Circulating CR2 levels | 9e-13 | rs1394622 | 1 | GCST90860456 | no MR -> candidate analysis |
| CR2 protein levels | 2e-12 | rs1394622 | 1 | GCST90468852 | no MR -> candidate analysis |
| Educational attainment | 6e-12 | rs468216 | 1 | GCST90105038 | no MR -> candidate analysis |
| Type 2 diabetes | 1e-11 | rs112725069 | 1 | GCST90444202 | no MR -> candidate analysis |
| _...and 10 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 32 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| neuroendocrine neoplasm | 0.348 | — | common-variant locus | no MR -> candidate analysis |
| diabetes mellitus | 0.295 | — | common-variant locus | no MR -> candidate analysis |
| Abdominal pain | 0.245 | — | common-variant locus | MR: beta=0.0412, p=0.0708 (trans) |
| disorder of ear | 0.073 | — | common-variant locus | no MR -> candidate analysis |
| aortic aneurysm | 0.043 | — | common-variant locus | no MR -> candidate analysis |
| type 2 diabetes mellitus | 0.038 | — | common-variant locus | no MR -> candidate analysis |
| liver disorder | 0.037 | — | common-variant locus | no MR -> candidate analysis |

> Of the 7 rows above, **6 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.5e-05, LOEUF=1.53 — LoF-tolerant |
| GWAS Catalog | 22 unique SNPs / 44 rows |
| ClinVar | 63 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 32 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'FAM174A'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 63 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 22 traits by best p-value, aggregated from 33 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q8TBP5 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000174132/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/FAM174A — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/FAM174A — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=FAM174A%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/FAM174A — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:33:56  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
