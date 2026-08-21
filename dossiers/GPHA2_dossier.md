# Protein Dossier — GPHA2 (Glycoprotein hormone alpha-2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Eye problems or disorders: Glaucoma | 0.124 | 0.0392 | 0.00161 | Wald ratio | 1 | trans | NA |
| Systolic blood pressure  automated reading | 0.017 | 0.00545 | 0.00181 | Wald ratio | 1 | trans | NA |
| Fractured bone site(s): Wrist | 0.0972 | 0.0345 | 0.00488 | Wald ratio | 1 | trans | NA |
| Mean cell haemoglobin concentration | 0.0224 | 0.00798 | 0.00494 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: R11 Nausea and vomiting | -0.325 | 0.119 | 0.00651 | Wald ratio | 1 | trans | NA |
| Cough on most days | 0.0683 | 0.0255 | 0.00743 | Wald ratio | 1 | trans | NA |
| Eye problems or disorders: Diabetes related eye disease | -0.2 | 0.0838 | 0.0167 | Wald ratio | 1 | trans | NA |
| ER-negative Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0617 | 0.0274 | 0.0243 | Wald ratio | 1 | trans | NA |
| Small vessel disease | -0.176 | 0.0792 | 0.026 | Wald ratio | 1 | trans | NA |
| Percent emphysema | -0.0902 | 0.0423 | 0.033 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: G47 Sleep disorders | 0.13 | 0.0613 | 0.0345 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: M54 Dorsalgia | 0.0794 | 0.0382 | 0.0378 | Wald ratio | 1 | trans | NA |
| _...and 98 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_2 association rows across 2 traits (1 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Uric acid levels | 2e-63 | rs1174410819 | 1 | GCST90239629 | no MR -> candidate analysis |
| Squamous cell lung carcinoma | 9e-6 | rs148033979 | 1 | GCST90652535 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 83 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| adolescent idiopathic scoliosis | 0.053 | — | common-variant locus | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.00037, LOEUF=1.27 — LoF-tolerant |
| GWAS Catalog | 45 unique SNPs / 88 rows |
| ClinVar | 36 records; 4 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 83 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'GPHA2'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 36 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 2 of 2 traits by best p-value, aggregated from 2 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q96T91 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000149735/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/GPHA2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/GPHA2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=GPHA2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/GPHA2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:53:14  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
