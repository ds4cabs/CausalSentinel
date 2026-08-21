# Protein Dossier — MAP2K2 (Dual specificity mitogen-activated protein kinase kinase 2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diastolic blood pressure  automated reading | -0.0168 | 0.00521 | 0.00131 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: asthma | 0.0406 | 0.0137 | 0.00299 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: depression | 0.0545 | 0.0199 | 0.00611 | Wald ratio | 1 | trans | NA |
| Sleep duration | 0.0108 | 0.00397 | 0.00665 | Wald ratio | 1 | trans | NA |
| Hearing difficulty or problems: Yes | 0.0221 | 0.0086 | 0.0102 | Wald ratio | 1 | trans | NA |
| Fasting insulin | 0.0168 | 0.00656 | 0.0103 | Wald ratio | 1 | trans | NA |
| Ischemic stroke | 0.0771 | 0.0348 | 0.0269 | Wald ratio | 1 | trans | NA |
| Height | -0.0135 | 0.00622 | 0.0306 | Wald ratio | 1 | trans | NA |
| Triglycerides | 0.021 | 0.00976 | 0.0311 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: iron deficiency anaemia | 0.132 | 0.0614 | 0.0313 | Wald ratio | 1 | trans | NA |
| Endometrioid ovarian cancer | 0.129 | 0.0604 | 0.0328 | Wald ratio | 1 | trans | NA |
| Lung cancer | 0.0742 | 0.0349 | 0.0333 | Wald ratio | 1 | trans | NA |
| _...and 112 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3628_3_4` | MP2K2 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_89 association rows across 65 traits (82 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Hematological traits (multi-trait analysis) | 2e-131 | rs350834 | 1 | GCST90838669 | no MR -> candidate analysis |
| Mean corpuscular volume (UKB data field 30040) | 2e-92 | rs56267960 | 2 | GCST90468086 | no MR -> candidate analysis |
| Height | 8e-74 | rs350897 | 7 | GCST90245848 | MR: beta=-0.0135, p=0.0306 (trans) |
| Red blood cell erythrocyte count (UKB data field 30010) | 9e-56 | rs56267960 | 1 | GCST90468098 | no MR -> candidate analysis |
| red blood cell count (RBC, maximum, inv-norm transformed) | 8e-53 | rs56267960 | 2 | GCST90480668 | no MR -> candidate analysis |
| Red blood cell count | 6e-52 | rs56267960 | 2 | GCST90662905 | MR: beta=0.00471, p=0.282 (trans) |
| red blood cell count (RBC, mean, inv-norm transformed) | 1e-49 | rs56267960 | 2 | GCST90480669 | no MR -> candidate analysis |
| red blood cell count (RBC, minimum, inv-norm transformed) | 1e-35 | rs56267960 | 1 | GCST90480670 | no MR -> candidate analysis |
| mean corpuscular volume (MCV, mean, inv-norm transformed) | 6e-27 | rs56267960 | 1 | GCST90475469 | no MR -> candidate analysis |
| mean corpuscular hemoglobin (MCH, mean, inv-norm transformed | 8e-27 | rs56267960 | 1 | GCST90475445 | no MR -> candidate analysis |
| mean corpuscular hemoglobin (MCH, minimum, inv-norm transfor | 3e-26 | rs56267960 | 1 | GCST90475449 | no MR -> candidate analysis |
| Standing height (UKB data field 50) | 7e-25 | rs72978905 | 1 | GCST90468178 | no MR -> candidate analysis |
| _...and 53 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 501 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| cardiofaciocutaneous syndrome | 0.89 | — | established (curated) | no MR -> candidate analysis |
| Noonan syndrome | 0.761 | — | established (curated) | no MR -> candidate analysis |
| RASopathy | 0.936 | — | established (curated) | no MR -> candidate analysis |
| hypertrophic cardiomyopathy | 0.012 | — | established (curated) | no MR -> candidate analysis |
| cardiofaciocutaneous syndrome 1 | 0.438 | — | established (curated) | no MR -> candidate analysis |
| Abnormality of the cardiovascular system | 0.683 | — | established (curated) | no MR -> candidate analysis |
| neurofibromatosis-Noonan syndrome | 0.486 | — | established (curated) | no MR -> candidate analysis |

> Of the 7 rows above, **7 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 16 known modulators (Dual specificity mitogen-activated protein kinase kinase 2) |
| gnomAD constraint | pLI=0.00025, LOEUF=0.773 — LoF-tolerant |
| GWAS Catalog | 106 unique SNPs / 226 rows |
| ClinVar | 1072 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 501 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'MAP2K2' and resolved to 'Dual specificity mitogen-activated protein kinase kinase 2' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 1072 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 65 traits by best p-value, aggregated from 89 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P36507 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000126934/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2964/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/MAP2K2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/MAP2K2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=MAP2K2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/MAP2K2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:43:25  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
