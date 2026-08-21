# Protein Dossier — PCOLCE (Procollagen C-endopeptidase enhancer 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Red blood cell count | -0.104 | 0.0118 | 1.95e-18 | Wald ratio | 1 | cis | NA |
| Mean cell haemoglobin | 0.461 | 0.0549 | 4.60e-17 | Wald ratio | 1 | cis | NA |
| Mean cell volume | 1.03 | 0.138 | 7.57e-14 | Wald ratio | 1 | cis | NA |
| Iron | 0.264 | 0.0487 | 6.38e-08 | Wald ratio | 1 | cis | NA |
| Transferrin Saturation | 0.258 | 0.0492 | 1.52e-07 | Wald ratio | 1 | cis | 0.883 |
| Packed cell volume | -0.467 | 0.0956 | 1.05e-06 | Wald ratio | 1 | cis | NA |
| Mean cell haemoglobin concentration | 0.0672 | 0.018 | 1.86e-04 | Wald ratio | 1 | cis | NA |
| Height | 0.0568 | 0.0166 | 6.07e-04 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | -0.0513 | 0.0152 | 7.35e-04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: joint disorder | 0.367 | 0.121 | 0.00241 | Wald ratio | 1 | cis | NA |
| Creatinine (enzymatic) in urine | -0.0339 | 0.0112 | 0.00252 | Wald ratio | 1 | cis | NA |
| Diastolic blood pressure  automated reading | -0.0355 | 0.012 | 0.00315 | Wald ratio | 1 | cis | NA |
| _...and 107 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_16 association rows across 14 traits (12 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Hematological traits (multi-trait analysis) | 1e-113 | rs11970888 | 1 | GCST90838669 | no MR -> candidate analysis |
| Circulating PCOLCE levels | 1e-35 | rs537022088 | 1 | GCST90860486 | no MR -> candidate analysis |
| LRCH4 protein levels | 6e-19 | rs62482223 | 1 | GCST90469791 | no MR -> candidate analysis |
| Pyruvate levels | 2e-15 | rs62482222 | 1 | GCST90501232 | no MR -> candidate analysis |
| PILRB protein levels | 6e-14 | rs112685211 | 1 | GCST90470237 | no MR -> candidate analysis |
| Mean corpuscular haemoglobin (UKB data field 30050) | 1e-13 | rs112888745 | 1 | GCST90468084 | no MR -> candidate analysis |
| Degree of unsaturation | 9e-12 | rs2734895 | 1 | GCST90501284 | no MR -> candidate analysis |
| Height | 6e-10 | rs2272575 | 1 | GCST90245848 | MR: beta=0.0568, p=6.07e-04 (cis) |
| Height (baseline) | 2e-9 | rs34048349 | 1 | GCST90565843 | no MR -> candidate analysis |
| Unsupervised deep imaging phenotypes (UDIP-FA) | 9e-9 | rs62482222 | 1 | GCST90860937 | no MR -> candidate analysis |
| Stool frequency | 1e-8 | rs62482222 | 3 | GCST90002250 | no MR -> candidate analysis |
| High-density lipoprotein levels (MTAG) | 3e-8 | rs2734895 | 1 | GCST90179147 | no MR -> candidate analysis |
| _...and 2 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 564 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| anemia (phenotype) | 0.124 | — | common-variant locus | no MR -> candidate analysis |
| hair color | 0.123 | — | common-variant locus | no MR -> candidate analysis |
| anemia | 0.104 | — | common-variant locus | no MR -> candidate analysis |
| polycythemia | 0.093 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Bone morphogenetic protein 1) |
| gnomAD constraint | pLI=2.3e-08, LOEUF=0.934 — LoF-tolerant |
| GWAS Catalog | 108 unique SNPs / 240 rows |
| ClinVar | 111 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 564 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'PCOLCE' and resolved to 'Bone morphogenetic protein 1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 111 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 14 of 14 traits by best p-value, aggregated from 16 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q15113 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000106333/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3898/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PCOLCE — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PCOLCE — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PCOLCE%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PCOLCE — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:12:44  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
