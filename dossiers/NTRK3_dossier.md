# Protein Dossier — NTRK3 (NT-3 growth factor receptor)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Alcohol intake frequency | -0.0628 | 0.0232 | 0.0067 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: anxiety or panic attacks | 0.254 | 0.106 | 0.0166 | Wald ratio | 1 | cis | NA |
| Years of schooling | -0.0498 | 0.0226 | 0.0278 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: migraine | -0.263 | 0.12 | 0.0281 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: G47 Sleep disorders | 0.32 | 0.153 | 0.0359 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: G56 Mononeuropathies of upper limb | -0.358 | 0.177 | 0.0433 | Wald ratio | 1 | cis | NA |
| Chronic kidney disease | 0.199 | 0.0995 | 0.0455 | Wald ratio | 1 | cis | NA |
| Hip osteoarthritis | -0.348 | 0.181 | 0.0547 | Wald ratio | 1 | cis | NA |
| Schizophrenia | 0.132 | 0.0697 | 0.0579 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: D25 Leiomyoma of uterus | -0.424 | 0.225 | 0.0589 | Wald ratio | 1 | cis | NA |
| Neo-openness to experience | -0.842 | 0.449 | 0.0608 | Wald ratio | 1 | cis | NA |
| Knee and hip osteoarthritis | -0.264 | 0.141 | 0.0616 | Wald ratio | 1 | cis | NA |
| _...and 86 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2658_27_1` | TrkC | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_110 association rows across 74 traits (63 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Bone mineral density mean | 1e-300 | rs35620181 | 1 | GCST90321120 | no MR -> candidate analysis |
| Circulating NTRK3 levels | 3e-208 | rs2009853 | 9 | GCST90859734 | no MR -> candidate analysis |
| NTRK3 protein levels | 3e-197 | rs28735437 | 6 | GCST90470098 | no MR -> candidate analysis |
| Circulating NTF3 levels | 4e-50 | rs9944243 | 6 | GCST90859904 | no MR -> candidate analysis |
| NTF3 protein levels | 2e-47 | rs117126605 | 2 | GCST90470094 | no MR -> candidate analysis |
| Height | 2e-23 | rs12441487 | 7 | GCST90245848 | no MR -> candidate analysis |
| Free Cholesterol to Cholesteryl Esters in Very Large HDL rat | 4e-21 | rs150343055 | 1 | GCST90828013 | no MR -> candidate analysis |
| NT-3 growth factor receptor levels | 2e-20 | rs28735437 | 3 | GCST90248741 | no MR -> candidate analysis |
| GLIPR1 protein levels | 8e-16 | rs148600537 | 1 | GCST90469357 | no MR -> candidate analysis |
| Neurotrophin-3 levels | 1e-12 | rs28735437 | 1 | GCST90274829 | no MR -> candidate analysis |
| Splenomegaly (PheCode 579.2) | 3e-12 | rs561662177 | 1 | GCST90480363 | no MR -> candidate analysis |
| Total PHF-tau (SNP x SNP interaction) | 5e-12 | rs7164988 x rs4954854 | 1 | GCST010340 | no MR -> candidate analysis |
| _...and 62 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 2978 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| neoplasm | 0.243 | — | established (curated) | MR: beta=-0.233, p=0.161 (cis) |
| ovarian neoplasm | 0.596 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 4 known modulators (NT-3 growth factor receptor) |
| gnomAD constraint | pLI=1, LOEUF=0.368 — LoF-INTOLERANT |
| GWAS Catalog | 94 unique SNPs / 183 rows |
| ClinVar | 179 records; 3 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 2978 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'NTRK3' and resolved to 'NT-3 growth factor receptor' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 179 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 74 traits by best p-value, aggregated from 110 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q16288 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000140538/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL5608/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/NTRK3 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/NTRK3 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=NTRK3%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/NTRK3 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:06:51  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
