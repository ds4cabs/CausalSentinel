# Protein Dossier — FGF2 (Fibroblast growth factor 2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Weight | -0.0171 | 0.0039 | 1.15e-05 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: psoriasis | 0.151 | 0.0358 | 2.61e-05 | Wald ratio | 1 | cis | NA |
| ER-positive Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0494 | 0.0141 | 4.55e-04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertrophic cardiomyopathy (hcm  or  hocm) | 0.567 | 0.182 | 0.00185 | Wald ratio | 1 | cis | NA |
| Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0339 | 0.0117 | 0.00375 | Wald ratio | 1 | cis | NA |
| Caudate volume | 27 | 9.6 | 0.00492 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R35 Polyuria | 0.16 | 0.0605 | 0.0081 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: asthma | 0.0306 | 0.012 | 0.0107 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hayfever or allergic rhinitis | 0.04 | 0.0174 | 0.0218 | Wald ratio | 1 | cis | NA |
| Low grade serous ovarian cancer | -0.203 | 0.0907 | 0.0255 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: kidney stone or ureter stone or bladder stone | 0.101 | 0.0452 | 0.026 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | -0.00976 | 0.00441 | 0.027 | Wald ratio | 1 | cis | NA |
| _...and 71 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3025_50_1` | bFGF | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_63 association rows across 29 traits (54 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating FGF2 levels (id: OID00954_OID20503) | 1e-2421 | rs2922979 | 2 | GCST90860185 | no MR -> candidate analysis |
| Circulating FGF2 levels (id: OID00770_OID20503) | 1e-2323 | rs2922979 | 2 | GCST90860105 | no MR -> candidate analysis |
| Fibroblast growth factor 2 levels | 8e-667 | rs2922979 | 5 | GCST90247583 | no MR -> candidate analysis |
| FGF2 protein levels | 9e-165 | rs41436350 | 20 | GCST90469224 | no MR -> candidate analysis |
| Height | 2e-96 | rs308412 | 4 | GCST90245848 | no MR -> candidate analysis |
| Lymphocyte count | 8e-23 | rs309375 | 4 | GCST90002316 | no MR -> candidate analysis |
| Neutrophil-to-lymphocyte ratio | 3e-19 | rs309375 | 3 | GCST90866310 | no MR -> candidate analysis |
| Lymphocyte percentage of white cells | 6e-19 | rs309375 | 1 | GCST90002389 | no MR -> candidate analysis |
| Lymphocyte percentage (UKB data field 30180) | 7e-19 | rs309375 | 1 | GCST90468083 | no MR -> candidate analysis |
| Neutrophil percentage of white cells | 3e-17 | rs309375 | 1 | GCST90002399 | no MR -> candidate analysis |
| Waist-hip ratio | 4e-17 | rs308403 | 1 | GCST007067 | no MR -> candidate analysis |
| Itch intensity from mosquito bite | 3e-13 | rs79712192 | 1 | GCST004861 | no MR -> candidate analysis |
| _...and 17 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 2488 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| atopic eczema | 0.563 | — | common-variant locus | no MR -> candidate analysis |
| stroke disorder | 0.421 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.421 | — | common-variant locus | no MR -> candidate analysis |
| vertebral column disorder | 0.384 | — | common-variant locus | no MR -> candidate analysis |
| asthma | 0.04 | — | common-variant locus | MR: beta=0.0306, p=0.0107 (cis) |

> Of the 5 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 1 known modulators (Fibroblast growth factor 2) |
| gnomAD constraint | pLI=0.00014, LOEUF=1.3 — LoF-tolerant |
| GWAS Catalog | 61 unique SNPs / 122 rows |
| ClinVar | 101 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 2 clinical annotations across 3 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 2488 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'FGF2' and resolved to 'Fibroblast growth factor 2' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 101 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 20 of 29 traits by best p-value, aggregated from 63 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P09038 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000138685/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3107/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/FGF2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/FGF2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=FGF2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=FGF2 — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/FGF2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:39:54  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
