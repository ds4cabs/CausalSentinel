# Protein Dossier — PEAR1 (Platelet endothelial aggregation receptor 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Systolic blood pressure  automated reading | 0.0405 | 0.0112 | 3.17e-04 | Wald ratio | 1 | cis | NA |
| Diastolic blood pressure  automated reading | 0.0345 | 0.0113 | 0.00218 | Wald ratio | 1 | cis | NA |
| Serum cystatin C (eGFRcys) | 0.0234 | 0.00898 | 0.00932 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | 0.0459 | 0.0179 | 0.0104 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K29 Gastritis and duodenitis | -0.214 | 0.0889 | 0.0162 | Wald ratio | 1 | cis | NA |
| Height | 0.0364 | 0.0153 | 0.0172 | Wald ratio | 1 | cis | NA |
| Potassium in urine | -0.0265 | 0.0112 | 0.0177 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: osteoarthritis | -0.0942 | 0.0405 | 0.02 | Wald ratio | 1 | cis | NA |
| Total cholesterol | -0.058 | 0.0256 | 0.0236 | Wald ratio | 1 | cis | NA |
| Creatinine (enzymatic) in urine | -0.0231 | 0.0105 | 0.0282 | Wald ratio | 1 | cis | NA |
| Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.0629 | 0.0305 | 0.0395 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: uterine fibroids | 0.156 | 0.0764 | 0.0407 | Wald ratio | 1 | cis | NA |
| _...and 107 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_207 association rows across 100 traits (202 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| neutrophil (absolute count, maximum, inv-norm transformed) | 1e-323 | rs2768762 | 1 | GCST90475525 | no MR -> candidate analysis |
| Mean platelet volume during third trimester of pregnancy | 1e-315 | rs12041331 | 4 | GCST90302231 | no MR -> candidate analysis |
| PEAR1 protein levels | 3e-232 | rs4661012 | 4 | GCST90470204 | no MR -> candidate analysis |
| Circulating PEAR1 levels | 5e-229 | rs4661012 | 4 | GCST90860639 | no MR -> candidate analysis |
| ENG/PEAR1 protein level ratio | 3e-188 | rs11264581 | 1 | GCST90314649 | no MR -> candidate analysis |
| Platelet count during  third trimester of pregnancy | 4e-163 | rs12041331 | 3 | GCST90302226 | no MR -> candidate analysis |
| Platelet count at delivery | 9e-154 | rs12048392 | 2 | GCST90302227 | no MR -> candidate analysis |
| Mean platelet thrombocyte volume (UKB data field 30100) | 5e-153 | rs12041331 | 3 | GCST90468087 | no MR -> candidate analysis |
| Mean platelet volume at delivery | 1e-147 | rs12041331 | 3 | GCST90302232 | no MR -> candidate analysis |
| Mean platelet volume | 1e-145 | rs12041331 | 13 | GCST90002349 | no MR -> candidate analysis |
| White blood cell count | 4e-140 | rs2768762 | 2 | GCST90026503 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 7e-132 | rs12566888 | 4 | GCST90838671 | no MR -> candidate analysis |
| _...and 88 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 145 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| platelet aggregation | 0.75 | — | common-variant locus | no MR -> candidate analysis |
| Thrombocytopenia | 0.584 | — | common-variant locus | no MR -> candidate analysis |
| Decreased total leukocyte count | 0.565 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.545 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.175 | — | common-variant locus | no MR -> candidate analysis |

> Of the 5 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=5.6e-33, LOEUF=1.01 — LoF-tolerant |
| GWAS Catalog | 111 unique SNPs / 242 rows |
| ClinVar | 210 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 15 clinical annotations across 4 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 145 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'PEAR1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 210 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 20 of 100 traits by best p-value, aggregated from 207 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q5VY43 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000187800/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PEAR1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PEAR1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PEAR1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=PEAR1 — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PEAR1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:17:02  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
