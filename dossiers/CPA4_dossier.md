# Protein Dossier — CPA4 (Carboxypeptidase A4)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diastolic blood pressure  automated reading | 0.00842 | 0.00218 | 1.09e-04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | 0.0112 | 0.00358 | 0.00174 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | 0.00654 | 0.00212 | 0.00208 | Wald ratio | 1 | cis | NA |
| Systolic blood pressure  automated reading | 0.00639 | 0.00217 | 0.00329 | Wald ratio | 1 | cis | NA |
| Neo-openness to experience | 0.181 | 0.0617 | 0.00335 | Wald ratio | 1 | cis | NA |
| Schizophrenia | 0.0261 | 0.00935 | 0.00529 | Wald ratio | 1 | cis | NA |
| Cigarettes smoked per day | 0.202 | 0.0733 | 0.00572 | Wald ratio | 1 | cis | NA |
| Platelet count | 0.934 | 0.35 | 0.00761 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hiatus hernia | 0.0344 | 0.0135 | 0.0106 | Wald ratio | 1 | cis | NA |
| Urate | -0.012 | 0.0048 | 0.0124 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K40 Inguinal hernia | 0.0304 | 0.0126 | 0.0159 | Wald ratio | 1 | cis | NA |
| Creatinine (enzymatic) in urine | 0.00482 | 0.00203 | 0.0178 | Wald ratio | 1 | cis | NA |
| _...and 106 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_29 association rows across 18 traits (25 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Carboxypeptidase A4 levels | 2e-3800 | rs34587586 | 2 | GCST90246874 | no MR -> candidate analysis |
| Carboxypeptidase A4 levels (CPA4.9267.2.3) | 4e-1248 | rs34587586 | 2 | GCST90240596 | no MR -> candidate analysis |
| Blood protein levels | 4e-332 | rs729167 | 1 | GCST006585 | no MR -> candidate analysis |
| CPA4 protein levels | 2e-296 | rs145012020 | 9 | GCST90468838 | no MR -> candidate analysis |
| Carboxypeptidase A4 level in Chronic kidney disease with hyp | 2e-161 | rs34587586 | 1 | GCST90239281 | no MR -> candidate analysis |
| Cerebrospinal fluid protein CPA4 levels | 5e-59 | rs73146784 | 1 | GCST90944211 | no MR -> candidate analysis |
| Sclerostin protein levels (SomaScan ID:9267-2) | 3e-44 | rs34587586 | 1 | GCST90444071 | no MR -> candidate analysis |
| CPA2 protein levels | 2e-37 | rs55811503 | 2 | GCST90468837 | no MR -> candidate analysis |
| Rheumatoid arthritis | 6e-12 | rs2306848 | 1 | GCST007843 | no MR -> candidate analysis |
| Height | 6e-12 | rs6467297 | 1 | GCST90245848 | no MR -> candidate analysis |
| Hip index | 3e-11 | rs7787960 | 1 | GCST90020026 | no MR -> candidate analysis |
| A body shape index | 2e-9 | rs7797371 | 1 | GCST90020024 | no MR -> candidate analysis |
| _...and 6 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 98 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| rheumatoid arthritis | 0.264 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.051 | — | common-variant locus | no MR -> candidate analysis |
| type 2 diabetes mellitus | 0.042 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Carboxypeptidase A4) |
| gnomAD constraint | pLI=1.7e-15, LOEUF=1.14 — LoF-tolerant |
| GWAS Catalog | 91 unique SNPs / 182 rows |
| ClinVar | 103 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 98 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'CPA4' and resolved to 'Carboxypeptidase A4' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 103 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 18 of 18 traits by best p-value, aggregated from 29 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9UI42 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000128510/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2644/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CPA4 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CPA4 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CPA4%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CPA4 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:59:26  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
