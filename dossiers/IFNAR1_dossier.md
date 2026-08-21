# Protein Dossier — IFNAR1 (Interferon alpha/beta receptor 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Cancer code  self-reported: basal cell carcinoma | 0.311 | 0.0957 | 0.00114 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: small intestine or small bowel cancer | 0.827 | 0.281 | 0.00323 | Wald ratio | 1 | cis | NA |
| Age at menopause | -0.276 | 0.104 | 0.00766 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: enlarged prostate | -0.42 | 0.167 | 0.0118 | Wald ratio | 1 | cis | NA |
| Fasting insulin | 0.0414 | 0.0166 | 0.0124 | Wald ratio | 1 | cis | NA |
| ER-negative Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.13 | 0.0604 | 0.0317 | Wald ratio | 1 | cis | NA |
| HbA1C | -0.0373 | 0.0176 | 0.0342 | Wald ratio | 1 | cis | NA |
| Birth weight | -0.0376 | 0.0183 | 0.0397 | Wald ratio | 1 | cis | NA |
| Age at menarche | 0.0656 | 0.0319 | 0.04 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | -0.0206 | 0.0102 | 0.0428 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R07 Pain in throat and chest | 0.0981 | 0.0502 | 0.0506 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: psoriasis | -0.318 | 0.166 | 0.0551 | Wald ratio | 1 | cis | NA |
| _...and 72 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_50 association rows across 23 traits (41 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Interferon alpha/beta receptor 1 levels | 3e-328 | rs2257167 | 5 | GCST90247991 | no MR -> candidate analysis |
| Cerebrospinal fluid protein IFNAR1 levels | 6e-281 | rs2211687 | 1 | GCST90943495 | no MR -> candidate analysis |
| Interferon alpha/beta receptor 1 (analyte X9183.7) levels | 9e-260 | rs2211687 | 1 | GCST90427684 | no MR -> candidate analysis |
| IL10RB protein levels | 1e-85 | rs10470090 | 10 | GCST90469545 | no MR -> candidate analysis |
| IFNAR1 protein levels | 9e-85 | rs62654645 | 8 | GCST90469512 | no MR -> candidate analysis |
| Interferon alpha/beta receptor 1 level in Chronic kidney dis | 5e-58 | rs2257167 | 1 | GCST90239231 | no MR -> candidate analysis |
| Serum levels of protein IFNAR1 | 1e-53 | rs2257167 | 2 | GCST90090540 | no MR -> candidate analysis |
| Blood protein levels | 3e-32 | rs2257167 | 1 | GCST006585 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 2e-31 | rs71314166 | 1 | GCST90838669 | no MR -> candidate analysis |
| Interferon alpha/beta receptor 1 levels (IFNAR1.9183.7.3) | 1e-15 | rs2257167 | 1 | GCST90241551 | no MR -> candidate analysis |
| Hypothyroidism | 4e-15 | rs969478 | 2 | GCST90627750 | no MR -> candidate analysis |
| Sperm acrosome-associated protein 5 protein levels (SomaScan | 5e-14 | rs62226371 | 1 | GCST90441594 | no MR -> candidate analysis |
| _...and 11 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 631 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| immunodeficiency 106, susceptibility to viral infections | 0.794 | — | established (curated) | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 1 known modulators (Interferon alpha/beta receptor 1) |
| gnomAD constraint | pLI=1.3e-12, LOEUF=0.966 — LoF-tolerant |
| GWAS Catalog | 103 unique SNPs / 219 rows |
| ClinVar | 439 records; 4 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 631 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'IFNAR1' and resolved to 'Interferon alpha/beta receptor 1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 439 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 23 traits by best p-value, aggregated from 50 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P17181 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000142166/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL1887/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/IFNAR1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/IFNAR1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=IFNAR1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/IFNAR1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:06:29  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
