# Protein Dossier — DKK3 (Dickkopf-related protein 3)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: D25 Leiomyoma of uterus | 0.149 | 0.0593 | 0.0121 | Wald ratio | 1 | cis | NA |
| Lung cancer | 0.145 | 0.0722 | 0.0439 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N92 Excessive  frequent and irregular menstruation | -0.117 | 0.0611 | 0.0555 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C50 Malignant neoplasm of breast | 0.1 | 0.0552 | 0.0695 | Wald ratio | 1 | cis | NA |
| Vascular or heart problems diagnosed by doctor: Angina | 0.0727 | 0.0406 | 0.0734 | Wald ratio | 1 | cis | NA |
| Hirschsprung's disease | -0.719 | 0.406 | 0.0767 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | -0.0119 | 0.00673 | 0.0773 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: basal cell carcinoma | 0.126 | 0.072 | 0.0802 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Other bones | 0.0557 | 0.032 | 0.0821 | Wald ratio | 1 | cis | NA |
| Hearing difficulty or problems: Yes | -0.0238 | 0.0137 | 0.0839 | Wald ratio | 1 | cis | NA |
| HDL cholesterol | -0.0336 | 0.0196 | 0.0869 | Wald ratio | 1 | cis | NA |
| Fractured or broken bones in last 5 years | 0.0396 | 0.0233 | 0.0899 | Wald ratio | 1 | cis | NA |
| _...and 88 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3607_71_1` | DKK3 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_51 association rows across 28 traits (38 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating DKK3 levels | 8e-737 | rs11022114 | 6 | GCST90860592 | no MR -> candidate analysis |
| DKK3 protein levels | 2e-250 | rs10734190 | 8 | GCST90468998 | no MR -> candidate analysis |
| Dickkopf-related protein 3 levels | 1e-122 | rs11022114 | 3 | GCST90247287 | no MR -> candidate analysis |
| Height | 4e-116 | rs3206824 | 5 | GCST90245848 | MR: beta=0.014, p=0.274 (cis) |
| ANGPTL2 protein levels | 1e-42 | rs138260315 | 2 | GCST90468303 | no MR -> candidate analysis |
| Dickkopf-related protein 3 levels (DKK3.3607.71.6) | 7e-36 | rs11022114 | 1 | GCST90240905 | no MR -> candidate analysis |
| Serum levels of protein DKK3 | 8e-31 | rs11022114 | 2 | GCST90088455 | no MR -> candidate analysis |
| Standing height (UKB data field 50) | 3e-19 | rs3206824 | 1 | GCST90468178 | no MR -> candidate analysis |
| Free Cholesterol to Cholesteryl Esters in Small HDL ratio | 1e-15 | rs17463794 | 1 | GCST90827928 | no MR -> candidate analysis |
| Height (baseline) | 2e-14 | rs6485328 | 3 | GCST90565843 | no MR -> candidate analysis |
| Body shape phenotype PC2 | 3e-13 | rs10734190 | 1 | GCST90832990 | no MR -> candidate analysis |
| Body mass index | 3e-10 | rs7396187 | 1 | GCST90662912 | MR: beta=-0.00901, p=0.246 (cis) |
| _...and 16 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 474 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Abnormality of the skeletal system | 0.706 | — | common-variant locus | no MR -> candidate analysis |
| hypothyroidism | 0.638 | — | common-variant locus | MR: beta=-0.0274, p=0.441 (cis) |
| Isolated polycystic liver disease | 0.552 | — | established (curated) | no MR -> candidate analysis |
| autosomal dominant polycystic liver disease | 0.552 | — | established (curated) | no MR -> candidate analysis |
| response to stimulus | 0.55 | — | common-variant locus | no MR -> candidate analysis |
| adverse effect | 0.55 | — | common-variant locus | no MR -> candidate analysis |
| bladder calculus | 0.45 | — | common-variant locus | no MR -> candidate analysis |
| diabetes mellitus | 0.438 | — | common-variant locus | no MR -> candidate analysis |
| autosomal dominant polycystic kidney disease | 0.228 | — | established (curated) | no MR -> candidate analysis |
| marfanoid habitus and intellectual disability | 0.195 | — | established (curated) | no MR -> candidate analysis |

> Of the 10 rows above, **9 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.5e-05, LOEUF=0.946 — LoF-tolerant |
| GWAS Catalog | 68 unique SNPs / 136 rows |
| ClinVar | 74 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 474 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'DKK3'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 74 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 28 traits by best p-value, aggregated from 51 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9UBP4 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000050165/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/DKK3 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/DKK3 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=DKK3%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/DKK3 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:17:42  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
