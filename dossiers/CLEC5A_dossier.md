# Protein Dossier — CLEC5A (C-type lectin domain family 5 member A)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Major depressive disorder | -0.113 | 0.0604 | 0.0603 | Wald ratio | 1 | trans | NA |
| Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.0275 | 0.017 | 0.105 | Wald ratio | 1 | trans | NA |
| Rheumatoid arthritis | -0.0765 | 0.0513 | 0.136 | Wald ratio | 1 | trans | NA |
| Squamous cell lung cancer | -0.112 | 0.0809 | 0.167 | Wald ratio | 1 | trans | NA |
| Hip osteoarthritis | 0.0828 | 0.0658 | 0.208 | Wald ratio | 1 | trans | NA |
| Platelet count | 24 | 19.7 | 0.222 | Wald ratio | 1 | trans | NA |
| Invasive mucinous ovarian cancer | -0.125 | 0.103 | 0.223 | Wald ratio | 1 | trans | NA |
| ER-positive Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.0244 | 0.0204 | 0.23 | Wald ratio | 1 | trans | NA |
| Primary sclerosing cholangitis  | -0.0911 | 0.0765 | 0.234 | Wald ratio | 1 | trans | NA |
| Depressive symptoms | 0.00993 | 0.00894 | 0.267 | Wald ratio | 1 | trans | NA |
| Knee and hip osteoarthritis | 0.051 | 0.0482 | 0.29 | Wald ratio | 1 | trans | NA |
| Birth weight | -0.0101 | 0.00964 | 0.293 | Wald ratio | 1 | trans | NA |
| _...and 7 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_2 association rows across 2 traits (1 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| C-type lectin domain family 5 member A levels | 1e-15 | rs1285971 | 1 | GCST90179263 | no MR -> candidate analysis |
| Compulsion score in obsessive compulsive disorder | 4e-6 | rs1285950 | 1 | GCST009819 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.00096, LOEUF=0.948 — LoF-tolerant |
| GWAS Catalog | 37 unique SNPs / 74 rows |
| ClinVar | 79 records; 8 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 623 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CLEC5A'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 79 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 2 of 2 traits by best p-value, aggregated from 2 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9NY25 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000258227/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CLEC5A — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CLEC5A — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CLEC5A%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CLEC5A — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:53:28  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
