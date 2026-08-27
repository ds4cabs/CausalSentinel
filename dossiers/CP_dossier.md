# Protein Dossier — CP (Ceruloplasmin)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | 0.156 | 0.0459 | 6.56e-04 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: H25 Senile cataract | 0.285 | 0.105 | 0.00659 | Wald ratio | 1 | cis | NA |
| Endometrioid ovarian cancer | -0.349 | 0.149 | 0.0188 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | 0.0338 | 0.0156 | 0.0305 | Wald ratio | 1 | cis | NA |
| High grade serous ovarian cancer | -0.159 | 0.0805 | 0.0482 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | -0.0418 | 0.0214 | 0.0513 | Wald ratio | 1 | cis | NA |
| Ovarian cancer | -0.128 | 0.0676 | 0.0586 | Wald ratio | 1 | cis | NA |
| Diastolic blood pressure  automated reading | -0.0233 | 0.0123 | 0.0593 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypopituitarism | 0.704 | 0.381 | 0.0646 | Wald ratio | 1 | cis | NA |
| Systolic blood pressure  automated reading | -0.0225 | 0.0123 | 0.0686 | Wald ratio | 1 | cis | NA |
| Weight | -0.0186 | 0.0106 | 0.0813 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | -0.367 | 0.219 | 0.0948 | Wald ratio | 1 | cis | NA |
| _...and 62 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_13 association rows across 7 traits (12 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Histidine levels | 3e-116 | rs10935742 | 5 | GCST90501120 | no MR -> candidate analysis |
| Core binding factor acute myeloid leukemia | 2e-34 | rs16861634; rs1879169; rs7652826; rs17838831; rs701748 | 2 | GCST008413 | no MR -> candidate analysis |
| Serum ceruloplasmin levels | 2e-11 | rs13072552 | 1 | GCST001318 | no MR -> candidate analysis |
| TCP11L1 protein levels | 4e-10 | rs35229573 | 1 | GCST90453389 | no MR -> candidate analysis |
| Copper levels | 1e-9 | rs34951015 | 2 | GCST90096810 | no MR -> candidate analysis |
| Putamen iron levels (R2* MRI) | 1e-9 | rs3772562 | 1 | GCST90551870 | no MR -> candidate analysis |
| Serum copper levels | 8e-7 | rs11708215 | 1 | GCST90100524 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 2134 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| aceruloplasminemia | 0.875 | — | established (curated) | no MR -> candidate analysis |
| Hermansky-Pudlak syndrome 3 | 0.928 | — | established (curated) | no MR -> candidate analysis |
| Hermansky-Pudlak syndrome | 0.851 | — | established (curated) | no MR -> candidate analysis |
| neurodegeneration with brain iron accumulation | 0.821 | — | established (curated) | no MR -> candidate analysis |
| hereditary disease | 0.562 | — | established (curated) | no MR -> candidate analysis |
| alcohol drinking | 0.418 | — | common-variant locus | no MR -> candidate analysis |
| ovarian dysfunction | 0.234 | — | common-variant locus | no MR -> candidate analysis |

> Of the 7 rows above, **7 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.4e-08, LOEUF=0.644 — LoF-tolerant |
| GWAS Catalog | 39 unique SNPs / 78 rows |
| ClinVar | 1188 records; 3 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 2134 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 1188 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 7 of 7 traits by best p-value, aggregated from 13 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P00450 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000047457/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CP — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CP — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CP%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CP — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:58:55  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: chembl
