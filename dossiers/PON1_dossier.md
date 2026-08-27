# Protein Dossier — PON1 (Serum paraoxonase/arylesterase 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Body mass index (BMI) | 0.00803 | 0.00312 | 0.00996 | Wald ratio | 1 | cis | NA |
| Lung cancer | -0.0545 | 0.0222 | 0.0139 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R04 Haemorrhage from respiratory passages | 0.0898 | 0.0397 | 0.0235 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: joint disorder | -0.113 | 0.0511 | 0.0275 | Wald ratio | 1 | cis | NA |
| Underlying (primary) cause of death: ICD10: E85.4 Organ-limited amyloidosis | 0.797 | 0.364 | 0.0284 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K20 Oesophagitis | 0.0608 | 0.0296 | 0.0401 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: J33 Nasal polyp | 0.0844 | 0.0417 | 0.0428 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: bone disorder | 0.12 | 0.0592 | 0.0429 | Wald ratio | 1 | cis | NA |
| Age at menopause | -0.0471 | 0.0236 | 0.0455 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: kidney stone or ureter stone or bladder stone | 0.0657 | 0.033 | 0.0465 | Wald ratio | 1 | cis | NA |
| Weight | 0.00536 | 0.00275 | 0.0514 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Wrist | -0.0454 | 0.0233 | 0.0514 | Wald ratio | 1 | cis | NA |
| _...and 104 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4261_55_2` | paraoxonase 1 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_254 association rows across 190 traits (248 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating PON3 levels | 2e-891 | rs10953142 | 1 | GCST90859987 | no MR -> candidate analysis |
| Testis-expressed sequence 29 protein levels | 4e-400 | rs662 | 2 | GCST90249809 | no MR -> candidate analysis |
| Myeloid leukemia factor 1 levels | 3e-316 | rs3917529 | 1 | GCST90248481 | no MR -> candidate analysis |
| Paraoxonase activity | 1e-303 | rs2057681 | 2 | GCST001677 | no MR -> candidate analysis |
| PON1 protein levels | 2e-215 | rs705379 | 13 | GCST90453213 | no MR -> candidate analysis |
| Proteasome subunit beta type-9 levels | 6e-148 | rs1157745 | 2 | GCST90249140 | no MR -> candidate analysis |
| T-cell surface protein tactile levels | 1e-99 | rs1157745 | 2 | GCST90249758 | no MR -> candidate analysis |
| Syntaxin-10 levels (STX10.12842.43.3) | 1e-93 | rs662 | 1 | GCST90242944 | no MR -> candidate analysis |
| Testis-expressed sequence 29 protein levels (TEX29.10557.6.3 | 3e-93 | rs3917539 | 2 | GCST90242989 | no MR -> candidate analysis |
| Filamin-A level in Chronic kidney disease with hypertension  | 6e-81 | rs662 | 1 | GCST90233147 | no MR -> candidate analysis |
| PON2 protein levels | 2e-79 | rs3917510 | 3 | GCST90470286 | no MR -> candidate analysis |
| NHL repeat-containing protein 3 levels | 3e-79 | rs1157745 | 1 | GCST90248677 | no MR -> candidate analysis |
| _...and 178 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 795 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| amyotrophic lateral sclerosis | 0.525 | — | established (curated) | no MR -> candidate analysis |
| atopic eczema | 0.554 | — | common-variant locus | no MR -> candidate analysis |
| obesity disorder | 0.475 | — | common-variant locus | no MR -> candidate analysis |
| idiopathic pulmonary fibrosis | 0.388 | — | common-variant locus | no MR -> candidate analysis |
| type 2 diabetes mellitus | 0.057 | — | common-variant locus | no MR -> candidate analysis |
| diabetes mellitus | 0.057 | — | common-variant locus | no MR -> candidate analysis |

> Of the 6 rows above, **6 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Serum paraoxonase/arylesterase 1) |
| gnomAD constraint | pLI=1.5e-12, LOEUF=1.24 — LoF-tolerant |
| GWAS Catalog | 120 unique SNPs / 251 rows |
| ClinVar | 97 records; 3 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 795 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'PON1' and resolved to 'Serum paraoxonase/arylesterase 1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 97 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 20 of 190 traits by best p-value, aggregated from 254 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P27169 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000005421/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3167/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PON1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PON1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PON1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PON1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:32:03  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: pharmgkb
