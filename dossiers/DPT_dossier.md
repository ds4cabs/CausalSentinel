# Protein Dossier — DPT (Dermatopontin)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Body mass index (BMI) | -0.0225 | 0.00587 | 1.24e-04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: deep venous thrombosis (dvt) | -0.166 | 0.0493 | 7.42e-04 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R10 Abdominal and pelvic pain | -0.0929 | 0.0312 | 0.00287 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Diabetes related eye disease | 0.176 | 0.0633 | 0.00542 | Wald ratio | 1 | cis | NA |
| Alcohol intake frequency | -0.0233 | 0.00868 | 0.00728 | Wald ratio | 1 | cis | NA |
| Weight | -0.0137 | 0.00519 | 0.00803 | Wald ratio | 1 | cis | NA |
| ER-negative Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0741 | 0.0289 | 0.0103 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I48 Atrial fibrillation and flutter | 0.124 | 0.0492 | 0.0118 | Wald ratio | 1 | cis | NA |
| Depressive symptoms | -0.0241 | 0.00963 | 0.0124 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | 0.0119 | 0.00482 | 0.0133 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: migraine | -0.0893 | 0.0372 | 0.0162 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M23 Internal derangement of knee | -0.101 | 0.0438 | 0.0207 | Wald ratio | 1 | cis | NA |
| _...and 74 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4979_34_2` | DERM | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_84 association rows across 39 traits (75 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Dermatopontin levels | 8e-211 | rs1018454 | 6 | GCST90247265 | no MR -> candidate analysis |
| DPT protein levels | 2e-207 | rs78032017 | 13 | GCST90469036 | no MR -> candidate analysis |
| XCL1 protein levels | 4e-128 | rs116047858 | 8 | GCST90471081 | no MR -> candidate analysis |
| Electrocardiogram morphology (amplitude at temporal datapoin | 5e-68 | rs531706 | 16 | GCST010796 | no MR -> candidate analysis |
| Dermatopontin levels (DPT.4979.34.2) | 8e-67 | rs1018454 | 1 | GCST90240890 | no MR -> candidate analysis |
| Cerebrospinal fluid protein DPT levels | 2e-63 | rs607484 | 1 | GCST90944747 | no MR -> candidate analysis |
| Serum levels of protein DPT | 3e-63 | rs1018454 | 1 | GCST90088840 | no MR -> candidate analysis |
| Blood protein levels | 7e-34 | rs1018454 | 1 | GCST006585 | no MR -> candidate analysis |
| ECG latent space | 3e-25 | rs635954 | 1 | GCST90250897 | no MR -> candidate analysis |
| neutrophil (fraction, minimum, inv-norm transformed) | 3e-21 | rs1337742 | 1 | GCST90479715 | no MR -> candidate analysis |
| ECG cardiac MRI latent space | 2e-19 | rs545833 | 1 | GCST90250896 | no MR -> candidate analysis |
| Thyroid stimulating hormone levels | 1e-18 | rs580360 | 1 | GCST90572789 | no MR -> candidate analysis |
| _...and 27 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 749 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Sensorineural hearing impairment | 0.663 | — | common-variant locus | no MR -> candidate analysis |
| hearing loss disorder | 0.647 | — | common-variant locus | no MR -> candidate analysis |
| hypothyroidism | 0.645 | — | common-variant locus | MR: beta=-0.0588, p=0.0339 (cis) |
| atrial fibrillation | 0.577 | — | common-variant locus | MR: beta=0.124, p=0.0118 (cis) |
| deep vein thrombosis | 0.571 | — | common-variant locus | no MR -> candidate analysis |
| Progressive sensorineural hearing impairment | 0.559 | — | established (curated) | no MR -> candidate analysis |
| COVID-19 | 0.553 | — | common-variant locus | no MR -> candidate analysis |
| severe acute respiratory syndrome | 0.553 | — | common-variant locus | no MR -> candidate analysis |
| restless legs syndrome | 0.529 | — | common-variant locus | no MR -> candidate analysis |
| phobic disorder | 0.484 | — | common-variant locus | no MR -> candidate analysis |
| septic shock | 0.484 | — | common-variant locus | no MR -> candidate analysis |
| blood coagulation disease | 0.476 | — | common-variant locus | no MR -> candidate analysis |
| lower respiratory tract disorder | 0.445 | — | common-variant locus | no MR -> candidate analysis |
| placenta praevia | 0.429 | — | common-variant locus | no MR -> candidate analysis |
| venous thromboembolism | 0.412 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **13 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.9e-05, LOEUF=0.968 — LoF-tolerant |
| GWAS Catalog | 80 unique SNPs / 154 rows |
| ClinVar | 69 records; 4 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 749 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'DPT'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 69 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 39 traits by best p-value, aggregated from 84 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q07507 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000143196/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/DPT — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/DPT — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=DPT%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/DPT — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:20:16  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
