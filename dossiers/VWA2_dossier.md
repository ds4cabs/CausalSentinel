# Protein Dossier — VWA2 (von Willebrand factor A domain-containing protein 2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Pallidum volume | -30.3 | 7.83 | 1.10e-04 | Wald ratio | 1 | cis | NA |
| Weight | 0.0297 | 0.00811 | 2.47e-04 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Wrist | 0.177 | 0.0551 | 0.00134 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | 0.0293 | 0.00919 | 0.00143 | Wald ratio | 1 | cis | NA |
| Hearing difficulty or problems: Yes | 0.0395 | 0.0152 | 0.00962 | Wald ratio | 1 | cis | NA |
| Parkinson's disease | -0.392 | 0.154 | 0.0109 | Wald ratio | 1 | cis | NA |
| Birth weight | 0.0353 | 0.0144 | 0.0142 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Injury or trauma resulting in loss of vision | 0.226 | 0.0967 | 0.0193 | Wald ratio | 1 | cis | NA |
| Neuroticism | -0.0255 | 0.0116 | 0.0278 | Wald ratio | 1 | cis | NA |
| Transferrin | -0.0838 | 0.0385 | 0.0297 | Wald ratio | 1 | cis | NA |
| Putamen volume | -52 | 24.7 | 0.0353 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M72 Fibroblastic disorders | 0.207 | 0.103 | 0.0442 | Wald ratio | 1 | cis | NA |
| _...and 99 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_16 association rows across 8 traits (14 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Serum levels of protein VWA2 | 6e-39 | rs597371 | 3 | GCST90089677 | no MR -> candidate analysis |
| von Willebrand factor A domain-containing protein 2 levels | 4e-35 | rs12572135 | 4 | GCST90426925 | no MR -> candidate analysis |
| Lymphocyte count | 5e-18 | rs66518778 | 2 | GCST90002316 | no MR -> candidate analysis |
| Free Cholesterol to Cholesteryl Esters in Small HDL ratio | 5e-12 | rs11816667 | 1 | GCST90827928 | no MR -> candidate analysis |
| Monocyte count | 3e-11 | rs138243320 | 2 | GCST90002340 | no MR -> candidate analysis |
| Body mass index | 6e-10 | rs9664945 | 2 | GCST90255621 | MR: beta=0.0293, p=0.00143 (cis) |
| Height | 1e-8 | rs10885543 | 1 | GCST90245848 | MR: beta=0.0155, p=0.163 (cis) |
| Oligodendroglioma | 9e-6 | rs9665610 | 1 | GCST90296472 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 60 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| ocular hypotension | 0.465 | — | common-variant locus | no MR -> candidate analysis |
| placenta praevia | 0.465 | — | common-variant locus | no MR -> candidate analysis |
| vesicoureteral reflux | 0.426 | — | established (curated) | no MR -> candidate analysis |
| streptococcal infection | 0.395 | — | common-variant locus | no MR -> candidate analysis |
| hypertensive disorder | 0.2 | — | common-variant locus | no MR -> candidate analysis |
| prostate carcinoma | 0.169 | — | common-variant locus | no MR -> candidate analysis |
| essential hypertension | 0.144 | — | common-variant locus | no MR -> candidate analysis |
| insomnia | 0.076 | — | common-variant locus | no MR -> candidate analysis |
| neuroendocrine neoplasm | 0.051 | — | common-variant locus | no MR -> candidate analysis |
| cardiovascular disorder | 0.045 | — | common-variant locus | no MR -> candidate analysis |
| lysosomal lipid storage disorder | 0.042 | — | common-variant locus | no MR -> candidate analysis |
| peripheral vascular disease | 0.04 | — | common-variant locus | no MR -> candidate analysis |
| Hirsutism | 0.039 | — | common-variant locus | no MR -> candidate analysis |

> Of the 13 rows above, **13 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Integrator complex subunit 6) |
| gnomAD constraint | pLI=3.9e-26, LOEUF=1.26 — LoF-tolerant |
| GWAS Catalog | 49 unique SNPs / 103 rows |
| ClinVar | 106 records; 3 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 60 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'VWA2' and resolved to 'Integrator complex subunit 6' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 106 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 8 of 8 traits by best p-value, aggregated from 16 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q5GFL6 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000165816/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL5724659/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/VWA2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/VWA2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=VWA2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/VWA2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:36:36  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
