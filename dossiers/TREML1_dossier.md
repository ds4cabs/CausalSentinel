# Protein Dossier — TREML1 (Trem-like transcript 1 protein)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Vascular or heart problems diagnosed by doctor: Angina | 0.229 | 0.0764 | 0.00269 | Wald ratio | 1 | cis | NA |
| Diastolic blood pressure  automated reading | -0.0459 | 0.0174 | 0.00838 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Diabetes related eye disease | 0.396 | 0.151 | 0.00861 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Wrist | 0.238 | 0.0968 | 0.0139 | Wald ratio | 1 | cis | NA |
| Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.103 | 0.0427 | 0.0159 | Wald ratio | 1 | cis | NA |
| High grade serous ovarian cancer | -0.249 | 0.108 | 0.0204 | Wald ratio | 1 | cis | NA |
| Red blood cell count | 0.0341 | 0.0161 | 0.0342 | Wald ratio | 1 | cis | NA |
| Neo-extraversion | -1.18 | 0.59 | 0.0447 | Wald ratio | 1 | cis | NA |
| Years of schooling | -0.0474 | 0.0237 | 0.0455 | Wald ratio | 1 | cis | NA |
| Packed cell volume | 0.248 | 0.124 | 0.0459 | Wald ratio | 1 | cis | NA |
| Body fat | -0.0796 | 0.0412 | 0.0535 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K80 Cholelithiasis | 0.189 | 0.0992 | 0.0562 | Wald ratio | 1 | cis | NA |
| _...and 93 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_4 association rows across 4 traits (3 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Triggering receptor expressed on myeloid cells 2 level in Ch | 7e-30 | rs73427270 | 1 | GCST90234514 | no MR -> candidate analysis |
| TREML2 protein levels | 3e-16 | rs114027364 | 1 | GCST90470962 | no MR -> candidate analysis |
| Circulating TREML2 levels | 6e-14 | rs547564061 | 1 | GCST90859936 | no MR -> candidate analysis |
| Alzheimer's disease, proxy Alzheimer's disease or related de | 2e-6 | rs116748189 | 1 | GCST90654664 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 214 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Parkinson disease | 0.152 | 0.152 | exploratory rare-variant signal | no MR -> candidate analysis |
| Alzheimer disease | 0.133 | — | common-variant locus | no MR -> candidate analysis |
| late-onset Alzheimers disease | 0.084 | — | common-variant locus | no MR -> candidate analysis |
| neurodegenerative disease | 0.084 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 1 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=3.6e-11, LOEUF=1.64 — LoF-tolerant |
| GWAS Catalog | 68 unique SNPs / 136 rows |
| ClinVar | 54 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 214 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'TREML1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 54 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 4 of 4 traits by best p-value, aggregated from 4 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q86YW5 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000161911/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/TREML1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/TREML1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=TREML1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/TREML1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:29:24  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
