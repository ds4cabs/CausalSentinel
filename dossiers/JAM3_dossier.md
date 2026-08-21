# Protein Dossier — JAM3 (Junctional adhesion molecule C)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Schizophrenia | -0.243 | 0.0587 | 3.48e-05 | Wald ratio | 1 | cis | NA |
| Pulse rate | 0.0795 | 0.0235 | 7.04e-04 | Wald ratio | 1 | cis | NA |
| Microalbuminuria | 0.332 | 0.114 | 0.00368 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: Z09 Follow-up examination after treatment for conditions other than malignant neoplasms | 0.214 | 0.0879 | 0.0148 | Wald ratio | 1 | cis | NA |
| Caudate volume | 62.5 | 26.6 | 0.0187 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | 0.0298 | 0.0133 | 0.0245 | Wald ratio | 1 | cis | NA |
| HDL cholesterol | -0.0587 | 0.0272 | 0.0308 | Wald ratio | 1 | cis | NA |
| HOMA-B | 0.0408 | 0.019 | 0.0321 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: small intestine or small bowel cancer | 0.733 | 0.345 | 0.0336 | Wald ratio | 1 | cis | NA |
| Cardioembolic stroke | -0.377 | 0.182 | 0.038 | Wald ratio | 1 | cis | NA |
| Lung adenocarcinoma | -0.326 | 0.16 | 0.0417 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C50 Malignant neoplasm of breast | 0.176 | 0.0877 | 0.0442 | Wald ratio | 1 | cis | NA |
| _...and 94 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2998_53_2` | JAM-C | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_22 association rows across 20 traits (20 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| JAM2/RGMB protein level ratio | 6e-29 | rs11223705 | 1 | GCST90315237 | no MR -> candidate analysis |
| JAM2 protein levels | 9e-23 | rs12289084 | 1 | GCST90469659 | no MR -> candidate analysis |
| Cerebrospinal fluid dimethylmalonic acid levels | 5e-22 | rs75201238 | 1 | GCST90318077 | no MR -> candidate analysis |
| Circulating JAM2 levels | 4e-19 | rs12277151 | 1 | GCST90859722 | no MR -> candidate analysis |
| Serum levels of protein JAM3 | 3e-16 | rs655627 | 1 | GCST90088176 | no MR -> candidate analysis |
| JAM3 protein levels | 1e-15 | rs76745913 | 1 | GCST90469660 | no MR -> candidate analysis |
| Blood protein levels | 4e-14 | rs655627 | 1 | GCST006585 | no MR -> candidate analysis |
| Height | 6e-13 | rs470631 | 1 | GCST90662911 | no MR -> candidate analysis |
| White blood cell count | 3e-12 | rs610829 | 1 | GCST90662906 | no MR -> candidate analysis |
| Atrial fibrillation | 2e-11 | rs34732010 | 2 | GCST90624411 | MR: beta=0.193, p=0.0663 (cis) |
| Junctional adhesion molecule C levels | 4e-11 | rs12270157 | 1 | GCST90425568 | no MR -> candidate analysis |
| Neutrophil count | 1e-10 | rs7947419 | 2 | GCST90002398 | no MR -> candidate analysis |
| _...and 8 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 2379 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| porencephaly-microcephaly-bilateral congenital cataract syndrome | 0.846 | — | established (curated) | no MR -> candidate analysis |
| atrial fibrillation | 0.571 | — | common-variant locus | MR: beta=0.193, p=0.0663 (cis) |
| stroke disorder | 0.423 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.423 | — | common-variant locus | no MR -> candidate analysis |
| nephrotic syndrome | 0.414 | — | common-variant locus | no MR -> candidate analysis |
| temporomandibular joint disorder | 0.414 | — | common-variant locus | no MR -> candidate analysis |
| blood vessel replacement | 0.389 | — | common-variant locus | no MR -> candidate analysis |
| corneal dystrophy | 0.389 | — | common-variant locus | no MR -> candidate analysis |
| bronchial disorder | 0.389 | — | common-variant locus | no MR -> candidate analysis |
| hereditary disease | 0.317 | — | established (curated) | no MR -> candidate analysis |
| Anxiety | 0.204 | — | common-variant locus | no MR -> candidate analysis |
| schizophrenia | 0.182 | — | established (curated) | MR: beta=-0.243, p=3.48e-05 (cis) |

> Of the 12 rows above, **10 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=4.8e-09, LOEUF=1.06 — LoF-tolerant |
| GWAS Catalog | 55 unique SNPs / 110 rows |
| ClinVar | 346 records; 7 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 2379 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'JAM3'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 346 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 20 traits by best p-value, aggregated from 22 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9BX67 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000166086/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/JAM3 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/JAM3 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=JAM3%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/JAM3 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:20:21  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
