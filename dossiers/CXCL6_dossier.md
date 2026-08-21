# Protein Dossier — CXCL6 (C-X-C motif chemokine 6)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Weight | 0.00644 | 0.00249 | 0.00954 | Wald ratio | 1 | cis | NA |
| Forearm bone mineral density | -0.0486 | 0.019 | 0.0107 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R07 Pain in throat and chest | 0.0303 | 0.0122 | 0.0129 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: osteoarthritis | -0.0236 | 0.00964 | 0.0143 | Wald ratio | 1 | cis | NA |
| Body fat | -0.0472 | 0.0203 | 0.0199 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K57 Diverticular disease of intestine | -0.0469 | 0.0208 | 0.0238 | Wald ratio | 1 | cis | NA |
| Sleep duration | -0.00459 | 0.0022 | 0.0369 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K35 Acute appendicitis | -0.0908 | 0.0443 | 0.0406 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | 0.00481 | 0.00244 | 0.0482 | Wald ratio | 1 | cis | NA |
| Cough on most days | 0.0276 | 0.0141 | 0.0498 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: bladder problem (not cancer) | 0.0661 | 0.0346 | 0.056 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C50 Malignant neoplasm of breast | 0.0391 | 0.0212 | 0.0645 | Wald ratio | 1 | cis | NA |
| _...and 85 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3495_15_2` | GCP-2 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_220 association rows across 112 traits (214 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating CXCL6 levels | 2e-2252 | rs16850073 | 4 | GCST90859888 | no MR -> candidate analysis |
| CXCL6/LAT protein level ratio | 4e-1490 | rs9999262 | 1 | GCST90314358 | no MR -> candidate analysis |
| CXCL6/DFFA protein level ratio | 4e-1458 | rs9999262 | 1 | GCST90314357 | no MR -> candidate analysis |
| CCL13/CXCL6 protein level ratio | 1e-1301 | rs9999262 | 1 | GCST90313677 | no MR -> candidate analysis |
| C-X-C motif chemokine 6 levels | 7e-1224 | rs16850073 | 12 | GCST90247207 | no MR -> candidate analysis |
| CXCL6/CXCL8 protein level ratio | 5e-1176 | rs9999262 | 1 | GCST90314356 | no MR -> candidate analysis |
| Platelet factor 4 variant levels | 4e-1101 | rs2367288 | 1 | GCST90248967 | no MR -> candidate analysis |
| Serum levels of protein TNFAIP8 | 1e-300 | rs2367288 | 1 | GCST90087071 | no MR -> candidate analysis |
| Blood protein levels | 2e-250 | rs872914 | 52 | GCST006585 | no MR -> candidate analysis |
| Serum levels of protein ID2 | 1e-206 | rs2367288 | 1 | GCST90090689 | no MR -> candidate analysis |
| Serum levels of protein RAB39B | 8e-189 | rs2367288 | 1 | GCST90086961 | no MR -> candidate analysis |
| Serum levels of protein SLC3A2 | 2e-169 | rs61360774 | 1 | GCST90089635 | no MR -> candidate analysis |
| _...and 100 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 415 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| hypertrophic cardiomyopathy | 0.337 | — | common-variant locus | MR: beta=0.195, p=0.246 (cis) |
| atrial fibrillation | 0.06 | — | common-variant locus | MR: beta=0.0259, p=0.319 (cis) |

> Of the 2 rows above, **0 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=3.4e-09, LOEUF=2.54 — LoF-tolerant |
| GWAS Catalog | 113 unique SNPs / 232 rows |
| ClinVar | 50 records; 7 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 415 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CXCL6'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 50 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 112 traits by best p-value, aggregated from 220 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P80162 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000124875/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CXCL6 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CXCL6 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CXCL6%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CXCL6 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:14:12  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
