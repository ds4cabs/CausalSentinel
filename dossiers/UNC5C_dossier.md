# Protein Dossier — UNC5C (Netrin receptor UNC5C)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Forearm bone mineral density | -0.113 | 0.0644 | 0.08 | Wald ratio | 1 | cis | NA |
| Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.033 | 0.0271 | 0.223 | Wald ratio | 1 | cis | NA |
| ER-positive Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0367 | 0.0323 | 0.255 | Wald ratio | 1 | cis | NA |
| Low grade serous ovarian cancer | -0.186 | 0.196 | 0.341 | Wald ratio | 1 | cis | NA |
| Endometrioid ovarian cancer | 0.0914 | 0.117 | 0.436 | Wald ratio | 1 | cis | NA |
| Clear cell ovarian cancer | -0.111 | 0.164 | 0.497 | Wald ratio | 1 | cis | NA |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5139_32_3` | UNC5H3 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_90 association rows across 66 traits (58 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Netrin receptor UNC5C levels | 9e-55 | rs13134684 | 3 | GCST90248759 | no MR -> candidate analysis |
| Netrin receptor UNC5B levels | 7e-31 | rs61432083 | 2 | GCST90248758 | no MR -> candidate analysis |
| Netrin receptor UNC5C levels (UNC5C.5139.32.3) | 2e-25 | rs57091121 | 2 | GCST90242044 | no MR -> candidate analysis |
| Metabolic syndrome | 1e-20 | rs3775002 | 3 | GCST90444487 | no MR -> candidate analysis |
| Serum levels of protein UNC5C | 5e-18 | rs35063103 | 1 | GCST90088952 | no MR -> candidate analysis |
| GLIPR1 protein levels | 5e-16 | rs151067671 | 1 | GCST90469357 | no MR -> candidate analysis |
| Cerebellar grey matter morphology (MOSTest) | 3e-13 | rs10026552 | 1 | GCST90728589 | no MR -> candidate analysis |
| Body mass index | 6e-13 | rs10856911 | 10 | GCST90662912 | no MR -> candidate analysis |
| Systolic blood pressure | 1e-12 | rs35508536 | 1 | GCST90435415 | no MR -> candidate analysis |
| Netrin receptor UNC5B (analyte X7776.20) levels | 1e-12 | rs13118653 | 1 | GCST90427061 | no MR -> candidate analysis |
| Blood protein levels | 2e-11 | rs10030217 | 1 | GCST006585 | no MR -> candidate analysis |
| Type 2 diabetes | 2e-11 | rs2289043 | 5 | GCST90492734 | no MR -> candidate analysis |
| _...and 54 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1812 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| type 2 diabetes mellitus | 0.72 | — | common-variant locus | no MR -> candidate analysis |
| diabetes mellitus | 0.67 | — | common-variant locus | no MR -> candidate analysis |
| hypertensive disorder | 0.652 | — | common-variant locus | no MR -> candidate analysis |
| angina pectoris | 0.627 | — | common-variant locus | no MR -> candidate analysis |
| myocardial ischemia | 0.597 | — | common-variant locus | no MR -> candidate analysis |
| bilirubin metabolism disease | 0.537 | — | common-variant locus | no MR -> candidate analysis |
| diabetic ketoacidosis | 0.523 | — | common-variant locus | no MR -> candidate analysis |
| Hypocalcemia | 0.523 | — | common-variant locus | no MR -> candidate analysis |
| ovarian dysfunction | 0.511 | — | common-variant locus | no MR -> candidate analysis |
| placental retention | 0.51 | — | common-variant locus | no MR -> candidate analysis |
| appendicitis | 0.51 | — | common-variant locus | no MR -> candidate analysis |
| placental abruption | 0.497 | — | common-variant locus | no MR -> candidate analysis |
| placenta praevia | 0.485 | — | common-variant locus | no MR -> candidate analysis |
| fracture of pelvis | 0.485 | — | common-variant locus | no MR -> candidate analysis |
| device complication | 0.485 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **15 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.00019, LOEUF=0.601 — LoF-tolerant |
| GWAS Catalog | 117 unique SNPs / 197 rows |
| ClinVar | 190 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1812 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'UNC5C'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 190 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 66 traits by best p-value, aggregated from 90 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O95185 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000182168/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/UNC5C — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/UNC5C — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=UNC5C%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/UNC5C — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:33:00  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
