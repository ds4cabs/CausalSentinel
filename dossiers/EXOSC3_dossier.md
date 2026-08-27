# Protein Dossier — EXOSC3 (Exosome complex component RRP40)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: emphysema or chronic bronchitis | 0.192 | 0.0607 | 0.00152 | Wald ratio | 1 | trans | NA |
| Forearm bone mineral density | 0.192 | 0.064 | 0.00275 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: D25 Leiomyoma of uterus | 0.168 | 0.0634 | 0.00808 | Wald ratio | 1 | trans | NA |
| Neuroticism | 0.0391 | 0.015 | 0.00932 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: M23 Internal derangement of knee | 0.128 | 0.0502 | 0.0105 | Wald ratio | 1 | trans | NA |
| Hearing difficulty or problems: Yes | 0.0358 | 0.0141 | 0.0111 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: osteoarthritis | 0.0639 | 0.0266 | 0.0162 | Wald ratio | 1 | trans | NA |
| Happiness | 0.0246 | 0.0105 | 0.0192 | Wald ratio | 1 | trans | NA |
| Type 2 diabetes | 0.259 | 0.113 | 0.0216 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: hiatus hernia | 0.11 | 0.0499 | 0.0268 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: K29 Gastritis and duodenitis | 0.106 | 0.0494 | 0.0326 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: K35 Acute appendicitis | -0.347 | 0.179 | 0.0523 | Wald ratio | 1 | trans | NA |
| _...and 61 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_5 association rows across 5 traits (3 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Height | 2e-33 | rs927631 | 1 | GCST90245848 | no MR -> candidate analysis |
| Reticulocyte count | 2e-9 | rs11330143 | 1 | GCST90002405 | no MR -> candidate analysis |
| Forced vital capacity (FVC) | 2e-8 | rs10973574 | 1 | GCST90705071 | no MR -> candidate analysis |
| Loneliness (linear analysis) | 2e-6 | rs78173384 | 1 | GCST003772 | no MR -> candidate analysis |
| Response to serotonin-norepinephrine reuptake inhibitors (re | 9e-6 | rs201857596 | 1 | GCST012159 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 150 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| pontocerebellar hypoplasia type 1 | 0.872 | — | established (curated) | no MR -> candidate analysis |
| pontocerebellar hypoplasia | 0.841 | — | established (curated) | no MR -> candidate analysis |
| Non-syndromic pontocerebellar hypoplasia | 0.841 | — | established (curated) | no MR -> candidate analysis |
| hereditary disease | 0.681 | — | established (curated) | no MR -> candidate analysis |
| microcephaly | 0.559 | — | established (curated) | no MR -> candidate analysis |
| Hypotonia | 0.559 | — | established (curated) | no MR -> candidate analysis |
| Abnormal cerebellum morphology | 0.559 | — | established (curated) | no MR -> candidate analysis |
| Abnormality of the nervous system | 0.559 | — | established (curated) | no MR -> candidate analysis |
| Paucity of anterior horn motor neurons | 0.559 | — | established (curated) | no MR -> candidate analysis |
| Lissencephaly | 0.559 | — | established (curated) | no MR -> candidate analysis |
| fetal akinesia deformation sequence 1 | 0.559 | — | established (curated) | no MR -> candidate analysis |
| congenital myopathy | 0.559 | — | established (curated) | no MR -> candidate analysis |
| Severe intrauterine growth retardation | 0.559 | — | established (curated) | no MR -> candidate analysis |
| Hypoplasia of the pons | 0.559 | — | established (curated) | no MR -> candidate analysis |

> Of the 14 rows above, **14 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=3.4e-05, LOEUF=1.06 — LoF-tolerant |
| GWAS Catalog | 21 unique SNPs / 39 rows |
| ClinVar | 399 records; 7 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 150 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'EXOSC3'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 399 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 5 of 5 traits by best p-value, aggregated from 5 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9NQT5 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000107371/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/EXOSC3 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/EXOSC3 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=EXOSC3%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/EXOSC3 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:30:11  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
