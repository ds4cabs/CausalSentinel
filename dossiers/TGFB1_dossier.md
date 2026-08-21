# Protein Dossier — TGFB1 (Transforming growth factor beta-1 proprotein)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Height | -0.0656 | 0.012 | 4.16e-08 | Wald ratio | 1 | cis | NA |
| Coronary heart disease | -0.165 | 0.037 | 7.78e-06 | Wald ratio | 1 | cis | NA |
| Systolic blood pressure  automated reading | -0.0346 | 0.00984 | 4.46e-04 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | 0.0429 | 0.0125 | 5.75e-04 | Wald ratio | 1 | cis | NA |
| Total cholesterol | 0.0436 | 0.0139 | 0.0017 | Wald ratio | 1 | cis | NA |
| Age at menopause | -0.232 | 0.0772 | 0.0027 | Wald ratio | 1 | cis | NA |
| Myocardial infarction | -0.121 | 0.0409 | 0.00302 | Wald ratio | 1 | cis | NA |
| Thalamus volume | -73 | 25.7 | 0.00447 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Wrist | 0.161 | 0.0587 | 0.00608 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: migraine | -0.182 | 0.067 | 0.00675 | Wald ratio | 1 | cis | NA |
| HDL cholesterol | 0.0363 | 0.0135 | 0.00724 | Wald ratio | 1 | cis | NA |
| Eczema | -0.183 | 0.0689 | 0.00789 | Wald ratio | 1 | cis | NA |
| _...and 114 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2333_72_1` | TGF-b1 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_169 association rows across 112 traits (161 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| ESAM/TGFB1 protein level ratio | 2e-437 | rs73045269 | 1 | GCST90314718 | no MR -> candidate analysis |
| Circulating TGFB1 levels (id: OID00480_OID20621) | 4e-340 | rs73045269 | 3 | GCST90859840 | no MR -> candidate analysis |
| TGFB1 protein levels | 2e-265 | rs73045269 | 2 | GCST90470843 | no MR -> candidate analysis |
| Circulating TGFB1 levels (id: OID00785_OID20621) | 6e-259 | rs73045269 | 3 | GCST90860117 | no MR -> candidate analysis |
| Bone mineral density mean | 7e-222 | rs35247140 | 1 | GCST90321120 | no MR -> candidate analysis |
| AXL/VCAM1 protein level ratio | 1e-134 | rs8109627 | 1 | GCST90313423 | no MR -> candidate analysis |
| AXL/IL18BP protein level ratio | 4e-134 | rs8109627 | 1 | GCST90313420 | no MR -> candidate analysis |
| CEACAM21 protein levels | 1e-111 | rs8109627 | 2 | GCST90468694 | no MR -> candidate analysis |
| Blood protein levels | 1e-84 | rs1800470 | 3 | GCST006585 | no MR -> candidate analysis |
| Circulating LTBP3 levels | 9e-82 | rs73045269 | 1 | GCST90860758 | no MR -> candidate analysis |
| Height | 1e-80 | rs11466321 | 1 | GCST90245848 | MR: beta=-0.0656, p=4.16e-08 (cis) |
| LTBP3 protein levels | 3e-79 | rs73045269 | 1 | GCST90469815 | no MR -> candidate analysis |
| _...and 100 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 4097 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Camurati-Engelmann disease | 0.886 | — | established (curated) | no MR -> candidate analysis |
| inflammatory bowel disease, immunodeficiency, and encephalopathy | 0.792 | — | established (curated) | no MR -> candidate analysis |
| Encephalopathy | 0.745 | — | established (curated) | no MR -> candidate analysis |
| IL10-related early-onset inflammatory bowel disease | 0.745 | — | established (curated) | no MR -> candidate analysis |
| cystic fibrosis | 0.565 | — | established (curated) | no MR -> candidate analysis |
| coronary artery disorder | 0.64 | — | common-variant locus | no MR -> candidate analysis |
| hereditary disease | 0.675 | — | established (curated) | no MR -> candidate analysis |
| coronary atherosclerosis | 0.587 | — | common-variant locus | no MR -> candidate analysis |
| Hematuria | 0.577 | — | common-variant locus | no MR -> candidate analysis |
| heart disorder | 0.55 | — | common-variant locus | no MR -> candidate analysis |
| myocardial infarction | 0.529 | — | common-variant locus | MR: beta=-0.121, p=0.00302 (cis) |
| cardiovascular disorder | 0.498 | — | common-variant locus | no MR -> candidate analysis |
| Microscopic hematuria | 0.479 | — | common-variant locus | no MR -> candidate analysis |
| osteoarthritis | 0.431 | — | common-variant locus | MR: beta=0.0597, p=0.0494 (cis) |
| essential hypertension | 0.453 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **13 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 3 known modulators (Transforming growth factor beta-1 proprotein) |
| gnomAD constraint | pLI=0.11, LOEUF=0.637 — LoF-tolerant |
| GWAS Catalog | 124 unique SNPs / 291 rows |
| ClinVar | 555 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 4 clinical annotations across 3 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 4097 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'TGFB1' and resolved to 'Transforming growth factor beta-1 proprotein' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 555 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 20 of 112 traits by best p-value, aggregated from 169 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P01137 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000105329/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL1795178/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/TGFB1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/TGFB1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=TGFB1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=TGFB1 — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/TGFB1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:20:05  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
