# Protein Dossier — EPHB6 (Ephrin type-B receptor 6)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Heel bone mineral density (BMD) T-score  automated | 0.0501 | 0.0149 | 7.48e-04 | Wald ratio | 1 | cis | NA |
| Lumbar spine bone mineral density | 0.11 | 0.0414 | 0.00779 | Wald ratio | 1 | cis | NA |
| Sodium in urine | -0.0282 | 0.0113 | 0.0124 | Wald ratio | 1 | cis | NA |
| Neuroticism | -0.0377 | 0.0167 | 0.0244 | Wald ratio | 1 | cis | NA |
| Endometrioid ovarian cancer | -0.298 | 0.138 | 0.0309 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M54 Dorsalgia | -0.244 | 0.116 | 0.0345 | Wald ratio | 1 | cis | NA |
| Thalamus volume | 64.6 | 30.7 | 0.0352 | Wald ratio | 1 | cis | NA |
| Alzheimer's disease | 0.159 | 0.0766 | 0.0384 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | 0.0237 | 0.0115 | 0.0389 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Injury or trauma resulting in loss of vision | 0.219 | 0.123 | 0.0748 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: osteoporosis | -0.197 | 0.114 | 0.0839 | Wald ratio | 1 | cis | NA |
| Coronary heart disease | 0.0797 | 0.0462 | 0.0847 | Wald ratio | 1 | cis | NA |
| _...and 65 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5078_82_3` | EphB6 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_23 association rows across 16 traits (19 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating EPHB6 levels | 2e-463 | rs7789303 | 2 | GCST90859677 | no MR -> candidate analysis |
| EPHB4/EPHB6 protein level ratio | 3e-316 | rs6464534 | 1 | GCST90314678 | no MR -> candidate analysis |
| EPHB6/LAYN protein level ratio | 4e-312 | rs6464534 | 1 | GCST90314681 | no MR -> candidate analysis |
| EFNA4/EPHB6 protein level ratio | 1e-286 | rs6464534 | 1 | GCST90314600 | no MR -> candidate analysis |
| Ephrin type-B receptor 6 levels | 5e-138 | rs7789303 | 4 | GCST90247482 | no MR -> candidate analysis |
| Serum levels of protein EPHB6 | 7e-38 | rs7789303 | 2 | GCST90088905 | no MR -> candidate analysis |
| Ephrin type-B receptor 6 levels (EPHB6.5078.82.3) | 2e-32 | rs7789303 | 1 | GCST90241075 | no MR -> candidate analysis |
| Blood protein levels | 6e-20 | rs7789303 | 2 | GCST006585 | no MR -> candidate analysis |
| Trypsin-2 levels (PRSS2.5034.79.1) | 4e-15 | rs62473589 | 1 | GCST90243126 | no MR -> candidate analysis |
| EPHB6 protein levels | 3e-12 | rs766323 | 1 | GCST90469133 | no MR -> candidate analysis |
| Height | 1e-9 | rs9986701 | 1 | GCST90245848 | no MR -> candidate analysis |
| Total PHF-tau (SNP x SNP interaction) | 1e-9 | rs2040375 x rs4487417 | 1 | GCST010340 | no MR -> candidate analysis |
| _...and 4 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Ephrin type-B receptor 6) |
| gnomAD constraint | pLI=5.4e-05, LOEUF=0.602 — LoF-tolerant |
| GWAS Catalog | 96 unique SNPs / 191 rows |
| ClinVar | 228 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 175 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'EPHB6' and resolved to 'Ephrin type-B receptor 6' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 228 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 16 of 16 traits by best p-value, aggregated from 23 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O15197 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000106123/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL5836/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/EPHB6 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/EPHB6 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=EPHB6%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/EPHB6 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:27:30  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
