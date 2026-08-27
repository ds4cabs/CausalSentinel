# Protein Dossier — S100A4 (Protein S100-A4)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: D25 Leiomyoma of uterus | 0.286 | 0.0762 | 1.72e-04 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: L03 Cellulitis | 0.286 | 0.0966 | 0.00309 | Wald ratio | 1 | cis | NA |
| Red blood cell count | 0.0323 | 0.0119 | 0.00659 | Wald ratio | 1 | cis | NA |
| Total cholesterol | -0.0652 | 0.0281 | 0.0205 | Wald ratio | 1 | cis | NA |
| Mean cell volume | -0.346 | 0.15 | 0.0216 | Wald ratio | 1 | cis | NA |
| Paget's disease | -0.879 | 0.397 | 0.027 | Wald ratio | 1 | cis | NA |
| PGC cross-disorder traits | -0.138 | 0.0628 | 0.0283 | Wald ratio | 1 | cis | NA |
| Mean cell haemoglobin | -0.125 | 0.0577 | 0.0304 | Wald ratio | 1 | cis | NA |
| Major depressive disorder | -0.296 | 0.14 | 0.034 | Wald ratio | 1 | cis | NA |
| Invasive mucinous ovarian cancer | -0.42 | 0.199 | 0.0346 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Wrist | 0.138 | 0.0714 | 0.0525 | Wald ratio | 1 | cis | NA |
| Systolic blood pressure  automated reading | 0.0224 | 0.0117 | 0.0552 | Wald ratio | 1 | cis | NA |
| _...and 101 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_10 association rows across 8 traits (9 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating S100A4 levels | 9e-158 | rs28594230 | 2 | GCST90860024 | no MR -> candidate analysis |
| S100A4 protein levels | 7e-155 | rs56350425 | 1 | GCST90470518 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 8e-29 | rs1810765 | 1 | GCST90838667 | no MR -> candidate analysis |
| S100A3 protein levels | 1e-27 | rs78031781 | 2 | GCST90470517 | no MR -> candidate analysis |
| Serum levels of protein S100A4 | 6e-16 | rs60969679 | 1 | GCST90087797 | no MR -> candidate analysis |
| Serum levels of protein S100A6 | 1e-12 | rs60969679 | 1 | GCST90087367 | no MR -> candidate analysis |
| Pulse pressure | 4e-8 | rs138957616 | 1 | GCST007269 | no MR -> candidate analysis |
| White blood cell count (monocyte) | 5e-8 | rs1810765 | 1 | GCST90026507 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Protein S100-A4) |
| gnomAD constraint | pLI=0.07, LOEUF=1.46 — LoF-tolerant |
| GWAS Catalog | 54 unique SNPs / 108 rows |
| ClinVar | 33 records; 7 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 617 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'S100A4' and resolved to 'Protein S100-A4' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 33 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 8 of 8 traits by best p-value, aggregated from 10 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P26447 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000196154/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2362976/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/S100A4 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/S100A4 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=S100A4%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/S100A4 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:54:50  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
