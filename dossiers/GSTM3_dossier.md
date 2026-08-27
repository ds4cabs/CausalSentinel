# Protein Dossier — GSTM3 (Glutathione S-transferase Mu 3)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| ER-positive Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.228 | 0.0582 | 9.22e-05 | Wald ratio | 1 | cis | NA |
| Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.189 | 0.049 | 1.13e-04 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | -0.0541 | 0.0188 | 0.00399 | Wald ratio | 1 | cis | NA |
| Paget's disease | 1.3 | 0.453 | 0.00418 | Wald ratio | 1 | cis | NA |
| Height | 0.0723 | 0.0269 | 0.00722 | Wald ratio | 1 | cis | NA |
| Happiness | 0.0594 | 0.0232 | 0.0105 | Wald ratio | 1 | cis | NA |
| Urate | 0.129 | 0.0522 | 0.0138 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: pernicious anaemia | 0.35 | 0.157 | 0.0259 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C50 Malignant neoplasm of breast | -0.265 | 0.122 | 0.0296 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Cataract | -0.161 | 0.076 | 0.0339 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K35 Acute appendicitis | 0.272 | 0.131 | 0.0379 | Wald ratio | 1 | cis | NA |
| Iron | 0.157 | 0.0783 | 0.0455 | Wald ratio | 1 | cis | NA |
| _...and 88 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_1 association rows across 1 traits (0 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Alpha-CEHC sulfate levels in elite athletes | 3e-6 | rs3814309 | 1 | GCST90133632 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 237 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| cystic fibrosis | 0.608 | — | established (curated) | no MR -> candidate analysis |
| urinary bladder cancer | 0.035 | — | common-variant locus | no MR -> candidate analysis |
| type 2 diabetes mellitus | 0.052 | — | common-variant locus | no MR -> candidate analysis |
| breast cancer | 0.04 | — | common-variant locus | MR: beta=-0.228, p=9.22e-05 (cis) |

> Of the 4 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Glutathione S-transferase Mu 3) |
| gnomAD constraint | pLI=1.4e-11, LOEUF=1.25 — LoF-tolerant |
| GWAS Catalog | 85 unique SNPs / 170 rows |
| ClinVar | 56 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 4 clinical annotations across 3 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 237 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'GSTM3' and resolved to 'Glutathione S-transferase Mu 3' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 56 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 1 of 1 traits by best p-value, aggregated from 1 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P21266 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000134202/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2242/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/GSTM3 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/GSTM3 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=GSTM3%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=GSTM3 — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/GSTM3 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:55:38  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
