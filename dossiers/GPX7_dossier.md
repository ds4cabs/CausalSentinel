# Protein Dossier — GPX7 (Protein peroxidase GPX7)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: pneumothorax | 0.608 | 0.153 | 7.19e-05 | Wald ratio | 1 | cis | NA |
| Height | 0.0231 | 0.00692 | 8.58e-04 | Wald ratio | 1 | cis | NA |
| Platelet count | -2.84 | 0.947 | 0.00274 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Ankle | -0.129 | 0.0545 | 0.0181 | Wald ratio | 1 | cis | NA |
| Major depressive disorder | -0.117 | 0.0501 | 0.0194 | Wald ratio | 1 | cis | NA |
| Myocardial infarction | -0.0565 | 0.0243 | 0.0202 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | -0.0122 | 0.00559 | 0.029 | Wald ratio | 1 | cis | NA |
| Coronary heart disease | -0.0463 | 0.0219 | 0.0348 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: kidney stone or ureter stone or bladder stone | 0.106 | 0.057 | 0.0643 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: uterine fibroids | -0.0916 | 0.0496 | 0.0649 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K40 Inguinal hernia | -0.0675 | 0.0366 | 0.0652 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | 0.00831 | 0.00459 | 0.0701 | Wald ratio | 1 | cis | NA |
| _...and 98 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_11 association rows across 9 traits (10 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Glutathione peroxidase 7 levels | 1e-1129 | rs1097234 | 1 | GCST90247798 | no MR -> candidate analysis |
| Glutathione peroxidase 7 levels (GPX7.8345.27.3) | 2e-73 | rs1097234 | 2 | GCST90241280 | no MR -> candidate analysis |
| Height | 5e-72 | rs6588432 | 2 | GCST90245848 | MR: beta=0.0231, p=8.58e-04 (cis) |
| Cyclin-dependent kinase 5:Cyclin-dependent kinase 5 activato | 2e-15 | rs1097234 | 1 | GCST90442596 | no MR -> candidate analysis |
| Height (baseline) | 3e-11 | rs1970951 | 1 | GCST90565843 | no MR -> candidate analysis |
| Genetically independent pain phenotypes (GIP1) | 5e-9 | rs111368900 | 1 | GCST90245879 | no MR -> candidate analysis |
| Ascending aorta distensibility (MTAG) | 8e-9 | rs835341 | 1 | GCST90137446 | no MR -> candidate analysis |
| Body size or adipose distribution (multivariate analysis) | 1e-8 | rs7527068 | 1 | GCST90624105 | no MR -> candidate analysis |
| General cognitive ability | 5e-6 | rs1047619 | 1 | GCST006269 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 286 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Abnormality of the skeletal system | 0.591 | — | common-variant locus | no MR -> candidate analysis |
| trauma complication | 0.095 | — | common-variant locus | no MR -> candidate analysis |
| cataract | 0.095 | — | common-variant locus | no MR -> candidate analysis |
| chronic musculoskeletal pain | 0.085 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=3.3e-07, LOEUF=1.28 — LoF-tolerant |
| GWAS Catalog | 19 unique SNPs / 38 rows |
| ClinVar | 39 records; 3 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 286 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'GPX7'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 39 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 9 of 9 traits by best p-value, aggregated from 11 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q96SL4 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000116157/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/GPX7 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/GPX7 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=GPX7%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/GPX7 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:53:44  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
