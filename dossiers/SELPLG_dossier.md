# Protein Dossier — SELPLG (P-selectin glycoprotein ligand 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: I84 Haemorrhoids | 0.208 | 0.0749 | 0.00547 | Wald ratio | 1 | cis | NA |
| Neuroticism | 0.0526 | 0.0191 | 0.00596 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: migraine | -0.279 | 0.111 | 0.0115 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: G56 Mononeuropathies of upper limb | 0.198 | 0.0897 | 0.0275 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | -0.164 | 0.0751 | 0.0294 | Wald ratio | 1 | cis | NA |
| Hippocampus volume | -59.5 | 27.7 | 0.0319 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: D12 Benign neoplasm of colon  rectum  anus and anal canal | 0.202 | 0.0995 | 0.0426 | Wald ratio | 1 | cis | NA |
| Depressive symptoms | 0.0478 | 0.0239 | 0.0455 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R55 Syncope and collapse | -0.538 | 0.285 | 0.0589 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I83 Varicose veins of lower extremities | -0.245 | 0.13 | 0.059 | Wald ratio | 1 | cis | NA |
| Diastolic blood pressure  automated reading | 0.0272 | 0.0146 | 0.0624 | Wald ratio | 1 | cis | NA |
| Pulse rate | 0.043 | 0.0251 | 0.0866 | Wald ratio | 1 | cis | NA |
| _...and 56 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_11 association rows across 8 traits (10 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating SELPLG levels | 8e-2505 | rs7311687 | 1 | GCST90859798 | no MR -> candidate analysis |
| P-selectin glycoprotein ligand 1 levels | 2e-544 | rs11114010 | 3 | GCST90012046 | no MR -> candidate analysis |
| SELPLG protein levels | 3e-82 | rs8179124 | 2 | GCST90470568 | no MR -> candidate analysis |
| Serum levels of protein SELPLG | 3e-20 | rs73191242 | 1 | GCST90086649 | no MR -> candidate analysis |
| Blood protein levels | 2e-12 | rs73191242 | 1 | GCST006585 | no MR -> candidate analysis |
| Haematocrit percentage (UKB data field 30030) | 2e-12 | rs7300422 | 1 | GCST90468073 | no MR -> candidate analysis |
| Lung function (FEV1/FVC) | 5e-9 | rs7300422 | 1 | GCST007080 | no MR -> candidate analysis |
| Conduct disorder (symptom count) | 3e-6 | rs8179116 | 1 | GCST000713 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 554 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| glaucoma | 0.653 | — | common-variant locus | MR: beta=0.0781, p=0.483 (cis) |
| Jaundice | 0.384 | — | common-variant locus | no MR -> candidate analysis |
| response to statin | 0.158 | — | common-variant locus | no MR -> candidate analysis |
| coronary artery disorder | 0.076 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 1 known modulators (P-selectin glycoprotein ligand 1) |
| gnomAD constraint | pLI=0.053, LOEUF=5.71 — LoF-tolerant |
| GWAS Catalog | 58 unique SNPs / 116 rows |
| ClinVar | 86 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 554 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'SELPLG' and resolved to 'P-selectin glycoprotein ligand 1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 86 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 8 of 8 traits by best p-value, aggregated from 11 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q14242 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000110876/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4183/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/SELPLG — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/SELPLG — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=SELPLG%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/SELPLG — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:58:02  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
