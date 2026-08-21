# Protein Dossier — TOR1AIP1 (Torsin-1A-interacting protein 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: high cholesterol | 0.0798 | 0.0309 | 0.0098 | Wald ratio | 1 | trans | NA |
| Internalizing problems | -0.263 | 0.114 | 0.0211 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: M17 Gonarthrosis [arthrosis of knee] | 0.16 | 0.0764 | 0.0362 | Wald ratio | 1 | trans | NA |
| Hippocampus volume | 52.2 | 25.3 | 0.039 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: J33 Nasal polyp | 0.285 | 0.138 | 0.0396 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: hypopituitarism | 0.755 | 0.368 | 0.0401 | Wald ratio | 1 | trans | NA |
| Cigarettes smoked per day | 0.886 | 0.432 | 0.0402 | Wald ratio | 1 | trans | NA |
| Clear cell ovarian cancer | 0.424 | 0.21 | 0.0432 | Wald ratio | 1 | trans | NA |
| Forced vital capacity (FVC) | -0.0196 | 0.0102 | 0.0538 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: kidney stone or ureter stone or bladder stone | 0.218 | 0.114 | 0.0555 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: polio  or  poliomyelitis | 0.558 | 0.301 | 0.0637 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: H25 Senile cataract | -0.396 | 0.222 | 0.0747 | Wald ratio | 1 | trans | NA |
| _...and 84 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_15 association rows across 8 traits (14 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| QSOX1 protein levels | 1e-45 | rs528065895 | 1 | GCST90470402 | no MR -> candidate analysis |
| TOR1AIP1 protein levels | 1e-40 | rs141729546 | 4 | GCST90470935 | no MR -> candidate analysis |
| Cerebrospinal fluid protein TOR1AIP1 levels | 2e-33 | rs538512 | 1 | GCST90944007 | no MR -> candidate analysis |
| Refractive error | 3e-10 | rs12062341 | 2 | GCST90841196 | no MR -> candidate analysis |
| Prostate cancer | 8e-10 | rs555526 | 4 | GCST90274713 | no MR -> candidate analysis |
| Thyroid stimulating hormone levels | 6e-9 | rs571822 | 1 | GCST90572789 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 7e-9 | rs7525395 | 1 | GCST90838669 | no MR -> candidate analysis |
| Gut microbial network clusters (BlueViolet (at 3 months) x H | 8e-9 | rs12139961 | 1 | GCST90569242 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 101 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| autosomal recessive limb-girdle muscular dystrophy type 2Y | 0.843 | — | established (curated) | no MR -> candidate analysis |
| TOR1AIP1-related myopathy | 0.608 | — | established (curated) | no MR -> candidate analysis |
| centronuclear myopathy | 0.559 | — | established (curated) | no MR -> candidate analysis |
| Abnormality of refraction | 0.475 | — | common-variant locus | no MR -> candidate analysis |
| aneurysm | 0.463 | — | common-variant locus | no MR -> candidate analysis |
| peripheral vascular disease | 0.393 | — | common-variant locus | no MR -> candidate analysis |
| prostate carcinoma | 0.364 | — | common-variant locus | no MR -> candidate analysis |
| hereditary disease | 0.318 | — | established (curated) | no MR -> candidate analysis |
| respiratory tract infectious disorder | 0.083 | — | common-variant locus | no MR -> candidate analysis |

> Of the 9 rows above, **9 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Torsin-1A-interacting protein 1) |
| gnomAD constraint | pLI=3.4e-16, LOEUF=1.07 — LoF-tolerant |
| GWAS Catalog | 48 unique SNPs / 96 rows |
| ClinVar | 582 records; 6 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 101 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'TOR1AIP1' and resolved to 'Torsin-1A-interacting protein 1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 582 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 8 of 8 traits by best p-value, aggregated from 15 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q5JTV8 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000143337/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL6067329/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/TOR1AIP1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/TOR1AIP1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=TOR1AIP1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/TOR1AIP1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:27:58  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
