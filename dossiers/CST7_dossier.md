# Protein Dossier — CST7 (Cystatin-F)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Mean cell haemoglobin concentration | -0.0146 | 0.00564 | 0.00984 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Other bones | 0.0393 | 0.0156 | 0.0119 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K29 Gastritis and duodenitis | 0.0566 | 0.0229 | 0.0133 | Wald ratio | 1 | cis | NA |
| Type 2 diabetes | 0.0764 | 0.0316 | 0.0155 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R35 Polyuria | -0.166 | 0.0711 | 0.0194 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: enlarged prostate | 0.0683 | 0.0299 | 0.0222 | Wald ratio | 1 | cis | NA |
| Age at menopause | 0.118 | 0.0525 | 0.0244 | Wald ratio | 1 | cis | NA |
| Sodium in urine | -0.00805 | 0.00368 | 0.0288 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M23 Internal derangement of knee | 0.0506 | 0.0239 | 0.0344 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Injury or trauma resulting in loss of vision | 0.0927 | 0.0446 | 0.0376 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: mania or bipolar disorder or manic depression | -0.185 | 0.089 | 0.038 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M72 Fibroblastic disorders | 0.095 | 0.0464 | 0.0404 | Wald ratio | 1 | cis | NA |
| _...and 92 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3302_58_1` | CYTF | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_22 association rows across 13 traits (21 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Cystatin-F levels | 4e-296 | rs76897221 | 3 | GCST90247218 | no MR -> candidate analysis |
| CST7 protein levels | 3e-233 | rs146160238 | 5 | GCST90468897 | no MR -> candidate analysis |
| Cerebrospinal fluid protein CST7 levels | 5e-80 | rs227653 | 1 | GCST90944227 | no MR -> candidate analysis |
| Cystatin-F levels (CST7.3302.58.1) | 6e-67 | rs76897221 | 2 | GCST90240832 | no MR -> candidate analysis |
| APMAP protein levels | 7e-46 | rs6050201 | 2 | GCST90453381 | no MR -> candidate analysis |
| Serum levels of protein CST7 | 5e-44 | rs73112274 | 2 | GCST90087734 | no MR -> candidate analysis |
| Eosinophil side scatter | 2e-36 | rs6050179 | 1 | GCST90281230 | no MR -> candidate analysis |
| Eosinophil side fluorescence | 2e-18 | rs6050181 | 1 | GCST90281231 | no MR -> candidate analysis |
| Adipocyte plasma membrane-associated protein levels (APMAP.1 | 3e-15 | rs73112274 | 1 | GCST90240199 | no MR -> candidate analysis |
| Eosinophil forward scatter | 4e-15 | rs1056036 | 1 | GCST90281232 | no MR -> candidate analysis |
| Tyrosine-protein phosphatase non-receptor type 4 levels (PTP | 3e-13 | rs227646 | 1 | GCST90243219 | no MR -> candidate analysis |
| C-reactive protein levels | 2e-9 | rs2256027 | 1 | GCST009777 | no MR -> candidate analysis |
| _...and 1 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 167 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| obesity disorder | 0.415 | — | common-variant locus | no MR -> candidate analysis |
| ovarian dysfunction | 0.389 | — | common-variant locus | no MR -> candidate analysis |
| smoking initiation | 0.046 | — | common-variant locus | no MR -> candidate analysis |
| frozen shoulder | 0.039 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.8e-06, LOEUF=1.76 — LoF-tolerant |
| GWAS Catalog | 80 unique SNPs / 160 rows |
| ClinVar | 42 records; 6 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 167 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CST7'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 42 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 13 of 13 traits by best p-value, aggregated from 22 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O76096 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000077984/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CST7 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CST7 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CST7%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CST7 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:08:32  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
