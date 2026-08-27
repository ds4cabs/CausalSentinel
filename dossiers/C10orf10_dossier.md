# Protein Dossier — C10orf10 (Protein DEPP1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Amyotrophic lateral sclerosis | 0.0553 | 0.0224 | 0.0134 | Wald ratio | 1 | trans | NA |
| Squamous cell lung cancer | -0.0918 | 0.0415 | 0.0272 | Wald ratio | 1 | trans | NA |
| Eczema | 0.0504 | 0.0294 | 0.0865 | Wald ratio | 1 | trans | NA |
| Rheumatoid arthritis | -0.0254 | 0.015 | 0.0899 | Wald ratio | 1 | trans | NA |
| Neuroticism | 0.0086 | 0.00516 | 0.0956 | Wald ratio | 1 | trans | NA |
| High grade serous ovarian cancer | -0.0257 | 0.0169 | 0.128 | Wald ratio | 1 | trans | NA |
| Lung cancer | -0.042 | 0.0287 | 0.143 | Wald ratio | 1 | trans | NA |
| Caudate volume | 12.4 | 8.66 | 0.152 | Wald ratio | 1 | trans | NA |
| Forearm bone mineral density | -0.086 | 0.0791 | 0.277 | Wald ratio | 1 | trans | NA |
| Alzheimer's disease | -0.0183 | 0.0171 | 0.284 | Wald ratio | 1 | trans | NA |
| Femoral neck bone mineral density | -0.0349 | 0.0337 | 0.301 | Wald ratio | 1 | trans | NA |
| Amygdala volume | -3.98 | 4.23 | 0.346 | Wald ratio | 1 | trans | NA |
| _...and 5 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_No GWAS Catalog associations mapped to this gene._

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 106 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| placental abruption | 0.076 | — | common-variant locus | no MR -> candidate analysis |
| malignant renal pelvis neoplasm | 0.073 | — | common-variant locus | no MR -> candidate analysis |
| psoriatic arthritis | 0.062 | — | common-variant locus | no MR -> candidate analysis |
| stroke disorder | 0.053 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.053 | — | common-variant locus | no MR -> candidate analysis |
| cellulitis | 0.048 | — | common-variant locus | no MR -> candidate analysis |
| abscess | 0.048 | — | common-variant locus | no MR -> candidate analysis |
| Hydrocephalus | 0.046 | — | common-variant locus | no MR -> candidate analysis |
| prostate carcinoma | 0.042 | — | common-variant locus | no MR -> candidate analysis |

> Of the 9 rows above, **9 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | not available |
| GWAS Catalog | 1 unique SNPs / 2 rows |
| ClinVar | no records |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 106 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'C10orf10'.
- **`gnomad`** — No gnomAD constraint data.
- **`clinvar`** — No ClinVar records.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — No GWAS Catalog associations mapped to this gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9NTK1 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000165507/associations — _Open Targets data release 26.06_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/C10orf10 — _GWAS Catalog REST (live; release not exposed by this endpoint)_

## Provenance

- Generated: 2026-08-14T01:19:41  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
