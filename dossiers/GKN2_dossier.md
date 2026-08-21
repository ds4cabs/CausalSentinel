# Protein Dossier — GKN2 (Gastrokine-2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Lung adenocarcinoma | 0.212 | 0.0633 | 8.28e-04 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | -0.012 | 0.00468 | 0.0102 | Wald ratio | 1 | cis | NA |
| Age at menopause | 0.159 | 0.0637 | 0.0124 | Wald ratio | 1 | cis | NA |
| Fracture resulting from simple fall | -0.0371 | 0.0155 | 0.017 | Wald ratio | 1 | cis | NA |
| Cough on most days | -0.0608 | 0.031 | 0.0498 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | 0.118 | 0.0606 | 0.0512 | Wald ratio | 1 | cis | NA |
| Putamen volume | -32.5 | 16.7 | 0.0519 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: pneumothorax | 0.383 | 0.2 | 0.0552 | Wald ratio | 1 | cis | NA |
| Platelet count | -4.86 | 2.55 | 0.0567 | Wald ratio | 1 | cis | NA |
| Height | -0.0234 | 0.0127 | 0.0668 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: G47 Sleep disorders | 0.118 | 0.0664 | 0.0753 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Glaucoma | 0.0768 | 0.0439 | 0.0804 | Wald ratio | 1 | cis | NA |
| _...and 82 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_18 association rows across 11 traits (15 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| TFF1/TFF2 protein level ratio | 2e-317 | rs62133345 | 1 | GCST90315914 | no MR -> candidate analysis |
| Gastrokine-2 levels | 9e-288 | rs62133344 | 2 | GCST90247690 | no MR -> candidate analysis |
| TFF1 protein levels | 2e-204 | rs62133344 | 2 | GCST90470835 | no MR -> candidate analysis |
| Trefoil factor 1 levels | 2e-104 | rs62133344 | 4 | GCST90249813 | no MR -> candidate analysis |
| Serum levels of protein GKN2 | 6e-99 | rs62133344 | 1 | GCST90089413 | no MR -> candidate analysis |
| Blood protein levels | 3e-34 | rs13008230 | 2 | GCST006585 | no MR -> candidate analysis |
| Serum levels of protein TFF1 | 2e-27 | rs62133344 | 2 | GCST90090541 | no MR -> candidate analysis |
| BMP10 protein levels | 3e-17 | rs76746873 | 1 | GCST90468452 | no MR -> candidate analysis |
| Benign neoplasm of unspecified sites (PheCode 229) | 6e-8 | rs75502905 | 1 | GCST90651747 | no MR -> candidate analysis |
| Adiponectin levels | 1e-7 | rs6705747 | 1 | GCST012168 | no MR -> candidate analysis |
| Lung cancer | 5e-6 | rs4254535 | 1 | GCST000459 | MR: beta=0.0372, p=0.437 (cis) |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 69 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Abnormality of the skeletal system | 0.472 | — | common-variant locus | no MR -> candidate analysis |
| aortic valve stenosis | 0.07 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=3.3e-05, LOEUF=1.13 — LoF-tolerant |
| GWAS Catalog | 32 unique SNPs / 64 rows |
| ClinVar | 38 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 69 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'GKN2'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 38 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 11 of 11 traits by best p-value, aggregated from 18 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q86XP6 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000183607/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/GKN2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/GKN2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=GKN2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/GKN2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:49:14  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
