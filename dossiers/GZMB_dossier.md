# Protein Dossier — GZMB (Granzyme B)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: M54 Dorsalgia | 0.109 | 0.03 | 2.70e-04 | Wald ratio | 1 | cis | NA |
| Lung adenocarcinoma | -0.132 | 0.0441 | 0.00284 | Wald ratio | 1 | cis | NA |
| Neo-agreeableness | -0.307 | 0.106 | 0.00388 | Wald ratio | 1 | cis | NA |
| Creatinine (enzymatic) in urine | -0.0107 | 0.00413 | 0.00956 | Wald ratio | 1 | cis | NA |
| Forearm bone mineral density | 0.0705 | 0.0273 | 0.00994 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N40 Hyperplasia of prostate | -0.126 | 0.051 | 0.0137 | Wald ratio | 1 | cis | NA |
| Lung cancer | -0.0698 | 0.0301 | 0.0203 | Wald ratio | 1 | cis | NA |
| Cough on most days | -0.0538 | 0.0233 | 0.0211 | Wald ratio | 1 | cis | NA |
| Alcohol intake frequency | -0.0131 | 0.00637 | 0.0396 | Wald ratio | 1 | cis | NA |
| Birth weight | -0.0132 | 0.00643 | 0.0407 | Wald ratio | 1 | cis | NA |
| Mean cell haemoglobin | 0.0371 | 0.0185 | 0.0455 | Wald ratio | 1 | cis | NA |
| Potassium in urine | -0.00867 | 0.00438 | 0.0475 | Wald ratio | 1 | cis | NA |
| _...and 87 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4133_54_2` | Granzyme B | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_16 association rows across 11 traits (16 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating GZMB levels (id: OID00743_OID20604) | 2e-571 | rs8192917 | 1 | GCST90860084 | no MR -> candidate analysis |
| Circulating GZMB levels (id: OID00840_OID20604) | 3e-544 | rs8192917 | 1 | GCST90860165 | no MR -> candidate analysis |
| GZMA/GZMB protein level ratio | 3e-489 | rs8192917 | 1 | GCST90315007 | no MR -> candidate analysis |
| Granzyme B levels (GZMB.4133.54.2) | 6e-352 | rs8192917 | 2 | GCST90241324 | no MR -> candidate analysis |
| Serum levels of protein GZMB | 5e-131 | rs8192917 | 1 | GCST90087736 | no MR -> candidate analysis |
| Blood protein levels | 3e-83 | rs11539752 | 2 | GCST006585 | no MR -> candidate analysis |
| GZMB protein levels | 1e-39 | rs59268439 | 3 | GCST90469424 | no MR -> candidate analysis |
| Granzyme B (analyte X14041.13) levels | 1e-22 | rs8192917 | 1 | GCST90422424 | no MR -> candidate analysis |
| Vitiligo | 9e-16 | rs8192917 | 2 | GCST004785 | no MR -> candidate analysis |
| Hairy/enhancer-of-split related with YRPW motif protein 1 pr | 1e-9 | rs8192917 | 1 | GCST90437219 | no MR -> candidate analysis |
| Nuclear receptor coactivator 7 protein levels (SomaScan ID:4 | 3e-8 | rs2236338 | 1 | GCST90443089 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 961 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| vitiligo | 0.55 | — | common-variant locus | no MR -> candidate analysis |
| respiratory failure | 0.448 | — | common-variant locus | no MR -> candidate analysis |
| bone remodeling disease | 0.353 | — | common-variant locus | no MR -> candidate analysis |
| respiratory tract neoplasm | 0.314 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.306 | — | common-variant locus | no MR -> candidate analysis |
| diabetes mellitus | 0.158 | — | common-variant locus | no MR -> candidate analysis |

> Of the 6 rows above, **6 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Granzyme B) |
| gnomAD constraint | pLI=1e-10, LOEUF=1.54 — LoF-tolerant |
| GWAS Catalog | 35 unique SNPs / 70 rows |
| ClinVar | 78 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 961 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'GZMB' and resolved to 'Granzyme B' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 78 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 11 of 11 traits by best p-value, aggregated from 16 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P10144 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000100453/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2316/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/GZMB — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/GZMB — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=GZMB%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/GZMB — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:56:50  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
