# Protein Dossier — TNFRSF6B (Tumor necrosis factor receptor superfamily member 6B)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Invasive mucinous ovarian cancer | -0.731 | 0.267 | 0.00625 | Wald ratio | 1 | cis | NA |
| ER-negative Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.123 | 0.0763 | 0.107 | Wald ratio | 1 | cis | NA |
| Birth weight | -0.0402 | 0.033 | 0.224 | Wald ratio | 1 | cis | NA |
| Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0446 | 0.0415 | 0.282 | Wald ratio | 1 | cis | NA |
| Endometrioid ovarian cancer | 0.149 | 0.185 | 0.421 | Wald ratio | 1 | cis | NA |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5070_76_3` | DcR3 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_183 association rows across 84 traits (170 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Telomere length (principal component 1) | 1e-300 | rs35640778 | 9 | GCST90435144 | no MR -> candidate analysis |
| Circulating TNFRSF6B levels | 2e-199 | rs118149249 | 3 | GCST90860007 | no MR -> candidate analysis |
| Leukocyte telomere length | 3e-144 | rs35640778 | 9 | GCST90709782 | no MR -> candidate analysis |
| Atopic dermatitis | 5e-109 | rs6062486 | 17 | GCST90244787 | no MR -> candidate analysis |
| TNFRSF6B protein levels | 4e-59 | rs115610405 | 5 | GCST90470914 | no MR -> candidate analysis |
| Glioblastoma | 4e-46 | rs2297440 | 4 | GCST004349 | no MR -> candidate analysis |
| Inflammatory bowel disease | 2e-44 | rs6062496 | 4 | GCST90292538 | no MR -> candidate analysis |
| Glioma | 2e-42 | rs2297440 | 8 | GCST004347 | no MR -> candidate analysis |
| Telomere length | 3e-33 | rs41309367 | 8 | GCST90103979 | no MR -> candidate analysis |
| Chronic inflammatory diseases (ankylosing spondylitis, Crohn | 2e-30 | rs6062496 | 1 | GCST005537 | no MR -> candidate analysis |
| Ulcerative colitis | 4e-26 | rs6062496 | 3 | GCST90446794 | no MR -> candidate analysis |
| Prostate cancer | 7e-26 | rs77552606 | 7 | GCST90274713 | no MR -> candidate analysis |
| _...and 72 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 327 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Wheezing | 0.66 | — | common-variant locus | no MR -> candidate analysis |
| prostate carcinoma | 0.624 | — | common-variant locus | no MR -> candidate analysis |
| atopic eczema | 0.64 | — | common-variant locus | no MR -> candidate analysis |
| idiopathic pulmonary fibrosis | 0.63 | — | common-variant locus | no MR -> candidate analysis |
| Crohn disease | 0.513 | — | common-variant locus | no MR -> candidate analysis |
| lower respiratory tract disorder | 0.495 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.483 | — | common-variant locus | no MR -> candidate analysis |
| dermatitis | 0.464 | — | common-variant locus | no MR -> candidate analysis |
| metabolic syndrome | 0.454 | — | common-variant locus | no MR -> candidate analysis |
| ulcerative colitis | 0.433 | — | common-variant locus | no MR -> candidate analysis |
| inflammatory bowel disease | 0.43 | — | common-variant locus | no MR -> candidate analysis |
| type 2 diabetes mellitus | 0.417 | — | common-variant locus | no MR -> candidate analysis |
| respiratory system disorder | 0.366 | — | common-variant locus | no MR -> candidate analysis |
| actinic keratosis | 0.359 | — | common-variant locus | no MR -> candidate analysis |
| asthma | 0.313 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **15 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=4.3e-10, LOEUF=1.82 — LoF-tolerant |
| GWAS Catalog | 178 unique SNPs / 492 rows |
| ClinVar | 561 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 327 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'TNFRSF6B'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 561 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 84 traits by best p-value, aggregated from 183 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O95407 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000243509/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/TNFRSF6B — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/TNFRSF6B — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=TNFRSF6B%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/TNFRSF6B — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:26:49  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
