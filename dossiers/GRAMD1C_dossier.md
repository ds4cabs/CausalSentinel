# Protein Dossier — GRAMD1C (Protein Aster-C)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Fractured bone site(s): Ankle | -0.154 | 0.041 | 1.74e-04 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | 0.0122 | 0.00411 | 0.00294 | Wald ratio | 1 | cis | NA |
| Weight | 0.0107 | 0.00363 | 0.00305 | Wald ratio | 1 | cis | NA |
| Ovarian cancer | -0.0614 | 0.0234 | 0.00879 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C50 Malignant neoplasm of breast | 0.0701 | 0.03 | 0.0193 | Wald ratio | 1 | cis | NA |
| Years of schooling | -0.0145 | 0.00645 | 0.0244 | Wald ratio | 1 | cis | NA |
| HbA1C | 0.0134 | 0.00597 | 0.0249 | Wald ratio | 1 | cis | NA |
| Lumbar spine bone mineral density | 0.0343 | 0.0154 | 0.0259 | Wald ratio | 1 | cis | NA |
| Fractured or broken bones in last 5 years | -0.0292 | 0.0132 | 0.0266 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hiatus hernia | 0.055 | 0.0255 | 0.0311 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R11 Nausea and vomiting | -0.166 | 0.0777 | 0.0329 | Wald ratio | 1 | cis | NA |
| Happiness | 0.0106 | 0.0051 | 0.0367 | Wald ratio | 1 | cis | NA |
| _...and 81 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_21 association rows across 11 traits (15 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| GRAM domain-containing protein 1C levels | 3e-338 | rs1872823 | 4 | GCST90247815 | no MR -> candidate analysis |
| Serum levels of protein GRAMD1C | 1e-262 | rs61634901 | 4 | GCST90090335 | no MR -> candidate analysis |
| GRAM domain-containing protein 1C levels (GRAMD1C.8842.16.3) | 3e-148 | rs61077924 | 4 | GCST90241314 | no MR -> candidate analysis |
| Blood protein levels | 4e-133 | rs4422272 | 1 | GCST006585 | no MR -> candidate analysis |
| CD200R1 protein levels | 5e-45 | rs564438696 | 2 | GCST90468605 | no MR -> candidate analysis |
| 3-hydroxypropylmercapturic acid levels in smokers | 8e-8 | rs114780919 | 1 | GCST002956 | no MR -> candidate analysis |
| Urinary uromodulin levels (raw) | 1e-6 | rs139248026 | 1 | GCST90103502 | no MR -> candidate analysis |
| Lateral ventricle temporal horn volume | 3e-6 | rs73230239 | 1 | GCST009218 | no MR -> candidate analysis |
| Stuttering | 5e-6 | rs145711937 | 1 | GCST90707223 | no MR -> candidate analysis |
| 5-HETrE levels in elite athletes | 7e-6 | rs6438172 | 1 | GCST90133836 | no MR -> candidate analysis |
| Prospective and Retrospective Memory Questionnaire (PRMQ) Re | 7e-6 | rs6798319 | 1 | GCST90448158 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 337 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| gastritis | 0.393 | — | common-variant locus | MR: beta=-0.0187, p=0.491 (cis) |
| myocardial ischemia | 0.324 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Protein Aster-C) |
| gnomAD constraint | pLI=8.7e-28, LOEUF=1.09 — LoF-tolerant |
| GWAS Catalog | 23 unique SNPs / 46 rows |
| ClinVar | 134 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 337 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'GRAMD1C' and resolved to 'Protein Aster-C' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 134 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 11 of 11 traits by best p-value, aggregated from 21 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q8IYS0 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000178075/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL6067584/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/GRAMD1C — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/GRAMD1C — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=GRAMD1C%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/GRAMD1C — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:54:00  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
