# Protein Dossier — ST6GALNAC6 (Alpha-N-acetylgalactosaminide alpha-2,6-sialyltransferase 6)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Squamous cell lung cancer | 0.452 | 0.388 | 0.244 | Wald ratio | 1 | cis | NA |
| Birth weight | -0.094 | 0.0838 | 0.262 | Wald ratio | 1 | cis | NA |
| Lung adenocarcinoma | -0.209 | 0.246 | 0.395 | Wald ratio | 1 | cis | NA |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_15 association rows across 13 traits (14 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| ENG/NOTCH1 protein level ratio | 8e-61 | rs3780670 | 1 | GCST90314648 | no MR -> candidate analysis |
| Circulating SELPLG levels | 1e-55 | rs10819317 | 1 | GCST90859798 | no MR -> candidate analysis |
| SELPLG protein levels | 2e-32 | rs10819317 | 1 | GCST90470568 | no MR -> candidate analysis |
| P-selectin glycoprotein ligand 1 levels | 8e-27 | rs10819317 | 1 | GCST90012046 | no MR -> candidate analysis |
| diastolic blood pressure (DBP, mean, inv-normal transformed) | 4e-19 | rs2417060 | 1 | GCST90475255 | no MR -> candidate analysis |
| monocyte (fraction, mean, inv-norm transformed) | 2e-15 | rs73606483 | 2 | GCST90475510 | no MR -> candidate analysis |
| monocyte (fraction, minimum, inv-norm transformed) | 7e-15 | rs73606483 | 2 | GCST90475513 | no MR -> candidate analysis |
| monocyte (absolute count, minimum, inv-norm transformed) | 5e-14 | rs73606483 | 1 | GCST90475504 | no MR -> candidate analysis |
| white blood cell count (WBC, mean, inv-norm transformed) | 8e-13 | rs2417060 | 1 | GCST90480724 | no MR -> candidate analysis |
| Hematocrit | 3e-9 | rs7027357 | 1 | GCST90278634 | no MR -> candidate analysis |
| Alpha-N-acetylgalactosaminide alpha-2,6-sialyltransferase 6  | 1e-8 | rs3758330 | 1 | GCST90426991 | no MR -> candidate analysis |
| Height | 2e-8 | rs10819317 | 1 | GCST90245848 | no MR -> candidate analysis |
| _...and 1 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.0011, LOEUF=0.813 — LoF-tolerant |
| GWAS Catalog | 76 unique SNPs / 152 rows |
| ClinVar | 96 records; 3 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 32 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'ST6GALNAC6'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 96 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 13 of 13 traits by best p-value, aggregated from 15 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q969X2 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000160408/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/ST6GALNAC6 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/ST6GALNAC6 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=ST6GALNAC6%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/ST6GALNAC6 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:14:43  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
