# Protein Dossier — IL23R (Interleukin-23 receptor)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Inflammatory bowel disease | 1.5 | 0.0546 | 2.21e-166 | Wald ratio | 1 | cis | 0.753 |
| Crohn's disease | 1.84 | 0.0707 | 5.80e-149 | Wald ratio | 1 | cis | 0.993 |
| Ulcerative colitis | 1.14 | 0.0686 | 4.34e-62 | Wald ratio | 1 | cis | 0.82 |
| Non-cancer illness code  self-reported: psoriasis | 0.431 | 0.0704 | 9.48e-10 | Wald ratio | 1 | cis | 0.971 |
| Non-cancer illness code  self-reported: ankylosing spondylitis | 0.524 | 0.131 | 6.19e-05 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hiatus hernia | 0.177 | 0.0632 | 0.00513 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: gout | 0.186 | 0.0803 | 0.0208 | Wald ratio | 1 | cis | NA |
| Primary sclerosing cholangitis  | 0.324 | 0.15 | 0.0305 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K57 Diverticular disease of intestine | 0.148 | 0.0699 | 0.0345 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Other bones | 0.0941 | 0.0454 | 0.0383 | Wald ratio | 1 | cis | NA |
| Femoral neck bone mineral density | -0.0703 | 0.0348 | 0.0435 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K29 Gastritis and duodenitis | 0.13 | 0.0653 | 0.0459 | Wald ratio | 1 | cis | NA |
| _...and 60 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5088_175_3` | IL-23 R | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_113 association rows across 44 traits (94 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Inflammatory bowel disease | 2e-170 | rs7547569 | 9 | GCST003043 | MR: beta=1.5, p=2.21e-166 (cis) |
| Crohn's disease | 1e-159 | rs7517847 | 19 | GCST003044 | MR: beta=1.84, p=5.80e-149 (cis) |
| Chronic inflammatory diseases (ankylosing spondylitis, Crohn | 1e-143 | rs80174646 | 4 | GCST005537 | no MR -> candidate analysis |
| Ulcerative colitis | 4e-62 | rs80174646 | 13 | GCST003045 | MR: beta=1.14, p=4.34e-62 (cis) |
| Crohn's disease vs rheumatoid arthritis (ordinary least squa | 5e-43 | rs7517847 | 1 | GCST90016610 | no MR -> candidate analysis |
| Interleukin-23 receptor levels | 1e-32 | rs1358748 | 3 | GCST90137730 | no MR -> candidate analysis |
| Ankylosing spondylitis | 6e-28 | rs11209026 | 4 | GCST005529 | MR: beta=0.524, p=6.19e-05 (cis) |
| Regional enteritis (PheCode 555.1) | 9e-27 | rs11805303 | 2 | GCST90480317 | no MR -> candidate analysis |
| Psoriasis | 1e-26 | rs9988642 | 11 | GCST005527 | MR: beta=0.431, p=9.48e-10 (cis) |
| Inflammatory bowel disease and other gasteroenteritis and co | 1e-26 | rs113935720 | 2 | GCST90476065 | no MR -> candidate analysis |
| Psoriasis and related disorder (PheCode 696) | 8e-23 | rs11581607 | 2 | GCST90476186 | no MR -> candidate analysis |
| Psoriasis (PheCode 696.4) | 2e-22 | rs11581607 | 2 | GCST90476187 | no MR -> candidate analysis |
| _...and 32 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 424 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| inflammatory bowel disease | 0.919 | — | common-variant locus | MR: beta=1.5, p=2.21e-166 (cis) |
| psoriasis | 0.898 | — | common-variant locus | MR: beta=0.431, p=9.48e-10 (cis) |
| Crohn disease | 0.911 | — | common-variant locus | no MR -> candidate analysis |
| ulcerative colitis | 0.904 | — | common-variant locus | MR: beta=1.14, p=4.34e-62 (cis) |
| enteritis | 0.834 | — | common-variant locus | no MR -> candidate analysis |
| ankylosing spondylitis | 0.824 | — | common-variant locus | MR: beta=0.524, p=6.19e-05 (cis) |
| sarcoidosis | 0.784 | — | common-variant locus | no MR -> candidate analysis |
| colitis | 0.752 | — | common-variant locus | MR: beta=1.14, p=4.34e-62 (cis) |
| psoriasis vulgaris | 0.76 | — | common-variant locus | no MR -> candidate analysis |
| autoimmune disease | 0.738 | — | common-variant locus | no MR -> candidate analysis |
| skin disorder | 0.724 | — | common-variant locus | no MR -> candidate analysis |
| ulcerative proctosigmoiditis | 0.681 | — | common-variant locus | no MR -> candidate analysis |
| seborrheic dermatitis | 0.662 | — | common-variant locus | no MR -> candidate analysis |
| intestinal disorder | 0.652 | — | common-variant locus | no MR -> candidate analysis |
| type 2 diabetes mellitus | 0.626 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **10 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Interleukin-23 receptor) |
| gnomAD constraint | pLI=8.4e-07, LOEUF=0.796 — LoF-tolerant |
| GWAS Catalog | 122 unique SNPs / 311 rows |
| ClinVar | 476 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 2 clinical annotations across 2 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 424 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'IL23R' and resolved to 'Interleukin-23 receptor' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 476 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 20 of 44 traits by best p-value, aggregated from 113 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q5VWK5 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000162594/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4296013/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/IL23R — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/IL23R — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=IL23R%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=IL23R — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/IL23R — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:15:06  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
