# Protein Dossier — NT5C (5'(3')-deoxyribonucleotidase, cytosolic type)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: K40 Inguinal hernia | 0.142 | 0.0491 | 0.0037 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: gastro-oesophageal reflux (gord)  or  gastric reflux | 0.109 | 0.04 | 0.00656 | Wald ratio | 1 | cis | NA |
| Schizophrenia | 0.118 | 0.0458 | 0.00989 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Ankle | -0.225 | 0.0999 | 0.0244 | Wald ratio | 1 | cis | NA |
| Depressive symptoms | -0.0345 | 0.0159 | 0.0303 | Wald ratio | 1 | cis | NA |
| Endometrioid ovarian cancer | 0.253 | 0.123 | 0.0392 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C50 Malignant neoplasm of breast | -0.162 | 0.0856 | 0.0591 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: malignant melanoma | 0.164 | 0.0898 | 0.0677 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: basal cell carcinoma | 0.146 | 0.084 | 0.0815 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M23 Internal derangement of knee | -0.121 | 0.0705 | 0.0863 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M17 Gonarthrosis [arthrosis of knee] | -0.126 | 0.076 | 0.0963 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K29 Gastritis and duodenitis | 0.0908 | 0.0548 | 0.0971 | Wald ratio | 1 | cis | NA |
| _...and 53 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_6 association rows across 6 traits (6 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Orotidine levels | 1e-351 | rs11541956 | 1 | GCST90103117 | no MR -> candidate analysis |
| 5'(3')-deoxyribonucleotidase, cytosolic type levels | 2e-127 | rs11541956 | 1 | GCST90421796 | no MR -> candidate analysis |
| Cerebrospinal fluid orotidine levels | 6e-30 | rs11541956 | 1 | GCST90317996 | no MR -> candidate analysis |
| Height | 3e-28 | rs12453556 | 1 | GCST90245848 | no MR -> candidate analysis |
| C-reactive protein levels | 5e-11 | rs4788867 | 1 | GCST009777 | no MR -> candidate analysis |
| Height (baseline) | 4e-8 | rs112659109 | 1 | GCST90565843 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 106 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| type 2 diabetes mellitus | 0.308 | — | common-variant locus | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (5'(3')-deoxyribonucleotidase, cytosolic type) |
| gnomAD constraint | pLI=0.0001, LOEUF=1.24 — LoF-tolerant |
| GWAS Catalog | 45 unique SNPs / 90 rows |
| ClinVar | 65 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 106 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'NT5C' and resolved to '5'(3')-deoxyribonucleotidase, cytosolic type' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 65 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 6 of 6 traits by best p-value, aggregated from 6 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q8TCD5 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000125458/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3751653/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/NT5C — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/NT5C — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=NT5C%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/NT5C — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:05:15  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
