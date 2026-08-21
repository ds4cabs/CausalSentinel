# Protein Dossier — NMB (Neuromedin-B)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Schizophrenia | 0.396 | 0.0695 | 1.25e-08 | Wald ratio | 1 | cis | NA |
| Height | -0.0976 | 0.0189 | 2.45e-07 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | -0.0547 | 0.0134 | 4.81e-05 | Wald ratio | 1 | cis | NA |
| Weight | -0.0519 | 0.0137 | 1.55e-04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: mania or bipolar disorder or manic depression | 0.599 | 0.174 | 5.59e-04 | Wald ratio | 1 | cis | NA |
| Bipolar disorder | 0.508 | 0.152 | 8.66e-04 | Wald ratio | 1 | cis | NA |
| Rheumatoid arthritis | -0.377 | 0.117 | 0.0012 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: emphysema or chronic bronchitis | 0.303 | 0.101 | 0.00257 | Wald ratio | 1 | cis | NA |
| Body fat | -0.0976 | 0.0348 | 0.005 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | -0.0352 | 0.0128 | 0.00578 | Wald ratio | 1 | cis | NA |
| Paget's disease | 1.04 | 0.386 | 0.00697 | Wald ratio | 1 | cis | NA |
| Diastolic blood pressure  automated reading | -0.0415 | 0.0159 | 0.00911 | Wald ratio | 1 | cis | NA |
| _...and 100 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_9 association rows across 8 traits (8 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Height (baseline) | 4e-26 | rs531061098 | 1 | GCST90565843 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 5e-12 | rs1107179 | 1 | GCST90838669 | no MR -> candidate analysis |
| Dilated cardiomyopathy (MTAG) | 3e-11 | rs1051168 | 1 | GCST011202 | no MR -> candidate analysis |
| Schizophrenia | 5e-10 | rs12908161 | 2 | GCST003048 | MR: beta=0.396, p=1.25e-08 (cis) |
| Physical function (baseline) | 2e-9 | rs531061098 | 1 | GCST90565837 | no MR -> candidate analysis |
| Creatine kinase levels | 1e-8 | rs2292462 | 1 | GCST006014 | no MR -> candidate analysis |
| Diastolic blood pressure | 1e-8 | rs2292462 | 1 | GCST90435414 | MR: beta=-0.0415, p=0.00911 (cis) |
| Dilated cardiomyopathy | 8e-8 | rs1051168 | 1 | GCST011210 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 185 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| schizophrenia | 0.54 | — | common-variant locus | MR: beta=0.396, p=1.25e-08 (cis) |
| bipolar disorder | 0.532 | — | common-variant locus | MR: beta=0.599, p=5.59e-04 (cis) |
| autism spectrum disorder | 0.443 | — | common-variant locus | no MR -> candidate analysis |
| heart failure | 0.376 | — | common-variant locus | no MR -> candidate analysis |
| major depressive disorder | 0.366 | — | common-variant locus | no MR -> candidate analysis |
| attention deficit-hyperactivity disorder | 0.366 | — | common-variant locus | no MR -> candidate analysis |
| obsessive-compulsive disorder | 0.366 | — | common-variant locus | no MR -> candidate analysis |
| anorexia nervosa | 0.366 | — | common-variant locus | no MR -> candidate analysis |
| Tourette syndrome | 0.366 | — | common-variant locus | no MR -> candidate analysis |
| mitral valve prolapse | 0.332 | — | common-variant locus | no MR -> candidate analysis |
| dilated cardiomyopathy | 0.316 | — | common-variant locus | no MR -> candidate analysis |
| open-angle glaucoma | 0.313 | — | common-variant locus | no MR -> candidate analysis |
| osteoarthritis | 0.279 | — | common-variant locus | MR: beta=-0.0513, p=0.35 (cis) |
| bipolar I disorder | 0.25 | — | common-variant locus | no MR -> candidate analysis |
| hypertrophic cardiomyopathy | 0.137 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **12 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 2 known modulators (Transmembrane glycoprotein NMB) |
| gnomAD constraint | pLI=4.6e-05, LOEUF=1.66 — LoF-tolerant |
| GWAS Catalog | 61 unique SNPs / 122 rows |
| ClinVar | 93 records; 3 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 185 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'NMB' and resolved to 'Transmembrane glycoprotein NMB' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 93 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 8 of 8 traits by best p-value, aggregated from 9 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P08949 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000197696/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3712919/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/NMB — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/NMB — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=NMB%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/NMB — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:59:37  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
