# Protein Dossier — FCGR2A;FCGR2B

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Ulcerative colitis | -0.138 | 0.0102 | 1.43e-41 | Wald ratio | 1 | cis | NA |
| Inflammatory bowel disease | -0.101 | 0.0081 | 8.51e-36 | Wald ratio | 1 | cis | NA |
| Crohn's disease | -0.0634 | 0.00979 | 9.46e-11 | Wald ratio | 1 | cis | NA |
| Rheumatoid arthritis | -0.0621 | 0.0114 | 5.67e-08 | Wald ratio | 1 | cis | NA |
| LDL cholesterol | -0.0182 | 0.00428 | 2.01e-05 | Wald ratio | 1 | cis | NA |
| Total cholesterol | -0.0177 | 0.0042 | 2.54e-05 | Wald ratio | 1 | cis | NA |
| Systemic lupus erythematosus | 0.14 | 0.0373 | 1.75e-04 | Wald ratio | 1 | cis | NA |
| Schizophrenia | 0.0296 | 0.00872 | 6.80e-04 | Wald ratio | 1 | cis | NA |
| Birth weight | 0.00961 | 0.00291 | 9.48e-04 | Wald ratio | 1 | cis | NA |
| Weight | 0.00473 | 0.00172 | 0.00597 | Wald ratio | 1 | cis | NA |
| IgA nephropathy | -0.185 | 0.0676 | 0.0062 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypopituitarism | 0.231 | 0.0846 | 0.00632 | Wald ratio | 1 | cis | NA |
| _...and 105 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_408 association rows across 240 traits (390 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Low affinity immunoglobulin gamma Fc region receptor II-a le | 7e-6401 | rs4657041 | 14 | GCST90247561 | no MR -> candidate analysis |
| Circulating FCGR2A levels | 6e-5626 | rs7529225 | 4 | GCST90860443 | no MR -> candidate analysis |
| Circulating FCGR3B levels | 2e-3176 | rs1674765 | 3 | GCST90860423 | no MR -> candidate analysis |
| Low affinity immunoglobulin gamma Fc region receptor II-a le | 1e-2102 | rs1801274 | 1 | GCST90241813 | no MR -> candidate analysis |
| FCGR2A/FCGR2B protein level ratio | 4e-1407 | rs1801274 | 1 | GCST90314793 | no MR -> candidate analysis |
| Low affinity immunoglobulin gamma Fc region receptor II-b le | 2e-769 | rs6665610 | 4 | GCST90241814 | no MR -> candidate analysis |
| Low affinity immunoglobulin gamma Fc region receptor II-b (a | 5e-616 | rs1801274 | 1 | GCST90425685 | no MR -> candidate analysis |
| Low affinity immunoglobulin gamma Fc region receptor II-b le | 4e-608 | rs7512140 | 15 | GCST90247562 | no MR -> candidate analysis |
| Blood protein levels | 6e-514 | rs7535475 | 1 | GCST006585 | no MR -> candidate analysis |
| Cerebrospinal fluid protein FCGR2B levels | 1e-412 | rs1801274 | 1 | GCST90942152 | no MR -> candidate analysis |
| CD16 on CD14- CD16+ monocyte | 7e-411 | rs56157533 | 1 | GCST90001979 | no MR -> candidate analysis |
| Circulating FCRLB levels | 2e-359 | rs61803040 | 1 | GCST90860085 | no MR -> candidate analysis |
| _...and 228 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 1 known modulators (Low affinity immunoglobulin gamma Fc region receptor II-b) |
| gnomAD constraint | not available |
| GWAS Catalog | no mapped SNPs |
| ClinVar | no records |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`uniprot`** — No reviewed human UniProt entry for 'FCGR2A;FCGR2B'.
- **`phenome`** — Could not resolve target 'FCGR2A;FCGR2B'.
- **`chembl`** — ChEMBL target matched by text search on 'FCGR2A;FCGR2B' and resolved to 'Low affinity immunoglobulin gamma Fc region receptor II-b' — confirm this is the intended target.
- **`gnomad`** — No gnomAD constraint data.
- **`gwas`** — No GWAS Catalog SNPs mapped to this gene.
- **`clinvar`** — No ClinVar records.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 240 traits by best p-value, aggregated from 408 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4662940/ — _ChEMBL_37 (released 2026-05-01)_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/FCGR2A;FCGR2B — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:37:02  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
