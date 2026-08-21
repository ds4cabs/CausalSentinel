# Protein Dossier — ADIPOQ (Adiponectin)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code self-reported: pulmonary embolism (with or without) dvt | 0.448 | 0.128 | 4.42e-04 | Wald ratio | 1 | cis | NA |
| Invasive mucinous ovarian cancer | -0.874 | 0.261 | 8.14e-04 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I80 Phlebitis and thrombophlebitis | 0.46 | 0.169 | 0.00649 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | -0.0564 | 0.0227 | 0.013 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N92 Excessive  frequent and irregular menstruation | 0.237 | 0.0982 | 0.0157 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: malignant melanoma | 0.33 | 0.148 | 0.026 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: prostate cancer | 0.326 | 0.154 | 0.034 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: diverticular disease or diverticulitis | 0.274 | 0.13 | 0.0345 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R10 Abdominal and pelvic pain | 0.155 | 0.0735 | 0.0351 | Wald ratio | 1 | cis | NA |
| Caudate volume | -67.2 | 32.9 | 0.041 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: asthma | 0.0912 | 0.0453 | 0.0439 | Wald ratio | 1 | cis | NA |
| Primary sclerosing cholangitis  | -0.405 | 0.202 | 0.0452 | Wald ratio | 1 | cis | NA |
| _...and 53 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3554_24_1` | Adiponectin | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_69 association rows across 34 traits (60 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| ADIPOQ protein levels | 4e-232 | rs562177400 | 5 | GCST90468245 | no MR -> candidate analysis |
| Adiponectin levels | 5e-149 | rs17366568 | 20 | GCST010050 | no MR -> candidate analysis |
| Adiponectin levels (BMI-adjusted) | 8e-55 | rs199938283 | 6 | GCST90011881 | no MR -> candidate analysis |
| Circulating CD163 levels | 8e-32 | rs9860747 | 1 | GCST90859926 | no MR -> candidate analysis |
| Kininogen-1 levels | 4e-30 | rs17366568 | 1 | GCST90162099 | no MR -> candidate analysis |
| HEPACAM2 protein levels | 3e-29 | rs9835223 | 2 | GCST90469445 | no MR -> candidate analysis |
| F11 protein levels | 4e-29 | rs66471222 | 3 | GCST90469165 | no MR -> candidate analysis |
| CD163 protein levels | 5e-24 | rs11923060 | 1 | GCST90468600 | no MR -> candidate analysis |
| Circulating LIFR levels | 1e-22 | rs9860747 | 1 | GCST90859867 | no MR -> candidate analysis |
| Serum levels of protein ADIPOQ | 3e-22 | rs143257534 | 1 | GCST90088439 | no MR -> candidate analysis |
| ST6GAL1 protein levels | 9e-22 | rs4686807 | 1 | GCST90470753 | no MR -> candidate analysis |
| LIFR protein levels | 2e-20 | rs9860747 | 1 | GCST90469769 | no MR -> candidate analysis |
| _...and 22 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1595 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| adiponectin deficiency | 0.718 | — | established (curated) | no MR -> candidate analysis |
| hearing loss disorder | 0.426 | — | common-variant locus | no MR -> candidate analysis |
| hyperpituitarism | 0.315 | — | common-variant locus | no MR -> candidate analysis |
| glomerulonephritis | 0.241 | — | common-variant locus | no MR -> candidate analysis |
| diabetes mellitus | 0.034 | — | common-variant locus | no MR -> candidate analysis |
| breast cancer | 0.032 | — | common-variant locus | MR: beta=0.0812, p=0.343 (cis) |

> Of the 6 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Adiponectin receptor protein 2) |
| gnomAD constraint | pLI=4.3e-08, LOEUF=1.73 — LoF-tolerant |
| GWAS Catalog | 116 unique SNPs / 282 rows |
| ClinVar | 87 records; 5 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 1 clinical annotations across 1 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1595 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'ADIPOQ' and resolved to 'Adiponectin receptor protein 2' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 87 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 20 of 34 traits by best p-value, aggregated from 69 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q15848 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000181092/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3392947/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/ADIPOQ — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/ADIPOQ — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=ADIPOQ%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=ADIPOQ — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/ADIPOQ — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T00:56:29  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
