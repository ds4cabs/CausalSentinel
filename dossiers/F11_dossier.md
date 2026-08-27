# Protein Dossier — F11 (Coagulation factor XI)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: hypopituitarism | 0.382 | 0.131 | 0.00356 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: hypopituitarism | 0.382 | 0.131 | 0.00356 | Inverse variance weighted | 2 | cis | NA |
| Eczema | 0.066 | 0.0245 | 0.00717 | Inverse variance weighted | 2 | trans | NA |
| Eczema | 0.066 | 0.0245 | 0.00717 | Inverse variance weighted | 2 | cis | NA |
| Years of schooling | 0.014 | 0.00562 | 0.0124 | Inverse variance weighted | 2 | trans | NA |
| Years of schooling | 0.014 | 0.00562 | 0.0124 | Inverse variance weighted | 2 | cis | NA |
| Diagnoses - main ICD10: I80 Phlebitis and thrombophlebitis | 0.252 | 0.107 | 0.0181 | Inverse variance weighted | 2 | trans | NA |
| Diagnoses - main ICD10: I80 Phlebitis and thrombophlebitis | 0.252 | 0.107 | 0.0181 | Inverse variance weighted | 2 | cis | NA |
| Paget's disease | 0.201 | 0.0877 | 0.0219 | Inverse variance weighted | 2 | trans | NA |
| Paget's disease | 0.201 | 0.0877 | 0.0219 | Inverse variance weighted | 2 | cis | NA |
| Vascular or heart problems diagnosed by doctor: Angina | -0.0445 | 0.0203 | 0.0289 | Inverse variance weighted | 2 | trans | NA |
| Vascular or heart problems diagnosed by doctor: Angina | -0.0445 | 0.0203 | 0.0289 | Inverse variance weighted | 2 | cis | NA |
| _...and 185 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2190_55_1` | Coagulation Factor XI | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_180 association rows across 88 traits (148 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Coagulation Factor XI levels | 2e-272 | rs2289252 | 6 | GCST90247103 | no MR -> candidate analysis |
| Venous thromboembolism | 4e-256 | rs3756011 | 15 | GCST90797305 | no MR -> candidate analysis |
| Venous thromboembolism or factor XI levels (pleiotropy) | 1e-251 | rs3756011 | 1 | GCST90129538 | no MR -> candidate analysis |
| Fibrinogen levels or factor VII levels or factor XI levels o | 4e-199 | rs4253417 | 1 | GCST90129560 | no MR -> candidate analysis |
| Ischemic stroke or factor XI levels (pleiotropy) | 1e-197 | rs4253417 | 1 | GCST90129552 | no MR -> candidate analysis |
| Factor XI | 3e-193 | rs4253417 | 1 | GCST004124 | no MR -> candidate analysis |
| Coronary artery disease or factor XI levels (pleiotropy) | 9e-189 | rs4253417 | 1 | GCST90129545 | no MR -> candidate analysis |
| Vertex-wise sulcal depth | 3e-139 | rs62348889 | 2 | GCST90095129 | no MR -> candidate analysis |
| Other venous embolism and thrombosis (PheCode 452) | 8e-127 | rs3756011 | 3 | GCST90476007 | no MR -> candidate analysis |
| Serum levels of protein F11 | 7e-125 | rs2289252 | 2 | GCST90087924 | no MR -> candidate analysis |
| F11 protein levels | 8e-125 | rs6848311 | 10 | GCST90469165 | no MR -> candidate analysis |
| Deep vein thrombosis [DVT] (PheCode 452.2) | 6e-98 | rs4444878 | 2 | GCST90476010 | no MR -> candidate analysis |
| _...and 76 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 306 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| factor XI deficiency | 0.964 | 0.901 | established (curated) | no MR -> candidate analysis |
| congenital factor XI deficiency | 0.877 | — | established (curated) | no MR -> candidate analysis |
| venous thromboembolism | 0.922 | — | common-variant locus | no MR -> candidate analysis |
| deep vein thrombosis | 0.901 | — | common-variant locus | no MR -> candidate analysis |
| pulmonary embolism | 0.888 | — | common-variant locus | MR: beta=0.237, p=0.102 (trans) |
| heart disorder | 0.878 | — | common-variant locus | no MR -> candidate analysis |
| phlebitis | 0.876 | — | common-variant locus | MR: beta=0.252, p=0.0181 (trans) |
| Thrombophlebitis | 0.869 | — | common-variant locus | MR: beta=0.252, p=0.0181 (trans) |
| cardiovascular disorder | 0.827 | — | common-variant locus | no MR -> candidate analysis |
| Thromboembolism | 0.819 | — | common-variant locus | no MR -> candidate analysis |
| ischemic stroke | 0.777 | — | common-variant locus | MR: beta=0.0396, p=0.0952 (trans) |
| Abnormal bleeding | 0.803 | — | established (curated) | no MR -> candidate analysis |
| Pulmonary Infarction | 0.801 | — | common-variant locus | no MR -> candidate analysis |
| thrombophilia | 0.781 | — | common-variant locus | no MR -> candidate analysis |
| hereditary disease | 0.772 | — | established (curated) | no MR -> candidate analysis |

> Of the 15 rows above, **11 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 1 exploratory rare-variant signal(s), 1 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 4 known modulators (Coagulation factor XI) |
| gnomAD constraint | pLI=1.8e-27, LOEUF=1.23 — LoF-tolerant |
| GWAS Catalog | 128 unique SNPs / 302 rows |
| ClinVar | 972 records; 23 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 1 clinical annotations across 1 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 306 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'F11' and resolved to 'Coagulation factor XI' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 972 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 20 of 88 traits by best p-value, aggregated from 180 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P03951 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000088926/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2820/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/F11 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/F11 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=F11%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=F11 — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/F11 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:30:52  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
