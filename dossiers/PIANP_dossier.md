# Protein Dossier — PIANP (PILR alpha-associated neural protein)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Neuroticism | 0.0265 | 0.0177 | 0.134 | Wald ratio | 1 | cis | NA |
| Coronary heart disease | -0.113 | 0.0787 | 0.153 | Wald ratio | 1 | cis | NA |
| Amyotrophic lateral sclerosis | 0.126 | 0.0981 | 0.201 | Wald ratio | 1 | cis | NA |
| Depressive symptoms | 0.0221 | 0.0177 | 0.211 | Wald ratio | 1 | cis | NA |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_6 association rows across 4 traits (6 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| PILR alpha-associated neural protein levels | 1e-22 | rs11064321 | 2 | GCST90249001 | no MR -> candidate analysis |
| CD4 protein levels | 1e-21 | rs2091780 | 1 | GCST90468636 | no MR -> candidate analysis |
| PILR alpha-associated neural protein levels (PIANP.9599.6.3) | 5e-17 | rs11064321 | 2 | GCST90242266 | no MR -> candidate analysis |
| Bone mineral density mean | 4e-9 | rs73049715 | 1 | GCST90321120 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.031, LOEUF=0.758 — LoF-tolerant |
| GWAS Catalog | 74 unique SNPs / 148 rows |
| ClinVar | 99 records; 5 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 39 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'PIANP'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 99 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 4 of 4 traits by best p-value, aggregated from 6 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q8IYJ0 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000139200/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PIANP — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PIANP — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PIANP%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PIANP — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:19:59  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
