# Protein Dossier — VTN (Vitronectin)

**MR feasibility tier: C** — No plasma pQTL found (accession + symbol match). Standard plasma pQTL MR is not currently feasible; gene-level genetic evidence below is the honest preview.

## 1. Published MR estimates (retrieved, not computed)

_None in the EpiGraphDB pQTL resource. Absence of an estimate is not evidence of no effect._

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_2142 association rows across 1478 traits (2134 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Vitronectin levels | 4e-6996 | rs704 | 2 | GCST90250177 | no MR -> candidate analysis |
| MICOS complex subunit MIC10 levels | 4e-5900 | rs704 | 1 | GCST90248470 | no MR -> candidate analysis |
| MAP kinase-activated protein kinase 5 levels | 8e-3943 | rs704 | 1 | GCST90248480 | no MR -> candidate analysis |
| Transmembrane protease serine 6 levels | 7e-3426 | rs704 | 1 | GCST90249925 | no MR -> candidate analysis |
| Methyl-CpG-binding domain protein 1 levels | 8e-2008 | rs704 | 1 | GCST90248454 | no MR -> candidate analysis |
| MICOS complex subunit MIC10 levels (MINOS1.7956.11.3) | 1e-1442 | rs704 | 1 | GCST90241930 | no MR -> candidate analysis |
| Blood protein levels | 9e-1306 | rs704 | 589 | GCST006585 | no MR -> candidate analysis |
| Vitronectin (analyte X13125.45) levels | 5e-987 | rs704 | 1 | GCST90422096 | no MR -> candidate analysis |
| Carboxypeptidase N subunit 2 levels | 2e-846 | rs704 | 2 | GCST90246881 | no MR -> candidate analysis |
| Inactive peptidyl-prolyl cis-trans isomerase FKBP6 levels (F | 2e-836 | rs704 | 1 | GCST90241487 | no MR -> candidate analysis |
| Vitronectin levels (VTN.8280.238.3) | 8e-770 | rs704 | 1 | GCST90243346 | no MR -> candidate analysis |
| GTP-binding protein GEM levels | 2e-688 | rs704 | 1 | GCST90247828 | no MR -> candidate analysis |
| _...and 1466 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 722 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| hypertensive disorder | 0.715 | — | common-variant locus | no MR -> candidate analysis |
| temporal arteritis | 0.572 | — | common-variant locus | no MR -> candidate analysis |
| age-related macular degeneration | 0.426 | — | common-variant locus | no MR -> candidate analysis |
| ventricular septal defect | 0.451 | — | common-variant locus | no MR -> candidate analysis |
| COVID-19 | 0.408 | — | common-variant locus | no MR -> candidate analysis |
| wet macular degeneration | 0.3 | — | common-variant locus | no MR -> candidate analysis |
| atrophic macular degeneration | 0.3 | — | common-variant locus | no MR -> candidate analysis |

> Of the 7 rows above, **7 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Vitronectin) |
| gnomAD constraint | pLI=6.4e-13, LOEUF=1.03 — LoF-tolerant |
| GWAS Catalog | 76 unique SNPs / 152 rows |
| ClinVar | 120 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 722 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'VTN' and resolved to 'Vitronectin' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 120 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 1478 traits by best p-value, aggregated from 2142 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P04004 — _UniProt release 2026_02 (10-June-2026)_
- `phenome`: https://platform.opentargets.org/target/ENSG00000109072/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL1075314/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/VTN — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/VTN — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=VTN%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/VTN — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:36:19  ·  Tier: C
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: mr_outcomes
