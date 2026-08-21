# Protein Dossier — SEMA4C (Semaphorin-4C)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Schizophrenia | -0.146 | 0.0541 | 0.00689 | Wald ratio | 1 | cis | NA |
| Systolic blood pressure  automated reading | 0.0304 | 0.0117 | 0.0092 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | -0.0248 | 0.00987 | 0.012 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | 0.111 | 0.0455 | 0.0144 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertrophic cardiomyopathy (hcm  or  hocm) | 0.916 | 0.375 | 0.0145 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: pneumothorax | 0.71 | 0.307 | 0.0207 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: uterine fibroids | 0.179 | 0.0777 | 0.021 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hayfever or allergic rhinitis | 0.0904 | 0.043 | 0.0356 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: D12 Benign neoplasm of colon  rectum  anus and anal canal | 0.167 | 0.0823 | 0.0425 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R11 Nausea and vomiting | 0.28 | 0.141 | 0.0463 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: Z09 Follow-up examination after treatment for conditions other than malignant neoplasms | 0.158 | 0.0799 | 0.0484 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | -0.018 | 0.00936 | 0.0538 | Wald ratio | 1 | cis | NA |
| _...and 57 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_13 association rows across 8 traits (10 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| What is your height? (cm, inv-normal transformed) | 9e-38 | rs114089901 | 2 | GCST90475368 | no MR -> candidate analysis |
| Height | 5e-36 | rs71427097 | 2 | GCST007841 | no MR -> candidate analysis |
| Physical function (baseline) | 1e-22 | rs71427097 | 1 | GCST90565837 | no MR -> candidate analysis |
| Height (maximum, inv-normal transformed) | 2e-17 | rs114089901 | 1 | GCST90479634 | no MR -> candidate analysis |
| height (mean, inv-normal transformed) | 5e-17 | rs114089901 | 1 | GCST90479635 | no MR -> candidate analysis |
| Calcium levels | 2e-16 | rs62152866 | 2 | GCST90019500 | no MR -> candidate analysis |
| Systolic blood pressure | 3e-10 | rs71427097 | 3 | GCST90662908 | MR: beta=0.0304, p=0.0092 (cis) |
| Pulse pressure | 5e-7 | rs71427097 | 1 | GCST90310296 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1, LOEUF=0.313 — LoF-INTOLERANT |
| GWAS Catalog | 25 unique SNPs / 50 rows |
| ClinVar | 205 records; 3 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 220 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'SEMA4C'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 205 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 8 of 8 traits by best p-value, aggregated from 13 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9C0C4 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000168758/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/SEMA4C — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/SEMA4C — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=SEMA4C%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/SEMA4C — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:59:13  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
