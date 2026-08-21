# Protein Dossier — ASPN (Asporin)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Height | 0.0508 | 0.00656 | 9.79e-15 | Wald ratio | 1 | cis | 1.47e-06 |
| Non-cancer illness code  self-reported: hypertension | 0.0306 | 0.009 | 6.77e-04 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | -0.018 | 0.00544 | 9.21e-04 | Wald ratio | 1 | cis | NA |
| Potassium in urine | 0.0146 | 0.00553 | 0.00806 | Wald ratio | 1 | cis | NA |
| Fasting glucose | -0.0165 | 0.00699 | 0.0181 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I84 Haemorrhoids | -0.0869 | 0.0382 | 0.023 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Glaucoma | 0.0937 | 0.0415 | 0.0239 | Wald ratio | 1 | cis | NA |
| Neuroticism | -0.0191 | 0.00847 | 0.0244 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | 0.0155 | 0.00704 | 0.0274 | Wald ratio | 1 | cis | NA |
| PGC cross-disorder traits | 0.0571 | 0.0262 | 0.0297 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M23 Internal derangement of knee | -0.0848 | 0.0399 | 0.0337 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: osteoarthritis | -0.0395 | 0.019 | 0.0372 | Wald ratio | 1 | cis | NA |
| _...and 99 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_13 association rows across 11 traits (12 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| COL6A3/OGN protein level ratio | 2e-3781 | rs8067 | 1 | GCST90314177 | no MR -> candidate analysis |
| COLEC12/OGN protein level ratio | 3e-3306 | rs8067 | 1 | GCST90314184 | no MR -> candidate analysis |
| IGFBP4/OGN protein level ratio | 1e-2613 | rs8067 | 1 | GCST90315134 | no MR -> candidate analysis |
| Circulating GDF2 levels | 2e-47 | rs200538582 | 1 | GCST90859810 | no MR -> candidate analysis |
| AGRP/CCN1 protein level ratio | 2e-36 | rs8067 | 1 | GCST90313202 | no MR -> candidate analysis |
| Asporin levels (ASPN.6451.64.3) | 2e-20 | rs41278695 | 1 | GCST90240347 | no MR -> candidate analysis |
| ASPN protein levels | 2e-14 | rs182736327 | 1 | GCST90468377 | no MR -> candidate analysis |
| GDF2 protein levels | 5e-12 | rs113478791 | 2 | GCST90469322 | no MR -> candidate analysis |
| Body mass index | 7e-10 | rs7033979 | 1 | GCST90018947 | MR: beta=-0.018, p=9.21e-04 (cis) |
| Urate levels | 3e-9 | rs3174352 | 2 | GCST008972 | no MR -> candidate analysis |
| Height | 2e-8 | rs13301537 | 1 | GCST90245844 | MR: beta=0.0508, p=9.79e-15 (cis) |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 756 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| obstructive sleep apnea syndrome | 0.205 | — | common-variant locus | no MR -> candidate analysis |
| skin disorder | 0.138 | — | common-variant locus | no MR -> candidate analysis |
| mononeuropathy | 0.131 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.11 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=3.8e-11, LOEUF=1.2 — LoF-tolerant |
| GWAS Catalog | 64 unique SNPs / 126 rows |
| ClinVar | 72 records; 4 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 756 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'ASPN'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 72 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 11 of 11 traits by best p-value, aggregated from 13 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9BXN1 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000106819/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/ASPN — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/ASPN — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=ASPN%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/ASPN — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:11:22  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
