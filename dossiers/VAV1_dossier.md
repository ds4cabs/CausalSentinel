# Protein Dossier — VAV1 (Proto-oncogene vav)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Alzheimer's disease | -0.342 | 0.114 | 0.00268 | Wald ratio | 1 | cis | NA |
| Red blood cell count | -0.0355 | 0.0138 | 0.00988 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I83 Varicose veins of lower extremities | 0.211 | 0.082 | 0.0102 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I30 Acute pericarditis | 0.939 | 0.376 | 0.0125 | Wald ratio | 1 | cis | NA |
| Nucleus accumbens volume | 16.2 | 6.56 | 0.0135 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: psoriasis | -0.704 | 0.306 | 0.0212 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: retinal detachment | 0.397 | 0.175 | 0.0234 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: L03 Cellulitis | 0.276 | 0.124 | 0.0256 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | -0.058 | 0.026 | 0.0258 | Wald ratio | 1 | cis | NA |
| Neo-agreeableness | 0.825 | 0.372 | 0.0265 | Wald ratio | 1 | cis | NA |
| Mean cell haemoglobin concentration | -0.0455 | 0.0209 | 0.0299 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertrophic cardiomyopathy (hcm  or  hocm) | 1.01 | 0.464 | 0.0302 | Wald ratio | 1 | cis | NA |
| _...and 79 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_54 association rows across 27 traits (50 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Mean platelet thrombocyte volume (UKB data field 30100) | 6e-75 | rs8106212 | 2 | GCST90468087 | no MR -> candidate analysis |
| mean platelet volume (MPV, mean, inv-norm transformed) | 6e-69 | rs8106212 | 3 | GCST90479708 | no MR -> candidate analysis |
| mean platelet volume (MPV, maximum, inv-norm transformed) | 5e-66 | rs8106212 | 3 | GCST90479707 | no MR -> candidate analysis |
| platelet count (mean, inv-norm transformed) | 8e-61 | rs8106212 | 3 | GCST90480651 | no MR -> candidate analysis |
| mean platelet volume (MPV, minimum, inv-norm transformed) | 7e-60 | rs8106212 | 3 | GCST90479709 | no MR -> candidate analysis |
| Mean platelet volume | 2e-57 | rs8106212 | 6 | GCST90002349 | MR: beta=0.00551, p=0.49 (cis) |
| platelet count (minimum, inv-norm transformed) | 1e-53 | rs8106212 | 3 | GCST90480652 | no MR -> candidate analysis |
| Platelet distribution width (UKB data field 30110) | 6e-51 | rs8106212 | 2 | GCST90468097 | no MR -> candidate analysis |
| platelet count (maximum, inv-norm transformed) | 2e-47 | rs8106212 | 3 | GCST90480650 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 7e-41 | rs8106212 | 1 | GCST90838669 | no MR -> candidate analysis |
| Platelet distribution width | 7e-40 | rs8106212 | 4 | GCST90002401 | no MR -> candidate analysis |
| Platelet count | 3e-31 | rs8106212 | 6 | GCST90002361 | MR: beta=-5.05, p=0.0696 (cis) |
| _...and 15 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Proto-oncogene vav) |
| gnomAD constraint | pLI=1, LOEUF=0.344 — LoF-INTOLERANT |
| GWAS Catalog | 81 unique SNPs / 162 rows |
| ClinVar | 681 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 389 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'VAV1' and resolved to 'Proto-oncogene vav' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 681 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 27 traits by best p-value, aggregated from 54 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P15498 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000141968/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3259472/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/VAV1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/VAV1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=VAV1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/VAV1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:34:14  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
