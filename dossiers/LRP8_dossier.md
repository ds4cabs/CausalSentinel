# Protein Dossier — LRP8 (Low-density lipoprotein receptor-related protein 8)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: I83 Varicose veins of lower extremities | 0.335 | 0.0817 | 4.19e-05 | Wald ratio | 1 | cis | NA |
| Depressive symptoms | 0.0964 | 0.0301 | 0.00137 | Wald ratio | 1 | cis | NA |
| Neuroticism | 0.0663 | 0.0241 | 0.00596 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: muscle or soft tissue injuries | 0.361 | 0.137 | 0.00828 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R04 Haemorrhage from respiratory passages | 0.395 | 0.156 | 0.0116 | Wald ratio | 1 | cis | NA |
| Triglycerides | 0.0753 | 0.0307 | 0.0142 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Cataract | 0.179 | 0.0746 | 0.0162 | Wald ratio | 1 | cis | NA |
| Sodium in urine | 0.038 | 0.016 | 0.0174 | Wald ratio | 1 | cis | NA |
| Creatinine (enzymatic) in urine | 0.036 | 0.0155 | 0.0203 | Wald ratio | 1 | cis | NA |
| Underlying (primary) cause of death: ICD10: E85.4 Organ-limited amyloidosis | 2.02 | 0.889 | 0.023 | Wald ratio | 1 | cis | NA |
| Hearing difficulty or problems: Yes | 0.06 | 0.0264 | 0.0231 | Wald ratio | 1 | cis | NA |
| Clear cell ovarian cancer | -0.608 | 0.271 | 0.0248 | Wald ratio | 1 | cis | NA |
| _...and 107 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3323_37_1` | LRP8 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_60 association rows across 53 traits (48 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Selenoprotein W levels | 1e-133 | rs5177 | 2 | GCST90249482 | no MR -> candidate analysis |
| Cerebellar grey matter morphology (MOSTest) | 2e-72 | rs11206127 | 1 | GCST90728589 | no MR -> candidate analysis |
| Low-density lipoprotein receptor-related protein 8 levels | 5e-48 | rs2297663 | 4 | GCST90248266 | no MR -> candidate analysis |
| Vertex-wise cortical thickness | 1e-28 | rs5174 | 1 | GCST90095131 | no MR -> candidate analysis |
| Whole brain restricted directional diffusion (multivariate a | 1e-26 | rs5174 | 1 | GCST90131905 | no MR -> candidate analysis |
| Vertex-wise sulcal depth | 3e-26 | rs5174 | 1 | GCST90095129 | no MR -> candidate analysis |
| Whole brain free water diffusion (multivariate analysis) | 3e-24 | rs11206127 | 1 | GCST90131906 | no MR -> candidate analysis |
| Whole brain restricted isotropic diffusion (multivariate ana | 7e-21 | rs3737983 | 1 | GCST90131904 | no MR -> candidate analysis |
| Educational attainment | 2e-20 | rs10788951 | 1 | GCST90105038 | no MR -> candidate analysis |
| Cortical thickness | 1e-17 | rs5174 | 1 | GCST90091061 | no MR -> candidate analysis |
| Serum levels of protein LRP8 | 4e-16 | rs3737984 | 1 | GCST90088315 | no MR -> candidate analysis |
| Brain morphology (MOSTest) | 9e-15 | rs5174 | 2 | GCST90239729 | no MR -> candidate analysis |
| _...and 41 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 509 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| myocardial infarction | 0.304 | — | established (curated) | MR: beta=0.149, p=0.0301 (cis) |
| irritable bowel syndrome | 0.415 | — | common-variant locus | no MR -> candidate analysis |
| risk-taking behaviour | 0.38 | — | common-variant locus | no MR -> candidate analysis |
| schizophrenia | 0.267 | — | common-variant locus | MR: beta=0.0964, p=0.179 (cis) |
| response to statin | 0.134 | — | common-variant locus | no MR -> candidate analysis |

> Of the 5 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.2, LOEUF=0.527 — LoF-tolerant |
| GWAS Catalog | 64 unique SNPs / 128 rows |
| ClinVar | 175 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 509 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'LRP8'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 175 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 53 traits by best p-value, aggregated from 60 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q14114 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000157193/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/LRP8 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/LRP8 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=LRP8%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/LRP8 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:37:40  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
