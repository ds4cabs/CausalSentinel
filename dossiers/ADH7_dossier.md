# Protein Dossier — ADH7 (All-trans-retinol dehydrogenase [NAD(+)] ADH7)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Alcohol intake frequency | -0.0509 | 0.0151 | 7.38e-04 | Wald ratio | 1 | cis | NA |
| Age at menopause | -0.224 | 0.0748 | 0.0027 | Wald ratio | 1 | cis | NA |
| Lung cancer | 0.164 | 0.0649 | 0.0116 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: gout | -0.293 | 0.116 | 0.012 | Wald ratio | 1 | cis | NA |
| Lung adenocarcinoma | 0.237 | 0.0964 | 0.0139 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: D25 Leiomyoma of uterus | 0.181 | 0.0756 | 0.0166 | Wald ratio | 1 | cis | NA |
| Caudate volume | -48.2 | 20.1 | 0.0166 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Injury or trauma resulting in loss of vision | 0.244 | 0.106 | 0.0212 | Wald ratio | 1 | cis | NA |
| Haemoglobin concentration | -0.0581 | 0.0254 | 0.0224 | Wald ratio | 1 | cis | NA |
| Urate | -0.0474 | 0.0212 | 0.0254 | Wald ratio | 1 | cis | NA |
| Mean cell haemoglobin concentration | -0.0327 | 0.0152 | 0.0318 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: J33 Nasal polyp | 0.247 | 0.118 | 0.0356 | Wald ratio | 1 | cis | NA |
| _...and 83 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_72 association rows across 44 traits (50 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Drinks per week | 5e-156 | rs4699743 | 8 | GCST90243984 | no MR -> candidate analysis |
| Alcohol dehydrogenase class 4 mu/sigma chain levels | 2e-98 | rs146315698 | 1 | GCST90246437 | no MR -> candidate analysis |
| Serum levels of protein ADH7 | 4e-24 | rs17589306 | 1 | GCST90086716 | no MR -> candidate analysis |
| Alcohol consumption (drinks per week) | 2e-22 | rs2165670 | 4 | GCST007461 | no MR -> candidate analysis |
| Protein quantitative trait loci (liver) | 2e-21 | rs1442493 | 6 | GCST011427 | no MR -> candidate analysis |
| Apolipoprotein A1 levels | 7e-20 | rs1583974 | 1 | GCST010241 | no MR -> candidate analysis |
| Bitter alcoholic beverage consumption | 3e-17 | rs62305780 | 2 | GCST008522 | no MR -> candidate analysis |
| Blood protein levels | 8e-17 | rs17529509 | 1 | GCST006585 | no MR -> candidate analysis |
| Oral cavity and pharyngeal cancer | 9e-17 | rs971074 | 1 | GCST001011 | no MR -> candidate analysis |
| Hemoglobin levels | 3e-15 | rs58382379 | 1 | GCST90662903 | no MR -> candidate analysis |
| Serum total protein levels | 5e-15 | rs200191165 | 1 | GCST90018976 | no MR -> candidate analysis |
| Substance use disorder | 6e-14 | rs58992395 | 3 | GCST90704949 | no MR -> candidate analysis |
| _...and 32 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 208 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| carcinoma of esophagus | 0.559 | — | common-variant locus | no MR -> candidate analysis |
| spondylolisthesis | 0.411 | — | common-variant locus | no MR -> candidate analysis |
| ovarian neoplasm | 0.411 | — | common-variant locus | no MR -> candidate analysis |
| high altitude adaptation | 0.357 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (All-trans-retinol dehydrogenase [NAD(+)] ADH7) |
| gnomAD constraint | pLI=1.1e-16, LOEUF=1.55 — LoF-tolerant |
| GWAS Catalog | 111 unique SNPs / 284 rows |
| ClinVar | 103 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 1 clinical annotations across 1 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 208 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'ADH7' and resolved to 'All-trans-retinol dehydrogenase [NAD(+)] ADH7' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 103 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 20 of 44 traits by best p-value, aggregated from 72 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P40394 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000196344/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3867/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/ADH7 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/ADH7 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=ADH7%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=ADH7 — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/ADH7 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T00:55:52  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
