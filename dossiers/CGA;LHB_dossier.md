# Protein Dossier — CGA;LHB

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Creatinine (enzymatic) in urine | 0.0208 | 0.00636 | 0.00108 | Wald ratio | 1 | trans | NA |
| Fractured or broken bones in last 5 years | 0.0601 | 0.0195 | 0.00209 | Wald ratio | 1 | trans | NA |
| Age at menarche | 0.0503 | 0.0166 | 0.0024 | Wald ratio | 1 | trans | NA |
| Alcohol intake frequency | -0.0298 | 0.00982 | 0.00242 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: kidney stone or ureter stone or bladder stone | 0.182 | 0.0628 | 0.00377 | Wald ratio | 1 | trans | NA |
| Cancer code  self-reported: prostate cancer | 0.175 | 0.0656 | 0.00777 | Wald ratio | 1 | trans | NA |
| Potassium in urine | 0.0174 | 0.00675 | 0.00986 | Wald ratio | 1 | trans | NA |
| Fractured bone site(s): Other bones | 0.069 | 0.027 | 0.0106 | Wald ratio | 1 | trans | NA |
| Weight | 0.0146 | 0.00587 | 0.0125 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: Z09 Follow-up examination after treatment for conditions other than malignant neoplasms | -0.159 | 0.0637 | 0.0127 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: C61 Malignant neoplasm of prostate | 0.166 | 0.0695 | 0.0171 | Wald ratio | 1 | trans | NA |
| Low grade serous ovarian cancer | 0.332 | 0.144 | 0.021 | Wald ratio | 1 | trans | NA |
| _...and 93 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_33 association rows across 25 traits (32 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Luteinizing hormone levels | 2e-187 | rs3795052 | 1 | GCST90248348 | no MR -> candidate analysis |
| Human Chorionic Gonadotropin levels | 2e-167 | rs113572723 | 1 | GCST90162185 | no MR -> candidate analysis |
| Human Chorionic Gonadotropin levels (CGA.CGB.4914.10.1) | 7e-100 | rs3795047 | 2 | GCST90241456 | no MR -> candidate analysis |
| Thyroid stimulating hormone levels | 5e-78 | rs1998615 | 4 | GCST90572789 | no MR -> candidate analysis |
| Lutropin subunit beta levels | 2e-67 | rs144948359 | 1 | GCST90248342 | no MR -> candidate analysis |
| Luteinizing hormone levels (CGA.LHB.2953.31.2) | 7e-43 | rs3795047 | 1 | GCST90241825 | no MR -> candidate analysis |
| Thyroid-stimulating hormone levels | 3e-22 | rs2031365 | 1 | GCST90662868 | no MR -> candidate analysis |
| White blood cell count | 2e-20 | rs4574603 | 2 | GCST90002378 | no MR -> candidate analysis |
| Circulating CGA levels | 2e-18 | rs2031367 | 1 | GCST90860633 | no MR -> candidate analysis |
| Neutrophil percentage of granulocytes | 6e-18 | rs67614146 | 1 | GCST004623 | no MR -> candidate analysis |
| CGA protein levels | 4e-17 | rs2031367 | 1 | GCST90468732 | no MR -> candidate analysis |
| LHB protein levels | 9e-17 | rs3795050 | 1 | GCST90469767 | no MR -> candidate analysis |
| _...and 13 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Glycoprotein hormones alpha chain) |
| gnomAD constraint | not available |
| GWAS Catalog | no mapped SNPs |
| ClinVar | no records |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`uniprot`** — No reviewed human UniProt entry for 'CGA;LHB'.
- **`phenome`** — Could not resolve target 'CGA;LHB'.
- **`chembl`** — ChEMBL target matched by text search on 'CGA;LHB' and resolved to 'Glycoprotein hormones alpha chain' — confirm this is the intended target.
- **`gnomad`** — No gnomAD constraint data.
- **`gwas`** — No GWAS Catalog SNPs mapped to this gene.
- **`clinvar`** — No ClinVar records.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 25 traits by best p-value, aggregated from 33 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2146305/ — _ChEMBL_37 (released 2026-05-01)_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CGA;LHB — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:49:35  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
