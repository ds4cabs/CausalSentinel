# Protein Dossier — CGA (Glycoprotein hormones alpha chain)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Creatinine (enzymatic) in urine | -0.0127 | 0.00388 | 0.00107 | Wald ratio | 1 | trans | NA |
| Alcohol intake frequency | 0.0183 | 0.00599 | 0.00223 | Wald ratio | 1 | trans | NA |
| Age at menarche | -0.0306 | 0.0101 | 0.0024 | Wald ratio | 1 | trans | NA |
| Fractured or broken bones in last 5 years | -0.0385 | 0.0131 | 0.0034 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: Z09 Follow-up examination after treatment for conditions other than malignant neoplasms | 0.0851 | 0.0303 | 0.00495 | Wald ratio | 1 | trans | NA |
| Potassium in urine | -0.0106 | 0.00411 | 0.00968 | Wald ratio | 1 | trans | NA |
| Weight | -0.00912 | 0.00358 | 0.0108 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: kidney stone or ureter stone or bladder stone | -0.129 | 0.0522 | 0.0132 | Wald ratio | 1 | trans | NA |
| Fractured bone site(s): Other bones | -0.0441 | 0.0184 | 0.0166 | Wald ratio | 1 | trans | NA |
| Low grade serous ovarian cancer | -0.203 | 0.0875 | 0.0201 | Wald ratio | 1 | trans | NA |
| Cancer code  self-reported: prostate cancer | -0.125 | 0.0539 | 0.0205 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: L03 Cellulitis | 0.0922 | 0.0412 | 0.0251 | Wald ratio | 1 | trans | NA |
| _...and 79 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2953_31_2` | Luteinizing hormone | Suhre K | 2019 |
| `prot-c-3032_11_2` | FSH | Suhre K | 2019 |
| `prot-c-3521_16_2` | TSH | Suhre K | 2019 |
| `prot-c-4914_10_1` | HCG | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_23 association rows across 16 traits (22 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Thyroid stimulating hormone levels | 5e-78 | rs1998615 | 4 | GCST90572789 | no MR -> candidate analysis |
| Thyroid-stimulating hormone levels | 3e-22 | rs2031365 | 1 | GCST90662868 | no MR -> candidate analysis |
| White blood cell count | 2e-20 | rs4574603 | 2 | GCST90002378 | no MR -> candidate analysis |
| Circulating CGA levels | 2e-18 | rs2031367 | 1 | GCST90860633 | no MR -> candidate analysis |
| Neutrophil percentage of granulocytes | 6e-18 | rs67614146 | 1 | GCST004623 | no MR -> candidate analysis |
| CGA protein levels | 4e-17 | rs2031367 | 1 | GCST90468732 | no MR -> candidate analysis |
| FSHB protein levels | 4e-15 | rs779759288 | 1 | GCST90469270 | no MR -> candidate analysis |
| Eosinophil percentage of granulocytes | 5e-15 | rs67614146 | 1 | GCST004617 | no MR -> candidate analysis |
| Free thyroxine levels within normal range in pregnancy | 1e-13 | rs9362387 | 1 | GCST90435196 | no MR -> candidate analysis |
| Neutrophil-to-lymphocyte ratio | 8e-13 | rs981087 | 3 | GCST90866310 | no MR -> candidate analysis |
| Eosinophil percentage of white cells | 6e-12 | rs67614146 | 1 | GCST004600 | no MR -> candidate analysis |
| Educational attainment | 5e-11 | rs9362387 | 1 | GCST90105038 | no MR -> candidate analysis |
| _...and 4 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 877 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| hypothyroidism | 0.807 | — | common-variant locus | no MR -> candidate analysis |
| interstitial lung disease | 0.244 | — | common-variant locus | no MR -> candidate analysis |
| placenta praevia | 0.216 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Glycoprotein hormones alpha chain) |
| gnomAD constraint | pLI=0.6, LOEUF=0.763 — LoF-tolerant |
| GWAS Catalog | 45 unique SNPs / 90 rows |
| ClinVar | 35 records; 12 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 877 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'CGA' and resolved to 'Glycoprotein hormones alpha chain' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 35 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 16 of 16 traits by best p-value, aggregated from 23 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P01215 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000135346/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2146305/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CGA — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CGA — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CGA%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CGA — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:49:07  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
