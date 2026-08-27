# Protein Dossier — LAMB1;LAMC1;LAMA1

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Height | 0.0408 | 0.0115 | 3.94e-04 | Inverse variance weighted | 2 | trans | NA |
| Height | 0.0408 | 0.0115 | 3.94e-04 | Inverse variance weighted | 2 | trans | NA |
| Eye problems or disorders: Glaucoma | -0.177 | 0.0592 | 0.00272 | Inverse variance weighted | 2 | trans | NA |
| Eye problems or disorders: Glaucoma | -0.177 | 0.0592 | 0.00272 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: chronic obstructive airways disease or copd | 0.237 | 0.0808 | 0.00335 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: chronic obstructive airways disease or copd | 0.237 | 0.0808 | 0.00335 | Inverse variance weighted | 2 | trans | NA |
| Caudate volume | -36.6 | 12.9 | 0.00456 | Inverse variance weighted | 2 | trans | NA |
| Caudate volume | -36.6 | 12.9 | 0.00456 | Inverse variance weighted | 2 | trans | NA |
| Serum creatinine (eGFRcrea) | 0.00885 | 0.00313 | 0.00471 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: joint disorder | 0.216 | 0.0795 | 0.00654 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: joint disorder | 0.216 | 0.0795 | 0.00654 | Inverse variance weighted | 2 | trans | NA |
| Triglycerides | -0.0327 | 0.0124 | 0.00846 | Inverse variance weighted | 2 | trans | NA |
| _...and 200 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_242 association rows across 130 traits (190 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Height | 2e-175 | rs4233192 | 10 | GCST90245848 | MR: beta=0.0408, p=3.94e-04 (trans) |
| Tenascin levels | 9e-119 | rs12138049 | 1 | GCST90249798 | no MR -> candidate analysis |
| N-acetylneuraminate levels | 8e-84 | rs116448311 | 2 | GCST90245326 | no MR -> candidate analysis |
| Laminin subunit gamma-2 levels | 8e-79 | rs3754525 | 1 | GCST90248237 | no MR -> candidate analysis |
| LAMB1 protein levels | 2e-78 | rs2237687 | 5 | GCST90469732 | no MR -> candidate analysis |
| Serum levels of protein LAMC2 | 8e-45 | rs3754525 | 1 | GCST90090762 | no MR -> candidate analysis |
| Laminin levels (LAMA1.LAMB1.LAMC1.2728.62.2) | 7e-34 | rs4129858 | 1 | GCST90241737 | no MR -> candidate analysis |
| LAMA4 protein levels | 5e-32 | rs2296296 | 2 | GCST90469731 | no MR -> candidate analysis |
| Circulating LAMA4 levels | 1e-28 | rs2296296 | 3 | GCST90860668 | no MR -> candidate analysis |
| Colorectal cancer | 1e-27 | rs8179460 | 9 | GCST90129505 | no MR -> candidate analysis |
| Standing height (UKB data field 50) | 1e-27 | rs10797816 | 1 | GCST90468178 | no MR -> candidate analysis |
| Bone mineral density mean | 2e-27 | rs144534951 | 1 | GCST90321120 | no MR -> candidate analysis |
| _...and 118 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Laminin subunit alpha-1) |
| gnomAD constraint | not available |
| GWAS Catalog | no mapped SNPs |
| ClinVar | no records |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`uniprot`** — No reviewed human UniProt entry for 'LAMB1;LAMC1;LAMA1'.
- **`phenome`** — Could not resolve target 'LAMB1;LAMC1;LAMA1'.
- **`chembl`** — ChEMBL target matched by text search on 'LAMB1;LAMC1;LAMA1' and resolved to 'Laminin subunit alpha-1' — confirm this is the intended target.
- **`gnomad`** — No gnomAD constraint data.
- **`gwas`** — No GWAS Catalog SNPs mapped to this gene.
- **`clinvar`** — No ClinVar records.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 130 traits by best p-value, aggregated from 242 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4523594/ — _ChEMBL_37 (released 2026-05-01)_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/LAMB1;LAMC1;LAMA1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:27:17  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
