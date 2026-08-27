# Protein Dossier — FMOD (Fibromodulin)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: I30 Acute pericarditis | 1.11 | 0.313 | 4.09e-04 | Wald ratio | 1 | cis | NA |
| Lumbar spine bone mineral density | 0.175 | 0.0522 | 7.87e-04 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | -0.0475 | 0.0148 | 0.00137 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M72 Fibroblastic disorders | 0.372 | 0.143 | 0.00907 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N92 Excessive  frequent and irregular menstruation | 0.214 | 0.0841 | 0.0108 | Wald ratio | 1 | cis | NA |
| Weight | -0.0317 | 0.0131 | 0.0155 | Wald ratio | 1 | cis | NA |
| Creatinine (enzymatic) in urine | -0.0343 | 0.0142 | 0.0156 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: gout | 0.226 | 0.1 | 0.0245 | Wald ratio | 1 | cis | NA |
| Pulse rate | -0.0553 | 0.0262 | 0.0351 | Wald ratio | 1 | cis | NA |
| Systolic blood pressure  automated reading | 0.0311 | 0.0152 | 0.041 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | -0.0391 | 0.0192 | 0.0418 | Wald ratio | 1 | cis | NA |
| Depressive symptoms | -0.04 | 0.02 | 0.0455 | Wald ratio | 1 | cis | NA |
| _...and 70 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_32 association rows across 19 traits (27 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| CHIT1 protein levels | 6e-101 | rs11581135 | 8 | GCST90468744 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 1e-64 | rs12060494 | 1 | GCST90838669 | no MR -> candidate analysis |
| Height | 6e-35 | rs1891174 | 3 | GCST90245848 | no MR -> candidate analysis |
| fibromodulin levels | 6e-33 | rs12077300 | 2 | GCST90426652 | no MR -> candidate analysis |
| PRELP protein levels | 3e-29 | rs142901388 | 3 | GCST90470321 | no MR -> candidate analysis |
| CHI3L1 protein levels | 6e-20 | rs10920621 | 2 | GCST90468743 | no MR -> candidate analysis |
| OPTC protein levels | 3e-18 | rs7410962 | 1 | GCST90470128 | no MR -> candidate analysis |
| Serum levels of protein FMOD | 4e-13 | rs4971252 | 1 | GCST90089371 | no MR -> candidate analysis |
| fibromodulin level in Chronic kidney disease with hypertensi | 1e-12 | rs6661575 | 1 | GCST90238227 | no MR -> candidate analysis |
| Body mass index | 2e-9 | rs16851349 | 1 | GCST90662887 | MR: beta=-0.0475, p=0.00137 (cis) |
| Osteoarthritis (hip) | 9e-9 | rs1977810 | 1 | GCST90566798 | no MR -> candidate analysis |
| Blood protein levels | 3e-8 | rs4971253 | 1 | GCST006585 | no MR -> candidate analysis |
| _...and 7 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1022 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Abnormality of the skeletal system | 0.575 | — | common-variant locus | no MR -> candidate analysis |
| temporomandibular joint disorder | 0.432 | — | common-variant locus | no MR -> candidate analysis |
| osteoarthritis, hip | 0.433 | — | common-variant locus | no MR -> candidate analysis |
| benign neoplasm of pituitary gland | 0.287 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.0038, LOEUF=0.854 — LoF-tolerant |
| GWAS Catalog | 64 unique SNPs / 128 rows |
| ClinVar | 87 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1022 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'FMOD'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 87 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 19 of 19 traits by best p-value, aggregated from 32 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q06828 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000122176/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/FMOD — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/FMOD — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=FMOD%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/FMOD — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:42:07  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
