# Protein Dossier — KLK12 (Kallikrein-12)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Neo-extraversion | 0.286 | 0.119 | 0.0164 | Wald ratio | 1 | cis | NA |
| Myocardial infarction | 0.043 | 0.0184 | 0.0193 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K57 Diverticular disease of intestine | -0.0677 | 0.0291 | 0.0202 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M16 Coxarthrosis [arthrosis of hip] | -0.0767 | 0.0348 | 0.0276 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: muscle or soft tissue injuries | -0.109 | 0.0511 | 0.0334 | Wald ratio | 1 | cis | NA |
| Microalbuminuria | -0.0772 | 0.0365 | 0.0348 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M54 Dorsalgia | 0.0568 | 0.0284 | 0.0455 | Wald ratio | 1 | cis | NA |
| Iron | 0.0314 | 0.0158 | 0.0474 | Wald ratio | 1 | cis | NA |
| Hearing difficulty or problems: Yes | -0.0133 | 0.00677 | 0.0495 | Wald ratio | 1 | cis | NA |
| Sleep duration | -0.00589 | 0.00302 | 0.051 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N81 Female genital prolapse | 0.0589 | 0.0305 | 0.0533 | Wald ratio | 1 | cis | NA |
| Packed cell volume | 0.0532 | 0.0276 | 0.054 | Wald ratio | 1 | cis | NA |
| _...and 96 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3199_54_2` | kallikrein 12 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_50 association rows across 20 traits (48 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating KLK12 levels | 2e-7562 | rs3745540 | 7 | GCST90860580 | no MR -> candidate analysis |
| Circulating KLK13 levels | 3e-1112 | rs3760739 | 2 | GCST90860002 | no MR -> candidate analysis |
| Kallikrein-12 levels | 6e-212 | rs3745540 | 7 | GCST90161667 | no MR -> candidate analysis |
| Kallikrein-13 levels | 3e-189 | rs2569459 | 3 | GCST90248158 | no MR -> candidate analysis |
| KLK12 protein levels | 2e-182 | rs77342236 | 9 | GCST90469698 | no MR -> candidate analysis |
| KLK10 protein levels | 6e-102 | rs35996455 | 3 | GCST90469696 | no MR -> candidate analysis |
| Circulating KLK10 levels | 8e-101 | rs3760744 | 1 | GCST90860356 | no MR -> candidate analysis |
| KLK14 protein levels | 2e-96 | rs2569459 | 2 | GCST90469700 | no MR -> candidate analysis |
| Serum levels of protein KLK13 | 1e-79 | rs2569459 | 2 | GCST90086572 | no MR -> candidate analysis |
| Blood protein levels | 4e-54 | rs3760739 | 2 | GCST006585 | no MR -> candidate analysis |
| Circulating KLK14 levels | 1e-44 | rs8103083 | 1 | GCST90860034 | no MR -> candidate analysis |
| Kallikrein-12 levels (KLK12.3199.54.2) | 3e-34 | rs3745540 | 1 | GCST90241671 | no MR -> candidate analysis |
| _...and 8 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Kallikrein-12) |
| gnomAD constraint | pLI=1.9e-09, LOEUF=1.63 — LoF-tolerant |
| GWAS Catalog | 190 unique SNPs / 466 rows |
| ClinVar | 76 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 84 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'KLK12' and resolved to 'Kallikrein-12' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 76 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 20 traits by best p-value, aggregated from 50 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9UKR0 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000186474/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4943/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/KLK12 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/KLK12 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=KLK12%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/KLK12 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:23:26  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
