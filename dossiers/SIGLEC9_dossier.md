# Protein Dossier — SIGLEC9 (Sialic acid-binding Ig-like lectin 9)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Weight | -0.00702 | 0.00174 | 5.55e-05 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | -0.00739 | 0.00197 | 1.75e-04 | Wald ratio | 1 | cis | NA |
| Amyotrophic lateral sclerosis | 0.0441 | 0.0145 | 0.00237 | Wald ratio | 1 | cis | NA |
| High grade serous ovarian cancer | -0.0379 | 0.013 | 0.00354 | Wald ratio | 1 | cis | NA |
| Neo-extraversion | -0.178 | 0.0641 | 0.0055 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: pneumothorax | 0.214 | 0.0784 | 0.00636 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | -0.0245 | 0.00898 | 0.00642 | Wald ratio | 1 | cis | NA |
| Microalbuminuria | -0.0449 | 0.018 | 0.0124 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: prostate cancer | -0.0596 | 0.0245 | 0.0149 | Wald ratio | 1 | cis | NA |
| Squamous cell lung cancer | -0.0515 | 0.0212 | 0.0152 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: chronic obstructive airways disease or copd | -0.0885 | 0.0369 | 0.0166 | Wald ratio | 1 | cis | NA |
| Iron | -0.0195 | 0.00816 | 0.0168 | Wald ratio | 1 | cis | NA |
| _...and 100 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3007_7_2` | Siglec-9 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_89 association rows across 45 traits (87 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Sialic acid-binding Ig-like lectin 9 levels | 2e-5041 | rs2075803 | 11 | GCST90249553 | no MR -> candidate analysis |
| Circulating SIGLEC9 levels | 3e-2701 | rs2075803 | 6 | GCST90859658 | no MR -> candidate analysis |
| Sialic acid-binding Ig-like lectin 9 levels (SIGLEC9.3007.7. | 6e-2142 | rs2075803 | 2 | GCST90242813 | no MR -> candidate analysis |
| Blood protein levels | 2e-723 | rs1039405 | 3 | GCST006585 | no MR -> candidate analysis |
| Sialic acid-binding Ig-like lectin 7 levels | 6e-420 | rs12983058 | 9 | GCST90425443 | no MR -> candidate analysis |
| Uromodulin levels | 3e-342 | rs2075803 | 2 | GCST90427813 | no MR -> candidate analysis |
| Cerebrospinal fluid protein SIGLEC7 levels | 2e-319 | rs12983058 | 1 | GCST90944577 | no MR -> candidate analysis |
| Circulating SIGLEC7 levels | 6e-310 | rs12983058 | 3 | GCST90860368 | no MR -> candidate analysis |
| SIGLEC7 protein levels | 3e-298 | rs12983058 | 4 | GCST90470635 | no MR -> candidate analysis |
| Serum uromodulin levels (aptamer-based assay) | 2e-280 | rs2075803 | 1 | GCST90129632 | no MR -> candidate analysis |
| Serum levels of protein UMOD | 3e-223 | rs2075803 | 1 | GCST90090697 | no MR -> candidate analysis |
| Protein quantitative trait loci | 5e-208 | rs2075803 | 1 | GCST010900 | no MR -> candidate analysis |
| _...and 33 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 102 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| obesity disorder | 0.24 | — | common-variant locus | no MR -> candidate analysis |
| arthropathy | 0.101 | — | common-variant locus | no MR -> candidate analysis |
| osteoarthritis, knee | 0.061 | — | common-variant locus | MR: beta=0.0165, p=0.438 (cis) |

> Of the 3 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Sialic acid-binding Ig-like lectin 9) |
| gnomAD constraint | pLI=1.4e-06, LOEUF=0.942 — LoF-tolerant |
| GWAS Catalog | 174 unique SNPs / 443 rows |
| ClinVar | 85 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 102 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'SIGLEC9' and resolved to 'Sialic acid-binding Ig-like lectin 9' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 85 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 45 traits by best p-value, aggregated from 89 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9Y336 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000129450/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4105860/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/SIGLEC9 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/SIGLEC9 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=SIGLEC9%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/SIGLEC9 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:06:43  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
