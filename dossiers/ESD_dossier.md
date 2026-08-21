# Protein Dossier — ESD (S-formylglutathione hydrolase)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: K43 Ventral hernia | -0.233 | 0.0978 | 0.0174 | Wald ratio | 1 | cis | NA |
| Intracranial volume | 9.04e+03 | 3.9e+03 | 0.0203 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | -0.0152 | 0.00663 | 0.0219 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: S66 Injury of muscle and tendon at wrist and hand level | -0.473 | 0.217 | 0.0296 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | -0.15 | 0.0711 | 0.0348 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R14 Flatulence and related conditions | 0.326 | 0.158 | 0.0393 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: depression | -0.0448 | 0.022 | 0.0421 | Wald ratio | 1 | cis | NA |
| Squamous cell lung cancer | 0.105 | 0.0526 | 0.0454 | Wald ratio | 1 | cis | NA |
| Ischemic stroke | 0.0697 | 0.0351 | 0.047 | Wald ratio | 1 | cis | NA |
| Fractured or broken bones in last 5 years | -0.0317 | 0.0165 | 0.0543 | Wald ratio | 1 | cis | NA |
| Lumbar spine bone mineral density | 0.0344 | 0.0181 | 0.057 | Wald ratio | 1 | cis | NA |
| Clear cell ovarian cancer | -0.157 | 0.0831 | 0.0595 | Wald ratio | 1 | cis | NA |
| _...and 70 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4984_83_1` | Esterase D | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_12 association rows across 6 traits (11 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| S-formylglutathione hydrolase levels | 7e-182 | rs73193056 | 6 | GCST90426175 | no MR -> candidate analysis |
| S-formylglutathione hydrolase levels (ESD.4984.83.1) | 1e-88 | rs8192888 | 2 | GCST90242707 | no MR -> candidate analysis |
| Protein quantitative trait loci | 4e-16 | rs2794658 | 1 | GCST010900 | no MR -> candidate analysis |
| Cerebrospinal fluid biomarker levels | 2e-15 | rs947409 | 1 | GCST004000 | no MR -> candidate analysis |
| Serum levels of protein ESD | 6e-12 | rs1216987 | 1 | GCST90088844 | no MR -> candidate analysis |
| Blood protein levels | 1e-7 | rs1216987 | 1 | GCST006585 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 113 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| rheumatic disorder | 0.492 | — | common-variant locus | no MR -> candidate analysis |
| kidney disorder | 0.331 | — | common-variant locus | no MR -> candidate analysis |
| placental retention | 0.331 | — | common-variant locus | no MR -> candidate analysis |
| placental abruption | 0.26 | — | common-variant locus | no MR -> candidate analysis |
| ovarian dysfunction | 0.246 | — | common-variant locus | no MR -> candidate analysis |
| diabetic ketoacidosis | 0.104 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.083 | — | common-variant locus | no MR -> candidate analysis |
| stroke disorder | 0.09 | — | common-variant locus | no MR -> candidate analysis |
| adolescent idiopathic scoliosis | 0.082 | — | common-variant locus | no MR -> candidate analysis |
| thrombophilia | 0.079 | — | common-variant locus | no MR -> candidate analysis |
| Subdural hemorrhage | 0.068 | — | common-variant locus | no MR -> candidate analysis |
| atrial fibrillation | 0.066 | — | common-variant locus | no MR -> candidate analysis |
| color vision disorder | 0.066 | — | common-variant locus | no MR -> candidate analysis |
| response to stimulus | 0.061 | — | common-variant locus | no MR -> candidate analysis |
| osteonecrosis | 0.061 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **15 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (S-formylglutathione hydrolase) |
| gnomAD constraint | pLI=4.8e-11, LOEUF=1.19 — LoF-tolerant |
| GWAS Catalog | 84 unique SNPs / 118 rows |
| ClinVar | 102 records; 4 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 113 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'ESD' and resolved to 'S-formylglutathione hydrolase' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 102 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 6 of 6 traits by best p-value, aggregated from 12 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P10768 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000139684/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2189130/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/ESD — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/ESD — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=ESD%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/ESD — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:29:29  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
