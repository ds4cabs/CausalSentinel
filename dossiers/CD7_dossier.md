# Protein Dossier — CD7 (T-cell antigen CD7)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: asthma | -0.0467 | 0.0171 | 0.00639 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: high cholesterol | 0.0411 | 0.0152 | 0.00667 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: psoriasis | -0.179 | 0.066 | 0.00676 | Wald ratio | 1 | cis | NA |
| Eczema | -0.132 | 0.0501 | 0.00836 | Wald ratio | 1 | cis | NA |
| Sleep duration | -0.0111 | 0.00455 | 0.015 | Wald ratio | 1 | cis | NA |
| Knee osteoarthritis | 0.169 | 0.0718 | 0.0186 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | 0.0568 | 0.0245 | 0.0206 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I84 Haemorrhoids | 0.0746 | 0.0349 | 0.0322 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K80 Cholelithiasis | 0.0788 | 0.0376 | 0.0361 | Wald ratio | 1 | cis | NA |
| Red blood cell count | 0.0149 | 0.00717 | 0.0382 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K40 Inguinal hernia | -0.0766 | 0.0386 | 0.0471 | Wald ratio | 1 | cis | NA |
| Cigarettes smoked per day | 0.725 | 0.388 | 0.0618 | Wald ratio | 1 | cis | NA |
| _...and 83 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_5 association rows across 5 traits (5 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| T-cell antigen CD7 levels | 5e-145 | rs3176831 | 1 | GCST90249782 | no MR -> candidate analysis |
| Monocyte percentage (UKB data field 30190) | 6e-24 | rs3176831 | 1 | GCST90468091 | no MR -> candidate analysis |
| Benign neoplasm of thyroid glands (PheCode 226) | 7e-12 | rs117913733 | 1 | GCST90651229 | no MR -> candidate analysis |
| Roundabout homolog 1 protein levels (SomaScan ID:12008-3) | 1e-8 | rs60894553 | 1 | GCST90440949 | no MR -> candidate analysis |
| Hypothyroidism | 2e-8 | rs60894553 | 1 | GCST90627750 | MR: beta=0.0568, p=0.0206 (cis) |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 778 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| benign thyroid gland neoplasm | 0.377 | — | common-variant locus | no MR -> candidate analysis |
| hypothyroidism | 0.21 | — | common-variant locus | MR: beta=0.0568, p=0.0206 (cis) |

> Of the 2 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.2e-07, LOEUF=1.58 — LoF-tolerant |
| GWAS Catalog | 60 unique SNPs / 120 rows |
| ClinVar | 89 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 778 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CD7'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 89 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 5 of 5 traits by best p-value, aggregated from 5 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P09564 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000173762/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CD7 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CD7 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CD7%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CD7 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:44:14  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
