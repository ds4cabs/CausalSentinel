# Protein Dossier — CPA2 (Carboxypeptidase A2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Alcohol intake frequency | -0.0295 | 0.013 | 0.0238 | Wald ratio | 1 | trans | NA |
| Primary sclerosing cholangitis  | -0.28 | 0.127 | 0.0275 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: R11 Nausea and vomiting | -0.646 | 0.297 | 0.0297 | Wald ratio | 1 | trans | NA |
| Sodium in urine | -0.0188 | 0.00868 | 0.0306 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: sleep apnoea | 0.263 | 0.125 | 0.0349 | Wald ratio | 1 | trans | NA |
| Systolic blood pressure  automated reading | 0.0182 | 0.00903 | 0.0436 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: G47 Sleep disorders | 0.19 | 0.0962 | 0.0485 | Wald ratio | 1 | trans | NA |
| Cancer code  self-reported: prostate cancer | -0.263 | 0.137 | 0.0557 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: N92 Excessive  frequent and irregular menstruation | -0.135 | 0.0707 | 0.056 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: C61 Malignant neoplasm of prostate | -0.281 | 0.147 | 0.0562 | Wald ratio | 1 | trans | NA |
| Squamous cell lung cancer | -0.203 | 0.112 | 0.0701 | Wald ratio | 1 | trans | NA |
| Eye problems or disorders: Glaucoma | 0.118 | 0.0657 | 0.0723 | Wald ratio | 1 | trans | NA |
| _...and 65 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_20 association rows across 14 traits (18 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating CPA2 levels | 3e-832 | rs6952090 | 4 | GCST90859671 | no MR -> candidate analysis |
| Carboxypeptidase A4 levels (CPA4.9267.2.3) | 9e-311 | rs4731674 | 1 | GCST90240596 | no MR -> candidate analysis |
| Cerebrospinal fluid protein CPA2 levels | 1e-157 | rs6952090 | 1 | GCST90944210 | no MR -> candidate analysis |
| Carboxypeptidase A4 levels | 1e-131 | rs73146784 | 1 | GCST90246874 | no MR -> candidate analysis |
| CPA2 protein levels | 2e-103 | rs751189658 | 4 | GCST90468837 | no MR -> candidate analysis |
| Cerebrospinal fluid protein CPA4 levels | 5e-59 | rs73146784 | 1 | GCST90944211 | no MR -> candidate analysis |
| Carboxypeptidase A2 levels | 3e-37 | rs2171493 | 1 | GCST90059933 | no MR -> candidate analysis |
| HS6ST1 protein levels | 1e-22 | rs10257530 | 1 | GCST90469479 | no MR -> candidate analysis |
| Circulating HS6ST1 levels | 4e-22 | rs6952090 | 1 | GCST90860515 | no MR -> candidate analysis |
| Neurological blood protein biomarker levels | 9e-15 | rs112255027 | 1 | GCST008478 | no MR -> candidate analysis |
| Asparaginase-induced acute pancreatitis in acute lymphoblast | 2e-8 | rs199695765 | 1 | GCST003501 | no MR -> candidate analysis |
| Body shape phenotype PC3 | 4e-8 | rs62489501 | 1 | GCST90832991 | no MR -> candidate analysis |
| _...and 2 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 435 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| exostosis | 0.36 | — | common-variant locus | no MR -> candidate analysis |
| drug allergy | 0.337 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Carboxypeptidase A2) |
| gnomAD constraint | pLI=3.9e-18, LOEUF=1.26 — LoF-tolerant |
| GWAS Catalog | 80 unique SNPs / 160 rows |
| ClinVar | 91 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 1 clinical annotations across 1 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 435 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'CPA2' and resolved to 'Carboxypeptidase A2' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 91 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 14 of 14 traits by best p-value, aggregated from 20 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P48052 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000158516/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4939/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CPA2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CPA2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CPA2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=CPA2 — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CPA2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:59:11  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
