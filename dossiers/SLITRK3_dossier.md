# Protein Dossier — SLITRK3 (SLIT and NTRK-like protein 3)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: hayfever or allergic rhinitis | 0.0938 | 0.0387 | 0.0155 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: malignant melanoma | 0.224 | 0.0946 | 0.0181 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | 0.0237 | 0.0103 | 0.0218 | Wald ratio | 1 | cis | NA |
| Pulse rate | 0.0397 | 0.0183 | 0.0306 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: prostate cancer | -0.37 | 0.182 | 0.0421 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: G56 Mononeuropathies of upper limb | -0.195 | 0.0965 | 0.0435 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | 0.0168 | 0.00848 | 0.0474 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: enlarged prostate | 0.151 | 0.0764 | 0.0477 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Injury or trauma resulting in loss of vision | 0.209 | 0.111 | 0.0601 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R04 Haemorrhage from respiratory passages | 0.22 | 0.117 | 0.0603 | Wald ratio | 1 | cis | NA |
| Primary sclerosing cholangitis  | -0.276 | 0.151 | 0.0668 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | 0.0164 | 0.00894 | 0.067 | Wald ratio | 1 | cis | NA |
| _...and 64 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_5 association rows across 5 traits (5 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| SLIT and NTRK-like protein 3 levels | 3e-143 | rs62282371 | 1 | GCST90249567 | no MR -> candidate analysis |
| SLIT and NTRK-like protein 3 levels (SLITRK3.10565.19.3) | 2e-49 | rs398062996 | 1 | GCST90242836 | no MR -> candidate analysis |
| Serum levels of protein SLITRK3 | 4e-31 | rs62282368 | 1 | GCST90086345 | no MR -> candidate analysis |
| Blood protein levels | 4e-19 | rs62282371 | 1 | GCST006585 | no MR -> candidate analysis |
| Eukaryotic translation initiation factor 2 subunit 2 protein | 6e-10 | rs62282368 | 1 | GCST90442203 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 67 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Intellectual disability | 0.547 | — | established (curated) | no MR -> candidate analysis |
| premature birth | 0.419 | — | common-variant locus | no MR -> candidate analysis |
| acquired polycythemia vera | 0.331 | — | common-variant locus | no MR -> candidate analysis |
| myeloproliferative disorder | 0.261 | — | common-variant locus | no MR -> candidate analysis |
| intracranial hemorrhage | 0.134 | — | common-variant locus | no MR -> candidate analysis |
| placenta praevia | 0.062 | — | common-variant locus | no MR -> candidate analysis |
| colon carcinoma | 0.054 | — | common-variant locus | no MR -> candidate analysis |
| placental abruption | 0.054 | — | common-variant locus | no MR -> candidate analysis |
| vascular disorder | 0.054 | — | common-variant locus | no MR -> candidate analysis |
| intestinal disorder | 0.054 | — | common-variant locus | no MR -> candidate analysis |
| gastrointestinal disease | 0.054 | — | common-variant locus | no MR -> candidate analysis |
| diaphragm disorder | 0.053 | — | common-variant locus | no MR -> candidate analysis |
| drug allergy | 0.041 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of the gastrointestinal tract | 0.034 | — | common-variant locus | no MR -> candidate analysis |
| neuropathy | 0.033 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **15 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1, LOEUF=0.382 — LoF-INTOLERANT |
| GWAS Catalog | 74 unique SNPs / 89 rows |
| ClinVar | 135 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 67 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'SLITRK3'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 135 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 5 of 5 traits by best p-value, aggregated from 5 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O94933 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000121871/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/SLITRK3 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/SLITRK3 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=SLITRK3%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/SLITRK3 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:08:54  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
