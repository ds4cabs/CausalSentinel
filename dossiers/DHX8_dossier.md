# Protein Dossier — DHX8 (ATP-dependent RNA helicase DHX8)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diastolic blood pressure  automated reading | -0.0135 | 0.0035 | 1.20e-04 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: osteoporosis | 0.0895 | 0.0251 | 3.62e-04 | Wald ratio | 1 | trans | NA |
| Sleep duration | 0.00904 | 0.00267 | 7.11e-04 | Wald ratio | 1 | trans | NA |
| Height | -0.0108 | 0.00417 | 0.00949 | Wald ratio | 1 | trans | NA |
| Total cholesterol | 0.0164 | 0.00678 | 0.0154 | Wald ratio | 1 | trans | NA |
| Percent emphysema | 0.0329 | 0.0138 | 0.0174 | Wald ratio | 1 | trans | NA |
| Urate | 0.0183 | 0.0077 | 0.0176 | Wald ratio | 1 | trans | NA |
| LDL cholesterol | 0.0168 | 0.00717 | 0.019 | Wald ratio | 1 | trans | NA |
| Lumbar spine bone mineral density | -0.0289 | 0.0124 | 0.0196 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: D12 Benign neoplasm of colon  rectum  anus and anal canal | -0.0718 | 0.031 | 0.0208 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: hyperthyroidism or thyrotoxicosis | -0.101 | 0.044 | 0.022 | Wald ratio | 1 | trans | NA |
| Ferritin | 0.0284 | 0.0133 | 0.0326 | Wald ratio | 1 | trans | NA |
| _...and 88 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_31 association rows across 26 traits (27 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating CD300LG levels | 2e-53 | rs573043394 | 1 | GCST90860606 | no MR -> candidate analysis |
| LRRC37A2 protein levels | 2e-19 | rs191524289 | 1 | GCST90469802 | no MR -> candidate analysis |
| Hip shape mode 9 | 2e-15 | rs2343132 | 1 | GCST90482712 | no MR -> candidate analysis |
| Standing height (UKB data field 50) | 4e-14 | rs4371196 | 1 | GCST90468178 | no MR -> candidate analysis |
| Aortic stenosis | 5e-14 | rs59386234 | 2 | GCST90837546 | no MR -> candidate analysis |
| HDL cholesterol levels x long total sleep time interaction ( | 1e-13 | rs75543966 | 1 | GCST009368 | no MR -> candidate analysis |
| Height (baseline) | 8e-12 | rs4371196 | 2 | GCST90565843 | no MR -> candidate analysis |
| Core binding factor acute myeloid leukemia | 1e-11 | rs12603053; rs3826413; rs9748005; rs11650719; rs7223638; rs4792997; rs7217897; rs12941944; rs7210301; rs1317254; rs1316956; rs4792900; rs7208294; rs4793000 | 2 | GCST008413 | no MR -> candidate analysis |
| Estimated glomerular filtration rate (creatinine, cystatin c | 2e-11 | rs34182830 | 1 | GCST90428446 | no MR -> candidate analysis |
| Alzheimer's disease or family history of Alzheimer's disease | 9e-11 | rs530555010 | 1 | GCST90624094 | no MR -> candidate analysis |
| Body mass index | 3e-10 | rs1728182 | 2 | GCST90255621 | no MR -> candidate analysis |
| Height | 3e-10 | rs9897859 | 2 | GCST90245848 | MR: beta=-0.0108, p=0.00949 (trans) |
| _...and 14 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 294 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| congenital anomaly of kidney and urinary tract | 0.426 | — | established (curated) | no MR -> candidate analysis |
| lens disorder | 0.214 | — | common-variant locus | no MR -> candidate analysis |
| upper extremity fracture | 0.21 | — | common-variant locus | no MR -> candidate analysis |
| duodenitis | 0.187 | — | common-variant locus | MR: beta=0.0201, p=0.353 (trans) |
| high grade ovarian serous adenocarcinoma | 0.117 | — | common-variant locus | no MR -> candidate analysis |

> Of the 5 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (ATP-dependent RNA helicase DHX8) |
| gnomAD constraint | pLI=3.2e-06, LOEUF=0.584 — LoF-tolerant |
| GWAS Catalog | 59 unique SNPs / 106 rows |
| ClinVar | 240 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 294 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'DHX8' and resolved to 'ATP-dependent RNA helicase DHX8' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 240 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 26 traits by best p-value, aggregated from 31 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q14562 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000067596/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL5465306/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/DHX8 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/DHX8 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=DHX8%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/DHX8 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:17:04  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
