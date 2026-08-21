# Protein Dossier — MTRF1L (Peptide chain release factor 1-like, mitochondrial)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| PGC cross-disorder traits | 0.284 | 0.0726 | 9.35e-05 | Wald ratio | 1 | cis | NA |
| Bipolar disorder | 0.544 | 0.14 | 1.06e-04 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | 0.0365 | 0.0126 | 0.00377 | Wald ratio | 1 | cis | NA |
| Major depressive disorder | 0.358 | 0.128 | 0.00522 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R14 Flatulence and related conditions | 0.795 | 0.305 | 0.00903 | Wald ratio | 1 | cis | NA |
| Haemoglobin concentration | 0.086 | 0.0333 | 0.00983 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | 0.0296 | 0.0119 | 0.0131 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K29 Gastritis and duodenitis | -0.297 | 0.129 | 0.0218 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K43 Ventral hernia | 0.35 | 0.159 | 0.0274 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: uterine fibroids | -0.385 | 0.18 | 0.0323 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: retinal detachment | 0.382 | 0.18 | 0.0338 | Wald ratio | 1 | cis | NA |
| Schizophrenia | 0.129 | 0.0636 | 0.0425 | Wald ratio | 1 | cis | NA |
| _...and 93 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_7 association rows across 7 traits (6 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Peptide chain release factor 1-like, mitochondrial levels | 8e-521 | rs12206911 | 1 | GCST90248896 | no MR -> candidate analysis |
| Chronotype | 3e-27 | rs62436127 | 1 | GCST007576 | no MR -> candidate analysis |
| Morning person | 3e-27 | rs62436127 | 1 | GCST007565 | no MR -> candidate analysis |
| Morningness | 1e-18 | rs62436127 | 1 | GCST007983 | no MR -> candidate analysis |
| Hepatocyte nuclear factor 1-alpha protein levels (SomaScan I | 9e-12 | rs2038332 | 1 | GCST90442591 | no MR -> candidate analysis |
| Morning vs. evening chronotype | 2e-8 | rs62436127 | 1 | GCST003429 | no MR -> candidate analysis |
| Amygdala volume | 9e-6 | rs9479479 | 1 | GCST009259 | MR: beta=-10.1, p=0.471 (cis) |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 104 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| ovarian benign neoplasm | 0.459 | — | common-variant locus | no MR -> candidate analysis |
| fallopian tube disorder | 0.153 | — | common-variant locus | no MR -> candidate analysis |
| ovarian disorder | 0.153 | — | common-variant locus | no MR -> candidate analysis |
| type 2 diabetes mellitus | 0.108 | — | common-variant locus | no MR -> candidate analysis |
| schizophrenia | 0.057 | — | common-variant locus | MR: beta=0.129, p=0.0425 (cis) |
| diabetes mellitus | 0.093 | — | common-variant locus | no MR -> candidate analysis |
| tooth disorder | 0.091 | — | common-variant locus | no MR -> candidate analysis |
| eye disorder | 0.091 | — | common-variant locus | no MR -> candidate analysis |
| placenta praevia | 0.09 | — | common-variant locus | no MR -> candidate analysis |
| hyperaldosteronism | 0.084 | — | common-variant locus | no MR -> candidate analysis |
| corneal dystrophy | 0.078 | — | common-variant locus | no MR -> candidate analysis |
| mathematical ability | 0.078 | — | common-variant locus | no MR -> candidate analysis |

> Of the 12 rows above, **11 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=8.1e-08, LOEUF=0.989 — LoF-tolerant |
| GWAS Catalog | 79 unique SNPs / 158 rows |
| ClinVar | 83 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 1 clinical annotations across 1 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 104 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'MTRF1L'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 83 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 7 of 7 traits by best p-value, aggregated from 7 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9UGC7 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000112031/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/MTRF1L — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/MTRF1L — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=MTRF1L%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=MTRF1L — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/MTRF1L — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:52:59  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
