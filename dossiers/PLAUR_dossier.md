# Protein Dossier — PLAUR (Urokinase plasminogen activator surface receptor)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: diverticular disease or diverticulitis | 0.298 | 0.103 | 0.00398 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K60 Fissure and fistula of anal and rectal regions | 0.392 | 0.149 | 0.00863 | Wald ratio | 1 | cis | NA |
| Height | -0.05 | 0.0195 | 0.0105 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | 0.0363 | 0.0145 | 0.0126 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | -0.0294 | 0.0119 | 0.0138 | Wald ratio | 1 | cis | NA |
| Hippocampus volume | -72 | 29.8 | 0.0157 | Wald ratio | 1 | cis | NA |
| Thalamus volume | -95.6 | 39.6 | 0.0158 | Wald ratio | 1 | cis | NA |
| Alzheimer's disease | -0.217 | 0.0995 | 0.0294 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K40 Inguinal hernia | 0.156 | 0.0766 | 0.0417 | Wald ratio | 1 | cis | NA |
| Rheumatoid arthritis | -0.186 | 0.0967 | 0.055 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hyperthyroidism or thyrotoxicosis | 0.247 | 0.135 | 0.0667 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | 0.0431 | 0.0238 | 0.0696 | Wald ratio | 1 | cis | NA |
| _...and 70 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2652_15_1` | suPAR | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_246 association rows across 155 traits (238 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating TNFRSF10C levels | 3e-5702 | rs4760 | 1 | GCST90859942 | no MR -> candidate analysis |
| ENG/TNFRSF10C protein level ratio | 1e-4708 | rs4760 | 1 | GCST90314650 | no MR -> candidate analysis |
| Circulating TNFSF10 levels (id: OID00488_OID20611) | 3e-842 | rs4760 | 1 | GCST90859847 | no MR -> candidate analysis |
| ENG/TNFSF10 protein level ratio | 2e-827 | rs4760 | 1 | GCST90314651 | no MR -> candidate analysis |
| Circulating TNFSF10 levels (id: OID00672_OID20611) | 2e-702 | rs4760 | 1 | GCST90860016 | no MR -> candidate analysis |
| Circulating TNFSF10 levels (id: OID00769_OID20611) | 2e-677 | rs4760 | 1 | GCST90860104 | no MR -> candidate analysis |
| Circulating PLAU levels (id: OID00631_OID21124) | 4e-346 | rs4251805 | 7 | GCST90859976 | no MR -> candidate analysis |
| Circulating FCGR3B levels | 3e-317 | rs4760 | 1 | GCST90860423 | no MR -> candidate analysis |
| Circulating BST1 levels | 8e-309 | rs4760 | 1 | GCST90860619 | no MR -> candidate analysis |
| Tumor necrosis factor receptor superfamily member 10C levels | 1e-266 | rs4760 | 1 | GCST90179449 | no MR -> candidate analysis |
| Circulating PLAU levels (id: OID00481_OID21124) | 5e-247 | rs4251805 | 7 | GCST90859841 | no MR -> candidate analysis |
| PLAU protein levels | 8e-200 | rs36229204 | 5 | GCST90470252 | no MR -> candidate analysis |
| _...and 143 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1776 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| abdominal aortic aneurysm | 0.792 | — | common-variant locus | no MR -> candidate analysis |
| Decreased total leukocyte count | 0.727 | — | common-variant locus | no MR -> candidate analysis |
| myocardial infarction | 0.585 | — | common-variant locus | no MR -> candidate analysis |
| aortic aneurysm | 0.582 | — | common-variant locus | no MR -> candidate analysis |
| angina pectoris | 0.573 | — | common-variant locus | no MR -> candidate analysis |
| coronary artery disorder | 0.547 | — | common-variant locus | no MR -> candidate analysis |
| breast carcinoma | 0.334 | — | common-variant locus | no MR -> candidate analysis |
| luminal A breast carcinoma | 0.202 | — | common-variant locus | no MR -> candidate analysis |
| breast cancer | 0.117 | — | common-variant locus | MR: beta=0.0782, p=0.291 (cis) |

> Of the 9 rows above, **8 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Urokinase plasminogen activator surface receptor) |
| gnomAD constraint | pLI=1.6e-05, LOEUF=0.941 — LoF-tolerant |
| GWAS Catalog | 108 unique SNPs / 250 rows |
| ClinVar | 84 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1776 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'PLAUR' and resolved to 'Urokinase plasminogen activator surface receptor' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 84 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 155 traits by best p-value, aggregated from 246 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q03405 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000011422/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4883/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PLAUR — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PLAUR — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PLAUR%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PLAUR — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:26:08  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
