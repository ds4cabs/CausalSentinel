# Protein Dossier — LGMN (Legumain)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Forced vital capacity (FVC) | 0.0421 | 0.0121 | 5.13e-04 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | 0.0437 | 0.0128 | 6.40e-04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: retinal detachment | 0.459 | 0.168 | 0.00649 | Wald ratio | 1 | cis | NA |
| Fractured or broken bones in last 5 years | 0.104 | 0.0416 | 0.0121 | Wald ratio | 1 | cis | NA |
| Birth weight | 0.053 | 0.0243 | 0.0289 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: high cholesterol | -0.0915 | 0.0439 | 0.0372 | Wald ratio | 1 | cis | NA |
| Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.0858 | 0.0425 | 0.0436 | Wald ratio | 1 | cis | NA |
| ER-positive Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.101 | 0.0507 | 0.0463 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M54 Dorsalgia | -0.325 | 0.164 | 0.0477 | Wald ratio | 1 | cis | NA |
| Squamous cell lung cancer | -0.32 | 0.165 | 0.0528 | Wald ratio | 1 | cis | NA |
| Sodium in urine | -0.0267 | 0.0145 | 0.0662 | Wald ratio | 1 | cis | NA |
| Weight | 0.0236 | 0.013 | 0.0709 | Wald ratio | 1 | cis | NA |
| _...and 64 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3622_33_4` | LGMN | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_55 association rows across 36 traits (53 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating LGMN levels | 2e-298 | rs148659834 | 7 | GCST90860643 | no MR -> candidate analysis |
| LGMN protein levels | 2e-298 | rs148659834 | 6 | GCST90469766 | no MR -> candidate analysis |
| LGMN/TIMP1 protein level ratio | 1e-278 | rs117845934 | 1 | GCST90315325 | no MR -> candidate analysis |
| CD164/LGMN protein level ratio | 3e-262 | rs117845934 | 1 | GCST90313741 | no MR -> candidate analysis |
| LGMN/SPINT2 protein level ratio | 3e-119 | rs17128502 | 1 | GCST90315324 | no MR -> candidate analysis |
| TMEM106A protein levels | 3e-97 | rs72701845 | 3 | GCST90470886 | no MR -> candidate analysis |
| Legumain levels | 1e-43 | rs7157038 | 4 | GCST90248281 | no MR -> candidate analysis |
| Transmembrane protein 106A levels | 5e-38 | rs72701845 | 3 | GCST90249752 | no MR -> candidate analysis |
| ASAH1 protein levels | 5e-33 | rs72701845 | 1 | GCST90468373 | no MR -> candidate analysis |
| Beta-mannosidase levels | 3e-31 | rs35792499 | 2 | GCST90246709 | no MR -> candidate analysis |
| CD164 protein levels | 6e-27 | rs72701845 | 1 | GCST90468602 | no MR -> candidate analysis |
| Legumain (analyte X3622.33) levels | 4e-22 | rs4904977 | 1 | GCST90425835 | no MR -> candidate analysis |
| _...and 24 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1008 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| crush injury | 0.49 | — | common-variant locus | no MR -> candidate analysis |
| Alzheimer disease | 0.419 | — | common-variant locus | no MR -> candidate analysis |
| post term pregnancy | 0.419 | — | common-variant locus | no MR -> candidate analysis |
| rosacea | 0.419 | — | common-variant locus | no MR -> candidate analysis |
| pathological myopia | 0.182 | — | established (curated) | no MR -> candidate analysis |
| myopia | 0.182 | — | established (curated) | no MR -> candidate analysis |

> Of the 6 rows above, **6 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Legumain) |
| gnomAD constraint | pLI=7.1e-08, LOEUF=0.836 — LoF-tolerant |
| GWAS Catalog | 114 unique SNPs / 196 rows |
| ClinVar | 135 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1008 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'LGMN' and resolved to 'Legumain' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 135 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 36 traits by best p-value, aggregated from 55 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q99538 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000100600/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4244/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/LGMN — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/LGMN — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=LGMN%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/LGMN — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:31:56  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
