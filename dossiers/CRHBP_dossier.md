# Protein Dossier — CRHBP (Corticotropin-releasing hormone-binding protein)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| HOMA-B | 0.016 | 0.00724 | 0.0267 | Wald ratio | 1 | cis | NA |
| Microalbuminuria | 0.0978 | 0.045 | 0.0297 | Wald ratio | 1 | cis | NA |
| Urinary albumin-to-creatinine ratio | 0.0294 | 0.0135 | 0.0297 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I48 Atrial fibrillation and flutter | -0.107 | 0.0521 | 0.0401 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hyperthyroidism or thyrotoxicosis | 0.105 | 0.0517 | 0.0431 | Wald ratio | 1 | cis | NA |
| Serum cystatin C (eGFRcys) | -0.00763 | 0.00391 | 0.0512 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: diverticular disease or diverticulitis | 0.0812 | 0.043 | 0.0592 | Wald ratio | 1 | cis | NA |
| Coronary heart disease | 0.0366 | 0.02 | 0.0671 | Wald ratio | 1 | cis | NA |
| Sodium in urine | -0.00879 | 0.00485 | 0.0699 | Wald ratio | 1 | cis | NA |
| Depressive symptoms | -0.0176 | 0.00978 | 0.0719 | Wald ratio | 1 | cis | NA |
| Creatinine (enzymatic) in urine | -0.00831 | 0.00472 | 0.0783 | Wald ratio | 1 | cis | NA |
| Putamen volume | 21.6 | 12.3 | 0.0792 | Wald ratio | 1 | cis | NA |
| _...and 86 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_14 association rows across 9 traits (12 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Hematological traits (multi-trait analysis) | 2e-110 | rs72763266 | 1 | GCST90838669 | no MR -> candidate analysis |
| Circulating CRHBP levels | 1e-84 | rs7721799 | 5 | GCST90860650 | no MR -> candidate analysis |
| CRHBP protein levels | 2e-35 | rs189832182 | 2 | GCST90468860 | no MR -> candidate analysis |
| Mean platelet thrombocyte volume (UKB data field 30100) | 2e-24 | rs492287 | 1 | GCST90468087 | no MR -> candidate analysis |
| Corticotropin-releasing factor-binding protein levels | 7e-15 | rs58714487 | 1 | GCST90247155 | no MR -> candidate analysis |
| Blood cell traits latent factor 5 (platelet) | 5e-9 | rs7734134 | 1 | GCST90559247 | no MR -> candidate analysis |
| Varicose veins | 9e-9 | rs247749 | 1 | GCST007225 | MR: beta=0.0251, p=0.456 (cis) |
| Chronotype | 1e-7 | rs32897 | 1 | GCST007576 | no MR -> candidate analysis |
| Acute graft-versus-host disease (gut) (donor effect) | 4e-7 | rs1651094 | 1 | GCST90102564 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 140 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| nephritis | 0.371 | — | common-variant locus | no MR -> candidate analysis |
| Nephropathy | 0.371 | — | common-variant locus | no MR -> candidate analysis |
| Varicose veins | 0.118 | — | common-variant locus | MR: beta=0.0251, p=0.456 (cis) |

> Of the 3 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Corticotropin-releasing factor-binding protein) |
| gnomAD constraint | pLI=0.0014, LOEUF=0.8 — LoF-tolerant |
| GWAS Catalog | 47 unique SNPs / 94 rows |
| ClinVar | 41 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 1 clinical annotations across 1 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 140 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'CRHBP' and resolved to 'Corticotropin-releasing factor-binding protein' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 41 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 9 of 9 traits by best p-value, aggregated from 14 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P24387 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000145708/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL5930/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CRHBP — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CRHBP — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CRHBP%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=CRHBP — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CRHBP — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:03:16  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
