# Protein Dossier — CRYZ (Zeta-crystallin)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: muscle or soft tissue injuries | 0.0989 | 0.0322 | 0.00211 | Wald ratio | 1 | cis | NA |
| Subjective well being | -0.0119 | 0.00426 | 0.00511 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: gout | 0.0624 | 0.0237 | 0.00838 | Wald ratio | 1 | cis | NA |
| Ischemic stroke | 0.0505 | 0.0195 | 0.00961 | Wald ratio | 1 | cis | NA |
| Body fat | 0.0165 | 0.00638 | 0.00969 | Wald ratio | 1 | cis | NA |
| Ferritin | 0.0285 | 0.0116 | 0.0138 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: S66 Injury of muscle and tendon at wrist and hand level | 0.158 | 0.0645 | 0.0142 | Wald ratio | 1 | cis | NA |
| Invasive mucinous ovarian cancer | 0.115 | 0.0475 | 0.0155 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Diabetes related eye disease | -0.0985 | 0.0425 | 0.0203 | Wald ratio | 1 | cis | NA |
| Lung adenocarcinoma | 0.088 | 0.0383 | 0.0214 | Wald ratio | 1 | cis | NA |
| Lung cancer | 0.0532 | 0.0235 | 0.0239 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: kidney stone or ureter stone or bladder stone | -0.0825 | 0.0369 | 0.0253 | Wald ratio | 1 | cis | NA |
| _...and 113 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_8 association rows across 6 traits (7 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Blood protein levels | 3e-292 | rs3819946 | 1 | GCST006585 | no MR -> candidate analysis |
| Estimated bone mineral density | 6e-10 | rs277402 | 1 | GCST90726625 | no MR -> candidate analysis |
| Protein quantitative trait loci (liver) | 1e-9 | rs61790703 | 2 | GCST011427 | no MR -> candidate analysis |
| Heel bone mineral density | 2e-9 | rs277402 | 1 | GCST006433 | no MR -> candidate analysis |
| Neurofibrillary tangles (SNP x SNP interaction) | 3e-9 | rs7512474 x rs12668317 | 2 | GCST010343 | no MR -> candidate analysis |
| Gut microbiota (bacterial taxa, hurdle binary method) | 8e-6 | rs150733404 | 1 | GCST010396 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 98 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| response to paracetamol | 0.444 | — | common-variant locus | no MR -> candidate analysis |
| ovarian neoplasm | 0.422 | — | common-variant locus | no MR -> candidate analysis |
| amyotrophic lateral sclerosis | 0.353 | — | common-variant locus | no MR -> candidate analysis |
| adolescent idiopathic scoliosis | 0.337 | — | common-variant locus | no MR -> candidate analysis |
| kidney cancer | 0.136 | — | common-variant locus | no MR -> candidate analysis |
| Wheezing | 0.09 | — | common-variant locus | no MR -> candidate analysis |
| jaw disease | 0.053 | — | common-variant locus | no MR -> candidate analysis |
| skin aging | 0.052 | — | common-variant locus | no MR -> candidate analysis |
| Cerebral degeneration | 0.033 | — | common-variant locus | no MR -> candidate analysis |
| health study participation | 0.031 | — | common-variant locus | no MR -> candidate analysis |

> Of the 10 rows above, **10 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Quinone oxidoreductase) |
| gnomAD constraint | pLI=8.3e-13, LOEUF=1.36 — LoF-tolerant |
| GWAS Catalog | 26 unique SNPs / 51 rows |
| ClinVar | 99 records; 3 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 98 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'CRYZ' and resolved to 'Quinone oxidoreductase' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 99 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 6 of 6 traits by best p-value, aggregated from 8 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q08257 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000116791/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL6118/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CRYZ — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CRYZ — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CRYZ%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CRYZ — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:05:16  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
