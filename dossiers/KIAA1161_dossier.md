# Protein Dossier — KIAA1161 (Alpha-galactosidase MYORG)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: hayfever or allergic rhinitis | 0.104 | 0.03 | 5.38e-04 | Wald ratio | 1 | cis | NA |
| Systolic blood pressure  automated reading | -0.0266 | 0.00829 | 0.00132 | Wald ratio | 1 | cis | NA |
| Weight | -0.0213 | 0.00715 | 0.00295 | Wald ratio | 1 | cis | NA |
| Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0613 | 0.0208 | 0.00315 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C61 Malignant neoplasm of prostate | 0.218 | 0.0805 | 0.00685 | Wald ratio | 1 | cis | NA |
| ER-positive Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0659 | 0.0247 | 0.00756 | Wald ratio | 1 | cis | NA |
| ER-negative Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0967 | 0.0376 | 0.0102 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: iron deficiency anaemia | 0.213 | 0.0905 | 0.0184 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | -0.0182 | 0.0081 | 0.0243 | Wald ratio | 1 | cis | NA |
| Diastolic blood pressure  automated reading | -0.0186 | 0.00829 | 0.0251 | Wald ratio | 1 | cis | NA |
| Amyotrophic lateral sclerosis | 0.129 | 0.0591 | 0.0292 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | -0.0222 | 0.0105 | 0.0344 | Wald ratio | 1 | cis | NA |
| _...and 70 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_No GWAS Catalog associations mapped to this gene._

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 78 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| bilateral striopallidodentate calcinosis | 0.925 | — | established (curated) | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.767 | — | common-variant locus | no MR -> candidate analysis |
| Basal ganglia calcification | 0.438 | — | established (curated) | no MR -> candidate analysis |
| hereditary disease | 0.243 | — | established (curated) | no MR -> candidate analysis |
| Dysarthria | 0.195 | — | established (curated) | no MR -> candidate analysis |
| osteoarthritis, knee | 0.195 | — | common-variant locus | no MR -> candidate analysis |
| total joint arthroplasty | 0.195 | — | common-variant locus | no MR -> candidate analysis |
| osteoarthritis, hip | 0.195 | — | common-variant locus | no MR -> candidate analysis |
| type 2 diabetes mellitus | 0.073 | — | common-variant locus | no MR -> candidate analysis |
| diabetes mellitus | 0.054 | — | common-variant locus | no MR -> candidate analysis |
| metabolic syndrome | 0.047 | — | common-variant locus | no MR -> candidate analysis |

> Of the 11 rows above, **11 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | not available |
| GWAS Catalog | no mapped SNPs |
| ClinVar | no records |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 78 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'KIAA1161'.
- **`gnomad`** — No gnomAD constraint data.
- **`gwas`** — No GWAS Catalog SNPs mapped to this gene.
- **`clinvar`** — No ClinVar records.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — No GWAS Catalog associations mapped to this gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q6NSJ0 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000164976/associations — _Open Targets data release 26.06_

## Provenance

- Generated: 2026-08-14T03:21:11  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
