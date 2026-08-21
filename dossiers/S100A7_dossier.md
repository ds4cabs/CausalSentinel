# Protein Dossier — S100A7 (Protein S100-A7)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: asthma | -0.0443 | 0.014 | 0.00151 | Wald ratio | 1 | cis | NA |
| Neuroticism | -0.0232 | 0.00828 | 0.00511 | Wald ratio | 1 | cis | NA |
| Bulimia nervosa | 0.0389 | 0.0141 | 0.0057 | Wald ratio | 1 | cis | NA |
| Eczema | 0.101 | 0.0367 | 0.00589 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: psoriasis | 0.101 | 0.0406 | 0.0127 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: chronic obstructive airways disease or copd | 0.161 | 0.0699 | 0.0214 | Wald ratio | 1 | cis | NA |
| Nucleus accumbens volume | 4.86 | 2.16 | 0.0246 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: depression | 0.0418 | 0.0188 | 0.0267 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N81 Female genital prolapse | -0.0947 | 0.0439 | 0.0308 | Wald ratio | 1 | cis | NA |
| Endometrioid ovarian cancer | -0.131 | 0.0613 | 0.0327 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: joint disorder | 0.129 | 0.0614 | 0.0353 | Wald ratio | 1 | cis | NA |
| Creatinine (enzymatic) in urine | 0.00919 | 0.00456 | 0.0439 | Wald ratio | 1 | cis | NA |
| _...and 64 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_10 association rows across 8 traits (8 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Protein S100-A7 levels | 6e-1077 | rs3014837 | 2 | GCST90249409 | no MR -> candidate analysis |
| IL6R protein levels | 6e-66 | rs4418538 | 2 | GCST90469602 | no MR -> candidate analysis |
| PGLYRP4 protein levels | 2e-21 | rs12132927 | 1 | GCST90470221 | no MR -> candidate analysis |
| S100A13 protein levels | 5e-14 | rs61804048 | 1 | GCST90470514 | no MR -> candidate analysis |
| HDL cholesterol levels x short total sleep time interaction  | 7e-10 | rs6672390 | 1 | GCST009367 | no MR -> candidate analysis |
| Gut microbial network clusters (BlueViolet (at 3 months) x H | 7e-10 | rs56074066 | 1 | GCST90569241 | no MR -> candidate analysis |
| Gut microbial network clusters (BlueViolet (at 3 months) x H | 3e-7 | rs56074066 | 1 | GCST90569242 | no MR -> candidate analysis |
| Obsessive-compulsive disorder | 1e-6 | rs28696717 | 1 | GCST007208 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.2, LOEUF=1.67 — LoF-tolerant |
| GWAS Catalog | 49 unique SNPs / 98 rows |
| ClinVar | 39 records; 5 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 355 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'S100A7'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 39 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 8 of 8 traits by best p-value, aggregated from 10 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P31151 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000143556/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/S100A7 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/S100A7 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=S100A7%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/S100A7 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:55:21  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
