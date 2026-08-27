# Protein Dossier — HDGF (Hepatoma-derived growth factor)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Heel bone mineral density (BMD) T-score  automated | 0.0435 | 0.0122 | 3.65e-04 | Wald ratio | 1 | cis | NA |
| Hearing difficulty or problems: Yes | -0.0558 | 0.0172 | 0.0012 | Wald ratio | 1 | cis | NA |
| Schizophrenia | -0.115 | 0.042 | 0.00625 | Wald ratio | 1 | cis | NA |
| Subjective well being | 0.0297 | 0.0112 | 0.00766 | Wald ratio | 1 | cis | NA |
| HDL cholesterol | -0.0494 | 0.019 | 0.00911 | Wald ratio | 1 | cis | NA |
| Systolic blood pressure  automated reading | 0.025 | 0.00966 | 0.00963 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I84 Haemorrhoids | 0.132 | 0.0533 | 0.0132 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: asthma | -0.0699 | 0.0284 | 0.0137 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Cataract | -0.146 | 0.06 | 0.0151 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | 0.0183 | 0.00774 | 0.0183 | Wald ratio | 1 | cis | NA |
| Invasive mucinous ovarian cancer | 0.366 | 0.156 | 0.0187 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: uterine fibroids | 0.153 | 0.0657 | 0.0197 | Wald ratio | 1 | cis | NA |
| _...and 113 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_29 association rows across 21 traits (29 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating HDGF levels | 1e-6099 | rs4501833 | 1 | GCST90860377 | no MR -> candidate analysis |
| HDGF protein levels | 2e-199 | rs116078160 | 5 | GCST90469442 | no MR -> candidate analysis |
| Serum levels of protein HDGF | 1e-42 | rs12039810 | 1 | GCST90090404 | no MR -> candidate analysis |
| White blood cell count | 3e-41 | rs4501833 | 1 | GCST90101726 | no MR -> candidate analysis |
| Neutrophil count | 7e-40 | rs12566986 | 1 | GCST90101731 | no MR -> candidate analysis |
| Height | 4e-38 | rs4399146 | 1 | GCST90245848 | MR: beta=0.0234, p=0.0719 (cis) |
| Aorta HDGF levels | 9e-24 | rs11264533 | 1 | GCST90798866 | no MR -> candidate analysis |
| Blood protein levels | 3e-23 | rs4399146 | 1 | GCST006585 | no MR -> candidate analysis |
| Liver HDGF levels | 2e-18 | rs9427242 | 1 | GCST90801724 | no MR -> candidate analysis |
| WFDC12 protein levels | 5e-18 | rs4399146 | 1 | GCST90471073 | no MR -> candidate analysis |
| Drinks per week | 1e-14 | rs12039810 | 2 | GCST90243984 | no MR -> candidate analysis |
| Polyunsaturated fatty acids to monounsaturated fatty acids r | 3e-11 | rs11264534 | 2 | GCST90502155 | no MR -> candidate analysis |
| _...and 9 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 236 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| prostate carcinoma | 0.626 | — | common-variant locus | no MR -> candidate analysis |
| thyrotoxicosis | 0.139 | — | common-variant locus | MR: beta=-0.215, p=0.122 (cis) |
| adolescent idiopathic scoliosis | 0.104 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Hepatoma-derived growth factor) |
| gnomAD constraint | pLI=1, LOEUF=0.351 — LoF-INTOLERANT |
| GWAS Catalog | 98 unique SNPs / 196 rows |
| ClinVar | 62 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 236 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'HDGF' and resolved to 'Hepatoma-derived growth factor' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 62 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 21 traits by best p-value, aggregated from 29 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P51858 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000143321/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL5724677/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/HDGF — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/HDGF — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=HDGF%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/HDGF — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:59:19  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
