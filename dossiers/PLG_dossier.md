# Protein Dossier — PLG (Plasminogen)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Weight | 0.0212 | 0.00609 | 5.16e-04 | Wald ratio | 1 | cis | NA |
| Coronary heart disease | -0.103 | 0.0303 | 6.29e-04 | Wald ratio | 1 | cis | NA |
| Amygdala volume | 21.8 | 7.02 | 0.00192 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: high cholesterol | -0.0589 | 0.0198 | 0.00293 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | 0.02 | 0.0069 | 0.00375 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: bone disorder | 0.288 | 0.112 | 0.01 | Wald ratio | 1 | cis | NA |
| Diastolic blood pressure  automated reading | 0.0178 | 0.00706 | 0.0117 | Wald ratio | 1 | cis | NA |
| Systolic blood pressure  automated reading | 0.0169 | 0.00705 | 0.0165 | Wald ratio | 1 | cis | NA |
| Alcohol intake frequency | -0.0239 | 0.0102 | 0.0193 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Arm | -0.196 | 0.0852 | 0.0216 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C61 Malignant neoplasm of prostate | -0.222 | 0.107 | 0.0386 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Other bones | 0.0584 | 0.0283 | 0.0392 | Wald ratio | 1 | cis | NA |
| _...and 77 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3710_49_2` | Angiostatin | Suhre K | 2019 |
| `prot-c-4150_75_2` | Plasmin | Suhre K | 2019 |
| `prot-c-4151_6_2` | Plasminogen | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_1122 association rows across 433 traits (1073 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Lipoprotein A levels (UKB data field 30790) | 1e-300 | rs76832359 | 21 | GCST90134488 | no MR -> candidate analysis |
| Lipoprotein (a) levels | 8e-285 | rs56393506 | 41 | GCST004398 | no MR -> candidate analysis |
| PLG protein levels | 2e-284 | rs4252129 | 15 | GCST90470257 | no MR -> candidate analysis |
| Cholesterol to Total Lipids in Very Large VLDL percentage | 8e-281 | rs56393506 | 2 | GCST90500518 | no MR -> candidate analysis |
| LPA protein levels | 1e-256 | rs783184 | 19 | GCST90469786 | no MR -> candidate analysis |
| Lipoprotein(a) levels adjusted for apolipoprotein(a) isoform | 2e-207 | rs186696265 | 4 | GCST004399 | no MR -> candidate analysis |
| Phospholipids to Total Lipids in Chylomicrons and Extremely  | 4e-182 | rs56393506 | 3 | GCST90501339 | no MR -> candidate analysis |
| Angiostatin levels | 2e-178 | rs537579467 | 6 | GCST90246505 | no MR -> candidate analysis |
| LDL cholesterol levels x alcohol consumption (drinkers vs no | 2e-178 | rs5014650 | 2 | GCST008079 | no MR -> candidate analysis |
| Plasminogen levels | 3e-176 | rs144981713 | 6 | GCST90249026 | no MR -> candidate analysis |
| Free Cholesterol to Total Lipids in Large VLDL percentage | 6e-148 | rs56393506 | 1 | GCST90501163 | no MR -> candidate analysis |
| Coronary artery disease | 9e-116 | rs186696265 | 11 | GCST90132314 | MR: beta=-0.103, p=6.29e-04 (cis) |
| _...and 421 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 3178 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| hypoplasminogenemia | 0.899 | — | established (curated) | no MR -> candidate analysis |
| hereditary angioedema | 0.867 | — | established (curated) | no MR -> candidate analysis |
| dysplasminogenemia | 0.745 | — | established (curated) | no MR -> candidate analysis |
| myocardial infarction | 0.751 | — | common-variant locus | MR: beta=-0.0634, p=0.0597 (cis) |
| coronary artery disorder | 0.804 | — | common-variant locus | no MR -> candidate analysis |
| atrial fibrillation | 0.779 | — | common-variant locus | MR: beta=0.0986, p=0.0972 (cis) |
| cardiovascular disorder | 0.79 | — | common-variant locus | no MR -> candidate analysis |
| Hypercholesterolemia | 0.738 | — | common-variant locus | MR: beta=-0.0589, p=0.00293 (cis) |
| hyperlipidemia | 0.704 | — | common-variant locus | no MR -> candidate analysis |
| temporal arteritis | 0.683 | — | common-variant locus | no MR -> candidate analysis |
| heart disorder | 0.672 | — | common-variant locus | no MR -> candidate analysis |
| metabolic syndrome | 0.64 | — | common-variant locus | no MR -> candidate analysis |
| metabolic disease | 0.635 | — | common-variant locus | no MR -> candidate analysis |
| abnormal chest sounds | 0.633 | — | common-variant locus | no MR -> candidate analysis |
| coronary atherosclerosis | 0.623 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **12 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 9 known modulators (Plasminogen) |
| gnomAD constraint | pLI=0.76, LOEUF=0.51 — LoF-tolerant |
| GWAS Catalog | 268 unique SNPs / 698 rows |
| ClinVar | 671 records; 3 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 3178 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'PLG' and resolved to 'Plasminogen' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 671 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 433 traits by best p-value, aggregated from 1122 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P00747 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000122194/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL1801/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PLG — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PLG — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PLG%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PLG — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:27:14  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
