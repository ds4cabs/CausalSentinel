# Protein Dossier — TLR4;LY96

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: hypertension | -0.00621 | 0.00226 | 0.00606 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: hypertension | -0.00621 | 0.00226 | 0.00606 | Inverse variance weighted | 2 | cis | NA |
| Non-cancer illness code  self-reported: psoriasis | 0.00151 | 0.000551 | 0.00619 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: psoriasis | 0.00151 | 0.000551 | 0.00619 | Inverse variance weighted | 2 | cis | NA |
| Systolic blood pressure  automated reading | -0.0144 | 0.00526 | 0.00632 | Inverse variance weighted | 2 | trans | NA |
| Systolic blood pressure  automated reading | -0.0144 | 0.00526 | 0.00632 | Inverse variance weighted | 2 | cis | NA |
| Cough on most days | 0.00926 | 0.0036 | 0.0101 | Inverse variance weighted | 2 | trans | NA |
| Cough on most days | 0.00926 | 0.0036 | 0.0101 | Inverse variance weighted | 2 | cis | NA |
| Total cholesterol | -0.0272 | 0.011 | 0.013 | Inverse variance weighted | 2 | trans | NA |
| Total cholesterol | -0.0272 | 0.011 | 0.013 | Inverse variance weighted | 2 | cis | NA |
| Fasting insulin | -0.0155 | 0.00627 | 0.0136 | Inverse variance weighted | 2 | trans | NA |
| Fasting insulin | -0.0155 | 0.00627 | 0.0136 | Inverse variance weighted | 2 | cis | NA |
| _...and 166 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_193 association rows across 94 traits (167 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Toll-like receptor 4:Lymphocyte antigen 96 complex levels | 2e-217 | rs117343502 | 11 | GCST90249896 | no MR -> candidate analysis |
| TLR4 protein levels | 1e-105 | rs4986790 | 3 | GCST90470880 | no MR -> candidate analysis |
| Toll-like receptor 4:Lymphocyte antigen 96 complex levels (T | 3e-70 | rs4986790 | 2 | GCST90243031 | no MR -> candidate analysis |
| LY96 protein levels | 3e-43 | rs6472812 | 2 | GCST90469823 | no MR -> candidate analysis |
| Prenylcysteine oxidase-like levels | 5e-43 | rs6472812 | 1 | GCST90426391 | no MR -> candidate analysis |
| IL27 protein levels | 1e-32 | rs4986790 | 2 | GCST90469060 | no MR -> candidate analysis |
| Circulating EBI3_IL27 levels | 2e-32 | rs117343502 | 2 | GCST90859764 | no MR -> candidate analysis |
| Telomere length (principal component 1) | 4e-29 | rs116339495 | 1 | GCST90435144 | no MR -> candidate analysis |
| Prostate-specific antigen levels | 5e-27 | rs12344353 | 3 | GCST90461907 | no MR -> candidate analysis |
| Insomnia | 9e-26 | rs4595203 | 34 | GCST90131901 | no MR -> candidate analysis |
| Depression | 1e-21 | rs913930 | 5 | GCST007342 | MR: beta=-0.000273, p=0.307 (trans) |
| Total cholesterol levels | 4e-19 | rs4385461 | 3 | GCST90239673 | no MR -> candidate analysis |
| _...and 82 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 1 known modulators (Toll-like receptor 4/MD-2) |
| gnomAD constraint | not available |
| GWAS Catalog | no mapped SNPs |
| ClinVar | no records |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`uniprot`** — No reviewed human UniProt entry for 'TLR4;LY96'.
- **`phenome`** — Could not resolve target 'TLR4;LY96'.
- **`chembl`** — ChEMBL target matched by text search on 'TLR4;LY96' and resolved to 'Toll-like receptor 4/MD-2' — confirm this is the intended target.
- **`gnomad`** — No gnomAD constraint data.
- **`gwas`** — No GWAS Catalog SNPs mapped to this gene.
- **`clinvar`** — No ClinVar records.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 94 traits by best p-value, aggregated from 193 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3038512/ — _ChEMBL_37 (released 2026-05-01)_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/TLR4;LY96 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:22:36  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
