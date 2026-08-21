# Protein Dossier — PDCD5 (Programmed cell death protein 5)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Serum creatinine (eGFRcrea) | -0.00932 | 0.00282 | 9.67e-04 | Wald ratio | 1 | cis | NA |
| Mean cell haemoglobin | 0.109 | 0.0353 | 0.00196 | Wald ratio | 1 | cis | NA |
| Bipolar disorder | 0.23 | 0.0757 | 0.00236 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: diverticular disease or diverticulitis | 0.177 | 0.0594 | 0.00282 | Wald ratio | 1 | cis | NA |
| Mean cell haemoglobin concentration | 0.0316 | 0.0113 | 0.00511 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R07 Pain in throat and chest | 0.0816 | 0.0307 | 0.00791 | Wald ratio | 1 | cis | NA |
| Mean cell volume | 0.229 | 0.0887 | 0.0098 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: Z09 Follow-up examination after treatment for conditions other than malignant neoplasms | 0.134 | 0.0533 | 0.0121 | Wald ratio | 1 | cis | NA |
| Squamous cell lung cancer | -0.197 | 0.0802 | 0.0139 | Wald ratio | 1 | cis | NA |
| Fractured or broken bones in last 5 years | 0.054 | 0.0221 | 0.0145 | Wald ratio | 1 | cis | NA |
| LDL cholesterol | -0.0427 | 0.0175 | 0.0149 | Wald ratio | 1 | cis | NA |
| Mean platelet volume | -0.0096 | 0.00395 | 0.0152 | Wald ratio | 1 | cis | NA |
| _...and 97 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_108 association rows across 64 traits (99 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Programmed cell death protein 5 levels | 2e-178 | rs4499344 | 2 | GCST90248904 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 6e-108 | rs4499344 | 2 | GCST90838669 | no MR -> candidate analysis |
| Mean corpuscular hemoglobin | 1e-65 | rs4499344 | 7 | GCST007068 | no MR -> candidate analysis |
| Mean corpuscular haemoglobin (UKB data field 30050) | 2e-61 | rs4499344 | 1 | GCST90468084 | no MR -> candidate analysis |
| Mean corpuscular volume (UKB data field 30040) | 1e-60 | rs4499344 | 2 | GCST90468086 | no MR -> candidate analysis |
| METAP2/PLPBP protein level ratio | 5e-52 | rs2903752 | 1 | GCST90315432 | no MR -> candidate analysis |
| EIF4B/METAP2 protein level ratio | 6e-51 | rs2903752 | 1 | GCST90314624 | no MR -> candidate analysis |
| red cell diameter width (RDW, minimum, inv-norm transformed) | 2e-50 | rs10405535 | 2 | GCST90476365 | no MR -> candidate analysis |
| Red cell distribution width | 4e-46 | rs34943133 | 7 | GCST90002369 | no MR -> candidate analysis |
| Mean platelet thrombocyte volume (UKB data field 30100) | 2e-43 | rs4499344 | 1 | GCST90468087 | no MR -> candidate analysis |
| METAP2 protein levels | 2e-42 | rs10402931 | 1 | GCST90469894 | no MR -> candidate analysis |
| Mean reticulocyte volume (UKB data field 30260) | 6e-42 | rs4499344 | 1 | GCST90468088 | no MR -> candidate analysis |
| _...and 52 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 176 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| systemic lupus erythematosus | 0.416 | — | common-variant locus | no MR -> candidate analysis |
| sialolithiasis | 0.285 | — | common-variant locus | no MR -> candidate analysis |
| asthma | 0.074 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Programmed cell death protein 5) |
| gnomAD constraint | pLI=6.9e-09, LOEUF=1.49 — LoF-tolerant |
| GWAS Catalog | 73 unique SNPs / 146 rows |
| ClinVar | 43 records; 4 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 176 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'PDCD5' and resolved to 'Programmed cell death protein 5' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 43 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 64 traits by best p-value, aggregated from 108 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O14737 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000105185/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL6066424/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PDCD5 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PDCD5 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PDCD5%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PDCD5 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:14:28  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
