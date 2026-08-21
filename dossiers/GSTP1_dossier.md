# Protein Dossier — GSTP1 (Glutathione S-transferase P)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Weight | 0.0535 | 0.0125 | 1.79e-05 | Wald ratio | 1 | cis | NA |
| Mean cell volume | 0.612 | 0.153 | 6.14e-05 | Wald ratio | 1 | cis | NA |
| Mean cell haemoglobin | 0.217 | 0.0601 | 2.98e-04 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K29 Gastritis and duodenitis | 0.245 | 0.072 | 6.45e-04 | Wald ratio | 1 | cis | NA |
| Endometrioid ovarian cancer | -0.449 | 0.169 | 0.00795 | Wald ratio | 1 | cis | NA |
| Knee osteoarthritis | 0.407 | 0.154 | 0.00822 | Wald ratio | 1 | cis | NA |
| Sleep duration | -0.0252 | 0.011 | 0.0222 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M17 Gonarthrosis [arthrosis of knee] | 0.193 | 0.0846 | 0.0222 | Wald ratio | 1 | cis | NA |
| Red blood cell count | -0.0281 | 0.0129 | 0.0297 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: depression | 0.113 | 0.0522 | 0.0305 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: asthma | 0.0773 | 0.0367 | 0.0351 | Wald ratio | 1 | cis | NA |
| Percent emphysema | -0.222 | 0.111 | 0.045 | Wald ratio | 1 | cis | NA |
| _...and 104 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4911_49_2` | Glutathione S-transferase Pi | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_30 association rows across 26 traits (29 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Glutathione S-transferase P (analyte X4911.49) levels | 5e-315 | rs1695 | 1 | GCST90426141 | no MR -> candidate analysis |
| Circulating GSTP1 levels | 1e-217 | rs7927657 | 2 | GCST90860696 | no MR -> candidate analysis |
| GSTP1 protein levels | 1e-210 | rs762803 | 2 | GCST90469414 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 3e-192 | rs6591250 | 1 | GCST90838669 | no MR -> candidate analysis |
| Height (baseline) | 7e-43 | rs145044531 | 1 | GCST90565843 | no MR -> candidate analysis |
| Glutathione S-transferase P levels | 4e-39 | rs11227841 | 1 | GCST90247750 | no MR -> candidate analysis |
| N-acetylglycine levels | 4e-29 | rs640777 | 3 | GCST90245320 | no MR -> candidate analysis |
| Cis-3,4-methyleneheptanoylglycine levels | 4e-20 | rs596603 | 1 | GCST90200274 | no MR -> candidate analysis |
| Hip circumference adjusted for BMI | 7e-17 | rs36051467 | 1 | GCST012227 | no MR -> candidate analysis |
| 2-butenoylglycine levels | 3e-16 | rs596603 | 1 | GCST90200152 | no MR -> candidate analysis |
| Glutathione S-transferase P level in Chronic kidney disease  | 8e-15 | rs1695 | 1 | GCST90237743 | no MR -> candidate analysis |
| Metabolite levels (N-acetyltryptophan) | 2e-14 | rs35297589 | 1 | GCST90300142 | no MR -> candidate analysis |
| _...and 14 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 760 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| connective tissue neoplasm | 0.21 | — | common-variant locus | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 1 known modulators (Glutathione S-transferase P) |
| gnomAD constraint | pLI=8.2e-10, LOEUF=1.3 — LoF-tolerant |
| GWAS Catalog | 72 unique SNPs / 144 rows |
| ClinVar | 83 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 22 clinical annotations across 17 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 760 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'GSTP1' and resolved to 'Glutathione S-transferase P' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 83 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 20 of 26 traits by best p-value, aggregated from 30 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P09211 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000084207/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3902/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/GSTP1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/GSTP1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=GSTP1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=GSTP1 — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/GSTP1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:56:19  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
