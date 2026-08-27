# Protein Dossier — POMC (Pro-opiomelanocortin)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: high cholesterol | -0.0734 | 0.0177 | 3.48e-05 | Wald ratio | 1 | trans | NA |
| ER-negative Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.102 | 0.0294 | 5.23e-04 | Wald ratio | 1 | trans | NA |
| Hearing difficulty or problems: Yes | -0.0317 | 0.0108 | 0.0035 | Wald ratio | 1 | trans | NA |
| Cough on most days | -0.0976 | 0.0343 | 0.00449 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: R14 Flatulence and related conditions | 0.463 | 0.165 | 0.00493 | Wald ratio | 1 | trans | NA |
| Forced vital capacity (FVC) | 0.0137 | 0.005 | 0.00614 | Wald ratio | 1 | trans | NA |
| Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.0424 | 0.016 | 0.00793 | Wald ratio | 1 | trans | NA |
| Forced expiratory volume in 1-second (FEV1) | 0.0133 | 0.00527 | 0.0113 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: mania or bipolar disorder or manic depression | 0.238 | 0.095 | 0.0121 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: ankylosing spondylitis | 0.205 | 0.0947 | 0.0302 | Wald ratio | 1 | trans | NA |
| High grade serous ovarian cancer | 0.0871 | 0.0407 | 0.0322 | Wald ratio | 1 | trans | NA |
| Sleep duration | 0.0101 | 0.00475 | 0.033 | Wald ratio | 1 | trans | NA |
| _...and 70 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2558_51_3` | b-Endorphin | Suhre K | 2019 |
| `prot-c-4890_10_1` | ACTH | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_24 association rows across 18 traits (20 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| POMC protein levels | 1e-29 | rs3754861 | 1 | GCST90470284 | no MR -> candidate analysis |
| Weight | 5e-27 | rs934778 | 2 | GCST90662910 | MR: beta=-0.0147, p=0.11 (trans) |
| Hair color | 3e-21 | rs4665773 | 1 | GCST007082 | no MR -> candidate analysis |
| Body mass index | 4e-21 | rs13388961 | 4 | GCST90301650 | no MR -> candidate analysis |
| Weight (UKB data field 21002) | 2e-20 | rs934778 | 1 | GCST90468183 | no MR -> candidate analysis |
| Metabolic syndrome | 1e-19 | rs934778 | 1 | GCST90444487 | no MR -> candidate analysis |
| Height (baseline) | 7e-17 | rs34914018 | 2 | GCST90565843 | no MR -> candidate analysis |
| Height | 3e-16 | rs7566506 | 1 | GCST90245848 | no MR -> candidate analysis |
| Uterine fibroids | 3e-15 | rs12619264 | 2 | GCST90461957 | no MR -> candidate analysis |
| Hip circumference adjusted for BMI | 2e-12 | rs12473543 | 1 | GCST90020028 | no MR -> candidate analysis |
| Red vs. brown/black hair color | 1e-10 | rs76645364 | 1 | GCST006986 | no MR -> candidate analysis |
| Body mass index (MTAG) | 5e-9 | rs3754861 | 1 | GCST90179150 | no MR -> candidate analysis |
| _...and 6 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1989 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| obesity due to pro-opiomelanocortin deficiency | 0.827 | — | established (curated) | no MR -> candidate analysis |
| Obesity | 0.739 | — | established (curated) | no MR -> candidate analysis |
| obesity disorder | 0.08 | — | common-variant locus | no MR -> candidate analysis |
| inherited obesity | 0.297 | — | established (curated) | no MR -> candidate analysis |
| hereditary disease | 0.679 | — | established (curated) | no MR -> candidate analysis |
| autoimmune disease | 0.618 | — | common-variant locus | no MR -> candidate analysis |
| hair color | 0.613 | — | common-variant locus | no MR -> candidate analysis |
| cardiovascular disorder | 0.51 | — | common-variant locus | no MR -> candidate analysis |
| uterine corpus leiomyoma | 0.476 | — | common-variant locus | no MR -> candidate analysis |
| hypertensive disorder | 0.457 | — | common-variant locus | no MR -> candidate analysis |
| Crohn disease | 0.457 | — | common-variant locus | no MR -> candidate analysis |
| ulcerative colitis | 0.456 | — | common-variant locus | no MR -> candidate analysis |
| inflammatory spondylopathy | 0.463 | — | common-variant locus | no MR -> candidate analysis |
| atrial fibrillation | 0.398 | — | common-variant locus | no MR -> candidate analysis |
| mental disorder | 0.344 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **15 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=2.2e-07, LOEUF=1.51 — LoF-tolerant |
| GWAS Catalog | 101 unique SNPs / 210 rows |
| ClinVar | 250 records; 5 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1989 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'POMC'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 250 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 18 of 18 traits by best p-value, aggregated from 24 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P01189 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000115138/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/POMC — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/POMC — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=POMC%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/POMC — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:30:35  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: pharmgkb
