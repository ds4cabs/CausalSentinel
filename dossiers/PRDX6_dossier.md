# Protein Dossier — PRDX6 (Peroxiredoxin-6)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Forced vital capacity (FVC) | 0.0215 | 0.00612 | 4.51e-04 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | 0.0206 | 0.00646 | 0.00142 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | -0.0303 | 0.00966 | 0.00171 | Wald ratio | 1 | cis | NA |
| Birth weight | 0.0305 | 0.0111 | 0.00616 | Wald ratio | 1 | cis | NA |
| Alcohol intake frequency | -0.0301 | 0.011 | 0.0063 | Wald ratio | 1 | cis | NA |
| Rheumatoid arthritis | -0.095 | 0.0356 | 0.00772 | Wald ratio | 1 | cis | NA |
| Schizophrenia | -0.0857 | 0.0327 | 0.00874 | Wald ratio | 1 | cis | NA |
| Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.0484 | 0.0196 | 0.0135 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: gastro-oesophageal reflux (gord)  or  gastric reflux | 0.0808 | 0.0332 | 0.015 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: migraine | -0.116 | 0.0485 | 0.0172 | Wald ratio | 1 | cis | NA |
| Sleep duration | -0.0139 | 0.00583 | 0.0174 | Wald ratio | 1 | cis | NA |
| Body fat | 0.4 | 0.169 | 0.018 | Wald ratio | 1 | cis | NA |
| _...and 104 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5018_68_1` | Peroxiredoxin-6 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_19 association rows across 16 traits (14 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| CASP8/PRDX6 protein level ratio | 5e-102 | rs7549074 | 1 | GCST90313655 | no MR -> candidate analysis |
| PRDX6 protein levels | 1e-95 | rs7529089 | 2 | GCST90470319 | no MR -> candidate analysis |
| Serum levels of protein PRDX6 | 9e-53 | rs34259759 | 1 | GCST90088875 | no MR -> candidate analysis |
| Blood protein levels | 9e-33 | rs6671141 | 1 | GCST006585 | no MR -> candidate analysis |
| TNN protein levels | 2e-22 | rs569204712 | 2 | GCST90470927 | no MR -> candidate analysis |
| Circulating PRDX6 levels | 4e-22 | rs35263596 | 1 | GCST90860534 | no MR -> candidate analysis |
| Ease of getting up in the morning | 1e-11 | rs148137538 | 1 | GCST007986 | no MR -> candidate analysis |
| Body mass index | 2e-9 | rs148137538 | 2 | GCST009871 | no MR -> candidate analysis |
| Non-alcoholic fatty liver disease or type 2 diabetes | 5e-9 | rs61828878 | 1 | GCST90272881 | no MR -> candidate analysis |
| Morningness | 6e-9 | rs148137538 | 1 | GCST007983 | no MR -> candidate analysis |
| Adult body size | 4e-8 | rs148137538 | 1 | GCST010988 | no MR -> candidate analysis |
| Phosphate levels | 8e-8 | rs571961047 | 1 | GCST90245374 | no MR -> candidate analysis |
| _...and 4 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 657 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| hypothyroidism | 0.543 | — | common-variant locus | MR: beta=-0.0479, p=0.169 (cis) |
| systemic lupus erythematosus | 0.469 | — | common-variant locus | MR: beta=-0.134, p=0.362 (cis) |
| rheumatoid arthritis | 0.468 | — | common-variant locus | MR: beta=-0.095, p=0.00772 (cis) |
| placental retention | 0.382 | — | common-variant locus | no MR -> candidate analysis |
| systemic sclerosis | 0.338 | — | common-variant locus | no MR -> candidate analysis |
| COVID-19 | 0.329 | — | common-variant locus | no MR -> candidate analysis |
| tricuspid valve disorder | 0.32 | — | common-variant locus | no MR -> candidate analysis |
| type 2 diabetes mellitus | 0.197 | — | common-variant locus | no MR -> candidate analysis |
| metabolic dysfunction-associated steatotic liver disease | 0.197 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.18 | — | common-variant locus | no MR -> candidate analysis |

> Of the 10 rows above, **7 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Peroxiredoxin-6) |
| gnomAD constraint | pLI=0.0013, LOEUF=1.03 — LoF-tolerant |
| GWAS Catalog | 37 unique SNPs / 73 rows |
| ClinVar | 71 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 657 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'PRDX6' and resolved to 'Peroxiredoxin-6' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 71 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 16 of 16 traits by best p-value, aggregated from 19 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P30041 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000117592/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4295741/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PRDX6 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PRDX6 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PRDX6%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PRDX6 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:36:12  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
