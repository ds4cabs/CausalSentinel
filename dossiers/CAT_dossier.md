# Protein Dossier — CAT (Catalase)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: C61 Malignant neoplasm of prostate | 0.152 | 0.06 | 0.0113 | Wald ratio | 1 | cis | NA |
| Ischemic stroke | -0.0918 | 0.0374 | 0.0141 | Wald ratio | 1 | cis | NA |
| Neo-openness to experience | -0.318 | 0.162 | 0.049 | Wald ratio | 1 | cis | NA |
| Pulse rate | 0.0189 | 0.01 | 0.0589 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K35 Acute appendicitis | 0.135 | 0.0715 | 0.0592 | Wald ratio | 1 | cis | NA |
| Cardioembolic stroke | -0.139 | 0.0736 | 0.0593 | Wald ratio | 1 | cis | NA |
| Large vessel disease | -0.145 | 0.0795 | 0.068 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: arthritis (nos) | -0.136 | 0.0752 | 0.0708 | Wald ratio | 1 | cis | NA |
| Neuroticism | 0.0176 | 0.00979 | 0.0719 | Wald ratio | 1 | cis | NA |
| Years of schooling | 0.0176 | 0.00979 | 0.0719 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C50 Malignant neoplasm of breast | -0.0871 | 0.0484 | 0.0721 | Wald ratio | 1 | cis | NA |
| Hirschsprung's disease | 0.446 | 0.25 | 0.0739 | Wald ratio | 1 | cis | NA |
| _...and 87 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3488_64_2` | Catalase | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_16 association rows across 8 traits (14 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| CAT protein levels | 7e-117 | rs7113917 | 4 | GCST90468551 | no MR -> candidate analysis |
| Catalase levels | 8e-80 | rs769218 | 5 | GCST90246842 | no MR -> candidate analysis |
| Core binding factor acute myeloid leukemia | 2e-25 | rs12786782; rs10768074; rs11032686; rs7111765; rs11032695; rs16925514; rs6484720; rs12295136; rs208681; rs7944397; rs208682; rs208683; rs12807961; rs12808450; rs554518; rs1107573 | 2 | GCST008413 | no MR -> candidate analysis |
| Type 2 diabetes | 9e-25 | rs1001179 | 1 | GCST90134620 | MR: beta=0.151, p=0.294 (cis) |
| Blood protein levels | 1e-20 | rs7933285 | 1 | GCST006585 | no MR -> candidate analysis |
| Major depressive disorder or hospitalized COVID-19 (pleiotro | 3e-9 | rs7118388 | 1 | GCST90296444 | no MR -> candidate analysis |
| Eugenol sulfate levels in elite athletes | 4e-6 | rs16925614 | 1 | GCST90134213 | no MR -> candidate analysis |
| COVID-19 (hospitalized covid vs population) | 5e-6 | rs1001179 | 1 | GCST90454507 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1561 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| acatalasia | 0.75 | — | established (curated) | no MR -> candidate analysis |
| type 2 diabetes mellitus | 0.553 | — | common-variant locus | no MR -> candidate analysis |
| COVID-19 | 0.421 | — | common-variant locus | no MR -> candidate analysis |
| major depressive disorder | 0.386 | — | common-variant locus | no MR -> candidate analysis |
| narcolepsy | 0.362 | — | common-variant locus | no MR -> candidate analysis |
| Intellectual disability | 0.198 | — | established (curated) | no MR -> candidate analysis |
| vitiligo | 0.034 | — | common-variant locus | no MR -> candidate analysis |

> Of the 7 rows above, **7 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Catalase) |
| gnomAD constraint | pLI=3.8e-11, LOEUF=0.94 — LoF-tolerant |
| GWAS Catalog | 68 unique SNPs / 135 rows |
| ClinVar | 113 records; 3 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 2 clinical annotations across 2 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1561 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'CAT' and resolved to 'Catalase' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 113 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 8 of 8 traits by best p-value, aggregated from 16 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P04040 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000121691/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3627594/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CAT — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CAT — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CAT%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=CAT — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CAT — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:28:39  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
