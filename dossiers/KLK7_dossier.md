# Protein Dossier — KLK7 (Kallikrein-7)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Age at menopause | 0.156 | 0.0569 | 0.00596 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hiatus hernia | 0.0896 | 0.0362 | 0.0132 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: gastro-oesophageal reflux (gord)  or  gastric reflux | 0.0662 | 0.0271 | 0.0148 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Ankle | 0.111 | 0.0461 | 0.0162 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M23 Internal derangement of knee | 0.0866 | 0.0372 | 0.0199 | Wald ratio | 1 | cis | NA |
| Mean cell volume | -0.219 | 0.0949 | 0.0209 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K40 Inguinal hernia | 0.0757 | 0.0341 | 0.0266 | Wald ratio | 1 | cis | NA |
| Subjective well being | -0.0185 | 0.00853 | 0.0303 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | -0.0165 | 0.0078 | 0.0341 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | 0.133 | 0.063 | 0.0342 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: iron deficiency anaemia | 0.151 | 0.0713 | 0.0347 | Wald ratio | 1 | cis | NA |
| Lumbar spine bone mineral density | 0.0451 | 0.0217 | 0.0377 | Wald ratio | 1 | cis | NA |
| _...and 103 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3378_49_2` | Kallikrein 7 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_47 association rows across 25 traits (44 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating KLK10 levels | 2e-587 | rs1654530 | 2 | GCST90860356 | no MR -> candidate analysis |
| Circulating KLK8 levels | 1e-351 | rs10418308 | 3 | GCST90860020 | no MR -> candidate analysis |
| KLK6/MOG protein level ratio | 6e-258 | rs1654535 | 1 | GCST90315255 | no MR -> candidate analysis |
| KLK6/PTPRN2 protein level ratio | 5e-214 | rs1654535 | 1 | GCST90315256 | no MR -> candidate analysis |
| KLK7 protein levels | 3e-168 | rs148022792 | 2 | GCST90469706 | no MR -> candidate analysis |
| Kallikrein-7 levels | 5e-154 | rs2659067 | 9 | GCST90248163 | no MR -> candidate analysis |
| Circulating KLK6 levels | 1e-85 | rs57392237 | 1 | GCST90859992 | no MR -> candidate analysis |
| Kallikrein-8 levels | 5e-85 | rs1122466 | 1 | GCST90248164 | no MR -> candidate analysis |
| Kallikrein-7 levels (KLK7.3378.49.2) | 1e-66 | rs2739419 | 2 | GCST90241679 | no MR -> candidate analysis |
| Serum levels of protein KLK10 | 2e-57 | rs57392237 | 1 | GCST90089306 | no MR -> candidate analysis |
| Cerebrospinal fluid protein KLK7 levels | 8e-53 | rs76662835 | 1 | GCST90944381 | no MR -> candidate analysis |
| kallikrein-11 levels | 2e-50 | rs1122466 | 1 | GCST90012012 | no MR -> candidate analysis |
| _...and 13 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 221 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| erythematosquamous dermatosis | 0.351 | — | common-variant locus | no MR -> candidate analysis |
| seborrheic dermatitis | 0.316 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Kallikrein-7) |
| gnomAD constraint | pLI=1.4e-05, LOEUF=1.21 — LoF-tolerant |
| GWAS Catalog | 167 unique SNPs / 422 rows |
| ClinVar | 74 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 221 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'KLK7' and resolved to 'Kallikrein-7' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 74 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 25 traits by best p-value, aggregated from 47 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P49862 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000169035/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2443/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/KLK7 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/KLK7 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=KLK7%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/KLK7 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:25:03  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
