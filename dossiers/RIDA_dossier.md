# Protein Dossier — RIDA (2-iminobutanoate/2-iminopropanoate deaminase)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| PGC cross-disorder traits | -0.119 | 0.0387 | 0.00209 | Wald ratio | 1 | cis | NA |
| Systolic blood pressure  automated reading | -0.0205 | 0.00778 | 0.00838 | Wald ratio | 1 | cis | NA |
| Hearing difficulty or problems: Yes | 0.031 | 0.0127 | 0.0147 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K80 Cholelithiasis | 0.107 | 0.0477 | 0.0249 | Wald ratio | 1 | cis | NA |
| Ischemic stroke | 0.11 | 0.0508 | 0.0297 | Wald ratio | 1 | cis | NA |
| HOMA-B | 0.0221 | 0.0103 | 0.0321 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K43 Ventral hernia | 0.201 | 0.0942 | 0.033 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: J33 Nasal polyp | -0.34 | 0.16 | 0.0334 | Wald ratio | 1 | cis | NA |
| Birth length | 0.0614 | 0.0304 | 0.0434 | Wald ratio | 1 | cis | NA |
| Systemic lupus erythematosus | 0.289 | 0.147 | 0.0492 | Wald ratio | 1 | cis | NA |
| Internalizing problems | -0.134 | 0.0688 | 0.0508 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M23 Internal derangement of knee | 0.0911 | 0.0468 | 0.0516 | Wald ratio | 1 | cis | NA |
| _...and 94 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_9 association rows across 9 traits (7 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| PTP4A3 protein levels | 7e-216 | rs2242197 | 1 | GCST90470375 | no MR -> candidate analysis |
| Ribonuclease UK114 levels | 7e-134 | rs77539382 | 1 | GCST90249398 | no MR -> candidate analysis |
| Cerebrospinal fluid protein RIDA levels | 4e-45 | rs2242197 | 1 | GCST90944540 | no MR -> candidate analysis |
| Ribonuclease UK114 levels (HRSP12.14636.25.3) | 2e-39 | rs1462977 | 1 | GCST90242670 | no MR -> candidate analysis |
| RIDA protein levels | 2e-15 | rs116843736 | 1 | GCST90470469 | no MR -> candidate analysis |
| Serum levels of protein RIDA | 8e-14 | rs2242197 | 1 | GCST90087895 | no MR -> candidate analysis |
| Blood protein levels | 6e-10 | rs57392722 | 1 | GCST006585 | no MR -> candidate analysis |
| Obesity-related traits | 6e-7 | rs10107366 | 1 | GCST001762 | no MR -> candidate analysis |
| Prion diseases | 9e-6 | rs2071598 | 1 | GCST001366 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 59 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Hodgkins lymphoma | 0.127 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.069 | — | common-variant locus | no MR -> candidate analysis |
| pernicious anemia | 0.059 | — | common-variant locus | no MR -> candidate analysis |
| placental retention | 0.053 | — | common-variant locus | no MR -> candidate analysis |
| brain disorder | 0.041 | — | common-variant locus | no MR -> candidate analysis |

> Of the 5 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Putative reactive intermediate deaminase TdcF) |
| gnomAD constraint | pLI=2.1e-06, LOEUF=1.43 — LoF-tolerant |
| GWAS Catalog | 37 unique SNPs / 74 rows |
| ClinVar | 45 records; 19 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 59 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'RIDA' and resolved to 'Putative reactive intermediate deaminase TdcF' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 45 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 9 of 9 traits by best p-value, aggregated from 9 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P52758 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000132541/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3309027/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/RIDA — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/RIDA — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=RIDA%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/RIDA — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:49:30  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
