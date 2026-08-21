# Protein Dossier — TIMP2 (Metalloproteinase inhibitor 2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Height | -0.0431 | 0.011 | 9.11e-05 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M72 Fibroblastic disorders | 0.306 | 0.0906 | 7.36e-04 | Wald ratio | 1 | cis | NA |
| Pulse rate | 0.0434 | 0.0158 | 0.00598 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R14 Flatulence and related conditions | 0.59 | 0.219 | 0.00692 | Wald ratio | 1 | cis | NA |
| Intracranial volume | 1.89e+04 | 7e+03 | 0.00697 | Wald ratio | 1 | cis | NA |
| Type 2 diabetes | -0.0938 | 0.0352 | 0.00772 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | -0.0195 | 0.00735 | 0.00786 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: anxiety or panic attacks | 0.168 | 0.0655 | 0.0103 | Wald ratio | 1 | cis | NA |
| Sleep duration | -0.0155 | 0.00699 | 0.027 | Wald ratio | 1 | cis | NA |
| Fasting insulin | 0.0263 | 0.012 | 0.0278 | Wald ratio | 1 | cis | NA |
| Sodium in urine | 0.0189 | 0.00882 | 0.0319 | Wald ratio | 1 | cis | NA |
| Parkinson's disease | -0.322 | 0.151 | 0.0326 | Wald ratio | 1 | cis | NA |
| _...and 111 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2278_61_4` | TIMP-2 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_50 association rows across 35 traits (40 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| LGALS3BP protein levels | 1e-77 | rs111526614 | 1 | GCST90469760 | no MR -> candidate analysis |
| Height | 2e-66 | rs8066695 | 6 | GCST90245848 | MR: beta=-0.0431, p=9.11e-05 (cis) |
| Serum levels of protein TIMP2 | 4e-47 | rs2376999 | 2 | GCST90087930 | no MR -> candidate analysis |
| TIMP2 protein levels | 5e-44 | rs8066695 | 2 | GCST90470870 | no MR -> candidate analysis |
| Galectin-3-binding protein levels | 4e-35 | rs111526614 | 2 | GCST90247672 | no MR -> candidate analysis |
| Circulating DSG4 levels | 3e-30 | rs55842605 | 1 | GCST90860253 | no MR -> candidate analysis |
| Blood protein levels | 3e-29 | rs2376999 | 1 | GCST006585 | no MR -> candidate analysis |
| DSG4 protein levels | 3e-29 | rs55842605 | 1 | GCST90469044 | no MR -> candidate analysis |
| DSG3/DSG4 protein level ratio | 2e-27 | rs7220336 | 1 | GCST90314558 | no MR -> candidate analysis |
| Heel bone mineral density | 9e-16 | rs35881190 | 4 | GCST006433 | no MR -> candidate analysis |
| Estimated bone mineral density | 1e-15 | rs35881190 | 1 | GCST90726625 | no MR -> candidate analysis |
| Height (baseline) | 2e-14 | rs55646445 | 2 | GCST90565843 | no MR -> candidate analysis |
| _...and 23 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 947 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| coronary artery disorder | 0.545 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.511 | — | common-variant locus | no MR -> candidate analysis |
| benign neoplasm | 0.432 | — | common-variant locus | MR: beta=-0.136, p=0.119 (cis) |
| neuroendocrine neoplasm | 0.212 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1, LOEUF=0.433 — LoF-INTOLERANT |
| GWAS Catalog | 92 unique SNPs / 184 rows |
| ClinVar | 62 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 947 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'TIMP2'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 62 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 35 traits by best p-value, aggregated from 50 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P16035 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000035862/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/TIMP2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/TIMP2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=TIMP2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/TIMP2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:21:36  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
