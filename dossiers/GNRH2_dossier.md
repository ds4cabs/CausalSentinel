# Protein Dossier — GNRH2 (Progonadoliberin-2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: polio  or  poliomyelitis | 0.843 | 0.248 | 6.67e-04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: asthma | 0.112 | 0.0351 | 0.00137 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R04 Haemorrhage from respiratory passages | 0.364 | 0.138 | 0.00859 | Wald ratio | 1 | cis | NA |
| Parkinson's disease | -0.533 | 0.233 | 0.0218 | Wald ratio | 1 | cis | NA |
| Thyroid cancer | 0.997 | 0.458 | 0.0294 | Wald ratio | 1 | cis | NA |
| Sodium in urine | -0.0292 | 0.0138 | 0.0339 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | -0.023 | 0.0115 | 0.0453 | Wald ratio | 1 | cis | NA |
| Haemoglobin concentration | -0.0699 | 0.035 | 0.0455 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: kidney stone or ureter stone or bladder stone | 0.251 | 0.126 | 0.0459 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I84 Haemorrhoids | -0.227 | 0.115 | 0.0483 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | 0.0262 | 0.014 | 0.0614 | Wald ratio | 1 | cis | NA |
| Putamen volume | -61.7 | 33.1 | 0.0618 | Wald ratio | 1 | cis | NA |
| _...and 83 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_8 association rows across 7 traits (6 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Progonadoliberin-2 levels | 2e-134 | rs8184100 | 2 | GCST90421204 | no MR -> candidate analysis |
| OXT protein levels | 8e-132 | rs6115764 | 1 | GCST90470139 | no MR -> candidate analysis |
| Serum levels of protein OXT | 2e-28 | rs6115763 | 1 | GCST90090149 | no MR -> candidate analysis |
| Oxytocin-neurophysin 1 levels | 2e-17 | rs6084240 | 1 | GCST90248810 | no MR -> candidate analysis |
| Body mass index | 3e-12 | rs676749 | 1 | GCST90255621 | MR: beta=0.0262, p=0.0614 (cis) |
| Maximum cranial width | 4e-7 | rs6115764 | 1 | GCST005940 | no MR -> candidate analysis |
| N-acetyl-beta-alanine levels in elite athletes | 7e-6 | rs8125955 | 1 | GCST90134018 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=9.3e-07, LOEUF=1.9 — LoF-tolerant |
| GWAS Catalog | 75 unique SNPs / 149 rows |
| ClinVar | 63 records; 6 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 72 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'GNRH2'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 63 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 7 of 7 traits by best p-value, aggregated from 8 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O43555 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000125787/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/GNRH2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/GNRH2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=GNRH2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/GNRH2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:51:30  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
