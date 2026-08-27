# Protein Dossier — IL17RA (Interleukin-17 receptor A)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Cancer code  self-reported: small intestine or small bowel cancer | 0.279 | 0.107 | 0.00932 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | 0.0092 | 0.00384 | 0.0166 | Wald ratio | 1 | cis | NA |
| Sodium in urine | 0.00671 | 0.00292 | 0.0213 | Wald ratio | 1 | cis | NA |
| Autism | -0.0747 | 0.0358 | 0.037 | Wald ratio | 1 | cis | NA |
| Haemoglobin concentration | 0.0366 | 0.0181 | 0.0425 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Wrist | -0.0426 | 0.0221 | 0.0535 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: basal cell carcinoma | 0.054 | 0.0293 | 0.0654 | Wald ratio | 1 | cis | NA |
| Coronary heart disease | -0.0212 | 0.0116 | 0.0665 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M23 Internal derangement of knee | -0.036 | 0.0207 | 0.0813 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: bladder problem (not cancer) | 0.0615 | 0.0366 | 0.0928 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: D12 Benign neoplasm of colon  rectum  anus and anal canal | -0.0425 | 0.0261 | 0.104 | Wald ratio | 1 | cis | NA |
| Pallidum volume | 3.76 | 2.37 | 0.112 | Wald ratio | 1 | cis | NA |
| _...and 83 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2992_59_2` | IL-17 sR | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_133 association rows across 43 traits (132 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating IL17RA levels | 4e-5490 | rs4819959 | 9 | GCST90859915 | no MR -> candidate analysis |
| Interleukin-17 receptor A levels | 8e-1169 | rs4819959 | 13 | GCST90248041 | no MR -> candidate analysis |
| Interleukin-17 receptor A levels (IL17RA.2992.59.2) | 6e-483 | rs397780227 | 3 | GCST90241597 | no MR -> candidate analysis |
| Monocyte count | 3e-465 | rs140221307 | 15 | GCST90025950 | no MR -> candidate analysis |
| Monocyte percentage of white cells | 1e-370 | rs140221307 | 6 | GCST90002394 | no MR -> candidate analysis |
| Blood protein levels | 8e-347 | rs2241047 | 1 | GCST006585 | no MR -> candidate analysis |
| monocyte (absolute count, mean, inv-norm transformed) | 1e-323 | rs140221307 | 2 | GCST90475502 | no MR -> candidate analysis |
| monocyte (fraction, mean, inv-norm transformed) | 1e-323 | rs140221307 | 2 | GCST90475511 | no MR -> candidate analysis |
| monocyte (absolute count, minimum, inv-norm transformed) | 3e-211 | rs140221307 | 2 | GCST90475505 | no MR -> candidate analysis |
| monocyte (fraction, maximum, inv-norm transformed) | 2e-203 | rs140221307 | 2 | GCST90475508 | no MR -> candidate analysis |
| monocyte (fraction, minimum, inv-norm transformed) | 1e-187 | rs140221307 | 2 | GCST90475514 | no MR -> candidate analysis |
| monocyte (absolute count, maximum, inv-norm transformed) | 4e-175 | rs140221307 | 2 | GCST90475499 | no MR -> candidate analysis |
| _...and 31 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 789 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| immunodeficiency 51 | 0.844 | — | established (curated) | no MR -> candidate analysis |
| psoriasis | 0.398 | — | established (curated) | MR: beta=-0.0258, p=0.368 (cis) |
| Chronic mucocutaneous candidosis | 0.608 | — | established (curated) | no MR -> candidate analysis |
| chronic mucocutaneous candidiasis | 0.574 | — | established (curated) | no MR -> candidate analysis |
| polycythemia | 0.214 | — | common-variant locus | no MR -> candidate analysis |
| enteritis | 0.207 | — | common-variant locus | no MR -> candidate analysis |

> Of the 6 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 1 known modulators (Interleukin-17 receptor A) |
| gnomAD constraint | pLI=3.3e-08, LOEUF=0.898 — LoF-tolerant |
| GWAS Catalog | 112 unique SNPs / 244 rows |
| ClinVar | 1113 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 1 clinical annotations across 1 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 789 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'IL17RA' and resolved to 'Interleukin-17 receptor A' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 1113 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 20 of 43 traits by best p-value, aggregated from 133 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q96F46 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000177663/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3580485/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/IL17RA — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/IL17RA — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=IL17RA%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=IL17RA — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/IL17RA — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:11:57  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
