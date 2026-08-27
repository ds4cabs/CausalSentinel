# Protein Dossier — EGF (Pro-epidermal growth factor)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Platelet count | -7.6 | 1.68 | 5.93e-06 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | 0.0441 | 0.0124 | 3.83e-04 | Wald ratio | 1 | cis | NA |
| Mean cell volume | -0.329 | 0.106 | 0.00182 | Wald ratio | 1 | cis | NA |
| Schizophrenia | -0.133 | 0.043 | 0.0019 | Wald ratio | 1 | cis | NA |
| Lumbar spine bone mineral density | 0.0869 | 0.0351 | 0.0134 | Wald ratio | 1 | cis | NA |
| Height | 0.0286 | 0.0117 | 0.0142 | Wald ratio | 1 | cis | NA |
| Neo-neuroticism | -0.922 | 0.379 | 0.0151 | Wald ratio | 1 | cis | NA |
| Mean cell haemoglobin | -0.0953 | 0.0411 | 0.0203 | Wald ratio | 1 | cis | NA |
| Red blood cell count | 0.0203 | 0.00904 | 0.0244 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C61 Malignant neoplasm of prostate | -0.4 | 0.183 | 0.0287 | Wald ratio | 1 | cis | NA |
| ER-positive Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0641 | 0.0298 | 0.0314 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | 0.0162 | 0.00787 | 0.04 | Wald ratio | 1 | cis | NA |
| _...and 112 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_182 association rows across 99 traits (168 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| CLEC1B/EGF protein level ratio | 6e-375 | rs4444903 | 1 | GCST90314089 | no MR -> candidate analysis |
| EGF/MPIG6B protein level ratio | 5e-348 | rs4444903 | 1 | GCST90314611 | no MR -> candidate analysis |
| EGF/GP6 protein level ratio | 1e-336 | rs4444903 | 1 | GCST90314608 | no MR -> candidate analysis |
| CD40LG/EGF protein level ratio | 3e-289 | rs4444903 | 1 | GCST90313819 | no MR -> candidate analysis |
| Platelet count | 6e-283 | rs11098063 | 18 | GCST90662907 | MR: beta=-7.6, p=5.93e-06 (cis) |
| EGF/PPIB protein level ratio | 2e-272 | rs4444903 | 1 | GCST90314612 | no MR -> candidate analysis |
| EGF/MGLL protein level ratio | 2e-239 | rs4444903 | 1 | GCST90314610 | no MR -> candidate analysis |
| ANGPT1/EGF protein level ratio | 6e-205 | rs4444903 | 1 | GCST90313264 | no MR -> candidate analysis |
| CRKL/EGF protein level ratio | 3e-202 | rs4444903 | 1 | GCST90314265 | no MR -> candidate analysis |
| EGF/MANF protein level ratio | 3e-195 | rs4444903 | 1 | GCST90314609 | no MR -> candidate analysis |
| APP/EGF protein level ratio | 4e-192 | rs4444903 | 1 | GCST90313322 | no MR -> candidate analysis |
| EGF/TNFSF14 protein level ratio | 2e-152 | rs4444903 | 1 | GCST90314615 | no MR -> candidate analysis |
| _...and 87 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1538 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| familial primary hypomagnesemia with normocalciuria and normocalcemia | 0.679 | — | established (curated) | no MR -> candidate analysis |
| atrial fibrillation | 0.63 | — | common-variant locus | no MR -> candidate analysis |
| osteonecrosis | 0.548 | — | common-variant locus | no MR -> candidate analysis |
| duodenitis | 0.362 | — | common-variant locus | no MR -> candidate analysis |
| Thrombocytopenia | 0.246 | — | common-variant locus | no MR -> candidate analysis |
| cholangiocarcinoma | 0.182 | — | established (curated) | no MR -> candidate analysis |
| hereditary renal cell carcinoma | 0.182 | — | established (curated) | no MR -> candidate analysis |

> Of the 7 rows above, **7 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Pro-epidermal growth factor) |
| gnomAD constraint | pLI=1.8e-20, LOEUF=0.784 — LoF-tolerant |
| GWAS Catalog | 101 unique SNPs / 206 rows |
| ClinVar | 684 records; 3 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 1 clinical annotations across 1 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1538 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'EGF' and resolved to 'Pro-epidermal growth factor' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 684 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 20 of 99 traits by best p-value, aggregated from 182 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P01133 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000138798/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL5734/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/EGF — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/EGF — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=EGF%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=EGF — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/EGF — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:24:18  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
