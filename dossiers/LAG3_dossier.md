# Protein Dossier — LAG3 (Lymphocyte activation gene 3 protein)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Eye problems or disorders: Injury or trauma resulting in loss of vision | 0.541 | 0.126 | 1.83e-05 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K80 Cholelithiasis | 0.301 | 0.0848 | 3.80e-04 | Wald ratio | 1 | cis | NA |
| Cigarettes smoked per day | -2.25 | 0.642 | 4.54e-04 | Wald ratio | 1 | cis | NA |
| Transferrin | 0.206 | 0.0695 | 0.00305 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: malignant melanoma | 0.35 | 0.133 | 0.00868 | Wald ratio | 1 | cis | NA |
| Femoral neck bone mineral density | -0.136 | 0.0548 | 0.0132 | Wald ratio | 1 | cis | NA |
| Thalamus volume | 100 | 41.2 | 0.0151 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M16 Coxarthrosis [arthrosis of hip] | 0.256 | 0.107 | 0.0161 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hayfever or allergic rhinitis | 0.138 | 0.0587 | 0.0184 | Wald ratio | 1 | cis | NA |
| Eczema | 0.241 | 0.115 | 0.0359 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: gout | 0.23 | 0.11 | 0.037 | Wald ratio | 1 | cis | NA |
| Pallidum volume | 25.5 | 12.7 | 0.0451 | Wald ratio | 1 | cis | NA |
| _...and 73 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5099_14_3` | LAG-3 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_38 association rows across 21 traits (37 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating LAG3 levels (id: OID01023_OID21315) | 4e-160 | rs3782735 | 4 | GCST90860248 | no MR -> candidate analysis |
| LAG3 protein levels | 8e-160 | rs3782735 | 3 | GCST90469727 | no MR -> candidate analysis |
| Circulating LAG3 levels (id: OID05553_OID21315) | 9e-159 | rs3782735 | 4 | GCST90860765 | no MR -> candidate analysis |
| Circulating CD4 levels (id: OID00466_OID20584) | 2e-50 | rs188343194 | 1 | GCST90859827 | no MR -> candidate analysis |
| Circulating CD4 levels (id: OID00776_OID20584) | 2e-47 | rs188343194 | 1 | GCST90860110 | no MR -> candidate analysis |
| Lymphocyte activation gene 3 protein levels | 9e-32 | rs3782735 | 1 | GCST90248233 | no MR -> candidate analysis |
| Sex hormone-binding globulin levels adjusted for BMI | 1e-21 | rs3782735 | 3 | GCST90012110 | no MR -> candidate analysis |
| Sex hormone-binding globulin levels | 3e-18 | rs3782735 | 7 | GCST90012111 | no MR -> candidate analysis |
| Phospholipids to Total Lipids in Very Large HDL percentage | 1e-16 | rs3782735 | 1 | GCST90501303 | no MR -> candidate analysis |
| Gamma glutamyl transferase levels | 2e-16 | rs3782735 | 1 | GCST90428730 | no MR -> candidate analysis |
| Gamma glutamyl transpeptidase | 6e-16 | rs3782735 | 1 | GCST90018954 | no MR -> candidate analysis |
| Gamma glutamyltransferase levels (UKB data field 30730) | 8e-16 | rs3782735 | 1 | GCST90468070 | no MR -> candidate analysis |
| _...and 9 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 675 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Hashimoto thyroiditis | 0.198 | — | common-variant locus | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 6 known modulators (Lymphocyte activation gene 3 protein) |
| gnomAD constraint | pLI=7.5e-06, LOEUF=0.807 — LoF-tolerant |
| GWAS Catalog | 74 unique SNPs / 148 rows |
| ClinVar | 177 records; 5 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 675 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'LAG3' and resolved to 'Lymphocyte activation gene 3 protein' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 177 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 21 traits by best p-value, aggregated from 38 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P18627 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000089692/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4630881/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/LAG3 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/LAG3 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=LAG3%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/LAG3 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:27:05  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
