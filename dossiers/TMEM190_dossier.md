# Protein Dossier — TMEM190 (Transmembrane protein 190)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: M16 Coxarthrosis [arthrosis of hip] | -0.0831 | 0.0219 | 1.47e-04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: osteoarthritis | -0.0212 | 0.00827 | 0.0103 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | 0.00484 | 0.0021 | 0.0208 | Wald ratio | 1 | cis | NA |
| Underlying (primary) cause of death: ICD10: E85.4 Organ-limited amyloidosis | 0.678 | 0.309 | 0.0282 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: muscle or soft tissue injuries | 0.0578 | 0.027 | 0.0321 | Wald ratio | 1 | cis | NA |
| Weight | 0.00456 | 0.00214 | 0.0329 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: D12 Benign neoplasm of colon  rectum  anus and anal canal | 0.0416 | 0.0196 | 0.0338 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K40 Inguinal hernia | -0.0322 | 0.0153 | 0.0352 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R11 Nausea and vomiting | 0.0753 | 0.0358 | 0.0354 | Wald ratio | 1 | cis | NA |
| Happiness | -0.00628 | 0.003 | 0.0361 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | 0.00409 | 0.00199 | 0.0395 | Wald ratio | 1 | cis | NA |
| Sleep duration | 0.00375 | 0.00189 | 0.0475 | Wald ratio | 1 | cis | NA |
| _...and 74 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_18 association rows across 16 traits (17 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Transmembrane protein 190 levels | 1e-2483 | rs4806666 | 2 | GCST90249908 | no MR -> candidate analysis |
| Transmembrane protein 190 levels (TMEM190.10442.1.3) | 4e-689 | rs4806666 | 1 | GCST90243093 | no MR -> candidate analysis |
| Blood protein levels | 1e-458 | rs35791293 | 1 | GCST006585 | no MR -> candidate analysis |
| Transmembrane protein 190 level in Chronic kidney disease wi | 5e-66 | rs4806666 | 1 | GCST90232872 | no MR -> candidate analysis |
| UPF0369 protein C6orf57 protein levels (SomaScan ID:10442-1) | 2e-43 | rs4806666 | 1 | GCST90440062 | no MR -> candidate analysis |
| PTPRH protein levels | 6e-19 | rs12980914 | 1 | GCST90470382 | no MR -> candidate analysis |
| Corpus callosum volume (MOSTest) | 2e-16 | rs35791293 | 1 | GCST90281350 | no MR -> candidate analysis |
| Corpus callosum central volume | 2e-13 | rs35791293 | 1 | GCST90281346 | no MR -> candidate analysis |
| Standing height (UKB data field 50) | 8e-12 | rs75653026 | 1 | GCST90468178 | no MR -> candidate analysis |
| Corpus callosum Mid-posterior volume | 9e-12 | rs4806666 | 1 | GCST90281347 | no MR -> candidate analysis |
| Height (baseline) | 5e-11 | rs75653026 | 1 | GCST90565843 | no MR -> candidate analysis |
| White matter microstructure (axial diusivities) | 2e-10 | rs11666276 | 1 | GCST009537 | no MR -> candidate analysis |
| _...and 4 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 21 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| injury | 0.212 | — | common-variant locus | MR: beta=0.0505, p=0.0928 (cis) |

> Of the 1 rows above, **0 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.4e-06, LOEUF=1.49 — LoF-tolerant |
| GWAS Catalog | 63 unique SNPs / 126 rows |
| ClinVar | 67 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 21 of 21 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'TMEM190'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 67 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 16 of 16 traits by best p-value, aggregated from 18 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q8WZ59 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000160472/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/TMEM190 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/TMEM190 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=TMEM190%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/TMEM190 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:24:30  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
