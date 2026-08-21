# Protein Dossier — CAPN1;CAPNS1

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Pulse rate | 0.0479 | 0.0108 | 9.27e-06 | Wald ratio | 1 | cis | NA |
| Height | -0.0327 | 0.00784 | 3.09e-05 | Wald ratio | 1 | cis | NA |
| Weight | -0.021 | 0.0054 | 9.66e-05 | Wald ratio | 1 | cis | NA |
| Systemic lupus erythematosus | -0.422 | 0.117 | 3.22e-04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: osteoporosis | 0.151 | 0.0422 | 3.49e-04 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | -0.0165 | 0.00501 | 9.91e-04 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K57 Diverticular disease of intestine | 0.103 | 0.0388 | 0.00785 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: joint disorder | 0.194 | 0.074 | 0.00888 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: depression | -0.067 | 0.027 | 0.0129 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: diverticular disease or diverticulitis | 0.127 | 0.051 | 0.0131 | Wald ratio | 1 | cis | NA |
| Platelet count | 2.67 | 1.08 | 0.0134 | Wald ratio | 1 | cis | NA |
| HOMA-IR | 0.024 | 0.0111 | 0.031 | Wald ratio | 1 | cis | NA |
| _...and 105 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_16 association rows across 14 traits (12 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Uric acid levels | 3e-61 | rs183467134 | 1 | GCST90104168 | no MR -> candidate analysis |
| GFAP protein levels | 3e-32 | rs10895991 | 1 | GCST90469325 | no MR -> candidate analysis |
| Urate levels | 3e-24 | rs34888828 | 3 | GCST008973 | no MR -> candidate analysis |
| EGFL7 protein levels | 3e-16 | rs2271450 | 1 | GCST90469083 | no MR -> candidate analysis |
| Patatin-like phospholipase domain-containing protein 2 level | 3e-12 | rs10895991 | 1 | GCST90249034 | no MR -> candidate analysis |
| High-density lipoprotein levels (MTAG) | 2e-11 | rs6591179 | 1 | GCST90179147 | no MR -> candidate analysis |
| Physical function (baseline) | 2e-11 | rs1129367 | 1 | GCST90565837 | no MR -> candidate analysis |
| High density lipoprotein cholesterol levels | 5e-9 | rs588450 | 1 | GCST90278635 | no MR -> candidate analysis |
| Triglyceride to HDL cholesterol ratio | 5e-9 | rs6591179 | 1 | GCST90435483 | no MR -> candidate analysis |
| Hip circumference adjusted for BMI | 2e-8 | rs1129367 | 1 | GCST90020028 | no MR -> candidate analysis |
| Forced expiratory volume (baseline) | 3e-8 | rs111816352 | 1 | GCST90565844 | no MR -> candidate analysis |
| 2-aminoadipate levels in elite athletes | 4e-6 | rs17882574 | 1 | GCST90133516 | no MR -> candidate analysis |
| _...and 2 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Calpain 1) |
| gnomAD constraint | not available |
| GWAS Catalog | no mapped SNPs |
| ClinVar | no records |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`uniprot`** — No reviewed human UniProt entry for 'CAPN1;CAPNS1'.
- **`phenome`** — Could not resolve target 'CAPN1;CAPNS1'.
- **`chembl`** — ChEMBL target matched by text search on 'CAPN1;CAPNS1' and resolved to 'Calpain 1' — confirm this is the intended target.
- **`gnomad`** — No gnomAD constraint data.
- **`gwas`** — No GWAS Catalog SNPs mapped to this gene.
- **`clinvar`** — No ClinVar records.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 14 of 14 traits by best p-value, aggregated from 16 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2111357/ — _ChEMBL_37 (released 2026-05-01)_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CAPN1;CAPNS1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:27:52  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
