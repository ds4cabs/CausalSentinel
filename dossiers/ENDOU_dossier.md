# Protein Dossier — ENDOU (Uridylate-specific endoribonuclease)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Cough on most days | 0.302 | 0.0612 | 8.37e-07 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: asthma | -0.187 | 0.0544 | 5.75e-04 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K35 Acute appendicitis | 0.487 | 0.145 | 7.91e-04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | 0.0641 | 0.0257 | 0.0125 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: S76 Injury of muscle and tendon at hip and thigh level | 0.887 | 0.365 | 0.0152 | Wald ratio | 1 | cis | NA |
| Squamous cell lung cancer | 0.484 | 0.2 | 0.0157 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: kidney stone or ureter stone or bladder stone | 0.322 | 0.134 | 0.0163 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: ankylosing spondylitis | 0.462 | 0.201 | 0.0214 | Wald ratio | 1 | cis | NA |
| Lung cancer | 0.257 | 0.126 | 0.041 | Wald ratio | 1 | cis | NA |
| Neuroticism | -0.0491 | 0.0245 | 0.0455 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Cataract | -0.22 | 0.111 | 0.0471 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | 0.29 | 0.147 | 0.0477 | Wald ratio | 1 | cis | NA |
| _...and 57 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_4 association rows across 4 traits (3 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Poly(U)-specific endoribonuclease levels | 4e-37 | rs11830795 | 1 | GCST90426432 | no MR -> candidate analysis |
| ENDOU protein levels | 8e-26 | rs2238145 | 1 | GCST90469107 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 3e-24 | rs7969186 | 1 | GCST90838669 | no MR -> candidate analysis |
| Dementia | 6e-6 | rs1234820 | 1 | GCST90449024 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 368 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| basal cell carcinoma | 0.312 | — | common-variant locus | MR: beta=0.198, p=0.158 (cis) |
| cardiovascular disorder | 0.197 | — | common-variant locus | no MR -> candidate analysis |
| kidney disorder | 0.118 | — | common-variant locus | no MR -> candidate analysis |
| lung cancer | 0.108 | — | common-variant locus | MR: beta=0.484, p=0.0157 (cis) |

> Of the 4 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.3e-15, LOEUF=1.15 — LoF-tolerant |
| GWAS Catalog | 74 unique SNPs / 148 rows |
| ClinVar | 74 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 368 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'ENDOU'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 74 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 4 of 4 traits by best p-value, aggregated from 4 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P21128 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000111405/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/ENDOU — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/ENDOU — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=ENDOU%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/ENDOU — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:25:24  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
