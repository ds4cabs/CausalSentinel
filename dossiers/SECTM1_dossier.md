# Protein Dossier — SECTM1 (Secreted and transmembrane protein 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Hirschsprung's disease | -1.61 | 0.588 | 0.00629 | Wald ratio | 1 | cis | NA |
| Caudate volume | -51.7 | 20.9 | 0.0132 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | 0.197 | 0.0845 | 0.0201 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: S76 Injury of muscle and tendon at hip and thigh level | 0.564 | 0.249 | 0.0236 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: D25 Leiomyoma of uterus | 0.147 | 0.0656 | 0.0251 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: high cholesterol | 0.0479 | 0.0221 | 0.0302 | Wald ratio | 1 | cis | NA |
| Parkinson's disease | -0.307 | 0.146 | 0.0352 | Wald ratio | 1 | cis | NA |
| Cough on most days | 0.0836 | 0.0404 | 0.0386 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: emphysema or chronic bronchitis | 0.134 | 0.0652 | 0.0395 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: asthma | -0.0513 | 0.0253 | 0.0426 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C61 Malignant neoplasm of prostate | 0.18 | 0.0887 | 0.0428 | Wald ratio | 1 | cis | NA |
| Subjective well being | -0.0214 | 0.0107 | 0.0455 | Wald ratio | 1 | cis | NA |
| _...and 106 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_16 association rows across 10 traits (16 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Secreted and transmembrane protein 1 levels | 8e-132 | rs4789763 | 5 | GCST90249478 | no MR -> candidate analysis |
| CD7 protein levels | 5e-120 | rs117376412 | 3 | GCST90468649 | no MR -> candidate analysis |
| Blood protein levels | 1e-61 | rs116473040 | 1 | GCST006585 | no MR -> candidate analysis |
| Serum levels of protein SECTM1 | 4e-39 | rs4789763 | 1 | GCST90087368 | no MR -> candidate analysis |
| T-cell antigen CD7 levels | 7e-33 | rs11575031 | 1 | GCST90421637 | no MR -> candidate analysis |
| Secreted and transmembrane protein 1 levels (SECTM1.13093.6. | 4e-30 | rs4789763 | 1 | GCST90242725 | no MR -> candidate analysis |
| Monocyte percentage of white cells | 8e-18 | rs76787525 | 1 | GCST90002394 | no MR -> candidate analysis |
| Benign neoplasm of thyroid glands (PheCode 226) | 7e-12 | rs117913733 | 1 | GCST90651229 | no MR -> candidate analysis |
| Gut microbiome abundance (class Bacteroides sp. 8 (at 1 year | 1e-9 | rs77560416 | 1 | GCST90569028 | no MR -> candidate analysis |
| Gut microbiome abundance (class Bacteroides sp. 8 (at 1 year | 2e-9 | rs77560416 | 1 | GCST90569048 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 85 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| hypothyroidism | 0.265 | — | common-variant locus | MR: beta=0.0544, p=0.132 (cis) |
| benign thyroid gland neoplasm | 0.04 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.019, LOEUF=0.939 — LoF-tolerant |
| GWAS Catalog | 57 unique SNPs / 114 rows |
| ClinVar | 83 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 85 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'SECTM1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 83 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 10 of 10 traits by best p-value, aggregated from 16 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q8WVN6 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000141574/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/SECTM1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/SECTM1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=SECTM1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/SECTM1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:57:10  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
