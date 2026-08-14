# Protein Dossier — PNPLA3 (1-acylglycerol-3-phosphate O-acyltransferase PNPLA3)

**MR feasibility tier: C** — No plasma pQTL found (accession + symbol match). Standard plasma pQTL MR is not currently feasible; gene-level genetic evidence below is the honest preview.

## 1. Published MR estimates (retrieved, not computed)

_None in the EpiGraphDB pQTL resource. Absence of an estimate is not evidence of no effect._

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_1236 association rows across 660 traits (1195 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Alanine aminotransferase levels | 2e-495 | rs738409 | 19 | GCST90428729 | no MR -> candidate analysis |
| Aspartate aminotransferase levels | 3e-361 | rs738409 | 17 | GCST90018944 | no MR -> candidate analysis |
| Chronic liver disease and cirrhosis (PheCode 571) | 1e-323 | rs738409 | 6 | GCST90476081 | no MR -> candidate analysis |
| Other chronic nonalcoholic liver disease (PheCode 571.5) | 1e-323 | rs738409 | 6 | GCST90476084 | no MR -> candidate analysis |
| Abnormal results of function study of liver (PheCode 573.7) | 1e-323 | rs738409 | 6 | GCST90476097 | no MR -> candidate analysis |
| Alanine transaminase (ALT, maximum, inv-norm transformed) | 1e-323 | rs738409 | 4 | GCST90475109 | no MR -> candidate analysis |
| Alanine transaminase (ALT, minimum, inv-norm transformed) | 1e-323 | rs738409 | 4 | GCST90475115 | no MR -> candidate analysis |
| Alanine transaminase (ALT, mean, inv-norm transformed) | 1e-323 | rs738409 | 4 | GCST90475112 | no MR -> candidate analysis |
| Aspartate aminotransferase (AST, maximum, inv-norm transform | 1e-323 | rs738409 | 4 | GCST90475118 | no MR -> candidate analysis |
| Aspartate aminotransferase (AST, mean, inv-norm transformed) | 1e-323 | rs738409 | 4 | GCST90475121 | no MR -> candidate analysis |
| Aspartate aminotransferase (AST, minimum, inv-norm transform | 1e-323 | rs738409 | 4 | GCST90475124 | no MR -> candidate analysis |
| Liver enzyme levels (alanine transaminase) | 1e-300 | rs738409 | 2 | GCST90013405 | no MR -> candidate analysis |
| _...and 648 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 308 total); genetic_association aggregates GWAS common-variant AND rare-variant evidence. **Associations are loci, not causal claims.**_

| Disease | genetic assoc. | overall | MR status |
|---|---|---|---|
| metabolic dysfunction-associated steatotic liver disease | 0.869 | 0.712 | no MR -> candidate analysis |
| liver disorder | 0.901 | 0.565 | no MR -> candidate analysis |
| gout | 0.883 | 0.555 | no MR -> candidate analysis |
| cirrhosis of liver | 0.874 | 0.545 | no MR -> candidate analysis |
| type 2 diabetes mellitus | 0.845 | 0.532 | no MR -> candidate analysis |
| hepatocellular carcinoma | 0.65 | 0.523 | no MR -> candidate analysis |
| diabetes mellitus | 0.826 | 0.518 | no MR -> candidate analysis |
| alcoholic liver diseases | 0.832 | 0.513 | no MR -> candidate analysis |
| esophageal varices | 0.837 | 0.509 | no MR -> candidate analysis |
| liver cancer | 0.786 | 0.486 | no MR -> candidate analysis |
| coronary artery disorder | 0.758 | 0.482 | no MR -> candidate analysis |
| Abnormality of the liver | 0.79 | 0.48 | no MR -> candidate analysis |
| portal hypertension | 0.773 | 0.48 | no MR -> candidate analysis |
| Hypercholesterolemia | 0.774 | 0.472 | no MR -> candidate analysis |
| intrahepatic bile duct cancer | 0.751 | 0.457 | no MR -> candidate analysis |

> **15 of the 15 genetically-supported diseases above have no MR estimate in this resource** — that gap is the candidate-analysis / comorbidity-hypothesis space.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.6e-14, LOEUF=1.26 — LoF-tolerant |
| GWAS Catalog | 109 unique SNPs / 256 rows |
| ClinVar | 216 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 2 clinical annotations across 6 drugs |

## Caveats declared by the tools

- **`mr_outcomes`** — No pQTL MR estimates for PNPLA3 in this resource. ABSENCE OF AN ESTIMATE IS NOT EVIDENCE OF NO EFFECT.
- **`phenome`** — Top 30 of 308 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'PNPLA3'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 216 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 20 of 660 traits by best p-value, aggregated from 1236 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9NST1 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000100344/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PNPLA3 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PNPLA3 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PNPLA3%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=PNPLA3 — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PNPLA3 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T00:48:17  ·  Tier: C
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
