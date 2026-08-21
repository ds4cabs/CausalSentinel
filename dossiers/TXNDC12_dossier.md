# Protein Dossier — TXNDC12 (Thioredoxin domain-containing protein 12)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Inflammatory bowel disease | 0.134 | 0.0147 | 9.90e-20 | Wald ratio | 1 | trans | 3.07e-31 |
| Crohn's disease | 0.133 | 0.0178 | 6.13e-14 | Wald ratio | 1 | trans | 9.83e-18 |
| Ulcerative colitis | 0.132 | 0.0184 | 5.86e-13 | Wald ratio | 1 | trans | 2.28e-22 |
| Serum creatinine (eGFRcrea) | 0.00548 | 0.0013 | 2.51e-05 | Wald ratio | 1 | trans | NA |
| Transferrin Saturation | -0.0592 | 0.0152 | 1.00e-04 | Wald ratio | 1 | trans | NA |
| Iron | -0.0586 | 0.0151 | 1.08e-04 | Wald ratio | 1 | trans | NA |
| Primary sclerosing cholangitis  | 0.163 | 0.0436 | 1.86e-04 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: hypertension | 0.0215 | 0.00607 | 3.86e-04 | Wald ratio | 1 | trans | NA |
| Age at menarche | -0.0297 | 0.00884 | 7.70e-04 | Wald ratio | 1 | trans | NA |
| Anorexia nervosa | 0.172 | 0.0512 | 7.82e-04 | Wald ratio | 1 | trans | NA |
| Heel bone mineral density (BMD) T-score  automated | -0.0156 | 0.00471 | 9.25e-04 | Wald ratio | 1 | trans | NA |
| Serum cystatin C (eGFRcys) | 0.00929 | 0.00288 | 0.00126 | Wald ratio | 1 | trans | NA |
| _...and 117 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4815_25_3` | TXD12 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_2 association rows across 2 traits (0 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Plasma PCSK9 levels | 1e-7 | rs35120342 | 1 | GCST90085917 | no MR -> candidate analysis |
| General cognitive ability | 2e-7 | rs12406969 | 1 | GCST006269 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 90 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| protozoa infectious disease | 0.389 | — | common-variant locus | no MR -> candidate analysis |
| response to statin | 0.033 | — | common-variant locus | no MR -> candidate analysis |
| knee fracture | 0.032 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.2e-07, LOEUF=1.3 — LoF-tolerant |
| GWAS Catalog | 6 unique SNPs / 12 rows |
| ClinVar | 94 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 90 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'TXNDC12'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 94 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 2 of 2 traits by best p-value, aggregated from 2 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O95881 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000117862/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/TXNDC12 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/TXNDC12 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=TXNDC12%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/TXNDC12 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:30:07  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
