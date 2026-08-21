# Protein Dossier — APCS (Serum amyloid P-component)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: muscle or soft tissue injuries | 0.286 | 0.0862 | 9.18e-04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: osteoarthritis | 0.0842 | 0.0297 | 0.00451 | Wald ratio | 1 | cis | NA |
| Low grade serous ovarian cancer | 0.55 | 0.224 | 0.0139 | Wald ratio | 1 | cis | NA |
| Urate | 0.049 | 0.0215 | 0.0227 | Wald ratio | 1 | cis | NA |
| Fasting proinsulin | 0.0633 | 0.0287 | 0.0272 | Wald ratio | 1 | cis | NA |
| Red blood cell count | -0.019 | 0.0092 | 0.0389 | Wald ratio | 1 | cis | NA |
| Schizophrenia | 0.0839 | 0.0415 | 0.0431 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: ankylosing spondylitis | 0.284 | 0.141 | 0.0436 | Wald ratio | 1 | cis | NA |
| Ischemic stroke | -0.129 | 0.0646 | 0.0459 | Wald ratio | 1 | cis | NA |
| Fractured or broken bones in last 5 years | 0.0564 | 0.0284 | 0.047 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R55 Syncope and collapse | -0.272 | 0.137 | 0.0473 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | -0.316 | 0.163 | 0.0516 | Wald ratio | 1 | cis | NA |
| _...and 75 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2474_54_5` | SAP | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_24 association rows across 16 traits (23 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| APCS protein levels | 7e-144 | rs36126250 | 3 | GCST90468328 | no MR -> candidate analysis |
| Serum amyloid P-component levels | 1e-61 | rs35737842 | 3 | GCST90249426 | no MR -> candidate analysis |
| C-reactive protein levels | 8e-57 | rs16842320 | 3 | GCST009777 | no MR -> candidate analysis |
| C-reactive protein levels (MTAG) | 6e-49 | rs61680681 | 2 | GCST90179146 | no MR -> candidate analysis |
| Circulating SPP1 levels | 1e-27 | rs28383572 | 1 | GCST90859966 | no MR -> candidate analysis |
| Phosphate levels (UKB data field 30810) | 2e-27 | rs28383573 | 1 | GCST90468094 | no MR -> candidate analysis |
| SLAMF8 protein levels | 6e-27 | rs138112491 | 1 | GCST90470652 | no MR -> candidate analysis |
| Serum levels of protein APCS | 2e-25 | rs28383573 | 1 | GCST90087947 | no MR -> candidate analysis |
| DNA methylation-estimated granulocyte proportions | 5e-18 | rs2808661 | 2 | GCST90014293 | no MR -> candidate analysis |
| SPP1 protein levels | 1e-15 | rs28383572 | 1 | GCST90470733 | no MR -> candidate analysis |
| C1QTNF5 protein levels | 4e-15 | rs35834732 | 1 | GCST90468489 | no MR -> candidate analysis |
| Aortic stenosis | 9e-12 | rs35485101 | 1 | GCST90837551 | no MR -> candidate analysis |
| _...and 4 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 336 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| splenic disorder | 0.363 | — | common-variant locus | no MR -> candidate analysis |
| restless legs syndrome | 0.342 | — | common-variant locus | no MR -> candidate analysis |
| acute tonsillitis | 0.342 | — | common-variant locus | no MR -> candidate analysis |
| bacterial infectious disease | 0.207 | — | common-variant locus | no MR -> candidate analysis |
| inherited retinal dystrophy | 0.195 | — | common-variant locus | no MR -> candidate analysis |
| pneumonia | 0.107 | — | common-variant locus | no MR -> candidate analysis |

> Of the 6 rows above, **6 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 2 known modulators (Serum amyloid P-component) |
| gnomAD constraint | pLI=0.11, LOEUF=2.53 — LoF-tolerant |
| GWAS Catalog | 101 unique SNPs / 210 rows |
| ClinVar | 46 records; 3 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 336 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'APCS' and resolved to 'Serum amyloid P-component' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 46 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 16 of 16 traits by best p-value, aggregated from 24 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P02743 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000132703/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4929/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/APCS — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/APCS — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=APCS%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/APCS — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:06:10  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
