# Protein Dossier — FAM151A (Protein FAM151A)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Underlying (primary) cause of death: ICD10: E85.4 Organ-limited amyloidosis | 2.03 | 0.321 | 2.77e-10 | Wald ratio | 1 | cis | 0.0156 |
| Non-cancer illness code  self-reported: vaginal prolapse or uterine prolapse | 0.301 | 0.0977 | 0.00207 | Wald ratio | 1 | cis | NA |
| Low grade serous ovarian cancer | 0.484 | 0.196 | 0.0133 | Wald ratio | 1 | cis | NA |
| Pallidum volume | -18.4 | 7.47 | 0.0137 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: S76 Injury of muscle and tendon at hip and thigh level | 0.626 | 0.266 | 0.0185 | Wald ratio | 1 | cis | NA |
| Microalbuminuria | 0.181 | 0.0792 | 0.0223 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | 0.0361 | 0.0158 | 0.0227 | Wald ratio | 1 | cis | NA |
| Years of schooling | 0.0339 | 0.0151 | 0.0244 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Wrist | -0.188 | 0.0837 | 0.0246 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: retinal detachment | 0.288 | 0.128 | 0.0247 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K80 Cholelithiasis | -0.171 | 0.0802 | 0.033 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hayfever or allergic rhinitis | -0.0893 | 0.0434 | 0.0397 | Wald ratio | 1 | cis | NA |
| _...and 87 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_3 association rows across 3 traits (3 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Protein FAM151A levels | 5e-74 | rs373739034 | 1 | GCST90247523 | no MR -> candidate analysis |
| Protein FAM151A levels (FAM151A.7856.51.3) | 3e-16 | rs373739034 | 1 | GCST90242450 | no MR -> candidate analysis |
| Gut microbiome abundance (class Tyzzerella sp. 3 (at 3 month | 2e-8 | rs2317686 | 1 | GCST90568581 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 46 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| COVID-19 | 0.548 | — | common-variant locus | no MR -> candidate analysis |
| placental retention | 0.47 | — | common-variant locus | no MR -> candidate analysis |
| Hyperhidrosis | 0.462 | — | common-variant locus | no MR -> candidate analysis |
| anus neoplasm | 0.121 | — | common-variant locus | no MR -> candidate analysis |
| colonic neoplasm | 0.121 | — | common-variant locus | no MR -> candidate analysis |
| rectal neoplasm | 0.121 | — | common-variant locus | no MR -> candidate analysis |
| cholelithiasis | 0.051 | — | common-variant locus | MR: beta=-0.171, p=0.033 (cis) |

> Of the 7 rows above, **6 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.1e-14, LOEUF=1.32 — LoF-tolerant |
| GWAS Catalog | 39 unique SNPs / 78 rows |
| ClinVar | 156 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 46 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'FAM151A'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 156 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 3 of 3 traits by best p-value, aggregated from 3 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q8WW52 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000162391/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/FAM151A — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/FAM151A — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=FAM151A%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/FAM151A — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:32:49  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
