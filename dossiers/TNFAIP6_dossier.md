# Protein Dossier — TNFAIP6 (Tumor necrosis factor-inducible gene 6 protein)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: S66 Injury of muscle and tendon at wrist and hand level | 0.279 | 0.0862 | 0.00121 | Wald ratio | 1 | cis | NA |
| Triglycerides | -0.0277 | 0.00858 | 0.00122 | Wald ratio | 1 | cis | NA |
| Height | -0.0159 | 0.00529 | 0.0027 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: basal cell carcinoma | -0.152 | 0.0551 | 0.00568 | Wald ratio | 1 | cis | NA |
| Neuroticism | 0.0146 | 0.00548 | 0.00766 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | -0.0155 | 0.00584 | 0.00814 | Wald ratio | 1 | cis | NA |
| Hirschsprung's disease | -0.615 | 0.235 | 0.00897 | Wald ratio | 1 | cis | NA |
| Myocardial infarction | -0.0473 | 0.0188 | 0.0119 | Wald ratio | 1 | cis | NA |
| Inflammatory bowel disease | -0.0463 | 0.0191 | 0.0155 | Wald ratio | 1 | cis | NA |
| Juvenile idiopathic arthritis | -0.24 | 0.101 | 0.0176 | Wald ratio | 1 | cis | NA |
| Ulcerative colitis | -0.0549 | 0.024 | 0.0223 | Wald ratio | 1 | cis | NA |
| Knee osteoarthritis | -0.113 | 0.0496 | 0.0227 | Wald ratio | 1 | cis | NA |
| _...and 106 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5036_50_1` | TSG-6 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_42 association rows across 26 traits (38 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Serum levels of protein TNFAIP6 | 1e-228 | rs2278089 | 2 | GCST90088890 | no MR -> candidate analysis |
| Tumor necrosis factor-inducible gene 6 protein levels | 1e-135 | rs2278089 | 7 | GCST90249989 | no MR -> candidate analysis |
| Blood protein levels | 7e-132 | rs2278089 | 1 | GCST006585 | no MR -> candidate analysis |
| NMI protein levels | 4e-49 | rs61345365 | 6 | GCST90470056 | no MR -> candidate analysis |
| Tumor necrosis factor-inducible gene 6 protein levels (TNFAI | 2e-25 | rs201323554 | 1 | GCST90243184 | no MR -> candidate analysis |
| Cerebrospinal fluid protein TNFAIP6 levels | 2e-21 | rs3771893 | 1 | GCST90943990 | no MR -> candidate analysis |
| Estimated glomerular filtration rate (creatinine) | 6e-18 | rs77964389 | 2 | GCST90100220 | no MR -> candidate analysis |
| mean corpuscular volume (MCV, minimum, inv-norm transformed) | 2e-15 | rs13020769 | 1 | GCST90479677 | no MR -> candidate analysis |
| mean corpuscular hemoglobin (MCH, minimum, inv-norm transfor | 1e-14 | rs3948498 | 1 | GCST90479674 | no MR -> candidate analysis |
| Skeletal muscle NMI levels | 3e-14 | rs12476687 | 1 | GCST90808044 | no MR -> candidate analysis |
| mean corpuscular hemoglobin (MCH, mean, inv-norm transformed | 4e-14 | rs3845843 | 1 | GCST90479673 | no MR -> candidate analysis |
| Estimated glomerular filtration rate (creatinine, cystatin c | 5e-14 | rs10930576 | 1 | GCST90428446 | no MR -> candidate analysis |
| _...and 14 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 394 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| cardiac transplant | 0.425 | — | common-variant locus | no MR -> candidate analysis |
| type 2 diabetes mellitus | 0.367 | — | common-variant locus | no MR -> candidate analysis |
| diabetes mellitus | 0.316 | — | common-variant locus | no MR -> candidate analysis |
| pneumoconiosis | 0.182 | — | common-variant locus | no MR -> candidate analysis |
| prostate carcinoma | 0.107 | — | common-variant locus | no MR -> candidate analysis |
| brain cancer | 0.076 | — | common-variant locus | no MR -> candidate analysis |

> Of the 6 rows above, **6 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.4e-13, LOEUF=1.41 — LoF-tolerant |
| GWAS Catalog | 55 unique SNPs / 98 rows |
| ClinVar | 73 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 394 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'TNFAIP6'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 73 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 26 traits by best p-value, aggregated from 42 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P98066 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000123610/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/TNFAIP6 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/TNFAIP6 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=TNFAIP6%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/TNFAIP6 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:25:10  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
