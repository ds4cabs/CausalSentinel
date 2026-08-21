# Protein Dossier — CST6 (Cystatin-M)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Alcohol intake frequency | 0.0572 | 0.019 | 0.00255 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | 0.0609 | 0.0206 | 0.0031 | Wald ratio | 1 | cis | NA |
| Forearm bone mineral density | -0.226 | 0.0809 | 0.00513 | Wald ratio | 1 | cis | NA |
| Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.0915 | 0.0355 | 0.01 | Wald ratio | 1 | cis | NA |
| Pallidum volume | -23.7 | 10.5 | 0.0238 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: H25 Senile cataract | 0.256 | 0.115 | 0.0264 | Wald ratio | 1 | cis | NA |
| Hip osteoarthritis | 0.32 | 0.144 | 0.027 | Wald ratio | 1 | cis | NA |
| Knee and hip osteoarthritis | 0.249 | 0.113 | 0.0284 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K40 Inguinal hernia | -0.215 | 0.0984 | 0.0288 | Wald ratio | 1 | cis | NA |
| ER-positive Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.0894 | 0.0427 | 0.0366 | Wald ratio | 1 | cis | NA |
| Primary sclerosing cholangitis  | -0.343 | 0.168 | 0.0408 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | 0.238 | 0.123 | 0.0522 | Wald ratio | 1 | cis | NA |
| _...and 70 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3303_23_2` | Cystatin M | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_17 association rows across 15 traits (16 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Cystatin-M (analyte X3303.23) levels | 4e-281 | rs1131544 | 1 | GCST90425683 | no MR -> candidate analysis |
| Cystatin-M (analyte X14711.27) levels | 1e-275 | rs1131544 | 1 | GCST90422581 | no MR -> candidate analysis |
| Cerebrospinal fluid protein CST6 levels | 1e-250 | rs1131544 | 1 | GCST90944731 | no MR -> candidate analysis |
| CST6 protein levels | 4e-206 | rs12576095 | 1 | GCST90468896 | no MR -> candidate analysis |
| Serum levels of protein CST6 | 1e-17 | rs72930985 | 1 | GCST90087915 | no MR -> candidate analysis |
| Waist circumference adjusted for body mass index | 3e-15 | rs12785292 | 1 | GCST90020029 | no MR -> candidate analysis |
| Height | 2e-14 | rs684546 | 3 | GCST008839 | no MR -> candidate analysis |
| Serum uric acid levels | 2e-11 | rs76541013 | 1 | GCST010512 | no MR -> candidate analysis |
| Multi-trait sex score | 1e-10 | rs12785292 | 1 | GCST90270116 | no MR -> candidate analysis |
| Waist-hip index | 4e-10 | rs12785292 | 1 | GCST90020027 | no MR -> candidate analysis |
| A body shape index | 1e-9 | rs12785292 | 1 | GCST90020024 | no MR -> candidate analysis |
| Alzheimer's disease | 1e-9 | rs12785292 | 1 | GCST90134416 | MR: beta=0.116, p=0.156 (cis) |
| _...and 3 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1581 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| autosomal recessive hypohidrotic ectodermal dysplasia | 0.555 | — | established (curated) | no MR -> candidate analysis |
| total hip arthroplasty | 0.313 | — | common-variant locus | no MR -> candidate analysis |
| osteoarthritis, hip | 0.313 | — | common-variant locus | MR: beta=0.32, p=0.027 (cis) |

> Of the 3 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Cystatin-B) |
| gnomAD constraint | pLI=0.0051, LOEUF=1.34 — LoF-tolerant |
| GWAS Catalog | 79 unique SNPs / 158 rows |
| ClinVar | 44 records; 4 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1581 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'CST6' and resolved to 'Cystatin-B' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 44 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 15 of 15 traits by best p-value, aggregated from 17 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q15828 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000175315/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL6066979/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CST6 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CST6 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CST6%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CST6 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:08:17  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
