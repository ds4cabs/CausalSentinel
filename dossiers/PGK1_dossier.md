# Protein Dossier — PGK1 (Phosphoglycerate kinase 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Fasting glucose | 0.0485 | 0.0193 | 0.0119 | Wald ratio | 1 | trans | NA |
| Underlying (primary) cause of death: ICD10: E85.4 Organ-limited amyloidosis | 1.59 | 0.671 | 0.0181 | Inverse variance weighted | 2 | trans | NA |
| Underlying (primary) cause of death: ICD10: E85.4 Organ-limited amyloidosis | 1.59 | 0.671 | 0.0181 | Inverse variance weighted | 2 | trans | NA |
| Large vessel disease | 0.483 | 0.213 | 0.0238 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: Z09 Follow-up examination after treatment for conditions other than malignant neoplasms | -0.216 | 0.0989 | 0.0289 | Inverse variance weighted | 2 | trans | NA |
| Diagnoses - main ICD10: Z09 Follow-up examination after treatment for conditions other than malignant neoplasms | -0.216 | 0.0989 | 0.0289 | Inverse variance weighted | 2 | trans | NA |
| Birth length | 0.126 | 0.0596 | 0.0348 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: N92 Excessive  frequent and irregular menstruation | -0.17 | 0.0805 | 0.0349 | Inverse variance weighted | 2 | trans | NA |
| Diagnoses - main ICD10: N92 Excessive  frequent and irregular menstruation | -0.17 | 0.0805 | 0.0349 | Inverse variance weighted | 2 | trans | NA |
| Ferritin | -0.121 | 0.0574 | 0.0352 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: K57 Diverticular disease of intestine | -0.17 | 0.0814 | 0.0367 | Inverse variance weighted | 2 | trans | NA |
| Diagnoses - main ICD10: K57 Diverticular disease of intestine | -0.17 | 0.0814 | 0.0367 | Inverse variance weighted | 2 | trans | NA |
| _...and 143 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5020_50_1` | phosphoglycerate kinase 1 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_4 association rows across 4 traits (4 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Height | 3e-30 | rs12837147 | 1 | GCST008839 | MR: beta=0.0336, p=0.0645 (trans) |
| Mean platelet volume | 3e-14 | rs5913634 | 1 | GCST90002395 | no MR -> candidate analysis |
| Weight | 1e-13 | rs151280158 | 1 | GCST90018729 | no MR -> candidate analysis |
| Red blood cell count | 1e-8 | rs16657 | 1 | GCST90018971 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 435 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| glycogen storage disease due to phosphoglycerate kinase 1 deficiency | 0.906 | — | established (curated) | no MR -> candidate analysis |
| Menkes disease | 0.946 | — | established (curated) | no MR -> candidate analysis |
| X-linked distal spinal muscular atrophy type 3 | 0.916 | — | established (curated) | no MR -> candidate analysis |
| occipital horn syndrome | 0.915 | — | established (curated) | no MR -> candidate analysis |
| hereditary disease | 0.838 | — | established (curated) | no MR -> candidate analysis |
| Obstructive azoospermia | 0.426 | — | established (curated) | no MR -> candidate analysis |
| Ehlers-Danlos syndrome | 0.304 | — | established (curated) | no MR -> candidate analysis |
| Intellectual disability | 0.245 | — | established (curated) | no MR -> candidate analysis |
| Charcot-Marie-Tooth disease | 0.228 | — | established (curated) | no MR -> candidate analysis |
| Epileptic encephalopathy | 0.195 | — | established (curated) | no MR -> candidate analysis |
| Au-Kline syndrome | 0.195 | — | established (curated) | no MR -> candidate analysis |
| Profound global developmental delay | 0.195 | — | established (curated) | no MR -> candidate analysis |
| Charcot-Marie-Tooth disease type 2 | 0.195 | — | established (curated) | no MR -> candidate analysis |
| optic atrophy | 0.182 | — | established (curated) | no MR -> candidate analysis |

> Of the 14 rows above, **14 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Phosphoglycerate kinase 1) |
| gnomAD constraint | pLI=1, LOEUF=0.288 — LoF-INTOLERANT |
| GWAS Catalog | 9 unique SNPs / 15 rows |
| ClinVar | 544 records; 3 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 435 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'PGK1' and resolved to 'Phosphoglycerate kinase 1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 544 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 4 of 4 traits by best p-value, aggregated from 4 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P00558 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000102144/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2886/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PGK1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PGK1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PGK1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PGK1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:18:48  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
