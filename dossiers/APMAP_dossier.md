# Protein Dossier — APMAP (Adipocyte plasma membrane-associated protein)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Body mass index (BMI) | 0.04 | 0.0122 | 0.00109 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | -0.0444 | 0.0159 | 0.00517 | Wald ratio | 1 | cis | NA |
| Creatinine (enzymatic) in urine | 0.0327 | 0.0117 | 0.00526 | Wald ratio | 1 | cis | NA |
| Weight | 0.0288 | 0.0108 | 0.00782 | Wald ratio | 1 | cis | NA |
| ER-positive Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.105 | 0.0411 | 0.0105 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: kidney stone or ureter stone or bladder stone | 0.271 | 0.107 | 0.0115 | Wald ratio | 1 | cis | NA |
| Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0836 | 0.0344 | 0.015 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: G56 Mononeuropathies of upper limb | 0.177 | 0.0786 | 0.024 | Wald ratio | 1 | cis | NA |
| Serum cystatin C (eGFRcys) | -0.0206 | 0.00944 | 0.0294 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K29 Gastritis and duodenitis | -0.208 | 0.0988 | 0.0353 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: Z09 Follow-up examination after treatment for conditions other than malignant neoplasms | -0.277 | 0.134 | 0.0393 | Wald ratio | 1 | cis | NA |
| Sodium in urine | 0.0244 | 0.0121 | 0.0429 | Wald ratio | 1 | cis | NA |
| _...and 90 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_27 association rows across 21 traits (24 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Serum levels of protein CST7 | 3e-171 | rs113136783 | 2 | GCST90087734 | no MR -> candidate analysis |
| Cystatin-F levels | 6e-151 | rs185515630 | 3 | GCST90161700 | no MR -> candidate analysis |
| APMAP protein levels | 9e-128 | rs12242 | 2 | GCST90453381 | no MR -> candidate analysis |
| CST7 protein levels | 8e-107 | rs79304811 | 2 | GCST90468897 | no MR -> candidate analysis |
| Eosinophil side scatter | 5e-69 | rs6114984 | 1 | GCST90281230 | no MR -> candidate analysis |
| Cystatin-F levels (CST7.3302.58.1) | 9e-62 | rs185515630 | 1 | GCST90240832 | no MR -> candidate analysis |
| Acetate levels | 6e-41 | rs6138465 | 1 | GCST90092803 | no MR -> candidate analysis |
| Serum levels of protein APMAP | 3e-32 | rs12242 | 1 | GCST90086361 | no MR -> candidate analysis |
| Eosinophil forward scatter | 2e-31 | rs56312312 | 1 | GCST90281232 | no MR -> candidate analysis |
| APMAP protein level (protein group normalized intensity) | 7e-22 | rs6138438 | 1 | GCST90570806 | no MR -> candidate analysis |
| Smoking initiation | 4e-18 | rs6050215 | 2 | GCST90243968 | no MR -> candidate analysis |
| Adipocyte plasma membrane-associated protein levels (APMAP.1 | 3e-16 | rs8125909 | 1 | GCST90240199 | no MR -> candidate analysis |
| _...and 9 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 447 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| smoking initiation | 0.439 | — | common-variant locus | no MR -> candidate analysis |
| obesity disorder | 0.354 | — | common-variant locus | no MR -> candidate analysis |
| ovarian dysfunction | 0.08 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Adipocyte plasma membrane-associated protein) |
| gnomAD constraint | pLI=3.5e-09, LOEUF=1.01 — LoF-tolerant |
| GWAS Catalog | 87 unique SNPs / 174 rows |
| ClinVar | 116 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 447 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'APMAP' and resolved to 'Adipocyte plasma membrane-associated protein' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 116 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 21 traits by best p-value, aggregated from 27 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9HDC9 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000101474/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL6067357/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/APMAP — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/APMAP — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=APMAP%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/APMAP — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:06:28  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
