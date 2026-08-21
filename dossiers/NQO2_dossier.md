# Protein Dossier — NQO2 (Ribosyldihydronicotinamide dehydrogenase [quinone])

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Amygdala volume | -12.3 | 6.28 | 0.0511 | Wald ratio | 1 | cis | NA |
| Eczema | -0.0809 | 0.0448 | 0.071 | Wald ratio | 1 | cis | NA |
| Schizophrenia | 0.0471 | 0.0274 | 0.085 | Wald ratio | 1 | cis | NA |
| Thalamus volume | -23 | 16.6 | 0.166 | Wald ratio | 1 | cis | NA |
| Pallidum volume | -5.77 | 5.11 | 0.259 | Wald ratio | 1 | cis | NA |
| Low grade serous ovarian cancer | 0.138 | 0.123 | 0.26 | Wald ratio | 1 | cis | NA |
| Femoral neck bone mineral density | -0.041 | 0.0384 | 0.286 | Wald ratio | 1 | cis | NA |
| ER-positive Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.0202 | 0.0191 | 0.289 | Wald ratio | 1 | cis | NA |
| ER-negative Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0303 | 0.029 | 0.295 | Wald ratio | 1 | cis | NA |
| Lung cancer | 0.0469 | 0.0464 | 0.312 | Wald ratio | 1 | cis | NA |
| Lung adenocarcinoma | 0.0714 | 0.071 | 0.315 | Wald ratio | 1 | cis | NA |
| Intracranial volume | 4.65e+03 | 5.07e+03 | 0.359 | Wald ratio | 1 | cis | NA |
| _...and 5 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_29 association rows across 13 traits (27 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Ribosyldihydronicotinamide dehydrogenase [quinone] levels | 5e-803 | rs138616686 | 5 | GCST90249391 | no MR -> candidate analysis |
| Ribosyldihydronicotinamide dehydrogenase [quinone] levels (N | 5e-181 | rs138616686 | 4 | GCST90242679 | no MR -> candidate analysis |
| Urine isoxanthopterin levels in chronic kidney disease | 1e-161 | rs6913474 | 1 | GCST90265420 | no MR -> candidate analysis |
| Serum levels of protein NQO2 | 2e-119 | rs6913474 | 3 | GCST90090801 | no MR -> candidate analysis |
| Urinary metabolite levels in chronic kidney disease | 3e-88 | rs6913474 | 2 | GCST009733 | no MR -> candidate analysis |
| Urine pterin levels in chronic kidney disease | 6e-76 | rs6913474 | 1 | GCST90265884 | no MR -> candidate analysis |
| Blood protein levels | 4e-64 | rs138616686 | 1 | GCST006585 | no MR -> candidate analysis |
| Metabolite levels (pterin) | 1e-36 | rs12200513 | 2 | GCST90301166 | no MR -> candidate analysis |
| S-arrestin levels | 2e-32 | rs2756078 | 1 | GCST90425311 | no MR -> candidate analysis |
| Protein quantitative trait loci (liver) | 2e-25 | rs3823096 | 6 | GCST011427 | no MR -> candidate analysis |
| Prenylcysteine oxidase-like protein levels (SomaScan ID:9754 | 9e-15 | rs4149358 | 1 | GCST90443407 | no MR -> candidate analysis |
| Early-onset Alzheimer's disease | 2e-6 | rs1963159 | 1 | GCST90558102 | no MR -> candidate analysis |
| _...and 1 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 191 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| intermediate coronary syndrome | 0.234 | — | common-variant locus | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Ribosyldihydronicotinamide dehydrogenase [quinone]) |
| gnomAD constraint | pLI=6.5e-06, LOEUF=1.21 — LoF-tolerant |
| GWAS Catalog | 59 unique SNPs / 115 rows |
| ClinVar | 106 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 1 clinical annotations across 2 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 191 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'NQO2' and resolved to 'Ribosyldihydronicotinamide dehydrogenase [quinone]' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 106 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 13 of 13 traits by best p-value, aggregated from 29 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P16083 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000124588/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3959/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/NQO2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/NQO2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=NQO2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=NQO2 — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/NQO2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:03:52  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
