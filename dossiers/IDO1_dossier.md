# Protein Dossier — IDO1 (Indoleamine 2,3-dioxygenase 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: uterine fibroids | -0.311 | 0.117 | 0.0081 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: vaginal prolapse or uterine prolapse | 0.285 | 0.108 | 0.00858 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I83 Varicose veins of lower extremities | 0.154 | 0.063 | 0.0145 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: small intestine or small bowel cancer | 0.661 | 0.28 | 0.0181 | Wald ratio | 1 | cis | NA |
| Subjective well being | 0.028 | 0.012 | 0.0196 | Wald ratio | 1 | cis | NA |
| Height | 0.0284 | 0.0136 | 0.0368 | Wald ratio | 1 | cis | NA |
| Coronary heart disease | -0.0895 | 0.0435 | 0.0395 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N40 Hyperplasia of prostate | -0.294 | 0.15 | 0.0504 | Wald ratio | 1 | cis | NA |
| Fasting insulin | -0.0288 | 0.0152 | 0.0581 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N81 Female genital prolapse | 0.142 | 0.0764 | 0.0635 | Wald ratio | 1 | cis | NA |
| Fracture resulting from simple fall | -0.0523 | 0.029 | 0.0712 | Wald ratio | 1 | cis | NA |
| Age at menarche | -0.048 | 0.0268 | 0.073 | Wald ratio | 1 | cis | NA |
| _...and 77 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_8 association rows across 8 traits (6 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Indoleamine 2,3-dioxygenase 1 levels (IDO1.9759.13.3) | 3e-20 | rs7010461 | 1 | GCST90241490 | no MR -> candidate analysis |
| IDO1 protein levels | 2e-16 | rs146413896 | 1 | GCST90469506 | no MR -> candidate analysis |
| Quinolinate levels | 4e-13 | rs7000868 | 1 | GCST90103166 | no MR -> candidate analysis |
| Kynurenine levels | 5e-13 | rs62512638 | 1 | GCST90103029 | no MR -> candidate analysis |
| Facial morphology (D332) | 8e-10 | rs59547557 | 1 | GCST90302914 | no MR -> candidate analysis |
| Caproate (6:0) levels | 4e-8 | rs561468024 | 1 | GCST90245132 | no MR -> candidate analysis |
| Vaginal microbiome MetaCyc pathway (PWY-6708|ubiquinol-8 bio | 6e-7 | rs79183354 | 1 | GCST90026888 | no MR -> candidate analysis |
| Vaginal microbiome MetaCyc pathway (UBISYN-PWY|superpathway  | 9e-6 | rs79183354 | 1 | GCST90026980 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1153 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| stomach disorder | 0.438 | — | common-variant locus | no MR -> candidate analysis |
| facial morphology | 0.319 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 2 known modulators (Indoleamine 2,3-dioxygenase 1) |
| gnomAD constraint | pLI=1.9e-11, LOEUF=1.2 — LoF-tolerant |
| GWAS Catalog | 23 unique SNPs / 46 rows |
| ClinVar | 136 records; 3 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 1 clinical annotations across 2 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1153 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'IDO1' and resolved to 'Indoleamine 2,3-dioxygenase 1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 136 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 8 of 8 traits by best p-value, aggregated from 8 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P14902 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000131203/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4685/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/IDO1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/IDO1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=IDO1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=IDO1 — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/IDO1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:05:32  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
