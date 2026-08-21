# Protein Dossier — ATP4B (Potassium-transporting ATPase subunit beta)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Red blood cell count | 0.0398 | 0.0125 | 0.00146 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: R04 Haemorrhage from respiratory passages | 0.414 | 0.131 | 0.0016 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: C50 Malignant neoplasm of breast | 0.24 | 0.0868 | 0.00566 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: pernicious anaemia | 0.424 | 0.175 | 0.0155 | Wald ratio | 1 | trans | NA |
| Subjective well being | -0.0398 | 0.0171 | 0.0196 | Wald ratio | 1 | trans | NA |
| Height | 0.0409 | 0.0176 | 0.0202 | Wald ratio | 1 | trans | NA |
| Serum cystatin C (eGFRcys) | 0.025 | 0.0108 | 0.0206 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: enlarged prostate | 0.217 | 0.0974 | 0.026 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: psoriasis | 0.232 | 0.106 | 0.0284 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: osteoporosis | 0.203 | 0.0927 | 0.0287 | Wald ratio | 1 | trans | NA |
| High grade serous ovarian cancer | -0.194 | 0.0927 | 0.0358 | Wald ratio | 1 | trans | NA |
| Alcohol intake frequency | 0.0408 | 0.0207 | 0.0487 | Wald ratio | 1 | trans | NA |
| _...and 83 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_5 association rows across 4 traits (5 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating AXL levels | 2e-16 | rs11839787 | 1 | GCST90859958 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 2e-15 | rs10161594 | 1 | GCST90838669 | no MR -> candidate analysis |
| Height | 1e-10 | rs75779304 | 2 | GCST008839 | MR: beta=0.0409, p=0.0202 (trans) |
| Gut microbiome abundance (class Roseburia sp. 7 (at 1 year)  | 3e-8 | rs72670606 | 1 | GCST90569166 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 13 known modulators (Potassium-transporting ATPase) |
| gnomAD constraint | pLI=8.8e-08, LOEUF=1.05 — LoF-tolerant |
| GWAS Catalog | 26 unique SNPs / 52 rows |
| ClinVar | 191 records; 5 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 182 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'ATP4B' and resolved to 'Potassium-transporting ATPase' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 191 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 4 of 4 traits by best p-value, aggregated from 5 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P51164 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000186009/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2095173/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/ATP4B — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/ATP4B — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=ATP4B%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/ATP4B — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:12:47  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
