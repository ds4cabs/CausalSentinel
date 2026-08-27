# Protein Dossier — C1QTNF3 (Complement C1q tumor necrosis factor-related protein 3)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Depressive symptoms | -0.0739 | 0.0246 | 0.0027 | Wald ratio | 1 | cis | NA |
| Birth length | 0.198 | 0.0734 | 0.00712 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I83 Varicose veins of lower extremities | 0.255 | 0.0972 | 0.00885 | Wald ratio | 1 | cis | NA |
| Large vessel disease | 0.668 | 0.26 | 0.0102 | Wald ratio | 1 | cis | NA |
| Haemoglobin concentration | 0.097 | 0.0419 | 0.0205 | Wald ratio | 1 | cis | NA |
| Neo-neuroticism | 1.65 | 0.712 | 0.0207 | Wald ratio | 1 | cis | NA |
| Height | 0.0493 | 0.0222 | 0.0263 | Wald ratio | 1 | cis | NA |
| Coronary heart disease | 0.141 | 0.0659 | 0.033 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K44 Diaphragmatic hernia | 0.238 | 0.114 | 0.0364 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: D12 Benign neoplasm of colon  rectum  anus and anal canal | 0.243 | 0.12 | 0.0419 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M72 Fibroblastic disorders | 0.357 | 0.176 | 0.0423 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C50 Malignant neoplasm of breast | 0.226 | 0.112 | 0.0441 | Wald ratio | 1 | cis | NA |
| _...and 81 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_24 association rows across 18 traits (19 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Complement C1q tumor necrosis factor-related protein 3 level | 2e-86 | rs7712366 | 2 | GCST90427006 | no MR -> candidate analysis |
| Cerebrospinal fluid 3-hydroxy-2-ethylpropionate levels | 6e-30 | rs10941112 | 1 | GCST90317964 | no MR -> candidate analysis |
| IgA nephropathy | 2e-14 | rs3217251 | 1 | GCST90448177 | no MR -> candidate analysis |
| Bone mineral density mean | 3e-12 | rs138365781 | 1 | GCST90321120 | no MR -> candidate analysis |
| Secondary hyperparathyroidism (of renal origin) (PheCode 588 | 4e-11 | rs535921475 | 1 | GCST90480386 | no MR -> candidate analysis |
| Skin color | 4e-10 | rs149359 | 2 | GCST90255690 | no MR -> candidate analysis |
| Waist-hip ratio | 9e-10 | rs299615 | 1 | GCST007067 | no MR -> candidate analysis |
| Waist-to-hip ratio adjusted for BMI | 2e-9 | rs299615 | 3 | GCST008994 | no MR -> candidate analysis |
| Skin phototype score | 2e-9 | rs36089417 | 3 | GCST90255688 | no MR -> candidate analysis |
| 1,7-dimethylurate levels | 6e-9 | rs561886765 | 1 | GCST90244877 | no MR -> candidate analysis |
| Abdominal size (multivariate analysis) | 1e-8 | rs10074193 | 1 | GCST90624103 | no MR -> candidate analysis |
| Blood protein levels | 3e-8 | rs840390 | 1 | GCST006585 | no MR -> candidate analysis |
| _...and 6 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 226 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Abnormality of the skeletal system | 0.555 | — | common-variant locus | no MR -> candidate analysis |
| secondary hyperparathyroidism of renal origin | 0.211 | — | common-variant locus | no MR -> candidate analysis |
| hair color | 0.071 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=7.5e-08, LOEUF=1.11 — LoF-tolerant |
| GWAS Catalog | 85 unique SNPs / 161 rows |
| ClinVar | 76 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 226 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'C1QTNF3'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 76 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 18 of 18 traits by best p-value, aggregated from 24 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9BXJ4 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000082196/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/C1QTNF3 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/C1QTNF3 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=C1QTNF3%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/C1QTNF3 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:20:52  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
