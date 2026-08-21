# Protein Dossier — CCL22 (C-C motif chemokine 22)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: high cholesterol | 0.222 | 0.0209 | 2.20e-26 | Wald ratio | 1 | trans | 1 |
| Non-cancer illness code  self-reported: deep venous thrombosis (dvt) | 0.294 | 0.0512 | 9.81e-09 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code self-reported: pulmonary embolism (with or without) dvt | 0.331 | 0.0775 | 1.97e-05 | Wald ratio | 1 | trans | NA |
| Forced expiratory volume in 1-second (FEV1) | 0.0312 | 0.00837 | 1.96e-04 | Wald ratio | 1 | trans | NA |
| Forced vital capacity (FVC) | 0.0285 | 0.00793 | 3.20e-04 | Wald ratio | 1 | trans | NA |
| Eye problems or disorders: Glaucoma | 0.229 | 0.0654 | 4.57e-04 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: M16 Coxarthrosis [arthrosis of hip] | 0.222 | 0.0648 | 6.19e-04 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: gout | -0.404 | 0.124 | 0.00108 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | 0.12 | 0.0381 | 0.00161 | Wald ratio | 1 | trans | NA |
| Schizophrenia | -0.148 | 0.048 | 0.00209 | Wald ratio | 1 | trans | NA |
| Systolic blood pressure  automated reading | -0.0283 | 0.00991 | 0.00425 | Wald ratio | 1 | trans | NA |
| Alcohol intake frequency | -0.04 | 0.0143 | 0.00512 | Wald ratio | 1 | trans | NA |
| _...and 63 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3508_78_3` | MDC | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_30 association rows across 22 traits (24 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| CCL17/PDGFB protein level ratio | 9e-164 | rs9925562 | 1 | GCST90313688 | no MR -> candidate analysis |
| CCL13/CCL17 protein level ratio | 2e-155 | rs9925562 | 1 | GCST90313674 | no MR -> candidate analysis |
| CCL17/THPO protein level ratio | 1e-149 | rs9925562 | 1 | GCST90313689 | no MR -> candidate analysis |
| CCL17/F2R protein level ratio | 1e-141 | rs9925562 | 1 | GCST90313686 | no MR -> candidate analysis |
| CCL22 protein levels | 4e-139 | rs41398344 | 4 | GCST90468574 | no MR -> candidate analysis |
| CX3CL1/RGMB protein level ratio | 1e-72 | rs35053878 | 1 | GCST90314327 | no MR -> candidate analysis |
| C-C motif chemokine 22 levels (CCL22.3508.78.3) | 4e-32 | rs41398344 | 1 | GCST90240490 | no MR -> candidate analysis |
| C-C motif chemokine 22 levels | 3e-31 | rs72784876 | 4 | GCST90246911 | no MR -> candidate analysis |
| Serum levels of protein CCL22 | 1e-22 | rs223883 | 1 | GCST90088427 | no MR -> candidate analysis |
| Systemic lupus erythematosus | 3e-15 | rs669763 | 3 | GCST011956 | no MR -> candidate analysis |
| High density lipoprotein cholesterol levels | 3e-15 | rs4359426 | 1 | GCST90019510 | no MR -> candidate analysis |
| C-C motif chemokine 17 levels | 8e-15 | rs9921681 | 1 | GCST90161830 | no MR -> candidate analysis |
| _...and 10 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 547 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| systemic lupus erythematosus | 0.65 | — | common-variant locus | no MR -> candidate analysis |
| pathological myopia | 0.116 | — | common-variant locus | no MR -> candidate analysis |
| Microscopic hematuria | 0.102 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (C-C motif chemokine 22) |
| gnomAD constraint | pLI=0.0033, LOEUF=1.72 — LoF-tolerant |
| GWAS Catalog | 77 unique SNPs / 154 rows |
| ClinVar | 48 records; 11 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 547 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'CCL22' and resolved to 'C-C motif chemokine 22' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 48 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 20 of 22 traits by best p-value, aggregated from 30 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O00626 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000102962/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4295649/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CCL22 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CCL22 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CCL22%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CCL22 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:35:12  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: pharmgkb
