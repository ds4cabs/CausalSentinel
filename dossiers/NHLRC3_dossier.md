# Protein Dossier — NHLRC3 (NHL repeat-containing protein 3)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Body mass index (BMI) | 0.0193 | 0.00742 | 0.00934 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: R04 Haemorrhage from respiratory passages | 0.208 | 0.0844 | 0.0136 | Wald ratio | 1 | trans | NA |
| Lung cancer | -0.128 | 0.0528 | 0.0152 | Wald ratio | 1 | trans | NA |
| Underlying (primary) cause of death: ICD10: E85.4 Organ-limited amyloidosis | 1.36 | 0.606 | 0.0248 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: J33 Nasal polyp | 0.192 | 0.0898 | 0.0321 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: K20 Oesophagitis | 0.139 | 0.0655 | 0.0332 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: bone disorder | 0.258 | 0.125 | 0.0386 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: kidney stone or ureter stone or bladder stone | 0.149 | 0.0726 | 0.0396 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: M17 Gonarthrosis [arthrosis of knee] | 0.0969 | 0.0486 | 0.0464 | Wald ratio | 1 | trans | NA |
| Weight | 0.0129 | 0.00655 | 0.0493 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: joint disorder | -0.292 | 0.149 | 0.0501 | Wald ratio | 1 | trans | NA |
| Fractured bone site(s): Wrist | -0.113 | 0.0595 | 0.0576 | Wald ratio | 1 | trans | NA |
| _...and 68 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_7 association rows across 5 traits (5 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| NHLRC3 protein levels | 5e-231 | rs41286947 | 3 | GCST90470046 | no MR -> candidate analysis |
| Cerebrospinal fluid protein NHLRC3 levels | 6e-17 | rs149175958 | 1 | GCST90944457 | no MR -> candidate analysis |
| Height | 7e-12 | rs9576717 | 1 | GCST90435412 | no MR -> candidate analysis |
| Fibroblast growth factor basic levels | 2e-6 | rs183751764 | 1 | GCST004459 | no MR -> candidate analysis |
| Alzheimer's disease (late onset) | 4e-6 | rs190094306 | 1 | GCST007511 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 65 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| musculoskeletal system disorder | 0.45 | — | common-variant locus | no MR -> candidate analysis |
| adolescent idiopathic scoliosis | 0.388 | — | common-variant locus | no MR -> candidate analysis |
| tooth disorder | 0.31 | — | common-variant locus | no MR -> candidate analysis |
| polycystic ovary syndrome | 0.31 | — | common-variant locus | no MR -> candidate analysis |
| gram-negative bacterial infections | 0.125 | — | common-variant locus | no MR -> candidate analysis |
| bile duct disorder | 0.121 | — | common-variant locus | no MR -> candidate analysis |
| preeclampsia | 0.119 | — | common-variant locus | no MR -> candidate analysis |
| muscle cramp | 0.119 | — | common-variant locus | no MR -> candidate analysis |
| Uterine leiomyoma | 0.091 | — | common-variant locus | no MR -> candidate analysis |
| uterine corpus leiomyoma | 0.079 | — | common-variant locus | no MR -> candidate analysis |
| Abnormal pupillary function | 0.061 | — | common-variant locus | no MR -> candidate analysis |
| atrioventricular block | 0.059 | — | common-variant locus | no MR -> candidate analysis |
| sialolithiasis | 0.054 | — | common-variant locus | no MR -> candidate analysis |
| insomnia | 0.054 | — | common-variant locus | no MR -> candidate analysis |
| Alkalosis | 0.043 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **15 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=2.4e-06, LOEUF=1.02 — LoF-tolerant |
| GWAS Catalog | 44 unique SNPs / 87 rows |
| ClinVar | 115 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 65 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'NHLRC3'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 115 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 5 of 5 traits by best p-value, aggregated from 7 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q5JS37 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000188811/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/NHLRC3 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/NHLRC3 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=NHLRC3%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/NHLRC3 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:58:31  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
