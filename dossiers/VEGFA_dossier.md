# Protein Dossier — VEGFA (Vascular endothelial growth factor A, long form)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Body mass index (BMI) | -0.00885 | 0.00344 | 0.01 | Wald ratio | 1 | cis | NA |
| Bulimia nervosa | -0.0256 | 0.00997 | 0.0101 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R07 Pain in throat and chest | -0.0396 | 0.016 | 0.0131 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: uterine fibroids | 0.0636 | 0.0261 | 0.0147 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R11 Nausea and vomiting | -0.153 | 0.0641 | 0.0167 | Wald ratio | 1 | cis | NA |
| Knee and hip osteoarthritis | 0.073 | 0.0306 | 0.017 | Wald ratio | 1 | cis | NA |
| Neo-agreeableness | 0.219 | 0.092 | 0.0173 | Wald ratio | 1 | cis | NA |
| Haemoglobin concentration | 0.0209 | 0.00883 | 0.0177 | Wald ratio | 1 | cis | NA |
| Birth length | 0.0322 | 0.015 | 0.0314 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Other bones | 0.0309 | 0.0145 | 0.033 | Wald ratio | 1 | cis | NA |
| Coronary heart disease | -0.0279 | 0.0135 | 0.0388 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: vaginal prolapse or uterine prolapse | 0.087 | 0.0428 | 0.042 | Wald ratio | 1 | cis | NA |
| _...and 100 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2597_8_3` | VEGF | Suhre K | 2019 |
| `prot-c-4867_15_2` | VEGF121 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_1384 association rows across 677 traits (1328 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Thyroid stimulating hormone levels | 1e-336 | rs2396083 | 7 | GCST90572789 | no MR -> candidate analysis |
| Waist-to-hip ratio adjusted for BMI | 3e-168 | rs998584 | 43 | GCST008733 | no MR -> candidate analysis |
| Triglyceride levels | 8e-159 | rs998584 | 26 | GCST90239661 | no MR -> candidate analysis |
| high density lipoprotein cholesterol (HDLC, mean, inv-norm t | 2e-145 | rs998584 | 3 | GCST90475352 | no MR -> candidate analysis |
| Waist-hip ratio | 3e-145 | rs998584 | 17 | GCST007067 | no MR -> candidate analysis |
| triglyceride (mean, inv-norm transformed) | 3e-144 | rs998584 | 3 | GCST90476435 | no MR -> candidate analysis |
| Waist-hip index | 7e-138 | rs998584 | 18 | GCST90020027 | no MR -> candidate analysis |
| A body shape index | 6e-129 | rs998584 | 16 | GCST90020024 | no MR -> candidate analysis |
| high density lipoprotein cholesterol (HDLC, minimm, inv-norm | 9e-129 | rs998584 | 3 | GCST90475356 | no MR -> candidate analysis |
| triglyceride (maximum, inv-norm transformed) | 7e-127 | rs998584 | 2 | GCST90476431 | no MR -> candidate analysis |
| high density lipoprotein cholesterol (HDLC, maximum, inv-nor | 8e-126 | rs998584 | 3 | GCST90475348 | no MR -> candidate analysis |
| Cholesteryl Esters in Large HDL | 2e-123 | rs998584 | 2 | GCST90501136 | no MR -> candidate analysis |
| _...and 665 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 6064 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| diabetic retinopathy | 0.069 | — | common-variant locus | no MR -> candidate analysis |
| wet macular degeneration | 0.068 | — | common-variant locus | no MR -> candidate analysis |
| breast cancer | 0.056 | — | common-variant locus | MR: beta=0.0242, p=0.184 (cis) |
| macular degeneration | 0.078 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 13 known modulators (Vascular endothelial growth factor A, long form) |
| gnomAD constraint | pLI=0.4, LOEUF=0.585 — LoF-tolerant |
| GWAS Catalog | 122 unique SNPs / 294 rows |
| ClinVar | 126 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 28 clinical annotations across 17 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 6064 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'VEGFA' and resolved to 'Vascular endothelial growth factor A, long form' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 126 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 20 of 677 traits by best p-value, aggregated from 1384 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P15692 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000112715/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL1783/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/VEGFA — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/VEGFA — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=VEGFA%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=VEGFA — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/VEGFA — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:34:58  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
