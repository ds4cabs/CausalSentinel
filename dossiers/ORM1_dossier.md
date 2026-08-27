# Protein Dossier — ORM1 (Alpha-1-acid glycoprotein 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Forced vital capacity (FVC) | -0.0373 | 0.00954 | 9.21e-05 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | -0.0384 | 0.0101 | 1.36e-04 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: S76 Injury of muscle and tendon at hip and thigh level | 0.857 | 0.253 | 6.93e-04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: polio  or  poliomyelitis | 0.701 | 0.236 | 0.00293 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | 0.0268 | 0.0116 | 0.0211 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M72 Fibroblastic disorders | 0.259 | 0.124 | 0.037 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: gastro-oesophageal reflux (gord)  or  gastric reflux | 0.1 | 0.0508 | 0.0484 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: G56 Mononeuropathies of upper limb | -0.219 | 0.112 | 0.05 | Wald ratio | 1 | cis | NA |
| Coronary heart disease | -0.115 | 0.0604 | 0.0571 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M23 Internal derangement of knee | -0.174 | 0.094 | 0.0641 | Wald ratio | 1 | cis | NA |
| Myocardial infarction | -0.122 | 0.066 | 0.0643 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | 0.0876 | 0.0475 | 0.0649 | Wald ratio | 1 | cis | NA |
| _...and 62 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_107 association rows across 85 traits (101 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating TGFBI levels | 4e-319 | rs10982156 | 2 | GCST90860488 | no MR -> candidate analysis |
| PDGFC protein levels | 8e-288 | rs113354603 | 2 | GCST90470190 | no MR -> candidate analysis |
| Circulating PDGFC levels | 6e-277 | rs113354603 | 3 | GCST90860265 | no MR -> candidate analysis |
| F10 protein levels | 1e-220 | rs10982156 | 1 | GCST90469163 | no MR -> candidate analysis |
| Glycoprotein acetyls levels | 1e-206 | rs10982156 | 4 | GCST90501111 | no MR -> candidate analysis |
| PROS1 protein levels | 4e-189 | rs10982156 | 1 | GCST90470337 | no MR -> candidate analysis |
| SPINK2 protein levels | 8e-146 | rs10982164 | 1 | GCST90470722 | no MR -> candidate analysis |
| Coagulation Factor X levels | 2e-85 | rs116994374 | 2 | GCST90247101 | no MR -> candidate analysis |
| Coagulation factor Xa levels | 8e-72 | rs10982156 | 3 | GCST90247102 | no MR -> candidate analysis |
| Circulating CLEC1A levels | 4e-62 | rs10982156 | 1 | GCST90860255 | no MR -> candidate analysis |
| CLEC1A protein levels | 2e-61 | rs10982156 | 2 | GCST90468767 | no MR -> candidate analysis |
| Circulating TNR levels | 2e-60 | rs10982156 | 1 | GCST90859737 | no MR -> candidate analysis |
| _...and 73 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (ORM1-like protein 3) |
| gnomAD constraint | pLI=0.04, LOEUF=0.768 — LoF-tolerant |
| GWAS Catalog | 101 unique SNPs / 208 rows |
| ClinVar | 78 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 815 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'ORM1' and resolved to 'ORM1-like protein 3' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 78 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 85 traits by best p-value, aggregated from 107 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P02763 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000229314/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL6066515/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/ORM1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/ORM1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=ORM1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/ORM1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:09:35  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
