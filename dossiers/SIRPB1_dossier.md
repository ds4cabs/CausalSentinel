# Protein Dossier — SIRPB1 (Signal-regulatory protein beta-1 isoform 3)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Neo-neuroticism | -0.46 | 0.139 | 9.27e-04 | Wald ratio | 1 | cis | NA |
| Endometrioid ovarian cancer | -0.126 | 0.0428 | 0.00324 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C61 Malignant neoplasm of prostate | -0.14 | 0.0502 | 0.0053 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Other bones | -0.045 | 0.0161 | 0.00532 | Wald ratio | 1 | cis | NA |
| Sleep duration | 0.00662 | 0.00277 | 0.0168 | Wald ratio | 1 | cis | NA |
| Serum cystatin C (eGFRcys) | -0.0059 | 0.00268 | 0.0278 | Wald ratio | 1 | cis | NA |
| Fractured or broken bones in last 5 years | -0.0245 | 0.0113 | 0.0304 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: prostate cancer | -0.097 | 0.0458 | 0.0342 | Wald ratio | 1 | cis | NA |
| Large vessel disease | -0.102 | 0.0504 | 0.0441 | Wald ratio | 1 | cis | NA |
| Mean cell haemoglobin | -0.0323 | 0.0162 | 0.0464 | Wald ratio | 1 | cis | NA |
| Low grade serous ovarian cancer | 0.136 | 0.0699 | 0.0515 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: depression | 0.0268 | 0.0142 | 0.0592 | Wald ratio | 1 | cis | NA |
| _...and 91 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_75 association rows across 46 traits (73 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| LTBR/SIRPB1 protein level ratio | 2e-2930 | rs76958425 | 1 | GCST90315339 | no MR -> candidate analysis |
| OSCAR/SIRPB1 protein level ratio | 6e-2733 | rs76958425 | 1 | GCST90315587 | no MR -> candidate analysis |
| Circulating SIRPB1 levels | 3e-2444 | rs75649571 | 4 | GCST90860614 | no MR -> candidate analysis |
| CD58/SIRPB1 protein level ratio | 2e-2380 | rs76958425 | 1 | GCST90313855 | no MR -> candidate analysis |
| Signal-regulatory protein beta-1 levels | 1e-1037 | rs12480515 | 4 | GCST90249559 | no MR -> candidate analysis |
| Circulating SIRPA levels | 6e-299 | rs2253427 | 1 | GCST90859973 | no MR -> candidate analysis |
| Serum levels of protein SIRPB1 | 2e-273 | rs16995228 | 3 | GCST90089319 | no MR -> candidate analysis |
| Blood protein levels | 5e-226 | rs4814391 | 1 | GCST006585 | no MR -> candidate analysis |
| Cerebrospinal fluid protein SIRPB1 levels | 4e-223 | rs2318043 | 1 | GCST90944578 | no MR -> candidate analysis |
| Signal-regulatory protein beta-1 levels (SIRPB1.6247.9.3) | 1e-213 | rs3848788 | 5 | GCST90242820 | no MR -> candidate analysis |
| Mean platelet thrombocyte volume (UKB data field 30100) | 5e-191 | rs11696739 | 1 | GCST90468087 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 5e-174 | rs6074894 | 2 | GCST90838669 | no MR -> candidate analysis |
| _...and 34 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 309 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| alcohol drinking | 0.463 | — | common-variant locus | no MR -> candidate analysis |
| type 1 diabetes mellitus | 0.253 | — | common-variant locus | no MR -> candidate analysis |
| rheumatoid arthritis | 0.153 | — | common-variant locus | no MR -> candidate analysis |
| tooth disorder | 0.087 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.3e-08, LOEUF=1.12 — LoF-tolerant |
| GWAS Catalog | 93 unique SNPs / 186 rows |
| ClinVar | 126 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 309 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'SIRPB1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 126 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 46 traits by best p-value, aggregated from 75 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q5TFQ8 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000101307/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/SIRPB1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/SIRPB1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=SIRPB1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/SIRPB1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:07:13  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
