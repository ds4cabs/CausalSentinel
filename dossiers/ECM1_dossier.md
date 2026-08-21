# Protein Dossier — ECM1 (Extracellular matrix protein 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Eczema | 0.113 | 0.0202 | 1.85e-08 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: osteoarthritis | 0.0358 | 0.0093 | 1.17e-04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: asthma | 0.0299 | 0.00783 | 1.38e-04 | Wald ratio | 1 | cis | NA |
| Platelet count | -1.79 | 0.473 | 1.53e-04 | Wald ratio | 1 | cis | NA |
| Subjective well being | 0.0118 | 0.00353 | 8.58e-04 | Wald ratio | 1 | cis | NA |
| Age at menarche | -0.0224 | 0.00676 | 9.30e-04 | Wald ratio | 1 | cis | NA |
| Neuroblastoma | 0.168 | 0.0517 | 0.00116 | Wald ratio | 1 | cis | NA |
| Hearing difficulty or problems: Yes | 0.0158 | 0.0049 | 0.00121 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: deep venous thrombosis (dvt) | 0.0606 | 0.0192 | 0.00162 | Wald ratio | 1 | cis | NA |
| Mean cell haemoglobin | 0.0346 | 0.012 | 0.00395 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M16 Coxarthrosis [arthrosis of hip] | 0.0615 | 0.0226 | 0.00639 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I83 Varicose veins of lower extremities | 0.0503 | 0.0191 | 0.00849 | Wald ratio | 1 | cis | NA |
| _...and 110 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3366_51_2` | ECM1 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_15 association rows across 10 traits (13 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Extracellular matrix protein 1 levels | 5e-754 | rs3737240 | 5 | GCST90247388 | no MR -> candidate analysis |
| ECM1 protein levels | 4e-186 | rs3737240 | 1 | GCST90453297 | no MR -> candidate analysis |
| Cerebrospinal fluid protein ECM1 levels | 3e-165 | rs13294 | 1 | GCST90945095 | no MR -> candidate analysis |
| Circulating CA14 levels | 9e-63 | rs138636989 | 1 | GCST90860279 | no MR -> candidate analysis |
| Protein levels in obesity | 7e-22 | rs13294 | 1 | GCST010196 | no MR -> candidate analysis |
| Serum levels of protein TNFRSF13B | 2e-14 | rs3737240 | 1 | GCST90088026 | no MR -> candidate analysis |
| Hip pain | 8e-10 | rs3737240 | 1 | GCST90245884 | no MR -> candidate analysis |
| Genetically independent pain phenotypes (GIP1) | 2e-9 | rs3737240 | 1 | GCST90245879 | no MR -> candidate analysis |
| Glucose-dependent insulinotropic peptide levels | 4e-8 | rs72698892 | 1 | GCST90091159 | no MR -> candidate analysis |
| Systolic blood pressure | 3e-7 | rs12031974 | 2 | GCST90244038 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 383 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| lipoid proteinosis | 0.841 | — | established (curated) | no MR -> candidate analysis |
| hereditary disease | 0.318 | — | established (curated) | no MR -> candidate analysis |
| aortic aneurysm | 0.272 | — | common-variant locus | no MR -> candidate analysis |
| osteoarthritis | 0.267 | — | common-variant locus | MR: beta=0.0358, p=1.17e-04 (cis) |
| multisite chronic pain | 0.264 | — | common-variant locus | no MR -> candidate analysis |
| Hip pain | 0.205 | — | common-variant locus | no MR -> candidate analysis |
| chronic musculoskeletal pain | 0.202 | — | common-variant locus | no MR -> candidate analysis |
| autism | 0.182 | — | established (curated) | no MR -> candidate analysis |
| sebaceous gland disorder | 0.161 | — | common-variant locus | no MR -> candidate analysis |
| asthma | 0.086 | — | common-variant locus | MR: beta=0.0299, p=1.38e-04 (cis) |
| atopic eczema | 0.142 | — | common-variant locus | no MR -> candidate analysis |
| circadian rhythm | 0.143 | — | common-variant locus | no MR -> candidate analysis |
| insomnia | 0.14 | — | common-variant locus | no MR -> candidate analysis |

> Of the 13 rows above, **11 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.2e-17, LOEUF=1.17 — LoF-tolerant |
| GWAS Catalog | 123 unique SNPs / 299 rows |
| ClinVar | 215 records; 10 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 383 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'ECM1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 215 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 10 of 10 traits by best p-value, aggregated from 15 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q16610 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000143369/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/ECM1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/ECM1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=ECM1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/ECM1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:23:14  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
