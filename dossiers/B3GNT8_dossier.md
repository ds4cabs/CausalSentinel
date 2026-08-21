# Protein Dossier — B3GNT8 (Queuosine-tRNA galactosyltransferase)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Height | -0.0376 | 0.00403 | 1.03e-20 | Wald ratio | 1 | cis | NA |
| Weight | -0.0128 | 0.00292 | 1.15e-05 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | -0.00985 | 0.00271 | 2.83e-04 | Wald ratio | 1 | cis | NA |
| Coronary heart disease | -0.0396 | 0.0126 | 0.00171 | Wald ratio | 1 | cis | NA |
| Diastolic blood pressure  automated reading | 0.0104 | 0.00339 | 0.00211 | Wald ratio | 1 | cis | NA |
| Potassium in urine | -0.0103 | 0.00336 | 0.00227 | Wald ratio | 1 | cis | NA |
| Creatinine (enzymatic) in urine | -0.00959 | 0.00317 | 0.00248 | Wald ratio | 1 | cis | NA |
| Thyroid cancer | 0.34 | 0.115 | 0.00299 | Wald ratio | 1 | cis | NA |
| Sleep duration | -0.00749 | 0.00258 | 0.00377 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | -0.00807 | 0.00286 | 0.00479 | Wald ratio | 1 | cis | NA |
| Thalamus volume | -22.8 | 8.47 | 0.00723 | Wald ratio | 1 | cis | NA |
| Ferritin | -0.0333 | 0.0128 | 0.00904 | Wald ratio | 1 | cis | NA |
| _...and 112 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_33 association rows across 22 traits (32 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| UDP-GlcNAc:betaGal beta-1,3-N-acetylglucosaminyltransferase  | 9e-726 | rs284662 | 2 | GCST90246634 | no MR -> candidate analysis |
| N-acetyllactosaminide beta-1,3-N-acetylglucosaminyltransfera | 1e-328 | rs284662 | 1 | GCST90248603 | no MR -> candidate analysis |
| Blood protein levels | 1e-238 | rs284663 | 1 | GCST006585 | no MR -> candidate analysis |
| Serum levels of protein B3GNT2 | 6e-73 | rs284662 | 1 | GCST90089962 | no MR -> candidate analysis |
| B3GNT8 protein levels | 1e-72 | rs284662 | 1 | GCST90453319 | no MR -> candidate analysis |
| Height | 2e-72 | rs284661 | 8 | GCST90662911 | MR: beta=-0.0376, p=1.03e-20 (cis) |
| Body size or adipose distribution (multivariate analysis) | 1e-50 | rs284660 | 1 | GCST90624105 | no MR -> candidate analysis |
| CD27/CD79B protein level ratio | 1e-34 | rs284663 | 1 | GCST90313770 | no MR -> candidate analysis |
| Circulating ADAM23 levels | 5e-31 | rs2569754 | 1 | GCST90859683 | no MR -> candidate analysis |
| ADAM23 protein levels | 5e-30 | rs284662 | 1 | GCST90468219 | no MR -> candidate analysis |
| Phosphopantothenoylcysteine decarboxylase protein levels (So | 7e-26 | rs284662 | 1 | GCST90439264 | no MR -> candidate analysis |
| Circulating ISLR2 levels | 4e-24 | rs2569754 | 1 | GCST90860750 | no MR -> candidate analysis |
| _...and 10 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 64 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| androgenetic alopecia | 0.26 | — | common-variant locus | no MR -> candidate analysis |
| atrial fibrillation | 0.179 | — | common-variant locus | no MR -> candidate analysis |
| heart failure | 0.17 | — | common-variant locus | no MR -> candidate analysis |
| hair color | 0.141 | — | common-variant locus | no MR -> candidate analysis |
| angina pectoris | 0.092 | — | common-variant locus | no MR -> candidate analysis |

> Of the 5 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=NA, LOEUF=NA — Constraint metrics missing; LoF tolerance cannot be judged. |
| GWAS Catalog | 104 unique SNPs / 238 rows |
| ClinVar | 110 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 64 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'B3GNT8'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 110 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 22 traits by best p-value, aggregated from 33 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q67FW5 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000177191/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/B3GNT8 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/B3GNT8 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=B3GNT8%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/B3GNT8 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:14:48  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
