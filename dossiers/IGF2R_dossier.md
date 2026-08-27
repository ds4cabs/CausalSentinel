# Protein Dossier — IGF2R (Cation-independent mannose-6-phosphate receptor)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Birth length | -0.0581 | 0.0159 | 2.62e-04 | Wald ratio | 1 | cis | NA |
| Vascular or heart problems diagnosed by doctor: Angina | -0.0655 | 0.0232 | 0.00472 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: H25 Senile cataract | 0.106 | 0.0398 | 0.00772 | Wald ratio | 1 | cis | NA |
| Fasting glucose | -0.0133 | 0.00512 | 0.00909 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | 0.0101 | 0.00387 | 0.00911 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: enlarged prostate | -0.0918 | 0.0363 | 0.0115 | Wald ratio | 1 | cis | NA |
| Weight | 0.00736 | 0.00342 | 0.0314 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Glaucoma | 0.0649 | 0.0303 | 0.0325 | Wald ratio | 1 | cis | NA |
| Transferrin | -0.0364 | 0.0171 | 0.0337 | Wald ratio | 1 | cis | NA |
| Bipolar disorder | -0.0818 | 0.0387 | 0.0346 | Wald ratio | 1 | cis | NA |
| Systemic lupus erythematosus | -0.169 | 0.0799 | 0.0346 | Wald ratio | 1 | cis | NA |
| Alzheimer's disease | -0.0556 | 0.0268 | 0.038 | Wald ratio | 1 | cis | NA |
| _...and 103 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3676_15_3` | IGF-II receptor | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_600 association rows across 288 traits (582 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating IGF2R levels | 2e-806 | rs13220323 | 6 | GCST90860615 | no MR -> candidate analysis |
| Cation-independent mannose-6-phosphate receptor levels | 1e-447 | rs3777404 | 12 | GCST90247067 | no MR -> candidate analysis |
| CTSO/IGF2R protein level ratio | 1e-420 | rs12202350 | 1 | GCST90314317 | no MR -> candidate analysis |
| IGF2R protein levels | 1e-256 | rs2297364 | 7 | GCST90469526 | no MR -> candidate analysis |
| Cation-independent mannose-6-phosphate receptor levels (IGF2 | 1e-162 | rs629849 | 3 | GCST90240631 | no MR -> candidate analysis |
| Serum levels of protein IGF2R | 2e-151 | rs629849 | 3 | GCST90088485 | no MR -> candidate analysis |
| Lipoprotein (a) levels | 3e-125 | rs117727234 | 15 | GCST90019513 | no MR -> candidate analysis |
| CTSO protein levels | 6e-125 | rs76778371 | 2 | GCST90468915 | no MR -> candidate analysis |
| Circulating CTSO levels | 1e-124 | rs76778371 | 4 | GCST90860333 | no MR -> candidate analysis |
| Low density lipoprotein cholesterol levels | 1e-86 | rs2297359 | 11 | GCST90239655 | no MR -> candidate analysis |
| Blood protein levels | 6e-86 | rs629849 | 2 | GCST006585 | no MR -> candidate analysis |
| Non-HDL cholesterol levels | 6e-69 | rs78425119 | 2 | GCST90239667 | no MR -> candidate analysis |
| _...and 276 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 909 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| coronary artery disorder | 0.814 | — | common-variant locus | no MR -> candidate analysis |
| hepatocellular carcinoma | 0.508 | — | established (curated) | no MR -> candidate analysis |
| Hypercholesterolemia | 0.7 | — | common-variant locus | no MR -> candidate analysis |
| heart disorder | 0.581 | — | common-variant locus | no MR -> candidate analysis |
| angina pectoris | 0.57 | — | common-variant locus | no MR -> candidate analysis |
| myocardial infarction | 0.544 | — | common-variant locus | no MR -> candidate analysis |
| myocardial ischemia | 0.534 | — | common-variant locus | no MR -> candidate analysis |
| metabolic disease | 0.504 | — | common-variant locus | no MR -> candidate analysis |
| coronary atherosclerosis | 0.459 | — | common-variant locus | no MR -> candidate analysis |
| hypertrophic cardiomyopathy | 0.421 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.442 | — | common-variant locus | no MR -> candidate analysis |
| primary ovarian failure | 0.438 | — | established (curated) | no MR -> candidate analysis |
| hyperlipidemia | 0.371 | — | common-variant locus | no MR -> candidate analysis |
| injury | 0.365 | — | common-variant locus | MR: beta=-0.0936, p=0.386 (cis) |
| diabetic ketoacidosis | 0.342 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **14 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Cation-independent mannose-6-phosphate receptor) |
| gnomAD constraint | pLI=1, LOEUF=0.4 — LoF-INTOLERANT |
| GWAS Catalog | 207 unique SNPs / 505 rows |
| ClinVar | 428 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 909 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'IGF2R' and resolved to 'Cation-independent mannose-6-phosphate receptor' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 428 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 288 traits by best p-value, aggregated from 600 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P11717 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000197081/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3240/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/IGF2R — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/IGF2R — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=IGF2R%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/IGF2R — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:07:51  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
