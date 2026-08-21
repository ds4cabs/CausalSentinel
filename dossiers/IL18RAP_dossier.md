# Protein Dossier — IL18RAP (Interleukin-18 receptor accessory protein)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: G56 Mononeuropathies of upper limb | 0.119 | 0.0363 | 0.00105 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: muscle or soft tissue injuries | 0.156 | 0.0544 | 0.0042 | Wald ratio | 1 | cis | NA |
| Urate | 0.0309 | 0.0119 | 0.0097 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: J33 Nasal polyp | -0.249 | 0.101 | 0.0139 | Wald ratio | 1 | cis | NA |
| Chronic kidney disease | 0.0803 | 0.033 | 0.0148 | Wald ratio | 1 | cis | NA |
| Percent emphysema | 0.0513 | 0.0229 | 0.0249 | Wald ratio | 1 | cis | NA |
| Coronary heart disease | 0.05 | 0.0224 | 0.0255 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hayfever or allergic rhinitis | -0.0508 | 0.0232 | 0.0288 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M16 Coxarthrosis [arthrosis of hip] | -0.109 | 0.0499 | 0.029 | Wald ratio | 1 | cis | NA |
| Serum creatinine (eGFRcrea) | -0.00412 | 0.0019 | 0.0297 | Wald ratio | 1 | cis | NA |
| Childhood intelligence | -0.0626 | 0.0288 | 0.0299 | Wald ratio | 1 | cis | NA |
| Platelet count | 1.82 | 0.887 | 0.0406 | Wald ratio | 1 | cis | NA |
| _...and 96 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2993_1_2` | IL-18 Rb | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_83 association rows across 47 traits (78 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Interleukin-18 receptor 1 levels (IL18R1.3446.7.2) | 1e-273 | rs1420106 | 1 | GCST90241607 | no MR -> candidate analysis |
| IL1RL1 protein levels | 7e-218 | rs115725744 | 4 | GCST90469574 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 3e-213 | rs4479442 | 1 | GCST90838669 | no MR -> candidate analysis |
| interleukin-18 receptor 1 levels | 1e-133 | rs1807782 | 1 | GCST90161790 | no MR -> candidate analysis |
| Atopic dermatitis | 2e-100 | rs2272128 | 9 | GCST90244787 | no MR -> candidate analysis |
| Interleukin-1 receptor-like 1 levels | 7e-98 | rs397868590 | 3 | GCST90248051 | no MR -> candidate analysis |
| IL18R1 protein levels | 5e-50 | rs181156130 | 9 | GCST90469565 | no MR -> candidate analysis |
| Interleukin-18 receptor accessory protein levels | 1e-40 | rs6748390 | 3 | GCST90137708 | no MR -> candidate analysis |
| Asthma or irritable bowel syndrome (MTAG) | 2e-37 | rs3755265 | 1 | GCST90570612 | no MR -> candidate analysis |
| ST2 levels | 9e-36 | rs11465729 | 1 | GCST90274911 | no MR -> candidate analysis |
| Lymphocyte count | 4e-32 | rs6755786 | 6 | GCST90002316 | no MR -> candidate analysis |
| Eosinophil count | 5e-32 | rs34020101 | 2 | GCST004606 | no MR -> candidate analysis |
| _...and 35 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 525 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| asthma | 0.766 | — | common-variant locus | no MR -> candidate analysis |
| atopic eczema | 0.71 | — | common-variant locus | no MR -> candidate analysis |
| inflammatory bowel disease | 0.679 | — | common-variant locus | MR: beta=0.0269, p=0.237 (cis) |
| Ascending aortic dissection | 0.684 | — | established (curated) | no MR -> candidate analysis |
| Crohn disease | 0.668 | — | common-variant locus | no MR -> candidate analysis |
| chronic rhinosinusitis | 0.629 | — | common-variant locus | no MR -> candidate analysis |
| ulcerative colitis | 0.545 | — | common-variant locus | MR: beta=0.0386, p=0.176 (cis) |
| Eczematoid dermatitis | 0.529 | — | common-variant locus | no MR -> candidate analysis |
| skin disorder | 0.511 | — | common-variant locus | no MR -> candidate analysis |
| celiac disease | 0.476 | — | common-variant locus | no MR -> candidate analysis |
| dermatitis | 0.457 | — | common-variant locus | no MR -> candidate analysis |
| lichen planus | 0.415 | — | common-variant locus | no MR -> candidate analysis |
| seborrheic keratosis | 0.409 | — | common-variant locus | no MR -> candidate analysis |
| allergic rhinitis | 0.364 | — | common-variant locus | MR: beta=-0.0508, p=0.0288 (cis) |
| atopic conjunctivitis | 0.334 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **12 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 1 known modulators (IL18 Receptor) |
| gnomAD constraint | pLI=3.9e-08, LOEUF=0.838 — LoF-tolerant |
| GWAS Catalog | 159 unique SNPs / 456 rows |
| ClinVar | 104 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 525 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'IL18RAP' and resolved to 'IL18 Receptor' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 104 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 47 traits by best p-value, aggregated from 83 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O95256 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000115607/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4804253/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/IL18RAP — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/IL18RAP — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=IL18RAP%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/IL18RAP — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:13:19  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
