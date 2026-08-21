# Protein Dossier — SPINT1 (Kunitz-type protease inhibitor 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Thyroid cancer | -1.23 | 0.237 | 2.37e-07 | Wald ratio | 1 | trans | 0.99 |
| Age at menopause | 0.282 | 0.0564 | 5.73e-07 | Wald ratio | 1 | trans | NA |
| Happiness | -0.0247 | 0.00841 | 0.00326 | Wald ratio | 1 | trans | NA |
| Heel bone mineral density (BMD) T-score  automated | -0.0231 | 0.0088 | 0.00863 | Wald ratio | 1 | trans | NA |
| Glioma | -0.316 | 0.125 | 0.0114 | Wald ratio | 1 | trans | NA |
| Height | 0.0192 | 0.00819 | 0.019 | Wald ratio | 1 | trans | NA |
| Putamen volume | -38.3 | 16.6 | 0.0207 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: C50 Malignant neoplasm of breast | 0.106 | 0.0479 | 0.0272 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: R10 Abdominal and pelvic pain | 0.0652 | 0.0308 | 0.0341 | Wald ratio | 1 | trans | NA |
| Amyotrophic lateral sclerosis | -0.1 | 0.0502 | 0.0461 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: M16 Coxarthrosis [arthrosis of hip] | 0.102 | 0.0512 | 0.0476 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: enlarged prostate | 0.103 | 0.0526 | 0.0501 | Wald ratio | 1 | trans | NA |
| _...and 96 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2828_82_2` | HAI-1 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_33 association rows across 19 traits (31 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating SPINT1 levels | 4e-517 | rs17658212 | 4 | GCST90860652 | no MR -> candidate analysis |
| CDSN protein levels | 5e-139 | rs17658212 | 3 | GCST90468688 | no MR -> candidate analysis |
| Circulating CDSN levels | 9e-114 | rs17658212 | 3 | GCST90860191 | no MR -> candidate analysis |
| PSAPL1 protein levels | 3e-96 | rs17658212 | 3 | GCST90470350 | no MR -> candidate analysis |
| Kunitz-type protease inhibitor 1 levels | 2e-84 | rs10220885 | 4 | GCST90137690 | no MR -> candidate analysis |
| Kunitz-type protease inhibitor 1 level in Chronic kidney dis | 4e-66 | rs12323939 | 1 | GCST90237108 | no MR -> candidate analysis |
| SPINT1 protein levels | 2e-38 | rs117454282 | 2 | GCST90470727 | no MR -> candidate analysis |
| PYDC1 protein levels | 3e-33 | rs17658212 | 1 | GCST90470397 | no MR -> candidate analysis |
| Cerebrospinal fluid protein SPINT1 levels | 6e-26 | rs17658212 | 1 | GCST90944902 | no MR -> candidate analysis |
| DnaJ homolog subfamily C member 17 levels (DNAJC17.14655.1.3 | 6e-19 | rs11549914 | 1 | GCST90240958 | no MR -> candidate analysis |
| Serum levels of protein SPINT1 | 2e-17 | rs17658212 | 1 | GCST90088089 | no MR -> candidate analysis |
| LGALS7 or LGALS7B protein levels | 4e-16 | rs17658212 | 1 | GCST90469763 | no MR -> candidate analysis |
| _...and 7 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Protein cereblon/Kunitz-type protease inhibitor 1) |
| gnomAD constraint | pLI=1.3e-09, LOEUF=0.927 — LoF-tolerant |
| GWAS Catalog | 49 unique SNPs / 98 rows |
| ClinVar | 125 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 180 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'SPINT1' and resolved to 'Protein cereblon/Kunitz-type protease inhibitor 1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 125 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 19 of 19 traits by best p-value, aggregated from 33 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O43278 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000166145/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4742262/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/SPINT1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/SPINT1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=SPINT1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/SPINT1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:12:37  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
