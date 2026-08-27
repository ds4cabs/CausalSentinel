# Protein Dossier — C1QTNF1 (Complement C1q tumor necrosis factor-related protein 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Age at menarche | -0.0722 | 0.0223 | 0.0012 | Inverse variance weighted | 2 | trans | NA |
| Age at menarche | -0.0722 | 0.0223 | 0.0012 | Inverse variance weighted | 2 | trans | NA |
| Parkinson's disease | -0.673 | 0.231 | 0.00352 | Wald ratio | 1 | trans | NA |
| Amyotrophic lateral sclerosis | -0.168 | 0.0619 | 0.00666 | Inverse variance weighted | 2 | trans | NA |
| Amyotrophic lateral sclerosis | -0.168 | 0.0619 | 0.00666 | Inverse variance weighted | 2 | trans | NA |
| Serum cystatin C (eGFRcys) | 0.0202 | 0.00748 | 0.00694 | Inverse variance weighted | 2 | trans | NA |
| Serum cystatin C (eGFRcys) | 0.0202 | 0.00748 | 0.00694 | Inverse variance weighted | 2 | trans | NA |
| Body mass index (BMI) | -0.0229 | 0.00849 | 0.00697 | Inverse variance weighted | 2 | trans | NA |
| Body mass index (BMI) | -0.0229 | 0.00849 | 0.00697 | Inverse variance weighted | 2 | trans | NA |
| Years of schooling | 0.036 | 0.0148 | 0.0147 | Inverse variance weighted | 2 | trans | NA |
| Years of schooling | 0.036 | 0.0148 | 0.0147 | Inverse variance weighted | 2 | trans | NA |
| Potassium in urine | 0.0205 | 0.00862 | 0.0173 | Inverse variance weighted | 2 | trans | NA |
| _...and 170 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_21 association rows across 11 traits (20 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| C1QTNF1 protein levels | 1e-300 | rs116539064 | 3 | GCST90468488 | no MR -> candidate analysis |
| Circulating C1QTNF1 levels | 5e-240 | rs62063350 | 4 | GCST90860498 | no MR -> candidate analysis |
| Bone mineral density mean | 4e-86 | rs138903370 | 1 | GCST90321120 | no MR -> candidate analysis |
| COL4A1 protein levels | 7e-80 | rs116539064 | 2 | GCST90468818 | no MR -> candidate analysis |
| Cerebrospinal fluid protein C1QTNF1 levels | 1e-63 | rs4789912 | 1 | GCST90944953 | no MR -> candidate analysis |
| Circulating COL4A1 levels | 1e-56 | rs62076468 | 2 | GCST90860524 | no MR -> candidate analysis |
| Height | 1e-28 | rs15538 | 2 | GCST90245848 | no MR -> candidate analysis |
| COL18A1 protein levels | 2e-20 | rs116539064 | 2 | GCST90468812 | no MR -> candidate analysis |
| Circulating COL18A1 levels | 3e-15 | rs61436076 | 2 | GCST90860468 | no MR -> candidate analysis |
| LGALS3BP protein levels | 2e-13 | rs147385581 | 1 | GCST90469760 | no MR -> candidate analysis |
| Drusen volume within a central 5 mm circle (model 2) | 9e-6 | rs62063772 | 1 | GCST90132239 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=9.1e-07, LOEUF=1.13 — LoF-tolerant |
| GWAS Catalog | 59 unique SNPs / 118 rows |
| ClinVar | 78 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 453 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'C1QTNF1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 78 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 11 of 11 traits by best p-value, aggregated from 21 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9BXJ1 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000173918/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/C1QTNF1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/C1QTNF1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=C1QTNF1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/C1QTNF1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:20:37  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
