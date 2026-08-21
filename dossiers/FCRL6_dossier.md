# Protein Dossier — FCRL6 (Fc receptor-like protein 6)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| IgA nephropathy | 0.411 | 0.174 | 0.0183 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: G47 Sleep disorders | 0.134 | 0.0573 | 0.0191 | Wald ratio | 1 | cis | NA |
| Hip osteoarthritis | 0.137 | 0.0589 | 0.0202 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: small intestine or small bowel cancer | 0.382 | 0.167 | 0.0218 | Wald ratio | 1 | cis | NA |
| Weight | 0.00961 | 0.00442 | 0.0298 | Wald ratio | 1 | cis | NA |
| Low grade serous ovarian cancer | 0.218 | 0.101 | 0.0308 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M72 Fibroblastic disorders | 0.127 | 0.0602 | 0.0348 | Wald ratio | 1 | cis | NA |
| Neo-extraversion | 0.312 | 0.152 | 0.0402 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: osteoarthritis | 0.0327 | 0.0162 | 0.044 | Wald ratio | 1 | cis | NA |
| Bipolar disorder | 0.0944 | 0.0479 | 0.0489 | Wald ratio | 1 | cis | NA |
| Knee and hip osteoarthritis | 0.0842 | 0.0441 | 0.0563 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M17 Gonarthrosis [arthrosis of knee] | 0.0631 | 0.0339 | 0.0627 | Wald ratio | 1 | cis | NA |
| _...and 103 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_37 association rows across 23 traits (33 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| FCRL6/KLRD1 protein level ratio | 4e-3394 | rs6656979 | 1 | GCST90314807 | no MR -> candidate analysis |
| FCRL6/GZMA protein level ratio | 2e-3265 | rs4443889 | 1 | GCST90314806 | no MR -> candidate analysis |
| CD48/FCRL6 protein level ratio | 2e-3023 | rs6656979 | 1 | GCST90313840 | no MR -> candidate analysis |
| CD244/FCRL6 protein level ratio | 5e-2917 | rs4443889 | 1 | GCST90313765 | no MR -> candidate analysis |
| Circulating FCRL6 levels | 2e-2914 | rs55650803 | 1 | GCST90860232 | no MR -> candidate analysis |
| CRTAM/FCRL6 protein level ratio | 1e-2901 | rs6656979 | 1 | GCST90314274 | no MR -> candidate analysis |
| FCRL6 protein levels | 6e-279 | rs12083595 | 8 | GCST90469209 | no MR -> candidate analysis |
| Circulating SLAMF8 levels | 5e-210 | rs72700617 | 3 | GCST90860577 | no MR -> candidate analysis |
| Fc receptor-like protein 6 levels (FCRL6.6617.12.3) | 3e-92 | rs58240276 | 2 | GCST90241155 | no MR -> candidate analysis |
| SLAMF8 protein levels | 8e-81 | rs55742616 | 3 | GCST90470652 | no MR -> candidate analysis |
| Fc receptor-like protein 6 levels | 2e-38 | rs6657365 | 1 | GCST90247569 | no MR -> candidate analysis |
| Cerebrospinal fluid protein FCRL6 levels | 3e-25 | rs11265278 | 1 | GCST90943370 | no MR -> candidate analysis |
| _...and 11 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 107 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| mental disorder | 0.035 | — | common-variant locus | no MR -> candidate analysis |
| glomerulonephritis | 0.035 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=8.6e-18, LOEUF=1.29 — LoF-tolerant |
| GWAS Catalog | 138 unique SNPs / 318 rows |
| ClinVar | 111 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 107 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'FCRL6'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 111 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 23 traits by best p-value, aggregated from 37 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q6DN72 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000181036/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/FCRL6 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/FCRL6 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=FCRL6%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/FCRL6 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:39:18  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
