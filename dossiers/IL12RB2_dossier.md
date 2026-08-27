# Protein Dossier — IL12RB2 (Interleukin-12 receptor subunit beta-2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: chronic obstructive airways disease or copd | 0.359 | 0.123 | 0.00352 | Wald ratio | 1 | cis | NA |
| Ulcerative colitis | 0.146 | 0.0523 | 0.00526 | Wald ratio | 1 | cis | NA |
| Inflammatory bowel disease | 0.114 | 0.0414 | 0.00569 | Wald ratio | 1 | cis | NA |
| Hirschsprung's disease | -1.4 | 0.505 | 0.00572 | Wald ratio | 1 | cis | NA |
| Urinary albumin-to-creatinine ratio | -0.0623 | 0.0241 | 0.00986 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R55 Syncope and collapse | 0.202 | 0.0883 | 0.0219 | Wald ratio | 1 | cis | NA |
| Cough on most days | 0.105 | 0.0466 | 0.0246 | Wald ratio | 1 | cis | NA |
| Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0576 | 0.0261 | 0.0272 | Wald ratio | 1 | cis | NA |
| ER-positive Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.067 | 0.0312 | 0.0316 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N81 Female genital prolapse | -0.23 | 0.108 | 0.0326 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C50 Malignant neoplasm of breast | -0.204 | 0.0979 | 0.0372 | Wald ratio | 1 | cis | NA |
| Age at menarche | 0.0506 | 0.0244 | 0.038 | Wald ratio | 1 | cis | NA |
| _...and 63 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3815_14_1` | IL-12 RB2 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_60 association rows across 29 traits (49 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Primary biliary cholangitis | 5e-65 | rs6679356 | 7 | GCST90061442 | no MR -> candidate analysis |
| Interleukin-12 receptor subunit beta-2 levels | 4e-49 | rs7518266 | 4 | GCST90425888 | no MR -> candidate analysis |
| Primary biliary cirrhosis | 2e-38 | rs72678531 | 2 | GCST005581 | no MR -> candidate analysis |
| Systemic lupus erythematosus (MTAG) | 8e-17 | rs6679356 | 3 | GCST90270940 | no MR -> candidate analysis |
| Serum levels of protein IL12RB2 | 3e-16 | rs12139687 | 1 | GCST90088527 | no MR -> candidate analysis |
| Hypothyroidism | 7e-14 | rs72678531 | 3 | GCST90627750 | MR: beta=0.0479, p=0.264 (cis) |
| Autoimmune hypothyroidism | 8e-14 | rs10489626 | 1 | GCST90837324 | no MR -> candidate analysis |
| Inflammatory skin disease | 6e-13 | rs12119179 | 1 | GCST002740 | no MR -> candidate analysis |
| Crohn's disease or systemic sclerosis | 1e-11 | rs6659932 | 1 | GCST010124 | no MR -> candidate analysis |
| Tics and stuttering (PheCode 313.2) | 2e-11 | rs192123185 | 1 | GCST90480763 | no MR -> candidate analysis |
| Behcet's disease | 2e-11 | rs1495965 | 3 | GCST000728 | no MR -> candidate analysis |
| ICD10 K50, K51: inflammatory bowel disease | 5e-11 | rs10889680 | 2 | GCST90432147 | no MR -> candidate analysis |
| _...and 17 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 311 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| primary biliary cholangitis | 0.743 | — | common-variant locus | no MR -> candidate analysis |
| rheumatoid arthritis | 0.752 | — | common-variant locus | no MR -> candidate analysis |
| hypothyroidism | 0.743 | — | common-variant locus | MR: beta=0.0479, p=0.264 (cis) |
| systemic lupus erythematosus | 0.686 | — | common-variant locus | no MR -> candidate analysis |
| Crohn disease | 0.686 | — | common-variant locus | no MR -> candidate analysis |
| systemic sclerosis | 0.663 | — | common-variant locus | no MR -> candidate analysis |
| biliary liver cirrhosis | 0.658 | — | common-variant locus | no MR -> candidate analysis |
| Behcet disease | 0.589 | — | common-variant locus | no MR -> candidate analysis |
| enteritis | 0.527 | — | common-variant locus | no MR -> candidate analysis |
| myositis disease | 0.493 | — | common-variant locus | no MR -> candidate analysis |
| Hashimoto thyroiditis | 0.49 | — | common-variant locus | no MR -> candidate analysis |
| ulcerative colitis | 0.487 | — | common-variant locus | MR: beta=0.146, p=0.00526 (cis) |
| retinal degeneration | 0.47 | — | common-variant locus | no MR -> candidate analysis |
| psoriasis | 0.456 | — | common-variant locus | no MR -> candidate analysis |
| Tics | 0.462 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **13 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=6.8e-26, LOEUF=1.1 — LoF-tolerant |
| GWAS Catalog | 77 unique SNPs / 154 rows |
| ClinVar | 714 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 311 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'IL12RB2'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 714 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 29 traits by best p-value, aggregated from 60 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q99665 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000081985/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/IL12RB2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/IL12RB2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=IL12RB2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/IL12RB2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:11:06  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
