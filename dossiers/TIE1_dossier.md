# Protein Dossier — TIE1 (Tyrosine-protein kinase receptor Tie-1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: hypertension | -0.0105 | 0.00291 | 3.13e-04 | Inverse variance weighted | 2 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | -0.0105 | 0.00291 | 3.13e-04 | Inverse variance weighted | 2 | trans | NA |
| Forced vital capacity (FVC) | -0.0156 | 0.00538 | 0.00374 | Inverse variance weighted | 2 | cis | NA |
| Forced vital capacity (FVC) | -0.0156 | 0.00538 | 0.00374 | Inverse variance weighted | 2 | trans | NA |
| Hirschsprung's disease | -1.19 | 0.431 | 0.00561 | Inverse variance weighted | 2 | cis | NA |
| Hirschsprung's disease | -1.19 | 0.431 | 0.00561 | Inverse variance weighted | 2 | trans | NA |
| Diagnoses - main ICD10: K80 Cholelithiasis | 0.00256 | 0.000946 | 0.0067 | Inverse variance weighted | 2 | cis | NA |
| Diagnoses - main ICD10: K80 Cholelithiasis | 0.00256 | 0.000946 | 0.0067 | Inverse variance weighted | 2 | trans | NA |
| HDL cholesterol | 0.027 | 0.0108 | 0.0123 | Inverse variance weighted | 2 | cis | NA |
| HDL cholesterol | 0.027 | 0.0108 | 0.0123 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: diverticular disease or diverticulitis | 0.00172 | 0.000706 | 0.0151 | Inverse variance weighted | 2 | cis | NA |
| Non-cancer illness code  self-reported: diverticular disease or diverticulitis | 0.00172 | 0.000706 | 0.0151 | Inverse variance weighted | 2 | trans | NA |
| _...and 197 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2844_53_2` | sTie-1 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_52 association rows across 36 traits (50 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating TIE1 levels | 7e-256 | rs4660729 | 2 | GCST90860467 | no MR -> candidate analysis |
| NOTCH1/TIE1 protein level ratio | 6e-249 | rs3120044 | 1 | GCST90315546 | no MR -> candidate analysis |
| TIE1 protein levels | 4e-243 | rs3768046 | 1 | GCST90470863 | no MR -> candidate analysis |
| Tyrosine-protein kinase receptor Tie-1, soluble levels | 2e-83 | rs3120276 | 2 | GCST90250042 | no MR -> candidate analysis |
| Height | 1e-39 | rs2275180 | 1 | GCST90245848 | no MR -> candidate analysis |
| Cerebrospinal fluid protein TIE1 levels | 1e-33 | rs3768046 | 1 | GCST90944914 | no MR -> candidate analysis |
| Serum levels of protein TIE1 | 1e-30 | rs3768046 | 1 | GCST90088101 | no MR -> candidate analysis |
| Platelet count | 8e-28 | rs140190628 | 2 | GCST90002402 | MR: beta=-1.94, p=0.0915 (cis) |
| Tyrosine-protein kinase receptor Tie-1, soluble levels (TIE1 | 5e-24 | rs2275180 | 1 | GCST90243207 | no MR -> candidate analysis |
| Hemoglobin concentration | 2e-21 | rs4660253 | 4 | GCST90002310 | no MR -> candidate analysis |
| Hemoglobin levels | 2e-20 | rs3120047 | 2 | GCST90662903 | no MR -> candidate analysis |
| Hemoglobin | 1e-17 | rs4660253 | 2 | GCST90002384 | no MR -> candidate analysis |
| _...and 24 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 551 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| lymphatic malformation 11 | 0.706 | — | established (curated) | no MR -> candidate analysis |
| cardiovascular disorder | 0.327 | — | common-variant locus | no MR -> candidate analysis |
| hypertensive disorder | 0.106 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 1 known modulators (Tyrosine-protein kinase receptor Tie-1) |
| gnomAD constraint | pLI=3.8e-20, LOEUF=0.813 — LoF-tolerant |
| GWAS Catalog | 76 unique SNPs / 152 rows |
| ClinVar | 221 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 551 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'TIE1' and resolved to 'Tyrosine-protein kinase receptor Tie-1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 221 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 36 traits by best p-value, aggregated from 52 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P35590 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000066056/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL5274/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/TIE1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/TIE1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=TIE1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/TIE1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:21:12  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
