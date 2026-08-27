# Protein Dossier — LRPAP1 (Alpha-2-macroglobulin receptor-associated protein)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Depressive symptoms | 0.0498 | 0.0176 | 0.00461 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Wrist | 0.149 | 0.0606 | 0.0138 | Wald ratio | 1 | cis | NA |
| Mean cell haemoglobin concentration | -0.0345 | 0.0155 | 0.0266 | Wald ratio | 1 | cis | NA |
| Neuroticism | 0.0381 | 0.0176 | 0.0303 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: D12 Benign neoplasm of colon  rectum  anus and anal canal | -0.216 | 0.104 | 0.0379 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: prostate cancer | -0.348 | 0.168 | 0.0388 | Wald ratio | 1 | cis | NA |
| Endometrioid ovarian cancer | 0.257 | 0.125 | 0.0394 | Wald ratio | 1 | cis | NA |
| Eczema | -0.159 | 0.0813 | 0.0507 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Cataract | -0.115 | 0.0597 | 0.0544 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: deep venous thrombosis (dvt) | 0.119 | 0.062 | 0.0552 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C61 Malignant neoplasm of prostate | -0.324 | 0.173 | 0.0604 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: uterine fibroids | -0.174 | 0.0953 | 0.0684 | Wald ratio | 1 | cis | NA |
| _...and 88 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3640_14_3` | RAP | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_27 association rows across 14 traits (26 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating LRPAP1 levels | 8e-324 | rs143486729 | 4 | GCST90859675 | no MR -> candidate analysis |
| LRPAP1 protein levels | 5e-298 | rs143486729 | 2 | GCST90469800 | no MR -> candidate analysis |
| alpha-2-macroglobulin receptor-associated protein levels | 3e-98 | rs1800493 | 4 | GCST90249239 | no MR -> candidate analysis |
| HGFAC protein levels | 4e-92 | rs183895110 | 5 | GCST90469448 | no MR -> candidate analysis |
| Circulating LRP1 levels | 1e-41 | rs143486729 | 1 | GCST90860254 | no MR -> candidate analysis |
| LRP1 protein levels | 2e-30 | rs143486729 | 2 | GCST90469797 | no MR -> candidate analysis |
| FVC | 2e-15 | rs10001975 | 1 | GCST90270083 | no MR -> candidate analysis |
| Cerebrospinal fluid protein LRPAP1 levels | 1e-14 | rs730748 | 1 | GCST90944406 | no MR -> candidate analysis |
| Nonsyndromic cleft palate | 5e-11 | rs3468 | 1 | GCST009356 | no MR -> candidate analysis |
| Height (baseline) | 5e-11 | rs13325 | 1 | GCST90565843 | no MR -> candidate analysis |
| Body fat percentage (adjusted for testosterone and SHBG) | 2e-9 | rs112726576 | 2 | GCST90432180 | no MR -> candidate analysis |
| Forced expiratory volume (baseline) | 8e-9 | rs13125213 | 1 | GCST90565844 | no MR -> candidate analysis |
| _...and 2 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 455 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Rare isolated myopia | 0.765 | — | established (curated) | no MR -> candidate analysis |
| Abnormality of limbs | 0.4 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.253 | — | common-variant locus | no MR -> candidate analysis |
| cleft palate | 0.248 | — | common-variant locus | no MR -> candidate analysis |
| bronchial disorder | 0.144 | — | common-variant locus | no MR -> candidate analysis |
| congenital anomaly of cardiovascular system | 0.101 | — | common-variant locus | no MR -> candidate analysis |
| spinal cord injury | 0.101 | — | common-variant locus | no MR -> candidate analysis |

> Of the 7 rows above, **7 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=7.5e-15, LOEUF=1.33 — LoF-tolerant |
| GWAS Catalog | 117 unique SNPs / 282 rows |
| ClinVar | 262 records; 13 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 455 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'LRPAP1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 262 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 14 of 14 traits by best p-value, aggregated from 27 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P30533 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000163956/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/LRPAP1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/LRPAP1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=LRPAP1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/LRPAP1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:37:54  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
