# Protein Dossier — TYMP (Thymidine phosphorylase)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Mean cell volume | 1.37 | 0.169 | 6.26e-16 | Wald ratio | 1 | cis | NA |
| Mean cell haemoglobin | 0.473 | 0.0672 | 1.97e-12 | Wald ratio | 1 | cis | NA |
| Inflammatory bowel disease | -0.283 | 0.0594 | 1.84e-06 | Wald ratio | 1 | cis | NA |
| Ulcerative colitis | -0.336 | 0.0744 | 6.28e-06 | Wald ratio | 1 | cis | NA |
| Hearing difficulty or problems: Yes | 0.0867 | 0.0229 | 1.52e-04 | Wald ratio | 1 | cis | NA |
| Weight | 0.0458 | 0.0128 | 3.38e-04 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | 0.0378 | 0.0119 | 0.00143 | Wald ratio | 1 | cis | NA |
| Multiple sclerosis | -0.304 | 0.0976 | 0.00183 | Wald ratio | 1 | cis | NA |
| Crohn's disease | -0.223 | 0.072 | 0.00192 | Wald ratio | 1 | cis | NA |
| Age at menopause | -0.441 | 0.147 | 0.0027 | Wald ratio | 1 | cis | NA |
| Red blood cell count | -0.0402 | 0.0147 | 0.00627 | Wald ratio | 1 | cis | NA |
| HbA1C | -0.0647 | 0.024 | 0.00706 | Wald ratio | 1 | cis | NA |
| _...and 99 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_15 association rows across 9 traits (14 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Mean corpuscular volume | 7e-68 | rs131801 | 4 | GCST90018746 | no MR -> candidate analysis |
| Mean corpuscular hemoglobin | 5e-45 | rs470119 | 3 | GCST90002323 | no MR -> candidate analysis |
| ARSA protein levels | 2e-41 | rs184299570 | 1 | GCST90468368 | no MR -> candidate analysis |
| 5-methyluridine (ribothymidine) levels | 5e-26 | rs470119 | 1 | GCST90102853 | no MR -> candidate analysis |
| 2'-deoxyuridine levels | 2e-25 | rs74624637 | 1 | GCST90200413 | no MR -> candidate analysis |
| Red cell distribution width | 3e-19 | rs131801 | 1 | GCST004621 | no MR -> candidate analysis |
| Red blood cell count | 2e-16 | rs131801 | 2 | GCST90662878 | MR: beta=-0.0402, p=0.00627 (cis) |
| Mean spheric corpuscular volume | 3e-9 | rs131804 | 1 | GCST90002397 | no MR -> candidate analysis |
| Mean reticulocyte volume | 6e-9 | rs131804 | 1 | GCST90002396 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 479 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| mitochondrial DNA depletion syndrome 1 | 0.937 | — | established (curated) | no MR -> candidate analysis |
| mitochondrial neurogastrointestinal encephalomyopathy | 0.819 | — | established (curated) | no MR -> candidate analysis |
| hereditary disease | 0.774 | — | established (curated) | no MR -> candidate analysis |
| renal carcinoma | 0.576 | — | common-variant locus | no MR -> candidate analysis |
| intestinal pseudo-obstruction | 0.438 | — | established (curated) | no MR -> candidate analysis |
| multiple sclerosis | 0.388 | — | common-variant locus | MR: beta=-0.304, p=0.00183 (cis) |
| B-cell chronic lymphocytic leukemia | 0.322 | — | common-variant locus | no MR -> candidate analysis |

> Of the 7 rows above, **6 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 1 known modulators (Thymidine phosphorylase) |
| gnomAD constraint | pLI=2.1e-17, LOEUF=1.39 — LoF-tolerant |
| GWAS Catalog | 115 unique SNPs / 276 rows |
| ClinVar | 1288 records; 17 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 1 clinical annotations across 2 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 479 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'TYMP' and resolved to 'Thymidine phosphorylase' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 1288 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 9 of 9 traits by best p-value, aggregated from 15 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P19971 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000025708/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3106/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/TYMP — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/TYMP — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=TYMP%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=TYMP — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/TYMP — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:31:18  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
