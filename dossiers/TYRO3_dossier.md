# Protein Dossier — TYRO3 (Tyrosine-protein kinase receptor TYRO3)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diastolic blood pressure  automated reading | 0.079 | 0.0169 | 3.03e-06 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | 0.0967 | 0.0256 | 1.58e-04 | Wald ratio | 1 | cis | NA |
| Years of schooling | -0.0932 | 0.0248 | 1.77e-04 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K80 Cholelithiasis | 0.302 | 0.0858 | 4.22e-04 | Wald ratio | 1 | cis | NA |
| Height | -0.0683 | 0.0205 | 8.58e-04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | 0.192 | 0.0609 | 0.00161 | Wald ratio | 1 | cis | NA |
| Alcohol intake frequency | 0.0678 | 0.0244 | 0.00551 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R35 Polyuria | 0.464 | 0.172 | 0.00708 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code self-reported: pulmonary embolism (with or without) dvt | 0.339 | 0.133 | 0.011 | Wald ratio | 1 | cis | NA |
| Neuroticism | 0.0621 | 0.0248 | 0.0124 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: small intestine or small bowel cancer | 0.901 | 0.37 | 0.0147 | Wald ratio | 1 | cis | NA |
| Cigarettes smoked per day | 1.33 | 0.563 | 0.0183 | Wald ratio | 1 | cis | NA |
| _...and 69 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2611_72_2` | Dtk | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_62 association rows across 50 traits (59 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating TYRO3 levels | 8e-2144 | rs8025483 | 2 | GCST90860397 | no MR -> candidate analysis |
| TYRO3 protein levels | 1e-279 | rs4924560 | 4 | GCST90470997 | no MR -> candidate analysis |
| Tyrosine-protein kinase receptor TYRO3 levels | 3e-87 | rs11639399 | 2 | GCST90179461 | no MR -> candidate analysis |
| SPESP1 protein levels | 2e-67 | rs8038764 | 1 | GCST90470720 | no MR -> candidate analysis |
| Standing height (UKB data field 50) | 3e-24 | rs8023311 | 1 | GCST90468178 | no MR -> candidate analysis |
| HDL cholesterol levels | 6e-20 | rs7170463 | 1 | GCST010242 | no MR -> candidate analysis |
| Haematocrit percentage (UKB data field 30030) | 1e-19 | rs7170463 | 1 | GCST90468073 | no MR -> candidate analysis |
| Height | 4e-19 | rs8036643 | 1 | GCST90435412 | MR: beta=-0.0683, p=8.58e-04 (cis) |
| Cholesteryl Esters in Medium HDL | 2e-17 | rs7170463 | 1 | GCST90501184 | no MR -> candidate analysis |
| Free Cholesterol in HDL | 3e-17 | rs7170463 | 1 | GCST90501114 | no MR -> candidate analysis |
| Cholesterol in Medium HDL | 3e-17 | rs7170463 | 1 | GCST90501182 | no MR -> candidate analysis |
| High density lipoprotein cholesterol levels | 1e-16 | rs7170463 | 2 | GCST90239649 | no MR -> candidate analysis |
| _...and 38 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 491 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| metabolic syndrome | 0.569 | — | common-variant locus | no MR -> candidate analysis |
| Moderate albuminuria | 0.48 | — | common-variant locus | no MR -> candidate analysis |
| chronic obstructive pulmonary disease | 0.477 | — | common-variant locus | no MR -> candidate analysis |
| cardiac arrhythmia | 0.383 | — | common-variant locus | no MR -> candidate analysis |
| intelligence | 0.287 | — | common-variant locus | no MR -> candidate analysis |
| Hereditary breast and ovarian cancer syndrome | 0.195 | — | established (curated) | no MR -> candidate analysis |
| hereditary breast ovarian cancer syndrome | 0.195 | — | established (curated) | no MR -> candidate analysis |
| 46,XX disorder of sex development | 0.182 | — | established (curated) | no MR -> candidate analysis |
| type 2 diabetes mellitus | 0.153 | — | common-variant locus | no MR -> candidate analysis |
| albuminuria | 0.113 | — | common-variant locus | no MR -> candidate analysis |

> Of the 10 rows above, **10 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Tyrosine-protein kinase receptor TYRO3) |
| gnomAD constraint | pLI=0.56, LOEUF=0.523 — LoF-tolerant |
| GWAS Catalog | 101 unique SNPs / 199 rows |
| ClinVar | 152 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 491 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'TYRO3' and resolved to 'Tyrosine-protein kinase receptor TYRO3' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 152 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 50 traits by best p-value, aggregated from 62 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q06418 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000092445/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL5314/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/TYRO3 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/TYRO3 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=TYRO3%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/TYRO3 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:31:37  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
