# Protein Dossier — B4GALT6 (Beta-1,4-galactosyltransferase 6)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Pallidum volume | 14.3 | 4.21 | 6.98e-04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: bladder problem (not cancer) | 0.15 | 0.0594 | 0.0116 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Cataract | 0.0658 | 0.0267 | 0.0138 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: D25 Leiomyoma of uterus | -0.12 | 0.0523 | 0.0216 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M23 Internal derangement of knee | 0.0724 | 0.0328 | 0.0274 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: S66 Injury of muscle and tendon at wrist and hand level | 0.228 | 0.106 | 0.0316 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R11 Nausea and vomiting | 0.149 | 0.0723 | 0.0397 | Wald ratio | 1 | cis | NA |
| Alcohol intake frequency | 0.0159 | 0.00775 | 0.0407 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: deep venous thrombosis (dvt) | 0.0682 | 0.0347 | 0.0495 | Wald ratio | 1 | cis | NA |
| Myocardial infarction | -0.0532 | 0.0277 | 0.0551 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: B37 Candidiasis | 0.347 | 0.184 | 0.0594 | Wald ratio | 1 | cis | NA |
| High grade serous ovarian cancer | -0.0636 | 0.0355 | 0.0734 | Wald ratio | 1 | cis | NA |
| _...and 57 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_20 association rows across 17 traits (13 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Beta-1,4-galactosyltransferase 6 levels | 9e-231 | rs113222817 | 2 | GCST90246641 | no MR -> candidate analysis |
| Serum levels of protein B4GALT6 | 1e-132 | rs113222817 | 1 | GCST90086466 | no MR -> candidate analysis |
| TRAIL levels | 7e-82 | rs62093514 | 1 | GCST004424 | no MR -> candidate analysis |
| Beta-1,4-galactosyltransferase 6 levels (B4GALT6.10832.24.3) | 2e-77 | rs201022770 | 2 | GCST90240404 | no MR -> candidate analysis |
| Blood protein levels | 8e-71 | rs113222817 | 1 | GCST006585 | no MR -> candidate analysis |
| Thyroxine levels | 4e-30 | rs184097503 | 2 | GCST90572790 | no MR -> candidate analysis |
| DSG2 protein levels | 3e-20 | rs71372020 | 1 | GCST90469042 | no MR -> candidate analysis |
| DSG3 protein levels | 1e-14 | rs183636416 | 1 | GCST90469043 | no MR -> candidate analysis |
| Retinol levels | 6e-14 | rs1667255 | 1 | GCST001216 | no MR -> candidate analysis |
| Height | 3e-8 | rs1667284 | 1 | GCST90245846 | no MR -> candidate analysis |
| Depression severity  x playing computer games interaction | 5e-8 | rs113081283 | 1 | GCST90101758 | no MR -> candidate analysis |
| Fasting insulin adjusted for BMI | 8e-8 | rs6506934 | 1 | GCST90503331 | no MR -> candidate analysis |
| _...and 5 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 69 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| osteoarthritis | 0.13 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of the immune system | 0.081 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.99, LOEUF=0.473 — LoF-INTOLERANT |
| GWAS Catalog | 37 unique SNPs / 71 rows |
| ClinVar | 100 records; 4 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 69 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'B4GALT6'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 100 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 17 of 17 traits by best p-value, aggregated from 20 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9UBX8 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000118276/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/B4GALT6 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/B4GALT6 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=B4GALT6%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/B4GALT6 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:15:39  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
