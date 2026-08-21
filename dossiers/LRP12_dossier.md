# Protein Dossier — LRP12 (Low-density lipoprotein receptor-related protein 12)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: gastro-oesophageal reflux (gord)  or  gastric reflux | 0.195 | 0.0564 | 5.32e-04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: pneumothorax | 0.877 | 0.327 | 0.0073 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: vaginal prolapse or uterine prolapse | 0.346 | 0.139 | 0.013 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K40 Inguinal hernia | 0.18 | 0.0729 | 0.0135 | Wald ratio | 1 | cis | NA |
| Pallidum volume | -25.9 | 11.4 | 0.0231 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | 0.0515 | 0.023 | 0.0252 | Wald ratio | 1 | cis | NA |
| Creatinine (enzymatic) in urine | 0.0301 | 0.0136 | 0.0268 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C61 Malignant neoplasm of prostate | 0.284 | 0.134 | 0.0344 | Wald ratio | 1 | cis | NA |
| Putamen volume | -75.1 | 35.7 | 0.0353 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: osteoporosis | 0.193 | 0.095 | 0.0425 | Wald ratio | 1 | cis | NA |
| ER-positive Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.0882 | 0.0441 | 0.0455 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M17 Gonarthrosis [arthrosis of knee] | 0.173 | 0.0868 | 0.0465 | Wald ratio | 1 | cis | NA |
| _...and 69 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_4 association rows across 3 traits (2 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Educational attainment | 5e-10 | rs3134530 | 1 | GCST90105038 | no MR -> candidate analysis |
| Type 2 diabetes | 3e-8 | rs28627996 | 2 | GCST90492734 | no MR -> candidate analysis |
| Facial morphology (factor 22) | 3e-6 | rs79944793 | 1 | GCST004326 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 130 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| oculopharyngodistal myopathy | 0.608 | — | established (curated) | no MR -> candidate analysis |
| oculopharyngodistal myopathy 1 | 0.617 | — | established (curated) | no MR -> candidate analysis |
| amyotrophic lateral sclerosis 28 | 0.617 | — | established (curated) | no MR -> candidate analysis |
| hypertensive disorder | 0.661 | — | common-variant locus | no MR -> candidate analysis |
| type 2 diabetes mellitus | 0.56 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.55 | — | common-variant locus | no MR -> candidate analysis |
| atrial fibrillation | 0.534 | — | common-variant locus | no MR -> candidate analysis |
| respiratory tract infectious disorder | 0.482 | — | common-variant locus | no MR -> candidate analysis |
| Abnormal abdomen morphology | 0.419 | — | common-variant locus | no MR -> candidate analysis |
| atrial flutter | 0.4 | — | common-variant locus | no MR -> candidate analysis |
| Increased blood pressure | 0.396 | — | common-variant locus | no MR -> candidate analysis |
| placenta praevia | 0.396 | — | common-variant locus | no MR -> candidate analysis |
| cardiovascular disorder | 0.364 | — | common-variant locus | no MR -> candidate analysis |
| cerebrovascular disorder | 0.365 | — | common-variant locus | no MR -> candidate analysis |
| open-angle glaucoma | 0.361 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **15 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1, LOEUF=0.332 — LoF-INTOLERANT |
| GWAS Catalog | 79 unique SNPs / 125 rows |
| ClinVar | 175 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 130 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'LRP12'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 175 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 3 of 3 traits by best p-value, aggregated from 4 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9Y561 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000147650/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/LRP12 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/LRP12 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=LRP12%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/LRP12 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:37:25  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
