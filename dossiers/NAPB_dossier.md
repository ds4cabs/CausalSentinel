# Protein Dossier — NAPB (Beta-soluble NSF attachment protein)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: enlarged prostate | 0.283 | 0.094 | 0.0026 | Wald ratio | 1 | trans | NA |
| Forced expiratory volume in 1-second (FEV1) | 0.0346 | 0.0125 | 0.0057 | Wald ratio | 1 | trans | NA |
| Fasting glucose | 0.0495 | 0.0196 | 0.0115 | Wald ratio | 1 | trans | NA |
| Hearing difficulty or problems: Yes | -0.0662 | 0.0267 | 0.013 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: bladder problem (not cancer) | 0.33 | 0.14 | 0.0181 | Wald ratio | 1 | trans | NA |
| Ferritin | -0.131 | 0.0576 | 0.0236 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: C50 Malignant neoplasm of breast | 0.192 | 0.0942 | 0.0412 | Wald ratio | 1 | trans | NA |
| Cancer code  self-reported: malignant melanoma | 0.259 | 0.129 | 0.0445 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: muscle or soft tissue injuries | 0.258 | 0.135 | 0.0556 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: Z09 Follow-up examination after treatment for conditions other than malignant neoplasms | -0.319 | 0.167 | 0.0567 | Wald ratio | 1 | trans | NA |
| Forced vital capacity (FVC) | 0.0225 | 0.0119 | 0.0577 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: migraine | 0.137 | 0.0732 | 0.0611 | Wald ratio | 1 | trans | NA |
| _...and 78 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_7 association rows across 4 traits (3 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Cystatin C levels | 8e-200 | rs78916169 | 3 | GCST90019504 | no MR -> candidate analysis |
| Factor VII activity | 4e-7 | rs6083120 | 1 | GCST007401 | no MR -> candidate analysis |
| COVID-19 (severe respiratory symptoms vs population) | 2e-6 | rs11480078 | 1 | GCST90027249 | no MR -> candidate analysis |
| Facial morphology (factor 15, philtrum width) | 3e-6 | rs6076065 | 2 | GCST004319 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 312 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| abortion | 0.317 | — | common-variant locus | no MR -> candidate analysis |
| hereditary disease | 0.314 | — | established (curated) | no MR -> candidate analysis |
| Spasticity - intellectual disability - X-linked epilepsy | 0.182 | — | established (curated) | no MR -> candidate analysis |
| developmental and epileptic encephalopathy, 1 | 0.182 | — | established (curated) | no MR -> candidate analysis |

> Of the 4 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=3.5e-05, LOEUF=0.808 — LoF-tolerant |
| GWAS Catalog | 39 unique SNPs / 77 rows |
| ClinVar | 74 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 312 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'NAPB'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 74 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 4 of 4 traits by best p-value, aggregated from 7 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9H115 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000125814/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/NAPB — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/NAPB — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=NAPB%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/NAPB — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:55:15  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
