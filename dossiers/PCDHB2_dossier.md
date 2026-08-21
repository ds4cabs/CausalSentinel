# Protein Dossier — PCDHB2 (Protocadherin beta-2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Bipolar disorder | 0.395 | 0.124 | 0.00143 | Wald ratio | 1 | trans | NA |
| Transferrin | 0.145 | 0.0525 | 0.00577 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: R35 Polyuria | 0.356 | 0.139 | 0.0105 | Wald ratio | 1 | trans | NA |
| Fractured bone site(s): Arm | 0.24 | 0.0973 | 0.0138 | Wald ratio | 1 | trans | NA |
| Melanoma | 0.614 | 0.261 | 0.0188 | Wald ratio | 1 | trans | NA |
| Triglycerides | -0.0566 | 0.0242 | 0.0196 | Wald ratio | 1 | trans | NA |
| Fasting insulin | -0.0359 | 0.0157 | 0.0223 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: K35 Acute appendicitis | 0.3 | 0.132 | 0.0227 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: K43 Ventral hernia | 0.311 | 0.137 | 0.0228 | Wald ratio | 1 | trans | NA |
| ER-positive Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0918 | 0.0411 | 0.0254 | Wald ratio | 1 | trans | NA |
| Happiness | -0.0334 | 0.0151 | 0.0271 | Wald ratio | 1 | trans | NA |
| Glioma | -0.489 | 0.224 | 0.0293 | Wald ratio | 1 | trans | NA |
| _...and 94 more outcomes (see JSON)_ | | | | | | | |

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
| gnomAD constraint | pLI=NA, LOEUF=NA — Constraint metrics missing; LoF tolerance cannot be judged. |
| GWAS Catalog | 19 unique SNPs / 38 rows |
| ClinVar | 152 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 15 of 15 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'PCDHB2'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 152 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — No GWAS Catalog associations mapped to this gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9Y5E7 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000112852/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PCDHB2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PCDHB2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PCDHB2%5Bgene%5D — _ClinVar build Build260809-1055.1_

## Provenance

- Generated: 2026-08-14T04:12:25  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
