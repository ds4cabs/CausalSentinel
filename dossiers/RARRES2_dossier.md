# Protein Dossier — RARRES2 (Retinoic acid receptor responder protein 2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Thyroid cancer | -1.35 | 0.268 | 4.54e-07 | Wald ratio | 1 | cis | NA |
| Sodium in urine | 0.0276 | 0.00716 | 1.15e-04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | -0.0366 | 0.0129 | 0.0045 | Wald ratio | 1 | cis | NA |
| Knee osteoarthritis | -0.222 | 0.0817 | 0.00668 | Wald ratio | 1 | cis | NA |
| Knee and hip osteoarthritis | -0.168 | 0.0621 | 0.00691 | Wald ratio | 1 | cis | NA |
| Creatinine (enzymatic) in urine | 0.0186 | 0.00697 | 0.00749 | Wald ratio | 1 | cis | NA |
| Alzheimer's disease | -0.113 | 0.0469 | 0.0165 | Wald ratio | 1 | cis | NA |
| Systolic blood pressure  automated reading | -0.0168 | 0.00745 | 0.0243 | Wald ratio | 1 | cis | NA |
| Potassium in urine | 0.0166 | 0.00739 | 0.0245 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: S66 Injury of muscle and tendon at wrist and hand level | 0.301 | 0.138 | 0.0288 | Wald ratio | 1 | cis | NA |
| Diastolic blood pressure  automated reading | -0.0155 | 0.00745 | 0.0374 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: H25 Senile cataract | 0.147 | 0.0721 | 0.0417 | Wald ratio | 1 | cis | NA |
| _...and 96 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3079_62_2` | TIG2 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_24 association rows across 17 traits (20 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating RARRES2 levels | 1e-385 | rs3735167 | 1 | GCST90859990 | no MR -> candidate analysis |
| RARRES2 protein levels | 1e-216 | rs3735167 | 1 | GCST90470428 | no MR -> candidate analysis |
| Retinoic acid receptor responder protein 2 levels | 6e-115 | rs3735167 | 5 | GCST90249382 | no MR -> candidate analysis |
| Serum levels of protein RARRES2 | 1e-71 | rs2098053 | 1 | GCST90088227 | no MR -> candidate analysis |
| Blood protein levels | 9e-46 | rs3735167 | 1 | GCST006585 | no MR -> candidate analysis |
| Cerebrospinal fluid protein RARRES2 levels | 1e-34 | rs57367026 | 1 | GCST90945039 | no MR -> candidate analysis |
| Chemerin levels | 2e-21 | rs3735167 | 1 | GCST007900 | no MR -> candidate analysis |
| Height | 1e-13 | rs3735167 | 1 | GCST90245848 | MR: beta=-0.00864, p=0.349 (cis) |
| Impedance of whole body (UKB data field 23106) | 6e-12 | rs10952252 | 1 | GCST90468173 | no MR -> candidate analysis |
| Protein levels in obesity | 2e-10 | rs10282458 | 1 | GCST010196 | no MR -> candidate analysis |
| Circulating chemerin levels | 2e-10 | rs10259796 | 2 | GCST004389 | no MR -> candidate analysis |
| Systolic blood pressure | 3e-10 | rs11771693 | 2 | GCST006624 | MR: beta=-0.0168, p=0.0243 (cis) |
| _...and 5 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 565 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Abnormality of the skeletal system | 0.693 | — | common-variant locus | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.0015, LOEUF=1.08 — LoF-tolerant |
| GWAS Catalog | 39 unique SNPs / 78 rows |
| ClinVar | 114 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 565 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'RARRES2'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 114 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 17 of 17 traits by best p-value, aggregated from 24 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q99969 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000106538/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/RARRES2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/RARRES2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=RARRES2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/RARRES2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:45:45  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
