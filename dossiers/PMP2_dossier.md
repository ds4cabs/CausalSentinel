# Protein Dossier — PMP2 (Myelin P2 protein)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: K60 Fissure and fistula of anal and rectal regions | 0.503 | 0.157 | 0.00134 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: joint disorder | 0.436 | 0.166 | 0.00862 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: hypertension | -0.0743 | 0.0312 | 0.0173 | Wald ratio | 1 | trans | NA |
| Lumbar spine bone mineral density | -0.135 | 0.0605 | 0.0255 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: hiatus hernia | -0.35 | 0.163 | 0.0324 | Wald ratio | 1 | trans | NA |
| Thalamus volume | 92.1 | 43.4 | 0.0338 | Wald ratio | 1 | trans | NA |
| Sodium in urine | 0.0336 | 0.0167 | 0.0446 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: I48 Atrial fibrillation and flutter | 0.25 | 0.128 | 0.05 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: asthma | 0.0843 | 0.0438 | 0.0544 | Wald ratio | 1 | trans | NA |
| Eye problems or disorders: Glaucoma | 0.223 | 0.116 | 0.0546 | Wald ratio | 1 | trans | NA |
| Cancer code  self-reported: malignant melanoma | 0.279 | 0.15 | 0.0625 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: I83 Varicose veins of lower extremities | -0.293 | 0.164 | 0.0746 | Wald ratio | 1 | trans | NA |
| _...and 70 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_12 association rows across 11 traits (3 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating FABP9 levels | 6e-11 | rs569513636 | 1 | GCST90860324 | no MR -> candidate analysis |
| Cerebrospinal fluid protein FABP5 levels | 6e-10 | rs16908973 | 1 | GCST90944294 | no MR -> candidate analysis |
| Lymphocytic thyroiditis | 4e-8 | rs144209445 | 1 | GCST90627755 | no MR -> candidate analysis |
| Cutaneous mastocytosis (childhood) | 6e-8 | rs1909936 | 1 | GCST011379 | no MR -> candidate analysis |
| Memory performance | 3e-6 | rs13252768 | 2 | GCST90448843 | no MR -> candidate analysis |
| Memory performance (excluding comorbidities) | 5e-6 | rs13252768 | 1 | GCST90448856 | no MR -> candidate analysis |
| Overall survival in serous epithelial ovarian cancer treated | 6e-6 | rs202280 | 1 | GCST004896 | no MR -> candidate analysis |
| Type 2 diabetes | 6e-6 | rs182719694 | 1 | GCST004774 | no MR -> candidate analysis |
| Night sleep phenotypes | 7e-6 | rs71519017 | 1 | GCST003542 | no MR -> candidate analysis |
| Stuttering | 9e-6 | rs146347922 | 1 | GCST90707227 | no MR -> candidate analysis |
| Baseline memory | 9e-6 | rs13252768 | 1 | GCST90448433 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 91 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Charcot-Marie-Tooth disease type 1G | 0.846 | — | established (curated) | no MR -> candidate analysis |
| peripheral neuropathy | 0.547 | — | established (curated) | no MR -> candidate analysis |
| hereditary disease | 0.551 | — | established (curated) | no MR -> candidate analysis |
| Charcot-Marie-Tooth disease type 1E | 0.195 | — | established (curated) | no MR -> candidate analysis |
| Hashimoto thyroiditis | 0.138 | — | common-variant locus | no MR -> candidate analysis |

> Of the 5 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Myelin P2 protein) |
| gnomAD constraint | pLI=0.0018, LOEUF=1.14 — LoF-tolerant |
| GWAS Catalog | 31 unique SNPs / 55 rows |
| ClinVar | 183 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 91 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'PMP2' and resolved to 'Myelin P2 protein' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 183 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 11 of 11 traits by best p-value, aggregated from 12 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P02689 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000147588/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3826864/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PMP2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PMP2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PMP2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PMP2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:28:31  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
