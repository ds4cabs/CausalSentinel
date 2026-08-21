# Protein Dossier — TNFRSF1B (Tumor necrosis factor receptor superfamily member 1B)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Eye problems or disorders: Injury or trauma resulting in loss of vision | 0.416 | 0.113 | 2.29e-04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | 0.161 | 0.049 | 0.00105 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I83 Varicose veins of lower extremities | 0.227 | 0.0723 | 0.0017 | Wald ratio | 1 | cis | NA |
| Forearm bone mineral density | 0.209 | 0.0836 | 0.0125 | Wald ratio | 1 | cis | NA |
| ER-positive Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.1 | 0.0429 | 0.0199 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K29 Gastritis and duodenitis | -0.251 | 0.109 | 0.0213 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: chronic obstructive airways disease or copd | 0.359 | 0.159 | 0.0245 | Wald ratio | 1 | cis | NA |
| Bulimia nervosa | -0.0989 | 0.0442 | 0.0252 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: high cholesterol | 0.0664 | 0.0327 | 0.0425 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: asthma | 0.0666 | 0.0339 | 0.0494 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: diverticular disease or diverticulitis | -0.342 | 0.179 | 0.056 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: Z09 Follow-up examination after treatment for conditions other than malignant neoplasms | -0.256 | 0.139 | 0.0658 | Wald ratio | 1 | cis | NA |
| _...and 94 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3152_57_1` | TNF sR-II | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_30 association rows across 19 traits (26 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| TNFRSF1A/TNFRSF1B protein level ratio | 3e-439 | rs5746012 | 1 | GCST90315937 | no MR -> candidate analysis |
| HAVCR2/TNFRSF1B protein level ratio | 7e-310 | rs5746026 | 1 | GCST90315030 | no MR -> candidate analysis |
| PIK3IP1/TNFRSF1B protein level ratio | 1e-266 | rs5746012 | 1 | GCST90315654 | no MR -> candidate analysis |
| Circulating TNFRSF1B levels | 2e-188 | rs5746017 | 4 | GCST90859916 | no MR -> candidate analysis |
| TNFRSF1B protein levels | 5e-128 | rs5746017 | 3 | GCST90470911 | no MR -> candidate analysis |
| Tumor necrosis factor receptor 2 levels | 5e-50 | rs5746026 | 2 | GCST90012026 | no MR -> candidate analysis |
| Tumor necrosis factor receptor superfamily member 1B levels | 4e-38 | rs5746011 | 2 | GCST90249840 | no MR -> candidate analysis |
| Eosinophil count | 8e-22 | rs474247 | 2 | GCST007065 | no MR -> candidate analysis |
| Hypothyroidism | 3e-20 | rs235220 | 4 | GCST90627750 | MR: beta=0.161, p=0.00105 (cis) |
| Autoimmune hypothyroidism | 1e-17 | rs235220 | 1 | GCST90837324 | no MR -> candidate analysis |
| Eosinophil percentage of white cells | 6e-17 | rs474247 | 1 | GCST90002382 | no MR -> candidate analysis |
| Tumor necrosis factor receptor superfamily member 1B levels  | 3e-15 | rs5746017 | 1 | GCST90243171 | no MR -> candidate analysis |
| _...and 7 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 939 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| hypothyroidism | 0.664 | — | common-variant locus | MR: beta=0.161, p=0.00105 (cis) |
| thyroid gland disorder | 0.487 | — | common-variant locus | no MR -> candidate analysis |
| childhood onset asthma | 0.346 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Tumor necrosis factor receptor superfamily member 1B) |
| gnomAD constraint | pLI=0.16, LOEUF=0.624 — LoF-tolerant |
| GWAS Catalog | 36 unique SNPs / 72 rows |
| ClinVar | 116 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 4 clinical annotations across 3 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 939 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'TNFRSF1B' and resolved to 'Tumor necrosis factor receptor superfamily member 1B' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 116 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 19 of 19 traits by best p-value, aggregated from 30 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P20333 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000028137/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL1250356/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/TNFRSF1B — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/TNFRSF1B — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=TNFRSF1B%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=TNFRSF1B — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/TNFRSF1B — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:26:31  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
