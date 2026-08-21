# Protein Dossier — ALDH3A1 (Aldehyde dehydrogenase, dimeric NADP-preferring)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Lung adenocarcinoma | -0.367 | 0.13 | 0.00469 | Wald ratio | 1 | cis | NA |
| Ferritin | 0.105 | 0.0405 | 0.00955 | Wald ratio | 1 | cis | NA |
| Pallidum volume | 20.8 | 8.2 | 0.011 | Wald ratio | 1 | cis | NA |
| Caudate volume | 52.6 | 21 | 0.0121 | Wald ratio | 1 | cis | NA |
| Lung cancer | -0.2 | 0.0814 | 0.014 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: gout | -0.283 | 0.119 | 0.017 | Wald ratio | 1 | cis | NA |
| Fracture resulting from simple fall | 0.0618 | 0.026 | 0.0175 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | 0.229 | 0.1 | 0.0228 | Wald ratio | 1 | cis | NA |
| Squamous cell lung cancer | -0.28 | 0.127 | 0.0277 | Wald ratio | 1 | cis | NA |
| Alcohol intake frequency | -0.0333 | 0.0155 | 0.0317 | Wald ratio | 1 | cis | NA |
| Cough on most days | -0.13 | 0.0613 | 0.0337 | Wald ratio | 1 | cis | NA |
| Iron | 0.09 | 0.043 | 0.0361 | Wald ratio | 1 | cis | NA |
| _...and 98 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_24 association rows across 16 traits (23 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating ALDH3A1 levels | 2e-1229 | rs11204414 | 1 | GCST90860258 | no MR -> candidate analysis |
| ALDH3A1 protein levels | 9e-307 | rs12938201 | 6 | GCST90468282 | no MR -> candidate analysis |
| Aldehyde dehydrogenase, dimeric NADP-preferring levels | 6e-41 | rs887241 | 2 | GCST90246481 | no MR -> candidate analysis |
| Serum levels of protein ALDH3A1 | 2e-23 | rs2108967 | 1 | GCST90086764 | no MR -> candidate analysis |
| Aldehyde dehydrogenase, dimeric NADP-preferring levels (ALDH | 8e-21 | rs887241 | 1 | GCST90240225 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 2e-19 | rs12938201 | 1 | GCST90838669 | no MR -> candidate analysis |
| Cerebrospinal fluid protein ALDH3A1 levels | 1e-16 | rs4646787 | 1 | GCST90943022 | no MR -> candidate analysis |
| Blood protein levels | 1e-13 | rs2108967 | 1 | GCST006585 | no MR -> candidate analysis |
| Corneal resistance factor (MTAG) | 2e-12 | rs4646785 | 1 | GCST90102517 | no MR -> candidate analysis |
| Keratoconus | 9e-12 | rs4646785 | 1 | GCST90013442 | no MR -> candidate analysis |
| Corneal resistance factor | 2e-10 | rs12939864 | 2 | GCST90100568 | no MR -> candidate analysis |
| Intraocular pressure | 5e-10 | rs2072327 | 2 | GCST005580 | no MR -> candidate analysis |
| _...and 4 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 195 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| keratoconus | 0.485 | — | established (curated) | no MR -> candidate analysis |
| blood coagulation disease | 0.082 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Aldehyde dehydrogenase, dimeric NADP-preferring) |
| gnomAD constraint | pLI=5.2e-15, LOEUF=1.18 — LoF-tolerant |
| GWAS Catalog | 35 unique SNPs / 70 rows |
| ClinVar | 172 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 1 clinical annotations across 3 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 195 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'ALDH3A1' and resolved to 'Aldehyde dehydrogenase, dimeric NADP-preferring' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 172 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 16 of 16 traits by best p-value, aggregated from 24 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P30838 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000108602/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3578/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/ALDH3A1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/ALDH3A1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=ALDH3A1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=ALDH3A1 — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/ALDH3A1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:01:17  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
