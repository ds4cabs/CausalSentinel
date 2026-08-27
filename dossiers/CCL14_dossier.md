# Protein Dossier — CCL14 (C-C motif chemokine 14)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Melanoma | 0.234 | 0.102 | 0.0217 | Wald ratio | 1 | cis | NA |
| Anorexia nervosa | 0.1 | 0.0512 | 0.0503 | Wald ratio | 1 | cis | NA |
| Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0246 | 0.0126 | 0.0504 | Inverse variance weighted | 2 | trans | NA |
| Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0246 | 0.0126 | 0.0504 | Inverse variance weighted | 2 | cis | NA |
| Non-cancer illness code  self-reported: gout | -0.0892 | 0.0469 | 0.0573 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: gout | -0.0892 | 0.0469 | 0.0573 | Inverse variance weighted | 2 | cis | NA |
| Diagnoses - main ICD10: S76 Injury of muscle and tendon at hip and thigh level | 0.375 | 0.212 | 0.0771 | Inverse variance weighted | 2 | trans | NA |
| Diagnoses - main ICD10: S76 Injury of muscle and tendon at hip and thigh level | 0.375 | 0.212 | 0.0771 | Inverse variance weighted | 2 | cis | NA |
| Platelet count | 1.25 | 0.705 | 0.0775 | Inverse variance weighted | 2 | trans | NA |
| Platelet count | 1.25 | 0.705 | 0.0775 | Inverse variance weighted | 2 | cis | NA |
| Urate | 0.0191 | 0.011 | 0.0829 | Inverse variance weighted | 2 | trans | NA |
| Urate | 0.0191 | 0.011 | 0.0829 | Inverse variance weighted | 2 | cis | NA |
| _...and 151 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2900_53_3` | HCC-1 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_139 association rows across 61 traits (132 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating CCL15 levels | 2e-5134 | rs854624 | 3 | GCST90859974 | no MR -> candidate analysis |
| CCL14/CCL23 protein level ratio | 8e-1578 | rs72830000 | 1 | GCST90313678 | no MR -> candidate analysis |
| C-C motif chemokine 15 levels | 3e-1432 | rs854628 | 12 | GCST90246903 | no MR -> candidate analysis |
| CCL15/CCL23 protein level ratio | 4e-1384 | rs75238886 | 1 | GCST90313681 | no MR -> candidate analysis |
| CCL14/CST3 protein level ratio | 1e-1319 | rs72830000 | 1 | GCST90313679 | no MR -> candidate analysis |
| Circulating CCL14 levels | 5e-1269 | rs9892586 | 2 | GCST90860489 | no MR -> candidate analysis |
| Circulating CCL23 levels (id: OID00530_OID20693) | 2e-1094 | rs712048 | 3 | GCST90859884 | no MR -> candidate analysis |
| Circulating CCL23 levels (id: OID00811_OID20693) | 2e-846 | rs712048 | 3 | GCST90860141 | no MR -> candidate analysis |
| C-C motif chemokine 14 levels | 2e-763 | rs7222922 | 10 | GCST90246902 | no MR -> candidate analysis |
| C-C motif chemokine 15 levels (CCL15.14109.15.3) | 3e-411 | rs854624 | 1 | GCST90240483 | no MR -> candidate analysis |
| Ck-beta-8-1 levels | 9e-326 | rs712048 | 3 | GCST90247039 | no MR -> candidate analysis |
| Serum levels of protein CCL15 | 3e-293 | rs41508645 | 1 | GCST90088428 | no MR -> candidate analysis |
| _...and 49 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 134 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Raynaud disease | 0.035 | — | common-variant locus | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.0012, LOEUF=1.76 — LoF-tolerant |
| GWAS Catalog | 151 unique SNPs / 378 rows |
| ClinVar | 26 records; 8 pathogenic in sample of 26 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 134 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CCL14'.
- **`clinvar`** — Pathogenic count is over the 26 record(s) retrieved, NOT over all 26 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 61 traits by best p-value, aggregated from 139 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q16627 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000276409/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CCL14 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CCL14 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CCL14%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CCL14 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:30:59  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
