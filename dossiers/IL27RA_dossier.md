# Protein Dossier — IL27RA (Interleukin-27 receptor subunit alpha)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Sleep duration | 0.00751 | 0.0026 | 0.00389 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: depression | 0.0322 | 0.0133 | 0.0154 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | -0.0366 | 0.0154 | 0.0172 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M54 Dorsalgia | 0.0548 | 0.0245 | 0.0252 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: bone disorder | 0.139 | 0.0621 | 0.0253 | Wald ratio | 1 | cis | NA |
| Endometrioid ovarian cancer | 0.108 | 0.0484 | 0.0261 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: H25 Senile cataract | 0.0766 | 0.0352 | 0.0296 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: uterine fibroids | -0.0598 | 0.0286 | 0.0364 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hiatus hernia | 0.0431 | 0.0209 | 0.0396 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: mania or bipolar disorder or manic depression | 0.114 | 0.0584 | 0.0509 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K43 Ventral hernia | -0.101 | 0.0555 | 0.0674 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Diabetes related eye disease | 0.0709 | 0.0398 | 0.0744 | Wald ratio | 1 | cis | NA |
| _...and 62 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5132_71_3` | TCCR | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_28 association rows across 20 traits (28 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Interleukin-27 receptor subunit alpha levels | 4e-542 | rs35026308 | 5 | GCST90248067 | no MR -> candidate analysis |
| Interleukin-27 receptor subunit alpha levels (IL27RA.5132.71 | 4e-239 | rs35026308 | 1 | GCST90241627 | no MR -> candidate analysis |
| Serum levels of protein IL27RA | 3e-199 | rs35026308 | 1 | GCST90088948 | no MR -> candidate analysis |
| Mitochondrial ubiquitin ligase activator of NFKB 1:Cytoplasm | 4e-25 | rs35026308 | 1 | GCST90441052 | no MR -> candidate analysis |
| Cerebrospinal fluid biomarker levels | 3e-15 | rs35026308 | 1 | GCST004000 | no MR -> candidate analysis |
| Neutrophil percentage of white cells | 1e-14 | rs35026308 | 1 | GCST90002399 | no MR -> candidate analysis |
| Lymphocyte count | 2e-13 | rs35026308 | 1 | GCST90002388 | no MR -> candidate analysis |
| Platelet count | 3e-13 | rs35018855 | 3 | GCST90662907 | no MR -> candidate analysis |
| Lymphocyte count (UKB data field 30120) | 1e-12 | rs35026308 | 1 | GCST90468082 | no MR -> candidate analysis |
| Platelet count (UKB data field 30080) | 1e-12 | rs2306191 | 1 | GCST90468095 | no MR -> candidate analysis |
| Lymphocyte percentage of white cells | 3e-12 | rs35026308 | 1 | GCST90002389 | no MR -> candidate analysis |
| Platelet crit (UKB data field 30090) | 5e-12 | rs2306191 | 1 | GCST90468096 | no MR -> candidate analysis |
| _...and 8 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 237 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| alcohol drinking | 0.054 | — | common-variant locus | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=5.1e-16, LOEUF=0.935 — LoF-tolerant |
| GWAS Catalog | 36 unique SNPs / 72 rows |
| ClinVar | 138 records; 3 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 237 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'IL27RA'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 138 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 20 traits by best p-value, aggregated from 28 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q6UWB1 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000104998/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/IL27RA — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/IL27RA — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=IL27RA%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/IL27RA — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:15:47  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
