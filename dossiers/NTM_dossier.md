# Protein Dossier — NTM (Putative uncharacterized protein NTM-AS1)

**MR feasibility tier: C** — No plasma pQTL found (accession + symbol match). Standard plasma pQTL MR is not currently feasible; gene-level genetic evidence below is the honest preview.

## 1. Published MR estimates (retrieved, not computed)

_None in the EpiGraphDB pQTL resource. Absence of an estimate is not evidence of no effect._

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_269 association rows across 168 traits (175 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Neurotrimin levels | 4e-244 | rs2511504 | 3 | GCST90248752 | no MR -> candidate analysis |
| Serum levels of protein NTM | 7e-97 | rs2511781 | 3 | GCST90090196 | no MR -> candidate analysis |
| Opioid-binding protein/cell adhesion molecule levels | 3e-71 | rs2511504 | 2 | GCST90248770 | no MR -> candidate analysis |
| Blood protein levels | 2e-58 | rs2511504 | 2 | GCST006585 | no MR -> candidate analysis |
| Refractive error | 2e-40 | rs1790165 | 3 | GCST90841196 | no MR -> candidate analysis |
| Lung function (FEV1/FVC) | 7e-28 | rs4491239 | 2 | GCST007080 | no MR -> candidate analysis |
| Smoking initiation | 2e-27 | rs617267 | 14 | GCST90243985 | no MR -> candidate analysis |
| FEV1 FVC ratio Z score (UKB data field 20258) | 7e-26 | rs7118465 | 1 | GCST90468165 | no MR -> candidate analysis |
| FEV1/FVC ratio | 1e-22 | rs10466626 | 1 | GCST90705072 | no MR -> candidate analysis |
| Chronic obstructive pulmonary disease liability (machine lea | 5e-21 | rs6590623 | 1 | GCST90244098 | no MR -> candidate analysis |
| GLIPR1 protein levels | 8e-20 | rs554309481 | 2 | GCST90469357 | no MR -> candidate analysis |
| Pre-treatment viral load in HIV-1 infection | 1e-16 | rs78430868 | 1 | GCST008758 | no MR -> candidate analysis |
| _...and 156 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 157 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| smoking initiation | 0.681 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.634 | — | common-variant locus | no MR -> candidate analysis |
| health study participation | 0.625 | — | common-variant locus | no MR -> candidate analysis |
| ovarian dysfunction | 0.605 | — | common-variant locus | no MR -> candidate analysis |
| chronic intestinal vascular insufficiency | 0.587 | — | common-variant locus | no MR -> candidate analysis |
| uterine polyp | 0.523 | — | common-variant locus | no MR -> candidate analysis |
| refractive error | 0.521 | — | common-variant locus | no MR -> candidate analysis |
| duodenitis | 0.51 | — | common-variant locus | no MR -> candidate analysis |
| mathematical ability | 0.508 | — | common-variant locus | no MR -> candidate analysis |
| placental abruption | 0.502 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.495 | — | common-variant locus | no MR -> candidate analysis |
| Hypermetropia | 0.495 | — | common-variant locus | no MR -> candidate analysis |
| response to beta blocker | 0.492 | — | common-variant locus | no MR -> candidate analysis |
| acute pancreatitis | 0.492 | — | common-variant locus | no MR -> candidate analysis |
| stroke disorder | 0.485 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **15 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.99, LOEUF=0.491 — LoF-INTOLERANT |
| GWAS Catalog | 152 unique SNPs / 389 rows |
| ClinVar | 144 records; 6 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 157 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'NTM'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 144 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 168 traits by best p-value, aggregated from 269 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q6ZSK4 — _UniProt release 2026_02 (10-June-2026)_
- `phenome`: https://platform.opentargets.org/target/ENSG00000182667/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/NTM — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/NTM — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=NTM%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/NTM — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:05:46  ·  Tier: C
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: mr_outcomes
