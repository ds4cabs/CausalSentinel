# Protein Dossier — LDOC1 (Protein LDOC1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: R11 Nausea and vomiting | -0.351 | 0.125 | 0.00498 | Wald ratio | 1 | trans | NA |
| Alcohol intake frequency | -0.0184 | 0.00802 | 0.022 | Wald ratio | 1 | trans | NA |
| Primary sclerosing cholangitis  | -0.171 | 0.0784 | 0.0291 | Wald ratio | 1 | trans | NA |
| Sodium in urine | -0.0114 | 0.00534 | 0.0322 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: sleep apnoea | 0.172 | 0.083 | 0.0384 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: C61 Malignant neoplasm of prostate | -0.156 | 0.0784 | 0.0463 | Wald ratio | 1 | trans | NA |
| Cancer code  self-reported: prostate cancer | -0.147 | 0.074 | 0.0466 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: G47 Sleep disorders | 0.123 | 0.0628 | 0.0499 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: N92 Excessive  frequent and irregular menstruation | -0.0804 | 0.041 | 0.0501 | Wald ratio | 1 | trans | NA |
| Systolic blood pressure  automated reading | 0.0107 | 0.00555 | 0.0534 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: bladder problem (not cancer) | -0.157 | 0.084 | 0.061 | Wald ratio | 1 | trans | NA |
| Squamous cell lung cancer | -0.127 | 0.0683 | 0.0623 | Wald ratio | 1 | trans | NA |
| _...and 67 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_No GWAS Catalog associations mapped to this gene._

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.62, LOEUF=0.963 — LoF-tolerant |
| GWAS Catalog | 1 unique SNPs / 2 rows |
| ClinVar | 216 records; 21 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 121 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'LDOC1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 216 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — No GWAS Catalog associations mapped to this gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O95751 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000182195/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/LDOC1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/LDOC1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=LDOC1%5Bgene%5D — _ClinVar build Build260809-1055.1_

## Provenance

- Generated: 2026-08-14T03:29:09  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
