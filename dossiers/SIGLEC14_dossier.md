# Protein Dossier — SIGLEC14 (Sialic acid-binding Ig-like lectin 14)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: N40 Hyperplasia of prostate | 0.0701 | 0.031 | 0.0239 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: osteoporosis | 0.0522 | 0.0243 | 0.0319 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Glaucoma | -0.0587 | 0.0283 | 0.0384 | Wald ratio | 1 | cis | NA |
| ER-positive Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0205 | 0.0107 | 0.0547 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: basal cell carcinoma | -0.068 | 0.0357 | 0.0572 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Injury or trauma resulting in loss of vision | 0.0728 | 0.0388 | 0.061 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: Z09 Follow-up examination after treatment for conditions other than malignant neoplasms | 0.044 | 0.0249 | 0.0771 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N81 Female genital prolapse | -0.047 | 0.028 | 0.0929 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Arm | 0.0477 | 0.0307 | 0.12 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K35 Acute appendicitis | -0.0743 | 0.0495 | 0.134 | Wald ratio | 1 | cis | NA |
| Amyotrophic lateral sclerosis | 0.0368 | 0.0246 | 0.134 | Wald ratio | 1 | cis | NA |
| Amygdala volume | -5.26 | 3.54 | 0.138 | Wald ratio | 1 | cis | NA |
| _...and 64 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5125_6_3` | SIG14 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_11 association rows across 10 traits (10 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| SIGLEC6 protein levels | 1e-66 | rs4801885 | 1 | GCST90470634 | no MR -> candidate analysis |
| Sialic acid-binding Ig-like lectin 14 levels | 8e-41 | rs201390621 | 1 | GCST90249547 | no MR -> candidate analysis |
| Sialic acid-binding Ig-like lectin 5 levels | 3e-20 | rs201390621 | 2 | GCST90249549 | no MR -> candidate analysis |
| Calcium levels | 6e-14 | rs2864908 | 1 | GCST90018951 | no MR -> candidate analysis |
| Sialic acid-binding Ig-like lectin 14 levels (SIGLEC14.8248. | 3e-13 | rs201390621 | 1 | GCST90242809 | no MR -> candidate analysis |
| Dolichyl-diphosphooligosaccharide--protein glycosyltransfera | 1e-10 | rs111304161 | 1 | GCST90247251 | no MR -> candidate analysis |
| Height | 2e-10 | rs883551 | 1 | GCST90435412 | no MR -> candidate analysis |
| Platelet distribution width | 4e-10 | rs11669500 | 1 | GCST90002401 | no MR -> candidate analysis |
| Monocyte count | 2e-9 | rs11669500 | 1 | GCST90002393 | no MR -> candidate analysis |
| IgA nephropathy | 4e-6 | rs2902877 | 1 | GCST90308724 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 181 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| benign digestive system neoplasm | 0.112 | — | common-variant locus | no MR -> candidate analysis |
| dentures | 0.109 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Sialic acid-binding Ig-like lectin 14) |
| gnomAD constraint | pLI=0.95, LOEUF=0.532 — LoF-INTOLERANT |
| GWAS Catalog | 115 unique SNPs / 250 rows |
| ClinVar | 78 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 181 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'SIGLEC14' and resolved to 'Sialic acid-binding Ig-like lectin 14' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 78 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 10 of 10 traits by best p-value, aggregated from 11 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q08ET2 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000254415/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4523280/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/SIGLEC14 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/SIGLEC14 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=SIGLEC14%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/SIGLEC14 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:05:40  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
