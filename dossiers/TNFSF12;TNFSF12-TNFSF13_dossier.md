# Protein Dossier — TNFSF12;TNFSF12-TNFSF13

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: hypertension | 0.0607 | 0.011 | 3.16e-08 | Wald ratio | 1 | cis | 0.000295 |
| Systolic blood pressure  automated reading | 0.0387 | 0.007 | 3.37e-08 | Wald ratio | 1 | cis | 0.938 |
| Diastolic blood pressure  automated reading | 0.0266 | 0.00701 | 1.46e-04 | Wald ratio | 1 | cis | NA |
| Primary sclerosing cholangitis  | 0.324 | 0.0966 | 7.92e-04 | Wald ratio | 1 | cis | NA |
| Fracture resulting from simple fall | 0.0483 | 0.0172 | 0.0049 | Wald ratio | 1 | cis | NA |
| Amyotrophic lateral sclerosis | -0.135 | 0.0506 | 0.00762 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: deep venous thrombosis (dvt) | 0.115 | 0.0433 | 0.00799 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I48 Atrial fibrillation and flutter | -0.213 | 0.0808 | 0.00826 | Wald ratio | 1 | cis | NA |
| Forearm bone mineral density | -0.113 | 0.044 | 0.0101 | Wald ratio | 1 | cis | NA |
| Urinary albumin-to-creatinine ratio | 0.0432 | 0.0178 | 0.0152 | Wald ratio | 1 | cis | NA |
| Birth weight | -0.0244 | 0.0107 | 0.0223 | Wald ratio | 1 | cis | NA |
| HbA1C | 0.0247 | 0.0109 | 0.0241 | Wald ratio | 1 | cis | NA |
| _...and 86 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_207 association rows across 127 traits (193 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Sex hormone-binding globulin levels | 8e-1628 | rs12940684 | 5 | GCST90020234 | no MR -> candidate analysis |
| TNFSF12/TNFSF13 protein level ratio | 4e-1279 | rs9899183 | 1 | GCST90315941 | no MR -> candidate analysis |
| Circulating TNFSF12 levels (id: OID00789_OID20624) | 6e-616 | rs9905587 | 2 | GCST90860121 | no MR -> candidate analysis |
| Circulating TNFSF12 levels (id: OID00555_OID20624) | 3e-598 | rs9905587 | 2 | GCST90859905 | no MR -> candidate analysis |
| Circulating TNFSF13 levels | 1e-429 | rs3803800 | 5 | GCST90860005 | no MR -> candidate analysis |
| Tumor necrosis factor ligand superfamily member 12 levels | 2e-333 | rs80067372 | 3 | GCST90249820 | no MR -> candidate analysis |
| Metabolic biomarkers (multivariate analysis) | 5e-324 | rs12940684 | 1 | GCST90038594 | no MR -> candidate analysis |
| Blood protein levels | 9e-200 | rs80067372 | 4 | GCST006585 | no MR -> candidate analysis |
| TNFSF13 protein levels | 9e-171 | rs142700143 | 5 | GCST90470921 | no MR -> candidate analysis |
| Serum levels of protein TNFSF12 | 9e-159 | rs77711855 | 1 | GCST90089244 | no MR -> candidate analysis |
| Low testosterone levels | 7e-154 | rs11078694 | 1 | GCST90026655 | no MR -> candidate analysis |
| Non-albumin protein levels | 7e-96 | rs3803800 | 5 | GCST90019515 | no MR -> candidate analysis |
| _...and 115 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 2 known modulators (Tumor necrosis factor ligand superfamily member 12) |
| gnomAD constraint | not available |
| GWAS Catalog | no mapped SNPs |
| ClinVar | no records |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`uniprot`** — No reviewed human UniProt entry for 'TNFSF12;TNFSF12-TNFSF13'.
- **`phenome`** — Could not resolve target 'TNFSF12;TNFSF12-TNFSF13'.
- **`chembl`** — ChEMBL target matched by text search on 'TNFSF12;TNFSF12-TNFSF13' and resolved to 'Tumor necrosis factor ligand superfamily member 12' — confirm this is the intended target.
- **`gnomad`** — No gnomAD constraint data.
- **`gwas`** — No GWAS Catalog SNPs mapped to this gene.
- **`clinvar`** — No ClinVar records.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 127 traits by best p-value, aggregated from 207 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3713023/ — _ChEMBL_37 (released 2026-05-01)_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/TNFSF12;TNFSF12-TNFSF13 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:27:21  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
