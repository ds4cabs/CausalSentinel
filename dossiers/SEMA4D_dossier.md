# Protein Dossier — SEMA4D (Semaphorin-4D)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Body mass index (BMI) | -0.0112 | 0.00351 | 0.00136 | Wald ratio | 1 | cis | NA |
| Ovarian cancer | 0.0573 | 0.0189 | 0.00242 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K20 Oesophagitis | 0.0931 | 0.0323 | 0.00398 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C61 Malignant neoplasm of prostate | -0.141 | 0.0497 | 0.00461 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: S76 Injury of muscle and tendon at hip and thigh level | 0.328 | 0.122 | 0.00726 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: pneumothorax | 0.335 | 0.125 | 0.00745 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R35 Polyuria | 0.122 | 0.0499 | 0.0143 | Wald ratio | 1 | cis | NA |
| Clear cell ovarian cancer | 0.143 | 0.0595 | 0.0159 | Wald ratio | 1 | cis | NA |
| Weight | -0.00676 | 0.0031 | 0.0293 | Wald ratio | 1 | cis | NA |
| Depressive symptoms | -0.0133 | 0.00626 | 0.0336 | Wald ratio | 1 | cis | NA |
| Lung cancer | 0.0512 | 0.0252 | 0.0417 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Ankle | 0.0575 | 0.0283 | 0.0421 | Wald ratio | 1 | cis | NA |
| _...and 69 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_220 association rows across 168 traits (202 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Semaphorin-4D levels | 5e-1164 | rs45464494 | 2 | GCST90249490 | no MR -> candidate analysis |
| Semaphorin-4D levels (SEMA4D.5737.61.3) | 2e-292 | rs140647145 | 2 | GCST90242748 | no MR -> candidate analysis |
| Blood protein levels | 2e-187 | rs45464494 | 1 | GCST006585 | no MR -> candidate analysis |
| CD84/SEMA4D protein level ratio | 2e-42 | rs11526468 | 1 | GCST90313917 | no MR -> candidate analysis |
| SEMA4D protein levels | 3e-41 | rs67607259 | 3 | GCST90470573 | no MR -> candidate analysis |
| Phospholipids to Total Lipids in Medium HDL percentage | 5e-28 | rs10908900 | 1 | GCST90501191 | no MR -> candidate analysis |
| Triglyceride levels | 9e-28 | rs3138490 | 6 | GCST90662893 | no MR -> candidate analysis |
| Vertex-wise sulcal depth | 9e-28 | rs3138493 | 1 | GCST90095129 | no MR -> candidate analysis |
| Gamma glutamyl transferase levels | 2e-21 | rs2183298 | 1 | GCST90662899 | no MR -> candidate analysis |
| Cholesterol to Total Lipids in Medium HDL percentage | 5e-20 | rs10908900 | 1 | GCST90501183 | no MR -> candidate analysis |
| Vertex-wise cortical surface area | 7e-20 | rs1007966 | 1 | GCST90095130 | no MR -> candidate analysis |
| Reticulocyte percentage (UKB data field 30240) | 8e-20 | rs11526468 | 1 | GCST90468101 | no MR -> candidate analysis |
| _...and 156 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 640 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| skin aging | 0.674 | — | common-variant locus | no MR -> candidate analysis |
| sclerosing cholangitis | 0.608 | — | established (curated) | no MR -> candidate analysis |
| placental abruption | 0.41 | — | common-variant locus | no MR -> candidate analysis |
| intelligence | 0.396 | — | common-variant locus | no MR -> candidate analysis |
| otosclerosis | 0.372 | — | common-variant locus | no MR -> candidate analysis |

> Of the 5 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 1 known modulators (Semaphorin-4D) |
| gnomAD constraint | pLI=1, LOEUF=0.42 — LoF-INTOLERANT |
| GWAS Catalog | 93 unique SNPs / 171 rows |
| ClinVar | 233 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 640 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'SEMA4D' and resolved to 'Semaphorin-4D' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 233 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 168 traits by best p-value, aggregated from 220 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q92854 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000187764/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4630887/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/SEMA4D — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/SEMA4D — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=SEMA4D%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/SEMA4D — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:59:29  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
