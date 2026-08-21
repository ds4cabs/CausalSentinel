# Protein Dossier — PIR (Pirin)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | 0.104 | 0.0412 | 0.0116 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: gout | -0.0823 | 0.035 | 0.0187 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: pernicious anaemia | 0.143 | 0.0616 | 0.0206 | Wald ratio | 1 | trans | NA |
| Body fat | 0.0192 | 0.00856 | 0.0253 | Wald ratio | 1 | trans | NA |
| Hirschsprung's disease | 0.453 | 0.233 | 0.0523 | Wald ratio | 1 | trans | NA |
| Neo-neuroticism | -0.289 | 0.149 | 0.0527 | Wald ratio | 1 | trans | NA |
| Neo-agreeableness | 0.186 | 0.0961 | 0.0528 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: bladder problem (not cancer) | -0.106 | 0.0562 | 0.0583 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: hypertension | -0.0121 | 0.00663 | 0.0678 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: Z09 Follow-up examination after treatment for conditions other than malignant neoplasms | 0.0536 | 0.0296 | 0.0703 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: G47 Sleep disorders | -0.1 | 0.0555 | 0.0713 | Wald ratio | 1 | trans | NA |
| Lung cancer | -0.053 | 0.0296 | 0.0735 | Wald ratio | 1 | trans | NA |
| _...and 98 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_14 association rows across 6 traits (13 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating VEGFD levels (id: OID00468_OID20662) | 9e-2227 | rs192812042 | 1 | GCST90859829 | no MR -> candidate analysis |
| Circulating VEGFD levels (id: OID01319_OID20662) | 2e-2062 | rs192812042 | 1 | GCST90860514 | no MR -> candidate analysis |
| Pirin levels | 5e-865 | rs925653 | 1 | GCST90249006 | no MR -> candidate analysis |
| vascular endothelial growth factor D levels | 1e-244 | rs192812042 | 6 | GCST90250162 | no MR -> candidate analysis |
| Serum levels of protein VEGFD | 2e-122 | rs192812042 | 4 | GCST90087372 | no MR -> candidate analysis |
| ACE2 levels | 9e-9 | rs143380244 | 1 | GCST90128424 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 250 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| COVID-19 | 0.534 | — | common-variant locus | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Pirin) |
| gnomAD constraint | pLI=1.2e-07, LOEUF=1.3 — LoF-tolerant |
| GWAS Catalog | 16 unique SNPs / 32 rows |
| ClinVar | 223 records; 8 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 250 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'PIR' and resolved to 'Pirin' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 223 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 6 of 6 traits by best p-value, aggregated from 14 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O00625 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000087842/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2010627/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PIR — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PIR — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PIR%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PIR — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:21:38  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: pharmgkb
