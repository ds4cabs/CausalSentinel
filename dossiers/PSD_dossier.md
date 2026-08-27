# Protein Dossier — PSD (PH and SEC7 domain-containing protein 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Forced vital capacity (FVC) | 0.0202 | 0.00633 | 0.00142 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: R10 Abdominal and pelvic pain | -0.13 | 0.0425 | 0.0022 | Wald ratio | 1 | trans | NA |
| ER-positive Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.075 | 0.0246 | 0.00232 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: hypertension | -0.0402 | 0.0137 | 0.00334 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: gastro-oesophageal reflux (gord)  or  gastric reflux | -0.114 | 0.0417 | 0.00647 | Wald ratio | 1 | trans | NA |
| Thalamus volume | 49.8 | 20 | 0.0127 | Wald ratio | 1 | trans | NA |
| Transferrin | -0.0806 | 0.0325 | 0.013 | Wald ratio | 1 | trans | NA |
| Forced expiratory volume in 1-second (FEV1) | 0.0164 | 0.00668 | 0.0143 | Wald ratio | 1 | trans | NA |
| Diastolic blood pressure  automated reading | -0.0166 | 0.00789 | 0.0353 | Wald ratio | 1 | trans | NA |
| Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0431 | 0.0207 | 0.0374 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: C50 Malignant neoplasm of breast | 0.111 | 0.0541 | 0.0407 | Wald ratio | 1 | trans | NA |
| Body mass index (BMI) | -0.0156 | 0.00771 | 0.043 | Wald ratio | 1 | trans | NA |
| _...and 96 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_8 association rows across 8 traits (8 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Phospholipids to Total Lipids in Large HDL percentage | 2e-16 | rs79931565 | 1 | GCST90501143 | no MR -> candidate analysis |
| Alanine transaminase (ALT, mean, inv-norm transformed) | 4e-12 | rs148337160 | 1 | GCST90479507 | no MR -> candidate analysis |
| Chronic elevation of alanine aminotransferase (cALT) levels | 3e-11 | rs148337160 | 1 | GCST90129601 | no MR -> candidate analysis |
| Alanine transaminase (ALT, maximum, inv-norm transformed) | 3e-11 | rs148337160 | 1 | GCST90479506 | no MR -> candidate analysis |
| Apolipoprotein B levels | 2e-10 | rs79931565 | 1 | GCST010243 | no MR -> candidate analysis |
| Alzheimer's disease or educational attainment (pleiotropy) | 4e-10 | rs55970842 | 1 | GCST90095190 | no MR -> candidate analysis |
| Phospholipids to total lipids in small HDL percentage (UKB d | 4e-10 | rs148337160 | 1 | GCST90269741 | no MR -> candidate analysis |
| Educational attainment (MTAG) | 1e-8 | rs3781291 | 1 | GCST006571 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 114 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| mathematical ability | 0.09 | — | common-variant locus | no MR -> candidate analysis |
| Abnormal nasolacrimal system morphology | 0.077 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.064 | — | common-variant locus | no MR -> candidate analysis |
| cannabis dependence | 0.062 | — | common-variant locus | no MR -> candidate analysis |
| attention deficit-hyperactivity disorder | 0.051 | — | common-variant locus | no MR -> candidate analysis |
| autism spectrum disorder | 0.051 | — | common-variant locus | no MR -> candidate analysis |
| intelligence | 0.051 | — | common-variant locus | MR: beta=0.0594, p=0.152 (trans) |
| dislocation | 0.036 | — | common-variant locus | no MR -> candidate analysis |

> Of the 8 rows above, **7 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (PH and SEC7 domain-containing protein 1) |
| gnomAD constraint | pLI=1, LOEUF=0.469 — LoF-INTOLERANT |
| GWAS Catalog | 89 unique SNPs / 177 rows |
| ClinVar | 178 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 114 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'PSD' and resolved to 'PH and SEC7 domain-containing protein 1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 178 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 8 of 8 traits by best p-value, aggregated from 8 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/A5PKW4 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000059915/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4523105/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PSD — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PSD — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PSD%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PSD — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:39:24  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
