# Protein Dossier — ISLR2 (Immunoglobulin superfamily containing leucine-rich repeat protein 2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| LDL cholesterol | -0.184 | 0.0282 | 7.03e-11 | Wald ratio | 1 | trans | 0.988 |
| Total cholesterol | -0.115 | 0.027 | 2.27e-05 | Wald ratio | 1 | trans | NA |
| Triglycerides | -0.0999 | 0.0259 | 1.16e-04 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: L03 Cellulitis | 0.00251 | 0.000842 | 0.00289 | Inverse variance weighted | 2 | cis | NA |
| Diagnoses - main ICD10: L03 Cellulitis | 0.00251 | 0.000842 | 0.00289 | Inverse variance weighted | 2 | trans | NA |
| Depressive symptoms | -0.0473 | 0.0168 | 0.00488 | Inverse variance weighted | 2 | cis | NA |
| Depressive symptoms | -0.0473 | 0.0168 | 0.00488 | Inverse variance weighted | 2 | trans | NA |
| Chronic kidney disease | 0.158 | 0.059 | 0.0073 | Inverse variance weighted | 2 | cis | NA |
| Chronic kidney disease | 0.158 | 0.059 | 0.0073 | Inverse variance weighted | 2 | trans | NA |
| Diagnoses - main ICD10: H25 Senile cataract | 0.002 | 0.000824 | 0.0149 | Inverse variance weighted | 2 | cis | NA |
| Diagnoses - main ICD10: H25 Senile cataract | 0.002 | 0.000824 | 0.0149 | Inverse variance weighted | 2 | trans | NA |
| HDL cholesterol | 0.0642 | 0.0267 | 0.016 | Wald ratio | 1 | trans | NA |
| _...and 153 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_1 association rows across 1 traits (1 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Standing height (UKB data field 50) | 3e-12 | rs112473448 | 1 | GCST90468178 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 110 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| undetermined early-onset epileptic encephalopathy | 0.438 | — | established (curated) | no MR -> candidate analysis |
| developmental and epileptic encephalopathy, 33 | 0.438 | — | established (curated) | no MR -> candidate analysis |
| aortic disorder | 0.419 | — | common-variant locus | no MR -> candidate analysis |
| Dermatochalasis | 0.318 | — | common-variant locus | no MR -> candidate analysis |
| skin aging | 0.245 | — | common-variant locus | no MR -> candidate analysis |
| COVID-19 | 0.206 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.164 | — | common-variant locus | no MR -> candidate analysis |
| osteoarthritis | 0.102 | — | common-variant locus | no MR -> candidate analysis |

> Of the 8 rows above, **8 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.0005, LOEUF=0.954 — LoF-tolerant |
| GWAS Catalog | 55 unique SNPs / 110 rows |
| ClinVar | 133 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 110 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'ISLR2'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 133 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 1 of 1 traits by best p-value, aggregated from 1 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q6UXK2 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000167178/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/ISLR2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/ISLR2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=ISLR2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/ISLR2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:18:22  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
