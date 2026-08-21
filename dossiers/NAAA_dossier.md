# Protein Dossier — NAAA (N-acylethanolamine-hydrolyzing acid amidase)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Rheumatoid arthritis | -0.089 | 0.0309 | 0.00396 | Wald ratio | 1 | cis | NA |
| Eczema | -0.0963 | 0.0338 | 0.00435 | Wald ratio | 1 | cis | NA |
| Hearing difficulty or problems: Yes | -0.0244 | 0.00863 | 0.00474 | Wald ratio | 1 | cis | NA |
| Thyroid cancer | 0.456 | 0.163 | 0.00507 | Wald ratio | 1 | cis | NA |
| Endometrioid ovarian cancer | 0.148 | 0.0579 | 0.0105 | Wald ratio | 1 | cis | NA |
| Alzheimer's disease | 0.0797 | 0.0323 | 0.0136 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: migraine | -0.0685 | 0.0302 | 0.0234 | Wald ratio | 1 | cis | NA |
| Age at menopause | -0.0729 | 0.0365 | 0.0455 | Wald ratio | 1 | cis | NA |
| Fasting proinsulin | 0.0292 | 0.0146 | 0.0455 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R04 Haemorrhage from respiratory passages | 0.119 | 0.0604 | 0.0488 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K44 Diaphragmatic hernia | 0.0717 | 0.0364 | 0.0489 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M23 Internal derangement of knee | 0.0601 | 0.0309 | 0.0517 | Wald ratio | 1 | cis | NA |
| _...and 98 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3173_49_2` | ASAHL | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_42 association rows across 22 traits (40 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating NAAA levels | 2e-2150 | rs112197434 | 3 | GCST90859725 | no MR -> candidate analysis |
| CTSF/NAAA protein level ratio | 6e-2078 | rs4859572 | 1 | GCST90314314 | no MR -> candidate analysis |
| CREG1/NAAA protein level ratio | 3e-1897 | rs4859572 | 1 | GCST90314250 | no MR -> candidate analysis |
| NAAA/SMPD1 protein level ratio | 2e-1786 | rs4859572 | 1 | GCST90315510 | no MR -> candidate analysis |
| CTSZ/NAAA protein level ratio | 7e-1722 | rs4859572 | 1 | GCST90314320 | no MR -> candidate analysis |
| N-acylethanolamine-hydrolyzing acid amidase levels | 1e-570 | rs111981122 | 12 | GCST90248592 | no MR -> candidate analysis |
| Serum levels of protein NAAA | 1e-263 | rs10518142 | 3 | GCST90088245 | no MR -> candidate analysis |
| CXCL10/CXCL9 protein level ratio | 1e-233 | rs13118503 | 1 | GCST90314331 | no MR -> candidate analysis |
| Blood protein levels | 4e-159 | rs58317633 | 2 | GCST006585 | no MR -> candidate analysis |
| N-acylethanolamine-hydrolyzing acid amidase levels (NAAA.317 | 4e-101 | rs9996608 | 3 | GCST90242013 | no MR -> candidate analysis |
| NAAA protein levels | 4e-99 | rs7664613 | 3 | GCST90469991 | no MR -> candidate analysis |
| N-acylethanolamine-hydrolyzing acid amidase level in Chronic | 4e-72 | rs111427893 | 1 | GCST90237251 | no MR -> candidate analysis |
| _...and 10 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 165 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Tietze syndrome | 0.41 | — | common-variant locus | no MR -> candidate analysis |
| cellulitis | 0.41 | — | common-variant locus | MR: beta=0.0877, p=0.0785 (cis) |
| abscess | 0.41 | — | common-variant locus | no MR -> candidate analysis |
| familial hemolytic anemia | 0.295 | — | common-variant locus | no MR -> candidate analysis |
| type 2 diabetes mellitus | 0.039 | — | common-variant locus | no MR -> candidate analysis |
| device complication | 0.038 | — | common-variant locus | no MR -> candidate analysis |

> Of the 6 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (N-acylethanolamine-hydrolyzing acid amidase) |
| gnomAD constraint | pLI=3.2e-12, LOEUF=1.14 — LoF-tolerant |
| GWAS Catalog | 93 unique SNPs / 186 rows |
| ClinVar | 110 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 165 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'NAAA' and resolved to 'N-acylethanolamine-hydrolyzing acid amidase' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 110 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 22 traits by best p-value, aggregated from 42 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q02083 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000138744/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4349/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/NAAA — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/NAAA — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=NAAA%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/NAAA — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:54:05  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
