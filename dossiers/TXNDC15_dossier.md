# Protein Dossier — TXNDC15 (Thioredoxin domain-containing protein 15)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Height | -0.0717 | 0.014 | 3.12e-07 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | -0.0474 | 0.00946 | 5.41e-07 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | -0.0378 | 0.00998 | 1.52e-04 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | 0.0421 | 0.0115 | 2.54e-04 | Wald ratio | 1 | cis | NA |
| Years of schooling | 0.0456 | 0.0163 | 0.00511 | Wald ratio | 1 | cis | NA |
| Amyotrophic lateral sclerosis | -0.209 | 0.0866 | 0.0158 | Wald ratio | 1 | cis | NA |
| Depressive symptoms | 0.0358 | 0.0163 | 0.0278 | Wald ratio | 1 | cis | NA |
| Alcohol intake frequency | 0.0373 | 0.017 | 0.0287 | Wald ratio | 1 | cis | NA |
| Sleep duration | -0.0196 | 0.00899 | 0.0294 | Wald ratio | 1 | cis | NA |
| Neuroblastoma | -0.452 | 0.214 | 0.035 | Wald ratio | 1 | cis | NA |
| Body fat | 0.0534 | 0.0254 | 0.0355 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N81 Female genital prolapse | -0.256 | 0.127 | 0.0436 | Wald ratio | 1 | cis | NA |
| _...and 90 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_9 association rows across 7 traits (7 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| TXNDC15 protein levels | 2e-66 | rs184061578 | 3 | GCST90470990 | no MR -> candidate analysis |
| Serum levels of protein TXNDC15 | 2e-26 | rs3733897 | 1 | GCST90089370 | no MR -> candidate analysis |
| Physical function (baseline) | 2e-11 | rs11950533 | 1 | GCST90565837 | no MR -> candidate analysis |
| Bioavailable testosterone levels | 4e-9 | rs3733897 | 1 | GCST90012103 | no MR -> candidate analysis |
| Parkinson's disease or first degree relation to individual w | 7e-9 | rs11950533 | 1 | GCST009325 | no MR -> candidate analysis |
| Congenital solitary functioning kidney | 6e-8 | rs73282857 | 1 | GCST90244792 | no MR -> candidate analysis |
| Type 2 diabetes | 2e-6 | rs319598 | 1 | GCST002352 | MR: beta=0.0645, p=0.187 (cis) |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 82 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| meckel syndrome 14 | 0.817 | — | established (curated) | no MR -> candidate analysis |
| Meckel syndrome | 0.702 | — | established (curated) | no MR -> candidate analysis |
| hereditary disease | 0.316 | — | established (curated) | no MR -> candidate analysis |
| severe combined immunodeficiency, autosomal recessive, T cell-negative, B cell-negative, NK cell-positive | 0.195 | — | established (curated) | no MR -> candidate analysis |

> Of the 4 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=3.2e-06, LOEUF=0.963 — LoF-tolerant |
| GWAS Catalog | 37 unique SNPs / 74 rows |
| ClinVar | 111 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 82 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'TXNDC15'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 111 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 7 of 7 traits by best p-value, aggregated from 9 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q96J42 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000113621/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/TXNDC15 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/TXNDC15 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=TXNDC15%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/TXNDC15 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:30:19  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
