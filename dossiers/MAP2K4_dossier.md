# Protein Dossier — MAP2K4 (Dual specificity mitogen-activated protein kinase kinase 4)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| HDL cholesterol | -0.169 | 0.0131 | 7.84e-38 | Wald ratio | 1 | trans | 0.992 |
| Triglycerides | 0.141 | 0.0127 | 1.43e-28 | Wald ratio | 1 | trans | 0.992 |
| Body mass index (BMI) | 0.0351 | 0.00922 | 1.43e-04 | Wald ratio | 1 | trans | NA |
| Eye problems or disorders: Diabetes related eye disease | 0.302 | 0.088 | 5.91e-04 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code self-reported: pulmonary embolism (with or without) dvt | 0.259 | 0.0795 | 0.00114 | Wald ratio | 1 | trans | NA |
| Fractured bone site(s): Wrist | 0.166 | 0.0559 | 0.00295 | Wald ratio | 1 | trans | NA |
| Sleep duration | -0.0213 | 0.0072 | 0.00314 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: deep venous thrombosis (dvt) | 0.154 | 0.0563 | 0.00637 | Wald ratio | 1 | trans | NA |
| Hirschsprung's disease | -1.48 | 0.57 | 0.00932 | Wald ratio | 1 | trans | NA |
| Caudate volume | -47.8 | 18.6 | 0.0101 | Wald ratio | 1 | trans | NA |
| Hippocampus volume | -45.9 | 17.9 | 0.0102 | Wald ratio | 1 | trans | NA |
| Putamen volume | -57.8 | 22.7 | 0.0111 | Wald ratio | 1 | trans | NA |
| _...and 86 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5242_37_3` | MP2K4 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_196 association rows across 71 traits (174 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Height | 7e-41 | rs11653406 | 2 | GCST90245848 | no MR -> candidate analysis |
| Ascending aorta diameter | 6e-30 | rs7215383 | 2 | GCST90267390 | no MR -> candidate analysis |
| Ascending thoracic aortic diameter | 5e-29 | rs7215383 | 2 | GCST90094400 | no MR -> candidate analysis |
| Male-pattern baldness | 3e-26 | rs2529703 | 2 | GCST007020 | no MR -> candidate analysis |
| Chronic obstructive pulmonary disease liability (machine lea | 5e-25 | rs5819355 | 1 | GCST90244098 | no MR -> candidate analysis |
| Ascending aorta minimum area | 2e-23 | rs7215383 | 1 | GCST90093370 | no MR -> candidate analysis |
| Ascending aorta maximum area | 2e-22 | rs7215383 | 2 | GCST90137440 | no MR -> candidate analysis |
| Inguinal hernia | 2e-22 | rs12453693 | 7 | GCST90239727 | MR: beta=-0.0441, p=0.456 (trans) |
| heart rate (HR, minimum, inv-normal transformed) | 3e-21 | rs4614769 | 2 | GCST90476341 | no MR -> candidate analysis |
| FEV1/FVC ratio | 4e-21 | rs56130357 | 1 | GCST90705072 | no MR -> candidate analysis |
| JT interval | 6e-21 | rs4614769 | 2 | GCST90179157 | no MR -> candidate analysis |
| Ascending aorta maximum area (MTAG) | 6e-20 | rs7215383 | 1 | GCST90137450 | no MR -> candidate analysis |
| _...and 59 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 481 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| breast carcinoma | 0.344 | — | common-variant locus | no MR -> candidate analysis |
| lymphatic system disorder | 0.5 | — | common-variant locus | no MR -> candidate analysis |
| Varicose veins | 0.5 | — | common-variant locus | no MR -> candidate analysis |
| vein disorder | 0.5 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Dual specificity mitogen-activated protein kinase kinase 4) |
| gnomAD constraint | pLI=1, LOEUF=0.189 — LoF-INTOLERANT |
| GWAS Catalog | 82 unique SNPs / 159 rows |
| ClinVar | 73 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 1 clinical annotations across 1 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 481 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'MAP2K4' and resolved to 'Dual specificity mitogen-activated protein kinase kinase 4' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 73 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 20 of 71 traits by best p-value, aggregated from 196 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P45985 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000065559/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2897/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/MAP2K4 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/MAP2K4 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=MAP2K4%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=MAP2K4 — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/MAP2K4 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:43:41  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
