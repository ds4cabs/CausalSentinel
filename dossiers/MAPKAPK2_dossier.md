# Protein Dossier — MAPKAPK2 (MAP kinase-activated protein kinase 2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Ulcerative colitis | 0.23 | 0.0421 | 4.84e-08 | Wald ratio | 1 | cis | NA |
| Inflammatory bowel disease | 0.169 | 0.0336 | 4.63e-07 | Wald ratio | 1 | cis | NA |
| Childhood intelligence | -0.143 | 0.0423 | 7.53e-04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: mania or bipolar disorder or manic depression | 0.358 | 0.112 | 0.00138 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | 0.207 | 0.0784 | 0.0083 | Wald ratio | 1 | cis | NA |
| Crohn's disease | 0.0945 | 0.0407 | 0.0202 | Wald ratio | 1 | cis | NA |
| Chronic kidney disease | 0.113 | 0.0491 | 0.0208 | Wald ratio | 1 | cis | NA |
| Multiple sclerosis | -0.126 | 0.0548 | 0.0213 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R14 Flatulence and related conditions | 0.495 | 0.216 | 0.0217 | Wald ratio | 1 | cis | NA |
| High grade serous ovarian cancer | -0.113 | 0.0515 | 0.0283 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: L03 Cellulitis | 0.165 | 0.0765 | 0.031 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: diverticular disease or diverticulitis | 0.143 | 0.0663 | 0.031 | Wald ratio | 1 | cis | NA |
| _...and 107 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3820_68_2` | MAPK2 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_14 association rows across 10 traits (10 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| MAP kinase-activated protein kinase 2 levels | 8e-129 | rs10863805 | 2 | GCST90248478 | no MR -> candidate analysis |
| MAPKAPK2 protein levels | 6e-86 | rs11119390 | 1 | GCST90469858 | no MR -> candidate analysis |
| Height | 6e-40 | rs4311892 | 2 | GCST90245848 | no MR -> candidate analysis |
| Mouth ulcers | 1e-19 | rs3813961 | 1 | GCST007839 | no MR -> candidate analysis |
| IL19 protein levels | 8e-19 | rs782170878 | 1 | GCST90469568 | no MR -> candidate analysis |
| Mitogen-activated protein kinase 14 levels | 3e-18 | rs11119385 | 1 | GCST90248407 | no MR -> candidate analysis |
| Mean corpuscular hemoglobin | 2e-12 | rs45514798 | 2 | GCST90002390 | no MR -> candidate analysis |
| Crohn's disease | 3e-7 | rs61815628 | 2 | GCST90301327 | MR: beta=0.0945, p=0.0202 (cis) |
| Crohn's disease x sex interaction (2df) | 4e-7 | rs61815628 | 1 | GCST90301328 | no MR -> candidate analysis |
| Plasma PCSK9 levels | 9e-7 | rs17015194 | 1 | GCST90085917 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 400 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| migraine disorder | 0.553 | — | common-variant locus | no MR -> candidate analysis |
| glomerulonephritis | 0.459 | — | common-variant locus | no MR -> candidate analysis |
| sialolithiasis | 0.363 | — | common-variant locus | no MR -> candidate analysis |
| neurodevelopmental disorder | 0.195 | — | established (curated) | no MR -> candidate analysis |
| type 2 diabetes mellitus | 0.085 | — | common-variant locus | no MR -> candidate analysis |
| diabetes mellitus | 0.085 | — | common-variant locus | no MR -> candidate analysis |

> Of the 6 rows above, **6 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 1 known modulators (MAP kinase-activated protein kinase 2) |
| gnomAD constraint | pLI=1, LOEUF=0.322 — LoF-INTOLERANT |
| GWAS Catalog | 57 unique SNPs / 114 rows |
| ClinVar | 77 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 400 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'MAPKAPK2' and resolved to 'MAP kinase-activated protein kinase 2' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 77 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 10 of 10 traits by best p-value, aggregated from 14 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P49137 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000162889/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2208/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/MAPKAPK2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/MAPKAPK2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=MAPKAPK2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/MAPKAPK2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:44:12  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
