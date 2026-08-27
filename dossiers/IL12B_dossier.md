# Protein Dossier — IL12B (Interleukin-12 subunit beta)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Inflammatory bowel disease | 0.418 | 0.0345 | 9.59e-34 | Wald ratio | 1 | cis | 1.41e-12 |
| Crohn's disease | 0.44 | 0.0419 | 7.95e-26 | Wald ratio | 1 | cis | 7.34e-12 |
| Ulcerative colitis | 0.365 | 0.0435 | 4.56e-17 | Wald ratio | 1 | cis | 3.23e-07 |
| Non-cancer illness code  self-reported: psoriasis | -0.00555 | 0.000892 | 5.10e-10 | Wald ratio | 1 | cis | 0.989 |
| High grade serous ovarian cancer | 0.229 | 0.0863 | 0.00794 | Wald ratio | 1 | trans | NA |
| Ovarian cancer | 0.188 | 0.0727 | 0.00958 | Wald ratio | 1 | trans | NA |
| Height | 0.0253 | 0.0102 | 0.0136 | Wald ratio | 1 | cis | NA |
| Internalizing problems | 0.174 | 0.0765 | 0.0228 | Wald ratio | 1 | cis | NA |
| Caudate volume | -36.5 | 16.8 | 0.0294 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Arm | -0.00177 | 0.00084 | 0.0352 | Wald ratio | 1 | cis | NA |
| Squamous cell lung cancer | 0.188 | 0.0893 | 0.0358 | Wald ratio | 1 | cis | NA |
| Alcohol intake frequency | 0.024 | 0.0122 | 0.0491 | Wald ratio | 1 | cis | NA |
| _...and 90 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4494_63_2` | IL-23 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_258 association rows across 107 traits (215 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating IL12B levels (id: OID00523_OID20666) | 3e-2108 | rs4244437 | 3 | GCST90859879 | no MR -> candidate analysis |
| Circulating IL12B levels (id: OID00368_OID20666) | 4e-1702 | rs4244437 | 3 | GCST90859730 | no MR -> candidate analysis |
| CD83/IL12A_IL12B protein level ratio | 5e-1617 | rs6556416 | 1 | GCST90313905 | no MR -> candidate analysis |
| CD38/IL12A_IL12B protein level ratio | 2e-1488 | rs6556416 | 1 | GCST90313808 | no MR -> candidate analysis |
| Circulating IL12A_IL12B levels | 2e-1474 | rs4244437 | 3 | GCST90860167 | no MR -> candidate analysis |
| CD302/IL12A_IL12B protein level ratio | 2e-1406 | rs6556416 | 1 | GCST90313806 | no MR -> candidate analysis |
| GZMA/IL12A_IL12B protein level ratio | 1e-1400 | rs6556416 | 1 | GCST90315009 | no MR -> candidate analysis |
| IL12A_IL12B/LAG3 protein level ratio | 8e-1395 | rs6556416 | 1 | GCST90315147 | no MR -> candidate analysis |
| BSG/IL12A_IL12B protein level ratio | 1e-1369 | rs6556416 | 1 | GCST90313532 | no MR -> candidate analysis |
| GFRA2/IL12A_IL12B protein level ratio | 2e-1367 | rs6556416 | 1 | GCST90314925 | no MR -> candidate analysis |
| Interleukin-12 subunit beta levels | 1e-361 | rs10076557 | 4 | GCST90274798 | no MR -> candidate analysis |
| Bone mineral density mean | 1e-300 | rs12513881 | 1 | GCST90321120 | no MR -> candidate analysis |
| _...and 95 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 513 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| psoriasis | 0.967 | — | common-variant locus | MR: beta=-0.00555, p=5.10e-10 (cis) |
| Crohn disease | 0.921 | — | common-variant locus | no MR -> candidate analysis |
| psoriasis vulgaris | 0.928 | — | common-variant locus | no MR -> candidate analysis |
| psoriatic arthritis | 0.901 | — | common-variant locus | no MR -> candidate analysis |
| ulcerative colitis | 0.883 | — | common-variant locus | MR: beta=0.365, p=4.56e-17 (cis) |
| inflammatory bowel disease | 0.887 | — | common-variant locus | MR: beta=0.418, p=9.59e-34 (cis) |
| skin disorder | 0.893 | — | common-variant locus | no MR -> candidate analysis |
| seborrheic dermatitis | 0.849 | — | common-variant locus | no MR -> candidate analysis |
| erythematosquamous dermatosis | 0.814 | — | common-variant locus | no MR -> candidate analysis |
| Oral ulcer | 0.749 | — | common-variant locus | no MR -> candidate analysis |
| type 2 diabetes mellitus | 0.757 | — | common-variant locus | no MR -> candidate analysis |
| Takayasu arteritis | 0.598 | — | common-variant locus | no MR -> candidate analysis |
| systemic lupus erythematosus | 0.601 | — | common-variant locus | no MR -> candidate analysis |
| multiple sclerosis | 0.592 | — | common-variant locus | no MR -> candidate analysis |
| primary biliary cholangitis | 0.593 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **12 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Interleukin-12 subunit beta) |
| gnomAD constraint | pLI=6.6e-07, LOEUF=0.949 — LoF-tolerant |
| GWAS Catalog | 172 unique SNPs / 424 rows |
| ClinVar | 271 records; 5 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 2 clinical annotations across 2 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 513 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'IL12B' and resolved to 'Interleukin-12 subunit beta' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 271 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 20 of 107 traits by best p-value, aggregated from 258 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P29460 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000113302/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3580484/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/IL12B — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/IL12B — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=IL12B%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=IL12B — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/IL12B — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:10:30  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
