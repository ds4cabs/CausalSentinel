# Protein Dossier — FN1 (Fibronectin)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Systolic blood pressure  automated reading | -0.0265 | 0.00393 | 1.70e-11 | Wald ratio | 1 | cis | NA |
| LDL cholesterol | 0.0342 | 0.0059 | 7.22e-09 | Wald ratio | 1 | cis | NA |
| Total cholesterol | 0.0299 | 0.00576 | 2.05e-07 | Wald ratio | 1 | cis | NA |
| Coronary heart disease | -0.0461 | 0.0152 | 0.00246 | Wald ratio | 1 | cis | NA |
| Large vessel disease | -0.166 | 0.0558 | 0.00288 | Wald ratio | 1 | cis | NA |
| Height | -0.0141 | 0.00492 | 0.00427 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: S76 Injury of muscle and tendon at hip and thigh level | 0.359 | 0.13 | 0.00571 | Wald ratio | 1 | cis | NA |
| Myocardial infarction | -0.043 | 0.0162 | 0.00815 | Wald ratio | 1 | cis | NA |
| Squamous cell lung cancer | 0.104 | 0.0428 | 0.0152 | Wald ratio | 1 | cis | NA |
| Triglycerides | 0.0125 | 0.00534 | 0.0192 | Wald ratio | 1 | cis | NA |
| Vascular or heart problems diagnosed by doctor: Angina | -0.0528 | 0.0227 | 0.02 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: retinal detachment | 0.132 | 0.0589 | 0.025 | Wald ratio | 1 | cis | NA |
| _...and 104 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3434_34_1` | FN1.3 | Suhre K | 2019 |
| `prot-c-3435_53_2` | FN1.4 | Suhre K | 2019 |
| `prot-c-4131_72_2` | Fibronectin | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_170 association rows across 85 traits (153 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Serum levels of protein FN1 | 2e-153 | rs1250258 | 3 | GCST90088589 | no MR -> candidate analysis |
| Circulating ITGA5 levels | 1e-108 | rs139078629 | 4 | GCST90860638 | no MR -> candidate analysis |
| Height | 3e-107 | rs1250258 | 10 | GCST90245848 | MR: beta=-0.0141, p=0.00427 (cis) |
| ITGA5 protein levels | 1e-104 | rs139078629 | 5 | GCST90469635 | no MR -> candidate analysis |
| Serum levels of protein NPNT | 6e-94 | rs1250259 | 1 | GCST90089355 | no MR -> candidate analysis |
| Blood protein levels | 5e-89 | rs1250259 | 9 | GCST006585 | no MR -> candidate analysis |
| Fibronectin Fragment 3 levels | 1e-49 | rs1250258 | 3 | GCST90101019 | no MR -> candidate analysis |
| cFib plasma levels | 4e-47 | rs1132741 | 1 | GCST90085720 | no MR -> candidate analysis |
| Fibronectin levels | 5e-46 | rs1250258 | 2 | GCST90161975 | no MR -> candidate analysis |
| Fibronectin Fragment 4 levels | 2e-42 | rs1250258 | 3 | GCST90101020 | no MR -> candidate analysis |
| FN1 protein levels | 2e-40 | rs3845846 | 6 | GCST90469255 | no MR -> candidate analysis |
| Pulse pressure | 8e-35 | rs1250259 | 11 | GCST90310296 | no MR -> candidate analysis |
| _...and 73 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1798 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| spondylometaphyseal dysplasia, 'corner fracture' type | 0.88 | — | established (curated) | no MR -> candidate analysis |
| glomerulopathy with fibronectin deposits 2 | 0.882 | — | established (curated) | no MR -> candidate analysis |
| coronary artery disorder | 0.928 | — | common-variant locus | no MR -> candidate analysis |
| fibronectin glomerulopathy | 0.608 | — | established (curated) | no MR -> candidate analysis |
| coronary atherosclerosis | 0.781 | — | common-variant locus | no MR -> candidate analysis |
| myocardial infarction | 0.743 | — | common-variant locus | MR: beta=-0.043, p=0.00815 (cis) |
| Abnormality of the skeletal system | 0.758 | — | common-variant locus | no MR -> candidate analysis |
| myocardial ischemia | 0.744 | — | common-variant locus | no MR -> candidate analysis |
| hereditary disease | 0.684 | — | established (curated) | no MR -> candidate analysis |
| spondylometaphyseal dysplasia | 0.663 | — | established (curated) | no MR -> candidate analysis |
| occlusion precerebral artery | 0.599 | — | common-variant locus | no MR -> candidate analysis |
| angina pectoris | 0.595 | — | common-variant locus | no MR -> candidate analysis |
| coronary artery bypass | 0.521 | — | common-variant locus | no MR -> candidate analysis |
| benign prostatic hyperplasia | 0.484 | — | common-variant locus | no MR -> candidate analysis |
| neurodevelopmental disorder | 0.438 | — | established (curated) | no MR -> candidate analysis |

> Of the 15 rows above, **14 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 2 known modulators (Coagulation factor XII) |
| gnomAD constraint | pLI=1, LOEUF=0.419 — LoF-INTOLERANT |
| GWAS Catalog | 66 unique SNPs / 132 rows |
| ClinVar | 2067 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1798 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'FN1' and resolved to 'Coagulation factor XII' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 2067 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 85 traits by best p-value, aggregated from 170 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P02751 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000115414/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2821/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/FN1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/FN1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=FN1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/FN1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:42:22  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
