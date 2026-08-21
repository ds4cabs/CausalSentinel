# Protein Dossier — GNLY (Granulysin)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Birth weight | 0.019 | 0.00556 | 6.29e-04 | Wald ratio | 1 | cis | NA |
| Height | 0.012 | 0.00452 | 0.00788 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K44 Diaphragmatic hernia | 0.0721 | 0.0277 | 0.00921 | Wald ratio | 1 | cis | NA |
| Bipolar disorder | -0.1 | 0.0388 | 0.00966 | Wald ratio | 1 | cis | NA |
| Diastolic blood pressure  automated reading | -0.00913 | 0.0038 | 0.0164 | Wald ratio | 1 | cis | NA |
| Vascular or heart problems diagnosed by doctor: Angina | -0.0512 | 0.0219 | 0.0195 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K40 Inguinal hernia | 0.0499 | 0.0216 | 0.0209 | Wald ratio | 1 | cis | NA |
| Caudate volume | 16.1 | 7.52 | 0.0324 | Wald ratio | 1 | cis | NA |
| IgA nephropathy | -0.284 | 0.135 | 0.035 | Wald ratio | 1 | cis | NA |
| Age at menopause | -0.0517 | 0.0259 | 0.0455 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: kidney stone or ureter stone or bladder stone | -0.0919 | 0.0461 | 0.0461 | Wald ratio | 1 | cis | NA |
| Primary sclerosing cholangitis  | 0.0875 | 0.044 | 0.0466 | Wald ratio | 1 | cis | NA |
| _...and 86 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3195_50_2` | Granulysin | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_58 association rows across 24 traits (56 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating GNLY levels | 6e-2124 | rs7603438 | 5 | GCST90860460 | no MR -> candidate analysis |
| GNLY/GZMA protein level ratio | 1e-2062 | rs751163 | 1 | GCST90314949 | no MR -> candidate analysis |
| Granulysin levels | 5e-802 | rs12151621 | 14 | GCST90247802 | no MR -> candidate analysis |
| Serum levels of protein GNLY | 7e-260 | rs12151742 | 4 | GCST90088260 | no MR -> candidate analysis |
| Blood protein levels | 5e-214 | rs7603438 | 3 | GCST006585 | no MR -> candidate analysis |
| Granulysin levels (GNLY.3195.50.2) | 7e-189 | rs12151621 | 2 | GCST90241322 | no MR -> candidate analysis |
| Granulysin (analyte X14102.6) levels | 7e-188 | rs12151742 | 1 | GCST90422468 | no MR -> candidate analysis |
| Granulysin (analyte X3195.50) levels | 2e-165 | rs12151742 | 1 | GCST90425647 | no MR -> candidate analysis |
| GNLY protein levels | 8e-158 | rs192642287 | 12 | GCST90469372 | no MR -> candidate analysis |
| Cerebrospinal fluid protein GNLY levels | 2e-87 | rs7603438 | 1 | GCST90944771 | no MR -> candidate analysis |
| Granulysin level in Chronic kidney disease with hypertension | 2e-51 | rs12151742 | 1 | GCST90234189 | no MR -> candidate analysis |
| Granulysin level in Chronic kidney disease with hypertension | 1e-44 | rs12151742 | 1 | GCST90237265 | no MR -> candidate analysis |
| _...and 12 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 331 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| cataract | 0.19 | 0.19 | exploratory rare-variant signal | MR: beta=-0.0658, p=0.146 (cis) |
| vertebral column disorder | 0.167 | — | common-variant locus | no MR -> candidate analysis |
| brain aneurysm | 0.167 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.087 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 1 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=4.5e-05, LOEUF=1.25 — LoF-tolerant |
| GWAS Catalog | 98 unique SNPs / 187 rows |
| ClinVar | 60 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 331 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'GNLY'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 60 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 24 traits by best p-value, aggregated from 58 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P22749 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000115523/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/GNLY — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/GNLY — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=GNLY%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/GNLY — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:50:16  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
