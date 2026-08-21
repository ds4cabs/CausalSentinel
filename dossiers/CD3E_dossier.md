# Protein Dossier — CD3E (T-cell surface glycoprotein CD3 epsilon chain)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: high cholesterol | 0.062 | 0.0239 | 0.00945 | Wald ratio | 1 | trans | NA |
| Clear cell ovarian cancer | 0.332 | 0.159 | 0.0376 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: hypopituitarism | 0.616 | 0.307 | 0.0452 | Wald ratio | 1 | trans | NA |
| Forced vital capacity (FVC) | -0.0152 | 0.00771 | 0.0487 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: J33 Nasal polyp | 0.216 | 0.112 | 0.0523 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: M17 Gonarthrosis [arthrosis of knee] | 0.116 | 0.0605 | 0.0542 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: H25 Senile cataract | -0.279 | 0.145 | 0.0546 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: kidney stone or ureter stone or bladder stone | 0.168 | 0.0906 | 0.0638 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: polio  or  poliomyelitis | 0.444 | 0.248 | 0.0732 | Wald ratio | 1 | trans | NA |
| Creatinine (enzymatic) in urine | 0.0158 | 0.00899 | 0.0782 | Wald ratio | 1 | trans | NA |
| Cigarettes smoked per day | 0.591 | 0.339 | 0.081 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: M23 Internal derangement of knee | 0.0984 | 0.0575 | 0.0869 | Wald ratio | 1 | trans | NA |
| _...and 82 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_24 association rows across 15 traits (15 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| TREH protein levels | 2e-58 | rs565299958 | 3 | GCST90470959 | no MR -> candidate analysis |
| Red blood cell count | 8e-14 | rs12798851 | 6 | GCST90662905 | no MR -> candidate analysis |
| Red blood cell erythrocyte count (UKB data field 30010) | 6e-13 | rs12798851 | 1 | GCST90468098 | no MR -> candidate analysis |
| Serum urate levels | 4e-12 | rs12798851 | 2 | GCST90455669 | no MR -> candidate analysis |
| Height (baseline) | 1e-9 | rs141752759 | 1 | GCST90565843 | no MR -> candidate analysis |
| Serum uric acid levels | 3e-9 | rs12798851 | 1 | GCST90018977 | no MR -> candidate analysis |
| Pulse pressure | 3e-8 | rs117204111 | 1 | GCST007096 | no MR -> candidate analysis |
| Crohn's disease | 5e-8 | rs141340254 | 2 | GCST90446792 | no MR -> candidate analysis |
| Lung cancer in ever smokers | 4e-7 | rs61677309 | 1 | GCST004749 | no MR -> candidate analysis |
| Pain | 7e-7 | rs17122021 | 1 | GCST000326 | MR: beta=0.0381, p=0.384 (trans) |
| Parental extreme longevity (95 years and older) | 1e-6 | rs11216843 | 1 | GCST003395 | no MR -> candidate analysis |
| High-sensitivity C-reactive protein (log-transformed) x plas | 1e-6 | rs12577841 | 1 | GCST90566442 | no MR -> candidate analysis |
| _...and 3 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 403 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| immunodeficiency 18 | 0.915 | — | established (curated) | no MR -> candidate analysis |
| T-B+ severe combined immunodeficiency due to CD3delta/CD3epsilon/CD3zeta | 0.608 | — | established (curated) | no MR -> candidate analysis |
| severe combined immunodeficiency | 0.509 | — | established (curated) | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 7 known modulators (T-cell surface glycoprotein CD3 epsilon chain) |
| gnomAD constraint | pLI=0.048, LOEUF=0.701 — LoF-tolerant |
| GWAS Catalog | 59 unique SNPs / 118 rows |
| ClinVar | 338 records; 3 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 403 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'CD3E' and resolved to 'T-cell surface glycoprotein CD3 epsilon chain' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 338 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 15 of 15 traits by best p-value, aggregated from 24 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P07766 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000198851/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL1975/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CD3E — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CD3E — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CD3E%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CD3E — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:42:59  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
