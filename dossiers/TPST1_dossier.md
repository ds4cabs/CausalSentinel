# Protein Dossier — TPST1 (Protein-tyrosine sulfotransferase 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Weight | -0.0378 | 0.00991 | 1.35e-04 | Wald ratio | 1 | cis | NA |
| Diastolic blood pressure  automated reading | -0.0368 | 0.0115 | 0.00135 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: migraine | 0.15 | 0.0561 | 0.00752 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M16 Coxarthrosis [arthrosis of hip] | -0.357 | 0.137 | 0.00898 | Wald ratio | 1 | cis | NA |
| Happiness | 0.0335 | 0.0139 | 0.0158 | Wald ratio | 1 | cis | NA |
| Triglycerides | 0.0532 | 0.022 | 0.0159 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | -0.0233 | 0.00972 | 0.0164 | Wald ratio | 1 | cis | NA |
| Rheumatoid arthritis | -0.17 | 0.0746 | 0.0231 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | -0.0204 | 0.00922 | 0.0268 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hyperthyroidism or thyrotoxicosis | 0.222 | 0.106 | 0.0361 | Wald ratio | 1 | cis | NA |
| Serum cystatin C (eGFRcys) | 0.0177 | 0.00865 | 0.0404 | Wald ratio | 1 | cis | NA |
| Mean cell volume | 0.233 | 0.114 | 0.0408 | Wald ratio | 1 | cis | NA |
| _...and 97 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_18 association rows across 10 traits (15 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Protein-tyrosine sulfotransferase 1 levels | 4e-64 | rs12537083 | 1 | GCST90249185 | no MR -> candidate analysis |
| Argininosuccinate lyase levels | 2e-31 | rs4145009 | 1 | GCST90246581 | no MR -> candidate analysis |
| White blood cell count | 9e-25 | rs12540307 | 8 | GCST90662906 | no MR -> candidate analysis |
| Height (baseline) | 2e-15 | rs4291144 | 1 | GCST90565843 | no MR -> candidate analysis |
| Bone mineral density mean | 7e-14 | rs75734022 | 1 | GCST90321120 | no MR -> candidate analysis |
| Smoking initiation | 3e-13 | rs62468710 | 1 | GCST90243968 | no MR -> candidate analysis |
| Neutrophil count | 3e-12 | rs12540307 | 1 | GCST90018968 | no MR -> candidate analysis |
| Triglyceride levels | 7e-10 | rs9969301 | 1 | GCST90662893 | no MR -> candidate analysis |
| Gout | 1e-7 | rs4149458 | 2 | GCST001356 | MR: beta=0.0934, p=0.28 (cis) |
| Hospitalization rate in serious mental illnesses | 7e-6 | rs146187962 | 1 | GCST90559268 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 77 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| smoking initiation | 0.254 | — | common-variant locus | no MR -> candidate analysis |
| poisoning | 0.135 | — | common-variant locus | no MR -> candidate analysis |
| Alzheimer disease | 0.064 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.00039, LOEUF=0.835 — LoF-tolerant |
| GWAS Catalog | 22 unique SNPs / 42 rows |
| ClinVar | 71 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 77 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'TPST1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 71 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 10 of 10 traits by best p-value, aggregated from 18 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O60507 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000169902/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/TPST1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/TPST1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=TPST1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/TPST1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:28:34  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
