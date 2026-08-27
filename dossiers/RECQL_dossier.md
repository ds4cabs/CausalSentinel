# Protein Dossier — RECQL (ATP-dependent DNA helicase Q1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Weight | -0.0199 | 0.00551 | 2.94e-04 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | -0.0198 | 0.00624 | 0.00146 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: uterine fibroids | -0.155 | 0.0591 | 0.00868 | Wald ratio | 1 | cis | NA |
| Small vessel disease | 0.23 | 0.0916 | 0.0118 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C50 Malignant neoplasm of breast | -0.129 | 0.0557 | 0.0202 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | 0.0601 | 0.0261 | 0.0213 | Wald ratio | 1 | cis | NA |
| Total cholesterol | -0.031 | 0.0135 | 0.0214 | Wald ratio | 1 | cis | NA |
| Depressive symptoms | -0.0193 | 0.00856 | 0.0244 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I30 Acute pericarditis | 0.508 | 0.228 | 0.0255 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Cataract | 0.0672 | 0.032 | 0.0354 | Wald ratio | 1 | cis | NA |
| Cough on most days | 0.0608 | 0.03 | 0.0426 | Wald ratio | 1 | cis | NA |
| Amygdala volume | 12.2 | 6.13 | 0.047 | Wald ratio | 1 | cis | NA |
| _...and 94 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_2 association rows across 2 traits (2 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Direct bilirubin levels | 2e-13 | rs73071387 | 1 | GCST90019505 | no MR -> candidate analysis |
| Total bilirubin levels | 3e-12 | rs73071387 | 1 | GCST90019521 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 170 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| RECON progeroid syndrome | 0.664 | — | established (curated) | no MR -> candidate analysis |
| Inherited cancer-predisposing syndrome | 0.83 | — | established (curated) | no MR -> candidate analysis |
| hereditary neoplastic syndrome | 0.83 | — | established (curated) | no MR -> candidate analysis |
| obesity disorder | 0.662 | — | common-variant locus | no MR -> candidate analysis |
| Hereditary breast and ovarian cancer syndrome | 0.538 | — | established (curated) | no MR -> candidate analysis |
| hereditary breast ovarian cancer syndrome | 0.538 | — | established (curated) | no MR -> candidate analysis |
| cancer | 0.438 | — | established (curated) | MR: beta=-0.155, p=0.00868 (cis) |
| overnutrition | 0.449 | — | common-variant locus | no MR -> candidate analysis |
| non-neoplastic bile duct disorder | 0.411 | — | common-variant locus | no MR -> candidate analysis |
| familial ovarian cancer | 0.245 | — | established (curated) | no MR -> candidate analysis |
| Abnormal facial shape | 0.195 | — | established (curated) | no MR -> candidate analysis |
| Short stature | 0.195 | — | established (curated) | no MR -> candidate analysis |
| hepatoblastoma | 0.182 | — | established (curated) | no MR -> candidate analysis |
| myopathy | 0.095 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.048 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **14 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (ATP-dependent DNA helicase Q1) |
| gnomAD constraint | pLI=2.5e-24, LOEUF=1.17 — LoF-tolerant |
| GWAS Catalog | 52 unique SNPs / 104 rows |
| ClinVar | 1930 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 170 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'RECQL' and resolved to 'ATP-dependent DNA helicase Q1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 1930 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 2 of 2 traits by best p-value, aggregated from 2 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P46063 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000004700/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL1293236/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/RECQL — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/RECQL — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=RECQL%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/RECQL — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:46:40  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
