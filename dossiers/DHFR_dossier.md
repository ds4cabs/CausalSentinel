# Protein Dossier — DHFR (Dihydrofolate reductase)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Platelet count | -2.82 | 0.975 | 0.00382 | Wald ratio | 1 | trans | NA |
| Coronary heart disease | 0.0465 | 0.0164 | 0.00456 | Wald ratio | 1 | trans | NA |
| Ferritin | 0.0451 | 0.0165 | 0.00642 | Wald ratio | 1 | trans | NA |
| Myocardial infarction | 0.0497 | 0.0184 | 0.00687 | Wald ratio | 1 | trans | NA |
| Neuroticism | 0.013 | 0.00486 | 0.00766 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code self-reported: pulmonary embolism (with or without) dvt | -0.134 | 0.0513 | 0.0091 | Wald ratio | 1 | trans | NA |
| Squamous cell lung cancer | -0.102 | 0.0448 | 0.0224 | Wald ratio | 1 | trans | NA |
| Potassium in urine | -0.00917 | 0.0041 | 0.0252 | Wald ratio | 1 | trans | NA |
| Bulimia nervosa | -0.0259 | 0.013 | 0.0455 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: migraine | 0.0446 | 0.0223 | 0.0457 | Wald ratio | 1 | trans | NA |
| Serum cystatin C (eGFRcys) | 0.00665 | 0.0034 | 0.0509 | Wald ratio | 1 | trans | NA |
| Mean platelet volume | 0.0047 | 0.00243 | 0.0532 | Wald ratio | 1 | trans | NA |
| _...and 83 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_14 association rows across 12 traits (12 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Vertex-wise cortical thickness | 1e-27 | rs1650697 | 1 | GCST90095131 | no MR -> candidate analysis |
| Brain morphology (MOSTest) | 8e-21 | rs863216 | 2 | GCST90239729 | no MR -> candidate analysis |
| Cortical thickness | 1e-17 | rs863216 | 2 | GCST90091061 | no MR -> candidate analysis |
| Regional cortical thickness (lateraloccipital) | 1e-15 | rs245100 | 1 | GCST90399885 | no MR -> candidate analysis |
| Occipital thickness (unadjusted for global measures) | 2e-12 | rs863216 | 1 | GCST90271808 | no MR -> candidate analysis |
| Standing height (UKB data field 50) | 2e-12 | rs36071238 | 1 | GCST90468178 | no MR -> candidate analysis |
| Occipital thickness | 4e-12 | rs863216 | 1 | GCST90572708 | no MR -> candidate analysis |
| Cortical thickness (MOSTest) | 2e-10 | rs863216 | 1 | GCST010700 | no MR -> candidate analysis |
| Vertex-wise sulcal depth | 7e-10 | rs863216 | 1 | GCST90095129 | no MR -> candidate analysis |
| Cortical surface area | 1e-8 | rs12517451 | 1 | GCST90091060 | no MR -> candidate analysis |
| Idiopathic downbeat nystagmus | 5e-7 | rs245100 | 1 | GCST010172 | no MR -> candidate analysis |
| Reaction time | 8e-6 | rs1650697 | 1 | GCST006268 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 647 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| constitutional megaloblastic anemia with severe neurologic disease | 0.752 | — | established (curated) | no MR -> candidate analysis |
| hereditary neoplastic syndrome | 0.917 | — | established (curated) | no MR -> candidate analysis |
| Inherited cancer-predisposing syndrome | 0.917 | — | established (curated) | no MR -> candidate analysis |
| familial adenomatous polyposis 4 | 0.879 | — | established (curated) | no MR -> candidate analysis |
| endometrial carcinoma | 0.702 | — | established (curated) | no MR -> candidate analysis |

> Of the 5 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 9 known modulators (Dihydrofolate reductase) |
| gnomAD constraint | not available |
| GWAS Catalog | 26 unique SNPs / 46 rows |
| ClinVar | 767 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 9 clinical annotations across 2 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 647 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'DHFR' and resolved to 'Dihydrofolate reductase' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 767 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 12 of 12 traits by best p-value, aggregated from 14 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P00374 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000228716/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL202/ — _ChEMBL_37 (released 2026-05-01)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/DHFR — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=DHFR%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=DHFR — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/DHFR — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:16:49  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: gnomad
