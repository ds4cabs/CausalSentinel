# Protein Dossier — C5 (Complement C5)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: C50 Malignant neoplasm of breast | 0.303 | 0.079 | 1.27e-04 | Wald ratio | 1 | cis | NA |
| Systolic blood pressure  automated reading | -0.0419 | 0.0139 | 0.00254 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: B37 Candidiasis | 0.882 | 0.297 | 0.00298 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Other bones | 0.138 | 0.0516 | 0.00745 | Wald ratio | 1 | cis | NA |
| Sodium in urine | 0.0352 | 0.0134 | 0.00832 | Wald ratio | 1 | cis | NA |
| Underlying (primary) cause of death: ICD10: E85.4 Organ-limited amyloidosis | 1.89 | 0.722 | 0.0087 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | 0.135 | 0.0529 | 0.0108 | Wald ratio | 1 | cis | NA |
| Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0896 | 0.0352 | 0.0109 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: pernicious anaemia | 0.424 | 0.169 | 0.0123 | Wald ratio | 1 | cis | NA |
| ER-positive Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.102 | 0.0418 | 0.0144 | Wald ratio | 1 | cis | NA |
| Fracture resulting from simple fall | -0.0916 | 0.0394 | 0.0199 | Wald ratio | 1 | cis | NA |
| Birth weight | 0.0473 | 0.0203 | 0.0201 | Wald ratio | 1 | cis | NA |
| _...and 94 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2381_52_4` | C5 | Suhre K | 2019 |
| `prot-c-2851_63_3` | C5a | Suhre K | 2019 |
| `prot-c-4482_66_2` | C5b, 6 Complex | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_40 association rows across 27 traits (32 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Complement C5 levels | 1e-74 | rs41309886 | 5 | GCST90246786 | no MR -> candidate analysis |
| Complement C5b-C6 complex levels | 9e-71 | rs41309886 | 4 | GCST90246789 | no MR -> candidate analysis |
| C5a anaphylatoxin levels | 8e-32 | rs17220750 | 2 | GCST90246788 | no MR -> candidate analysis |
| GSN protein levels | 3e-18 | rs117952610 | 1 | GCST90469409 | no MR -> candidate analysis |
| Height (baseline) | 3e-17 | rs76481162 | 1 | GCST90565843 | no MR -> candidate analysis |
| Height | 2e-15 | rs12685289 | 2 | GCST90435412 | MR: beta=0.0203, p=0.217 (cis) |
| Serum levels of protein C5 | 2e-15 | rs1035029 | 2 | GCST90087935 | no MR -> candidate analysis |
| Elevated prostate specific antigen [PSA] (PheCode 796) | 5e-15 | rs7045519 | 1 | GCST90480590 | no MR -> candidate analysis |
| Blood protein levels | 2e-13 | rs1035029 | 1 | GCST006585 | no MR -> candidate analysis |
| Estimated glomerular filtration rate (cystatin c) | 5e-13 | rs141350020 | 1 | GCST90428448 | no MR -> candidate analysis |
| Rheumatoid arthritis (rheumatoid factor and/or anti-cyclic c | 6e-13 | rs35942002 | 1 | GCST90131438 | no MR -> candidate analysis |
| Hypothyroidism | 6e-13 | rs10739580 | 1 | GCST90627750 | MR: beta=0.135, p=0.0108 (cis) |
| _...and 15 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 814 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Immunodeficiency due to a late component of complements deficiency | 0.841 | — | established (curated) | no MR -> candidate analysis |
| immunodeficiency due to a late component of complement deficiency | 0.608 | — | established (curated) | no MR -> candidate analysis |
| lathosterolosis | 0.559 | — | established (curated) | no MR -> candidate analysis |
| alcohol drinking | 0.514 | — | common-variant locus | no MR -> candidate analysis |
| coronary artery disorder | 0.48 | — | common-variant locus | no MR -> candidate analysis |
| peripheral vascular disease | 0.403 | — | common-variant locus | no MR -> candidate analysis |
| urolithiasis | 0.403 | — | common-variant locus | no MR -> candidate analysis |

> Of the 7 rows above, **7 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=3.4e-28, LOEUF=0.736 — LoF-tolerant |
| GWAS Catalog | 89 unique SNPs / 175 rows |
| ClinVar | 951 records; 8 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 1 clinical annotations across 1 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 814 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 951 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 20 of 27 traits by best p-value, aggregated from 40 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P01031 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000106804/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/C5 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/C5 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=C5%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=C5 — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/C5 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:22:40  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: chembl
