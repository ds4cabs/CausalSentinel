# Protein Dossier — DRGX (Dorsal root ganglia homeobox protein)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: I48 Atrial fibrillation and flutter | -0.16 | 0.0409 | 8.78e-05 | Wald ratio | 1 | trans | NA |
| Height | 0.0166 | 0.00442 | 1.77e-04 | Wald ratio | 1 | trans | NA |
| Heel bone mineral density (BMD) T-score  automated | 0.017 | 0.00476 | 3.54e-04 | Wald ratio | 1 | trans | NA |
| Red blood cell count | -0.00898 | 0.00332 | 0.00676 | Wald ratio | 1 | trans | NA |
| Alcohol intake frequency | -0.0127 | 0.00543 | 0.0193 | Wald ratio | 1 | trans | NA |
| Happiness | -0.0101 | 0.00453 | 0.0252 | Wald ratio | 1 | trans | NA |
| Putamen volume | 19.8 | 8.86 | 0.0253 | Wald ratio | 1 | trans | NA |
| Packed cell volume | -0.0583 | 0.0271 | 0.0313 | Wald ratio | 1 | trans | NA |
| Haemoglobin concentration | -0.0181 | 0.00856 | 0.0346 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: vaginal prolapse or uterine prolapse | -0.114 | 0.056 | 0.0415 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: bone disorder | 0.138 | 0.0685 | 0.0434 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: vitiligo | 0.312 | 0.168 | 0.0635 | Wald ratio | 1 | trans | NA |
| _...and 90 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_52 association rows across 48 traits (17 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| heart rate (HR, mean, inv-normal transformed) | 9e-36 | rs10776560 | 2 | GCST90476338 | no MR -> candidate analysis |
| GLIPR1 protein levels | 1e-24 | rs546183174 | 1 | GCST90469357 | no MR -> candidate analysis |
| ASAH2 protein levels | 2e-20 | rs2889780 | 2 | GCST90468374 | no MR -> candidate analysis |
| Appendicular lean mass | 8e-17 | rs10776560 | 1 | GCST90000025 | no MR -> candidate analysis |
| Theophylline levels | 2e-11 | rs571081313 | 1 | GCST90245454 | no MR -> candidate analysis |
| total creatine kinase (minimum, inv-norm transformed) | 2e-11 | rs4540769 | 1 | GCST90480710 | no MR -> candidate analysis |
| Neutral ceramidase levels | 3e-11 | rs148805593 | 1 | GCST90161676 | no MR -> candidate analysis |
| Height | 1e-10 | rs11598726 | 2 | GCST90435412 | MR: beta=0.0166, p=1.77e-04 (trans) |
| Physical function (baseline) | 7e-10 | rs10776560 | 1 | GCST90565837 | no MR -> candidate analysis |
| Vaginal microbiome presence (o_Bacteroidales) | 1e-8 | rs7903692 | 2 | GCST90026675 | no MR -> candidate analysis |
| Gut microbial network clusters (Pink (at 1 year) x Any Breas | 2e-8 | rs77969576 | 1 | GCST90569458 | no MR -> candidate analysis |
| Bone mineral density mean | 2e-8 | rs139463353 | 1 | GCST90321120 | no MR -> candidate analysis |
| _...and 36 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 150 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| frozen shoulder | 0.382 | — | common-variant locus | no MR -> candidate analysis |
| diabetes mellitus | 0.382 | — | common-variant locus | no MR -> candidate analysis |
| systemic lupus erythematosus | 0.251 | — | common-variant locus | no MR -> candidate analysis |
| Hernia of the abdominal wall | 0.119 | — | common-variant locus | no MR -> candidate analysis |
| response to antihypertensive drug | 0.115 | — | common-variant locus | no MR -> candidate analysis |
| placental abruption | 0.114 | — | common-variant locus | no MR -> candidate analysis |

> Of the 6 rows above, **6 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=4.9e-06, LOEUF=1.06 — LoF-tolerant |
| GWAS Catalog | 37 unique SNPs / 74 rows |
| ClinVar | 94 records; 16 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 150 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'DRGX'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 94 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 48 traits by best p-value, aggregated from 52 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/A6NNA5 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000165606/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/DRGX — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/DRGX — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=DRGX%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/DRGX — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:20:28  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
