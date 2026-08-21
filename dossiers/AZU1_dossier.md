# Protein Dossier — AZU1 (Azurocidin)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Heel bone mineral density (BMD) T-score  automated | 0.101 | 0.016 | 2.28e-10 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Glaucoma | 0.248 | 0.0813 | 0.00229 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: chronic obstructive airways disease or copd | 0.404 | 0.145 | 0.0054 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: osteoarthritis | -0.13 | 0.0472 | 0.006 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: D25 Leiomyoma of uterus | -0.464 | 0.18 | 0.0102 | Wald ratio | 1 | cis | NA |
| Hearing difficulty or problems: Yes | -0.0559 | 0.0226 | 0.0133 | Wald ratio | 1 | cis | NA |
| Fasting glucose | 0.0509 | 0.0218 | 0.0193 | Wald ratio | 1 | cis | NA |
| Creatinine (enzymatic) in urine | -0.0268 | 0.0118 | 0.0238 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K57 Diverticular disease of intestine | -0.259 | 0.114 | 0.0238 | Wald ratio | 1 | cis | NA |
| Eczema | -0.215 | 0.101 | 0.0337 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: ankylosing spondylitis | 0.359 | 0.169 | 0.0338 | Wald ratio | 1 | cis | NA |
| Paget's disease | 0.665 | 0.314 | 0.0342 | Wald ratio | 1 | cis | NA |
| _...and 95 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2751_16_2` | Azurocidin | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_62 association rows across 38 traits (62 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| MPO/PRTN3 protein level ratio | 3e-939 | rs12052108 | 1 | GCST90315492 | no MR -> candidate analysis |
| LCN2/PRTN3 protein level ratio | 7e-873 | rs12052108 | 1 | GCST90315307 | no MR -> candidate analysis |
| Circulating PRTN3 levels | 1e-838 | rs61242663 | 2 | GCST90859963 | no MR -> candidate analysis |
| Myeloblastin levels | 1e-243 | rs2074639 | 4 | GCST90248550 | no MR -> candidate analysis |
| Circulating AZU1 levels | 4e-226 | rs138032111 | 5 | GCST90859945 | no MR -> candidate analysis |
| AZU1 protein levels | 2e-204 | rs138032111 | 2 | GCST90468408 | no MR -> candidate analysis |
| Myeloblastin levels (PRTN3.3514.49.2) | 8e-110 | rs10425544 | 3 | GCST90241987 | no MR -> candidate analysis |
| Neutrophil forward scatter | 2e-82 | rs7254911 | 1 | GCST90281224 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 2e-54 | rs76427287 | 1 | GCST90838669 | no MR -> candidate analysis |
| Neutrophil side scatter distribution width | 6e-54 | rs138303849 | 1 | GCST90281225 | no MR -> candidate analysis |
| Neutrophil side scatter | 6e-52 | rs76427287 | 1 | GCST90281222 | no MR -> candidate analysis |
| Neutrophil side fluorescence | 1e-45 | rs7254911 | 1 | GCST90281223 | no MR -> candidate analysis |
| _...and 26 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 259 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| low tension glaucoma | 0.278 | — | common-variant locus | no MR -> candidate analysis |
| anti-neutrophil antibody associated vasculitis | 0.073 | — | common-variant locus | no MR -> candidate analysis |
| open-angle glaucoma | 0.042 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of refraction | 0.035 | — | common-variant locus | no MR -> candidate analysis |
| gestational diabetes | 0.035 | — | common-variant locus | no MR -> candidate analysis |

> Of the 5 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=7.5e-09, LOEUF=1.7 — LoF-tolerant |
| GWAS Catalog | 126 unique SNPs / 304 rows |
| ClinVar | 100 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 259 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'AZU1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 100 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 38 traits by best p-value, aggregated from 62 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P20160 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000172232/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/AZU1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/AZU1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=AZU1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/AZU1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:13:04  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
