# Protein Dossier — C1QL1 (C1q-related factor)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Systolic blood pressure  automated reading | 0.0377 | 0.00883 | 1.91e-05 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K43 Ventral hernia | 0.331 | 0.094 | 4.33e-04 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | 0.0384 | 0.0112 | 5.81e-04 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | -0.024 | 0.00708 | 6.96e-04 | Wald ratio | 1 | cis | NA |
| Height | -0.0358 | 0.0108 | 8.58e-04 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Wrist | 0.168 | 0.0522 | 0.00126 | Wald ratio | 1 | cis | NA |
| Iron | 0.106 | 0.0362 | 0.00338 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | -0.0201 | 0.00747 | 0.007 | Wald ratio | 1 | cis | NA |
| Transferrin Saturation | 0.0914 | 0.0366 | 0.0124 | Wald ratio | 1 | cis | NA |
| Diastolic blood pressure  automated reading | 0.0202 | 0.00883 | 0.0223 | Wald ratio | 1 | cis | NA |
| Serum creatinine (eGFRcrea) | 0.00717 | 0.0033 | 0.0297 | Wald ratio | 1 | cis | NA |
| Hirschsprung's disease | -1.03 | 0.48 | 0.0326 | Wald ratio | 1 | cis | NA |
| _...and 104 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_4 association rows across 4 traits (2 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| C1q-related factor levels | 6e-68 | rs1055646 | 1 | GCST90246765 | no MR -> candidate analysis |
| Serum levels of protein C1QL1 | 3e-53 | rs1055646 | 1 | GCST90089401 | no MR -> candidate analysis |
| DNA methylation (variation) | 2e-6 | rs1007190 | 1 | GCST002058 | no MR -> candidate analysis |
| Dry eye disease with Sjogren-like syndromes | 4e-6 | rs3024285 | 1 | GCST90444403 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 115 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| anxiety disorder | 0.31 | — | common-variant locus | no MR -> candidate analysis |
| epilepsy | 0.164 | — | common-variant locus | no MR -> candidate analysis |
| enteritis | 0.123 | — | common-variant locus | no MR -> candidate analysis |
| intelligence | 0.112 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=3.6e-06, LOEUF=1.62 — LoF-tolerant |
| GWAS Catalog | 74 unique SNPs / 148 rows |
| ClinVar | 56 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 115 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'C1QL1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 56 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 4 of 4 traits by best p-value, aggregated from 4 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O75973 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000131094/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/C1QL1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/C1QL1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=C1QL1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/C1QL1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:20:23  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
