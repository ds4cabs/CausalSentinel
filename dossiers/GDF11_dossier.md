# Protein Dossier — GDF11 (Growth/differentiation factor 11)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Body mass index (BMI) | -0.0539 | 0.0101 | 1.06e-07 | Inverse variance weighted | 2 | trans | 0.0313 |
| Body mass index (BMI) | -0.0539 | 0.0101 | 1.06e-07 | Inverse variance weighted | 2 | trans | 0.139 |
| Eczema | 0.264 | 0.0718 | 2.32e-04 | Inverse variance weighted | 2 | trans | NA |
| Eczema | 0.264 | 0.0718 | 2.32e-04 | Inverse variance weighted | 2 | trans | NA |
| Ulcerative colitis | -0.222 | 0.0773 | 0.00412 | Wald ratio | 1 | trans | NA |
| Lung adenocarcinoma | -0.297 | 0.116 | 0.0107 | Inverse variance weighted | 2 | trans | NA |
| Lung adenocarcinoma | -0.297 | 0.116 | 0.0107 | Inverse variance weighted | 2 | trans | NA |
| Diagnoses - main ICD10: D25 Leiomyoma of uterus | -0.304 | 0.123 | 0.0139 | Inverse variance weighted | 2 | trans | NA |
| Diagnoses - main ICD10: D25 Leiomyoma of uterus | -0.304 | 0.123 | 0.0139 | Inverse variance weighted | 2 | trans | NA |
| Diastolic blood pressure  automated reading | -0.0243 | 0.0104 | 0.0192 | Inverse variance weighted | 2 | trans | NA |
| Diastolic blood pressure  automated reading | -0.0243 | 0.0104 | 0.0192 | Inverse variance weighted | 2 | trans | NA |
| Neuroblastoma | -0.407 | 0.182 | 0.0258 | Inverse variance weighted | 2 | trans | NA |
| _...and 187 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2765_4_3` | GDF-11 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_2 association rows across 2 traits (2 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| CD63 protein levels | 2e-18 | rs188443236 | 1 | GCST90468642 | no MR -> candidate analysis |
| Circulating CD63 levels | 5e-18 | rs188443236 | 1 | GCST90860756 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 2457 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| vertebral hypersegmentation and orofacial anomalies | 0.58 | — | established (curated) | no MR -> candidate analysis |
| orofacial cleft | 0.426 | — | established (curated) | no MR -> candidate analysis |
| neurodevelopmental disorder | 0.195 | — | established (curated) | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.86, LOEUF=0.565 — LoF-tolerant |
| GWAS Catalog | 27 unique SNPs / 54 rows |
| ClinVar | 61 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 2457 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'GDF11'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 61 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 2 of 2 traits by best p-value, aggregated from 2 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O95390 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000135414/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/GDF11 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/GDF11 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=GDF11%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/GDF11 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:47:05  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
