# Protein Dossier — CREG1 (Protein CREG1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: H25 Senile cataract | 0.383 | 0.083 | 3.95e-06 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: asthma | 0.0907 | 0.0271 | 8.17e-04 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: J33 Nasal polyp | 0.321 | 0.113 | 0.00464 | Wald ratio | 1 | cis | NA |
| Low grade serous ovarian cancer | 0.562 | 0.212 | 0.00811 | Wald ratio | 1 | cis | NA |
| Neo-extraversion | -0.828 | 0.332 | 0.0126 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: psoriasis | -0.356 | 0.146 | 0.0148 | Wald ratio | 1 | cis | NA |
| Mean cell volume | 0.267 | 0.13 | 0.0402 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: G56 Mononeuropathies of upper limb | -0.203 | 0.0998 | 0.0419 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K57 Diverticular disease of intestine | -0.184 | 0.0904 | 0.0422 | Wald ratio | 1 | cis | NA |
| Large vessel disease | -0.322 | 0.159 | 0.0434 | Wald ratio | 1 | cis | NA |
| Transferrin | -0.091 | 0.0453 | 0.0447 | Wald ratio | 1 | cis | NA |
| Fasting insulin | 0.0315 | 0.0158 | 0.0455 | Wald ratio | 1 | cis | NA |
| _...and 97 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_24 association rows across 20 traits (18 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| CREG1 protein levels | 2e-208 | rs7513428 | 1 | GCST90468857 | no MR -> candidate analysis |
| CREG1/PLA2G15 protein level ratio | 1e-197 | rs10753760 | 1 | GCST90314251 | no MR -> candidate analysis |
| CREG1/CTSZ protein level ratio | 9e-176 | rs10753760 | 1 | GCST90314247 | no MR -> candidate analysis |
| ARSA/CREG1 protein level ratio | 4e-123 | rs1773548 | 1 | GCST90313352 | no MR -> candidate analysis |
| Protein CREG1 levels | 1e-71 | rs1229430 | 4 | GCST90247153 | no MR -> candidate analysis |
| Serum levels of protein CREG1 | 2e-33 | rs7516079 | 1 | GCST90090652 | no MR -> candidate analysis |
| Blood protein levels | 5e-28 | rs7516079 | 1 | GCST006585 | no MR -> candidate analysis |
| Protein CREG1 levels (CREG1.9357.4.3) | 1e-20 | rs7513428 | 1 | GCST90242426 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 1e-15 | rs9287085 | 2 | GCST90838669 | no MR -> candidate analysis |
| GLIPR1 protein levels | 7e-14 | rs539422655 | 1 | GCST90469357 | no MR -> candidate analysis |
| Vitamin D deficiency | 2e-11 | rs140599862 | 1 | GCST90667553 | no MR -> candidate analysis |
| CD3 on CD39+ activated CD4 regulatory T cell | 1e-10 | rs10918708 | 1 | GCST90001854 | no MR -> candidate analysis |
| _...and 8 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 137 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| acquired neutropenia | 0.473 | — | common-variant locus | no MR -> candidate analysis |
| venous thromboembolism | 0.41 | — | common-variant locus | no MR -> candidate analysis |
| stroke disorder | 0.362 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.362 | — | common-variant locus | no MR -> candidate analysis |
| open-angle glaucoma | 0.07 | — | common-variant locus | no MR -> candidate analysis |
| asthma | 0.034 | — | common-variant locus | MR: beta=0.0907, p=8.17e-04 (cis) |
| chronic rhinosinusitis | 0.034 | — | common-variant locus | no MR -> candidate analysis |

> Of the 7 rows above, **6 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.3e-07, LOEUF=1.46 — LoF-tolerant |
| GWAS Catalog | 70 unique SNPs / 127 rows |
| ClinVar | 66 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 137 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CREG1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 66 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 20 traits by best p-value, aggregated from 24 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O75629 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000143162/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CREG1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CREG1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CREG1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CREG1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:02:46  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
