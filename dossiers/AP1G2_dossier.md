# Protein Dossier — AP1G2 (AP-1 complex subunit gamma-like 2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: C50 Malignant neoplasm of breast | 0.226 | 0.0793 | 0.00434 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: ankylosing spondylitis | 0.418 | 0.162 | 0.0102 | Wald ratio | 1 | cis | NA |
| Height | -0.041 | 0.0164 | 0.0124 | Wald ratio | 1 | cis | NA |
| Depressive symptoms | 0.0522 | 0.0224 | 0.0196 | Wald ratio | 1 | cis | NA |
| Endometrioid ovarian cancer | 0.483 | 0.214 | 0.0242 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: kidney stone or ureter stone or bladder stone | -0.595 | 0.285 | 0.0367 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hiatus hernia | 0.149 | 0.0719 | 0.038 | Wald ratio | 1 | cis | NA |
| Paget's disease | -0.634 | 0.309 | 0.0399 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: migraine | 0.127 | 0.0646 | 0.0501 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | -0.0312 | 0.0164 | 0.0564 | Wald ratio | 1 | cis | NA |
| Birth length | -0.101 | 0.0534 | 0.0572 | Wald ratio | 1 | cis | NA |
| Diastolic blood pressure  automated reading | -0.0242 | 0.0129 | 0.0607 | Wald ratio | 1 | cis | NA |
| _...and 90 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_7 association rows across 6 traits (6 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| AP1G2 protein levels | 6e-38 | rs77436356 | 2 | GCST90468323 | no MR -> candidate analysis |
| AP-1 complex subunit gamma-like 2 levels | 1e-34 | rs12897422 | 1 | GCST90246528 | no MR -> candidate analysis |
| THTPA protein levels | 1e-15 | rs12897422 | 1 | GCST90470860 | no MR -> candidate analysis |
| Blood protein levels | 1e-14 | rs12897422 | 1 | GCST006585 | no MR -> candidate analysis |
| Eosinophil count | 3e-8 | rs77436356 | 1 | GCST007065 | no MR -> candidate analysis |
| Sudden cardiac arrest | 6e-8 | rs2281680 | 1 | GCST001099 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 62 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Tracheoesophageal fistula | 0.426 | — | established (curated) | no MR -> candidate analysis |
| esophageal atresia/tracheoesophageal fistula | 0.426 | — | established (curated) | no MR -> candidate analysis |
| Global developmental delay | 0.195 | — | established (curated) | no MR -> candidate analysis |
| Genu valgum | 0.072 | — | common-variant locus | no MR -> candidate analysis |
| Genu varum | 0.072 | — | common-variant locus | no MR -> candidate analysis |

> Of the 5 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=7.1e-26, LOEUF=1.06 — LoF-tolerant |
| GWAS Catalog | 17 unique SNPs / 34 rows |
| ClinVar | 179 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 62 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'AP1G2'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 179 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 6 of 6 traits by best p-value, aggregated from 7 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O75843 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000213983/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/AP1G2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/AP1G2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=AP1G2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/AP1G2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:05:21  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
