# Protein Dossier — FRZB (Secreted frizzled-related protein 3)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Height | 0.0371 | 0.00884 | 2.67e-05 | Wald ratio | 1 | cis | NA |
| Weight | 0.0206 | 0.00578 | 3.63e-04 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | 0.0269 | 0.00848 | 0.00152 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: gastro-oesophageal reflux (gord)  or  gastric reflux | 0.0905 | 0.0288 | 0.00168 | Wald ratio | 1 | cis | NA |
| Major depressive disorder | -0.18 | 0.0601 | 0.00272 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: asthma | -0.0557 | 0.0194 | 0.00411 | Wald ratio | 1 | cis | NA |
| Sleep duration | 0.0137 | 0.00511 | 0.00714 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | 0.165 | 0.0664 | 0.0129 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K35 Acute appendicitis | 0.191 | 0.0782 | 0.0144 | Wald ratio | 1 | cis | NA |
| Ferritin | -0.067 | 0.0274 | 0.0145 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: L03 Cellulitis | 0.138 | 0.0638 | 0.0305 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M23 Internal derangement of knee | 0.0862 | 0.0405 | 0.0331 | Wald ratio | 1 | cis | NA |
| _...and 87 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2841_13_2` | sFRP-3 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_46 association rows across 24 traits (44 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating FRZB levels | 8e-970 | rs13009 | 3 | GCST90859676 | no MR -> candidate analysis |
| Secreted frizzled-related protein 3 levels | 5e-201 | rs288326 | 7 | GCST90249516 | no MR -> candidate analysis |
| Height | 5e-120 | rs1561369 | 5 | GCST90245848 | MR: beta=0.0371, p=2.67e-05 (cis) |
| FRZB protein levels | 2e-102 | rs112797950 | 2 | GCST90469269 | no MR -> candidate analysis |
| Secreted frizzled-related protein 3 (analyte X2841.13) level | 6e-64 | rs288326 | 1 | GCST90425498 | no MR -> candidate analysis |
| Serum levels of protein FRZB | 2e-55 | rs288326 | 2 | GCST90087651 | no MR -> candidate analysis |
| Secreted frizzled-related protein 3 levels (FRZB.13740.51.3) | 4e-55 | rs288326 | 2 | GCST90242728 | no MR -> candidate analysis |
| Heel bone mineral density | 4e-21 | rs10206992 | 5 | GCST007066 | MR: beta=0.0269, p=0.00152 (cis) |
| Estimated bone mineral density | 4e-20 | rs10206992 | 1 | GCST90726625 | no MR -> candidate analysis |
| Secreted frizzled-related protein 3 (analyte X13740.51) leve | 2e-19 | rs1561369 | 1 | GCST90422339 | no MR -> candidate analysis |
| Vertex-wise sulcal depth | 4e-19 | rs288326 | 1 | GCST90095129 | no MR -> candidate analysis |
| Neurological blood protein biomarker levels | 8e-19 | rs288326 | 1 | GCST008478 | no MR -> candidate analysis |
| _...and 12 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 815 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| osteoarthritis | 0.525 | — | established (curated) | MR: beta=0.0863, p=0.236 (cis) |
| hypertrophic cardiomyopathy 14 | 0.195 | — | established (curated) | no MR -> candidate analysis |
| retinitis pigmentosa | 0.185 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.2e-12, LOEUF=1.39 — LoF-tolerant |
| GWAS Catalog | 51 unique SNPs / 102 rows |
| ClinVar | 93 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 815 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'FRZB'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 93 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 24 traits by best p-value, aggregated from 46 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q92765 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000162998/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/FRZB — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/FRZB — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=FRZB%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/FRZB — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:43:06  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
