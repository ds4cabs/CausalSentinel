# Protein Dossier — NQO1 (NAD(P)H dehydrogenase [quinone] 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Body mass index (BMI) | -0.0199 | 0.00414 | 1.56e-06 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | 0.016 | 0.0034 | 2.74e-06 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | 0.0151 | 0.00359 | 2.57e-05 | Wald ratio | 1 | cis | NA |
| Age at menarche | 0.036 | 0.01 | 3.30e-04 | Wald ratio | 1 | cis | NA |
| Height | 0.0173 | 0.00493 | 4.42e-04 | Wald ratio | 1 | cis | NA |
| Vascular or heart problems diagnosed by doctor: Angina | -0.0825 | 0.0253 | 0.00109 | Wald ratio | 1 | cis | NA |
| Subjective well being | -0.0173 | 0.00533 | 0.00115 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: asthma | -0.0392 | 0.0121 | 0.00117 | Wald ratio | 1 | cis | NA |
| Systolic blood pressure  automated reading | 0.0132 | 0.00424 | 0.00189 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: S76 Injury of muscle and tendon at hip and thigh level | 0.406 | 0.134 | 0.00247 | Wald ratio | 1 | cis | NA |
| Potassium in urine | -0.0127 | 0.00421 | 0.00249 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | -0.0581 | 0.0195 | 0.00291 | Wald ratio | 1 | cis | NA |
| _...and 120 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_63 association rows across 53 traits (57 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| NAD(P)H dehydrogenase [quinone] 1 levels | 2e-320 | rs689455 | 2 | GCST90427942 | no MR -> candidate analysis |
| heart rate (HR, mean, inv-normal transformed) | 1e-59 | rs2917677 | 1 | GCST90476338 | no MR -> candidate analysis |
| sodium (minimum, inv-norm transformed) | 6e-45 | rs564381127 | 1 | GCST90480704 | no MR -> candidate analysis |
| Cerebrospinal fluid protein NQO1 levels | 6e-41 | rs1437135 | 1 | GCST90942536 | no MR -> candidate analysis |
| Estimated glomerular filtration rate (cystatin c) | 8e-39 | rs113441031 | 2 | GCST90428448 | no MR -> candidate analysis |
| Estimated glomerular filtration rate (creatinine, cystatin c | 1e-37 | rs113441031 | 1 | GCST90428446 | no MR -> candidate analysis |
| Estimated glomerular filtration rate based on creatinine and | 3e-33 | rs113441031 | 1 | GCST90566737 | no MR -> candidate analysis |
| Cystatin C levels in bottom 99% of individuals by creatinine | 4e-33 | rs113441031 | 1 | GCST90566734 | no MR -> candidate analysis |
| Type 2 diabetes | 6e-32 | rs2917677 | 1 | GCST90492734 | MR: beta=0.0264, p=0.187 (cis) |
| Body mass index | 5e-31 | rs2917677 | 1 | GCST90301650 | MR: beta=-0.0199, p=1.56e-06 (cis) |
| IGF 1 (UKB data field 30770) | 6e-27 | rs113441031 | 1 | GCST90468078 | no MR -> candidate analysis |
| Estimated glomerular filtration rate (creatinine) | 7e-27 | rs113441031 | 3 | GCST90103633 | no MR -> candidate analysis |
| _...and 41 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 751 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| smoking initiation | 0.306 | — | common-variant locus | no MR -> candidate analysis |
| smoking behavior | 0.25 | — | common-variant locus | no MR -> candidate analysis |
| coronary artery disorder | 0.231 | — | common-variant locus | no MR -> candidate analysis |
| risk-taking behaviour | 0.21 | — | common-variant locus | no MR -> candidate analysis |
| chronic kidney disease | 0.089 | — | common-variant locus | MR: beta=-0.0213, p=0.4 (cis) |

> Of the 5 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (NQO1 protein) |
| gnomAD constraint | pLI=2.7e-10, LOEUF=1.27 — LoF-tolerant |
| GWAS Catalog | 102 unique SNPs / 186 rows |
| ClinVar | 317 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 9 clinical annotations across 7 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 751 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'NQO1' and resolved to 'NQO1 protein' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 317 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 20 of 53 traits by best p-value, aggregated from 63 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P15559 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000181019/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2169730/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/NQO1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/NQO1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=NQO1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=NQO1 — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/NQO1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:03:33  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
