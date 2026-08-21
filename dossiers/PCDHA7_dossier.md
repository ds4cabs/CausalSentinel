# Protein Dossier — PCDHA7 (Protocadherin alpha-7)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Eye problems or disorders: Glaucoma | 0.331 | 0.0831 | 6.71e-05 | Wald ratio | 1 | trans | NA |
| Eye problems or disorders: Injury or trauma resulting in loss of vision | 0.452 | 0.116 | 9.73e-05 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: K60 Fissure and fistula of anal and rectal regions | 0.49 | 0.127 | 1.11e-04 | Wald ratio | 1 | trans | NA |
| Squamous cell lung cancer | -0.586 | 0.168 | 4.65e-04 | Wald ratio | 1 | trans | NA |
| Forced vital capacity (FVC) | 0.0353 | 0.0113 | 0.00172 | Wald ratio | 1 | trans | NA |
| Packed cell volume | -0.387 | 0.146 | 0.00814 | Wald ratio | 1 | trans | NA |
| Haemoglobin concentration | -0.127 | 0.0484 | 0.00848 | Wald ratio | 1 | trans | NA |
| Height | 0.0501 | 0.0206 | 0.015 | Wald ratio | 1 | trans | NA |
| Percent emphysema | -0.126 | 0.0545 | 0.0205 | Wald ratio | 1 | trans | NA |
| Forced expiratory volume in 1-second (FEV1) | 0.0272 | 0.0119 | 0.0218 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: kidney stone or ureter stone or bladder stone | 0.266 | 0.121 | 0.0276 | Wald ratio | 1 | trans | NA |
| Serum creatinine (eGFRcrea) | 0.0122 | 0.00556 | 0.0278 | Wald ratio | 1 | trans | NA |
| _...and 83 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_25 association rows across 19 traits (22 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Refractive error | 6e-17 | rs246073 | 3 | GCST90841196 | no MR -> candidate analysis |
| Pulse pressure | 2e-12 | rs246074 | 2 | GCST90292476 | no MR -> candidate analysis |
| Systolic blood pressure | 1e-11 | rs246074 | 2 | GCST90292477 | MR: beta=-0.00978, p=0.487 (trans) |
| Schizophrenia | 6e-11 | rs246061 | 2 | GCST90503210 | MR: beta=-0.0428, p=0.492 (trans) |
| Body size (confirmatory factor analysis Factor 21) | 6e-10 | rs251350 | 1 | GCST90309355 | no MR -> candidate analysis |
| Lung function (FVC) | 7e-10 | rs190175998 | 1 | GCST007081 | no MR -> candidate analysis |
| Post-traumatic stress disorder symptom severity (avoidance) | 8e-10 | rs251350 | 1 | GCST90271780 | no MR -> candidate analysis |
| Sum basophil neutrophil counts | 4e-9 | rs150616068 | 1 | GCST004620 | no MR -> candidate analysis |
| Neutrophil count | 4e-9 | rs150616068 | 1 | GCST004629 | no MR -> candidate analysis |
| Intelligence | 8e-9 | rs251368 | 1 | GCST90264174 | no MR -> candidate analysis |
| Personality traits or cognitive traits (multivariate analysi | 9e-9 | rs782706309 | 1 | GCST90270074 | no MR -> candidate analysis |
| Post-traumatic stress disorder symptom severity (total) | 1e-8 | rs251350 | 2 | GCST90271777 | no MR -> candidate analysis |
| _...and 7 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 22 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Thrombocytosis | 0.195 | — | established (curated) | no MR -> candidate analysis |
| major depressive disorder | 0.072 | — | common-variant locus | no MR -> candidate analysis |
| ocular hypotension | 0.055 | — | common-variant locus | no MR -> candidate analysis |
| cervical carcinoma | 0.053 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=2.5e-08, LOEUF=0.851 — LoF-tolerant |
| GWAS Catalog | 43 unique SNPs / 86 rows |
| ClinVar | 1491 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 22 of 22 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'PCDHA7'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 1491 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 19 of 19 traits by best p-value, aggregated from 25 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9UN72 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000204963/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PCDHA7 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PCDHA7 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PCDHA7%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PCDHA7 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:12:12  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
