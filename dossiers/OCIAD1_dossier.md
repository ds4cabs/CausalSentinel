# Protein Dossier — OCIAD1 (OCIA domain-containing protein 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Myocardial infarction | -0.121 | 0.0348 | 4.76e-04 | Wald ratio | 1 | trans | NA |
| Coronary heart disease | -0.105 | 0.0315 | 8.64e-04 | Wald ratio | 1 | trans | NA |
| Amyotrophic lateral sclerosis | -0.186 | 0.0571 | 0.00113 | Wald ratio | 1 | trans | NA |
| Eczema | 0.168 | 0.0558 | 0.00266 | Wald ratio | 1 | trans | NA |
| Years of schooling | -0.0372 | 0.0124 | 0.0027 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: N92 Excessive  frequent and irregular menstruation | 0.134 | 0.0457 | 0.00341 | Wald ratio | 1 | trans | NA |
| Chronic kidney disease | 0.136 | 0.0496 | 0.00596 | Wald ratio | 1 | trans | NA |
| Forced vital capacity (FVC) | -0.0167 | 0.00614 | 0.00649 | Wald ratio | 1 | trans | NA |
| LDL cholesterol | -0.0468 | 0.0174 | 0.00701 | Wald ratio | 1 | trans | NA |
| Sodium in urine | 0.0186 | 0.00736 | 0.0115 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: deep venous thrombosis (dvt) | -0.155 | 0.0622 | 0.0127 | Wald ratio | 1 | trans | NA |
| Heel bone mineral density (BMD) T-score  automated | 0.0237 | 0.00968 | 0.0143 | Wald ratio | 1 | trans | NA |
| _...and 100 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3635_76_4` | OCAD1 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_14 association rows across 12 traits (12 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| COX5B protein levels | 1e-66 | rs112327139 | 1 | GCST90468834 | no MR -> candidate analysis |
| Age at menopause | 7e-14 | rs7665209 | 1 | GCST007079 | MR: beta=0.062, p=0.317 (trans) |
| ICAM4 protein levels | 5e-13 | rs201178302 | 1 | GCST90469501 | no MR -> candidate analysis |
| Pulse pressure | 7e-13 | rs13141838 | 1 | GCST90310296 | no MR -> candidate analysis |
| Type 2 diabetes | 2e-12 | rs62310934 | 2 | GCST90492734 | MR: beta=-0.0614, p=0.187 (trans) |
| Mean corpuscular hemoglobin | 1e-11 | rs7687992 | 1 | GCST007068 | no MR -> candidate analysis |
| Systolic blood pressure | 5e-11 | rs13141838 | 2 | GCST90310294 | MR: beta=0.0135, p=0.0773 (trans) |
| Medication use for hypertension (number of purchases) | 4e-9 | rs62310934 | 1 | GCST90250905 | no MR -> candidate analysis |
| Breast cancer | 6e-9 | rs4695407 | 1 | GCST90308751 | MR: beta=0.0549, p=0.0269 (trans) |
| Chronic sputum production | 6e-9 | rs79998532 | 1 | GCST90269902 | no MR -> candidate analysis |
| COVID-19 hospitalization or rheumatoid arthritis (MTAG) | 3e-8 | rs2354938 | 1 | GCST90255368 | no MR -> candidate analysis |
| Type 2 diabetes (PheCode 250.2) | 1e-6 | rs2354944 | 1 | GCST90651113 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 129 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| breast carcinoma | 0.141 | — | common-variant locus | no MR -> candidate analysis |
| type 2 diabetes mellitus | 0.123 | — | common-variant locus | no MR -> candidate analysis |
| migraine disorder | 0.101 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.07 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (OCIA domain-containing protein 1) |
| gnomAD constraint | pLI=4.7e-08, LOEUF=1.02 — LoF-tolerant |
| GWAS Catalog | 48 unique SNPs / 96 rows |
| ClinVar | 77 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 129 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'OCIAD1' and resolved to 'OCIA domain-containing protein 1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 77 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 12 of 12 traits by best p-value, aggregated from 14 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9NX40 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000109180/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL6067371/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/OCIAD1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/OCIAD1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=OCIAD1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/OCIAD1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:08:49  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
