# Protein Dossier — GGH (Gamma-glutamyl hydrolase)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: S66 Injury of muscle and tendon at wrist and hand level | 0.434 | 0.0999 | 1.40e-05 | Wald ratio | 1 | cis | NA |
| Diastolic blood pressure  automated reading | 0.0182 | 0.00623 | 0.00351 | Wald ratio | 1 | cis | NA |
| Fracture resulting from simple fall | -0.0428 | 0.0165 | 0.00965 | Wald ratio | 1 | cis | NA |
| Hip osteoarthritis | 0.164 | 0.07 | 0.0191 | Wald ratio | 1 | cis | NA |
| Packed cell volume | -0.1 | 0.0428 | 0.0193 | Wald ratio | 1 | cis | NA |
| Forearm bone mineral density | 0.0815 | 0.0382 | 0.033 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N40 Hyperplasia of prostate | 0.118 | 0.0565 | 0.0369 | Wald ratio | 1 | cis | NA |
| Mean cell haemoglobin concentration | 0.0179 | 0.00864 | 0.0382 | Wald ratio | 1 | cis | NA |
| Birth length | -0.0485 | 0.0235 | 0.0395 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K29 Gastritis and duodenitis | 0.072 | 0.0367 | 0.0497 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: small intestine or small bowel cancer | 0.396 | 0.203 | 0.0509 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: L03 Cellulitis | 0.118 | 0.0604 | 0.0513 | Wald ratio | 1 | cis | NA |
| _...and 87 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_13 association rows across 7 traits (13 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Gamma-glutamyl hydrolase levels | 8e-261 | rs12676348 | 3 | GCST90247726 | no MR -> candidate analysis |
| GGH protein levels | 5e-226 | rs190945668 | 3 | GCST90469335 | no MR -> candidate analysis |
| Serum levels of protein GGH | 9e-112 | rs3758147 | 2 | GCST90090663 | no MR -> candidate analysis |
| Gamma-glutamyl hydrolase levels (GGH.9370.69.3) | 2e-42 | rs116323041 | 1 | GCST90241235 | no MR -> candidate analysis |
| Calcium levels | 1e-11 | rs111291669 | 2 | GCST90018951 | no MR -> candidate analysis |
| Alanine transaminase (ALT, minimum, inv-norm transformed) | 2e-11 | rs3780129 | 1 | GCST90479508 | no MR -> candidate analysis |
| Hemoglobin concentration | 2e-10 | rs3780129 | 1 | GCST90002314 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 176 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Limb pain | 0.368 | — | common-variant locus | no MR -> candidate analysis |
| Headache | 0.368 | — | common-variant locus | no MR -> candidate analysis |
| Abdominal pain | 0.368 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.097 | — | common-variant locus | no MR -> candidate analysis |
| urolithiasis | 0.097 | — | common-variant locus | no MR -> candidate analysis |
| exostosis | 0.097 | — | common-variant locus | no MR -> candidate analysis |
| glomerulonephritis | 0.094 | — | common-variant locus | no MR -> candidate analysis |
| dementia | 0.071 | — | common-variant locus | no MR -> candidate analysis |
| lung cancer | 0.037 | — | established (curated) | MR: beta=0.076, p=0.262 (cis) |

> Of the 9 rows above, **8 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Gamma-glutamyl hydrolase) |
| gnomAD constraint | pLI=0.04, LOEUF=0.681 — LoF-tolerant |
| GWAS Catalog | 36 unique SNPs / 69 rows |
| ClinVar | 77 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 11 clinical annotations across 4 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 176 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'GGH' and resolved to 'Gamma-glutamyl hydrolase' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 77 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 7 of 7 traits by best p-value, aggregated from 13 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q92820 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000137563/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2223/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/GGH — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/GGH — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=GGH%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=GGH — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/GGH — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:48:45  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
