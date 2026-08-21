# Protein Dossier — FAM3D (Protein FAM3D)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Amyotrophic lateral sclerosis | -0.173 | 0.0601 | 0.00395 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R10 Abdominal and pelvic pain | 0.105 | 0.0371 | 0.00478 | Wald ratio | 1 | cis | NA |
| HOMA-B | 0.027 | 0.0112 | 0.0161 | Wald ratio | 1 | cis | NA |
| Fractured or broken bones in last 5 years | 0.0582 | 0.025 | 0.0201 | Wald ratio | 1 | cis | NA |
| Pulse rate | -0.0337 | 0.015 | 0.0243 | Wald ratio | 1 | cis | NA |
| Invasive mucinous ovarian cancer | 0.305 | 0.142 | 0.0319 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K80 Cholelithiasis | 0.112 | 0.0531 | 0.035 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Injury or trauma resulting in loss of vision | -0.336 | 0.16 | 0.036 | Wald ratio | 1 | cis | NA |
| Fasting proinsulin | 0.052 | 0.0249 | 0.0372 | Wald ratio | 1 | cis | NA |
| Lung adenocarcinoma | -0.202 | 0.0975 | 0.0386 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Ankle | 0.131 | 0.064 | 0.0407 | Wald ratio | 1 | cis | NA |
| Platelet count | 2.8 | 1.42 | 0.048 | Wald ratio | 1 | cis | NA |
| _...and 105 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_20 association rows across 14 traits (14 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| FAM3D protein levels | 2e-263 | rs13097314 | 4 | GCST90469188 | no MR -> candidate analysis |
| Protein FAM3D (analyte X13102.1) levels | 3e-65 | rs7433100 | 1 | GCST90422080 | no MR -> candidate analysis |
| Protein FAM3D levels | 5e-45 | rs6445998 | 2 | GCST90161287 | no MR -> candidate analysis |
| Protein FAM3D levels (FAM3D.13102.1.3) | 2e-31 | rs3749290 | 2 | GCST90242469 | no MR -> candidate analysis |
| Serum levels of protein FAM3D | 3e-28 | rs56292712 | 1 | GCST90087374 | no MR -> candidate analysis |
| Blood protein levels | 3e-18 | rs6807381 | 1 | GCST006585 | no MR -> candidate analysis |
| Core binding factor acute myeloid leukemia | 1e-11 | rs753819; rs753821; rs9862196; rs6790074; rs6777469; rs11130662; rs11130665 | 2 | GCST008413 | no MR -> candidate analysis |
| Cerebrospinal fluid protein FAM3D levels | 6e-9 | rs12493101 | 1 | GCST90943365 | no MR -> candidate analysis |
| Gut microbial network clusters (Salmon (at 1 year) x Any Bre | 8e-7 | rs900872 | 1 | GCST90569450 | no MR -> candidate analysis |
| Gut microbiota (bacterial taxa, hurdle binary method) | 2e-6 | rs111423440 | 1 | GCST010396 | no MR -> candidate analysis |
| Night sleep phenotypes | 4e-6 | rs77510899 | 1 | GCST003542 | no MR -> candidate analysis |
| Osteonecrosis (time to event) in systemic lupus erythematosu | 4e-6 | rs3860562 | 1 | GCST90295969 | no MR -> candidate analysis |
| _...and 2 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 340 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| knee fracture | 0.199 | — | common-variant locus | no MR -> candidate analysis |
| nephrotic syndrome | 0.176 | — | common-variant locus | no MR -> candidate analysis |
| ovarian dysfunction | 0.109 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.5e-08, LOEUF=1.21 — LoF-tolerant |
| GWAS Catalog | 40 unique SNPs / 72 rows |
| ClinVar | 63 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 340 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'FAM3D'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 63 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 14 of 14 traits by best p-value, aggregated from 20 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q96BQ1 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000198643/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/FAM3D — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/FAM3D — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=FAM3D%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/FAM3D — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:35:31  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: pharmgkb
