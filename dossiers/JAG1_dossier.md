# Protein Dossier — JAG1 (Protein jagged-1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Large vessel disease | -0.573 | 0.157 | 2.60e-04 | Wald ratio | 1 | trans | NA |
| Ulcerative colitis | -0.159 | 0.0594 | 0.00735 | Wald ratio | 1 | trans | NA |
| Fractured bone site(s): Arm | 0.234 | 0.0885 | 0.00825 | Wald ratio | 1 | trans | NA |
| Height | 0.0328 | 0.0136 | 0.0164 | Wald ratio | 1 | trans | NA |
| Heel bone mineral density (BMD) T-score  automated | -0.0335 | 0.0143 | 0.0189 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: B37 Candidiasis | 0.671 | 0.298 | 0.024 | Wald ratio | 1 | trans | NA |
| Cardioembolic stroke | 0.307 | 0.147 | 0.0369 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: K57 Diverticular disease of intestine | -0.197 | 0.0954 | 0.0391 | Wald ratio | 1 | trans | NA |
| Packed cell volume | -0.164 | 0.0801 | 0.0408 | Wald ratio | 1 | trans | NA |
| Alzheimer's disease | -0.142 | 0.071 | 0.0448 | Wald ratio | 1 | trans | NA |
| Parkinson's disease | -0.365 | 0.189 | 0.0532 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: muscle or soft tissue injuries | 0.203 | 0.108 | 0.06 | Wald ratio | 1 | trans | NA |
| _...and 107 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5092_51_3` | JAG1 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_125 association rows across 82 traits (120 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Estimated bone mineral density | 1e-89 | rs141094380 | 3 | GCST90726625 | no MR -> candidate analysis |
| Heel bone mineral density | 1e-87 | rs17457340 | 15 | GCST006433 | MR: beta=-0.0335, p=0.0189 (trans) |
| PSPN protein levels | 1e-34 | rs549768142 | 1 | GCST90470364 | no MR -> candidate analysis |
| CALCA protein levels | 5e-26 | rs3790163 | 1 | GCST90468528 | no MR -> candidate analysis |
| Brain morphology (MOSTest) | 4e-25 | rs6077868 | 2 | GCST90239729 | no MR -> candidate analysis |
| High light scatter reticulocyte count (UKB data field 30300) | 4e-25 | rs1997814 | 1 | GCST90468076 | no MR -> candidate analysis |
| Circulating CALCA levels | 4e-25 | rs3790163 | 1 | GCST90860308 | no MR -> candidate analysis |
| High light scatter reticulocyte percentage (UKB data field 3 | 3e-23 | rs1997814 | 1 | GCST90468077 | no MR -> candidate analysis |
| Immature reticulocyte fraction (UKB data field 30280) | 6e-21 | rs1997814 | 1 | GCST90468079 | no MR -> candidate analysis |
| Lumbar spine bone mineral density | 3e-19 | rs3790160 | 1 | GCST001482 | MR: beta=0.0342, p=0.393 (trans) |
| Subcortical volume (MOSTest) | 3e-19 | rs6133987 | 1 | GCST010702 | no MR -> candidate analysis |
| Diastolic blood pressure (UKB data field 4079) | 3e-19 | rs889509 | 1 | GCST90468163 | no MR -> candidate analysis |
| _...and 70 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1880 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Alagille syndrome due to a JAG1 point mutation | 0.945 | — | established (curated) | no MR -> candidate analysis |
| Alagille syndrome | 0.791 | — | established (curated) | no MR -> candidate analysis |
| Tetralogy of Fallot | 0.85 | — | established (curated) | no MR -> candidate analysis |
| Charcot-Marie-Tooth disease, axonal, Type 2HH | 0.867 | — | established (curated) | no MR -> candidate analysis |
| deafness, congenital heart defects, and posterior embryotoxon | 0.834 | — | established (curated) | no MR -> candidate analysis |
| Abnormality of the cardiovascular system | 0.875 | — | established (curated) | no MR -> candidate analysis |
| hypertensive disorder | 0.851 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.81 | — | common-variant locus | no MR -> candidate analysis |
| Increased blood pressure | 0.789 | — | common-variant locus | no MR -> candidate analysis |
| cataract | 0.754 | — | common-variant locus | MR: beta=0.137, p=0.217 (trans) |
| migraine disorder | 0.762 | — | common-variant locus | no MR -> candidate analysis |
| hereditary disease | 0.721 | — | established (curated) | no MR -> candidate analysis |
| essential hypertension | 0.696 | — | common-variant locus | no MR -> candidate analysis |
| keloid | 0.648 | — | common-variant locus | no MR -> candidate analysis |
| osteoporosis | 0.638 | — | common-variant locus | MR: beta=0.0665, p=0.425 (trans) |

> Of the 15 rows above, **13 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Protein jagged-1) |
| gnomAD constraint | pLI=1, LOEUF=0.219 — LoF-INTOLERANT |
| GWAS Catalog | 109 unique SNPs / 223 rows |
| ClinVar | 2760 records; 12 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1880 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'JAG1' and resolved to 'Protein jagged-1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 2760 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 82 traits by best p-value, aggregated from 125 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P78504 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000101384/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3217396/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/JAG1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/JAG1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=JAG1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/JAG1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:19:48  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
