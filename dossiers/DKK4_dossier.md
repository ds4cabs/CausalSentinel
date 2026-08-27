# Protein Dossier — DKK4 (Dickkopf-related protein 4)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: hyperthyroidism or thyrotoxicosis | 0.33 | 0.0588 | 1.88e-08 | Wald ratio | 1 | trans | NA |
| Lumbar spine bone mineral density | 0.0688 | 0.025 | 0.00585 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: diverticular disease or diverticulitis | -0.227 | 0.0839 | 0.00682 | Wald ratio | 1 | trans | NA |
| Femoral neck bone mineral density | 0.0557 | 0.0214 | 0.00926 | Wald ratio | 1 | trans | NA |
| Height | 0.0217 | 0.00841 | 0.0097 | Wald ratio | 1 | trans | NA |
| Cigarettes smoked per day | -0.6 | 0.235 | 0.0108 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: muscle or soft tissue injuries | -0.253 | 0.108 | 0.0195 | Wald ratio | 1 | trans | NA |
| Cardioembolic stroke | 0.21 | 0.091 | 0.021 | Wald ratio | 1 | trans | NA |
| Fractured or broken bones in last 5 years | -0.0498 | 0.023 | 0.0303 | Wald ratio | 1 | trans | NA |
| Forced expiratory volume in 1-second (FEV1) | 0.0128 | 0.00606 | 0.0342 | Wald ratio | 1 | trans | NA |
| Crohn's disease | -0.0727 | 0.0362 | 0.0447 | Wald ratio | 1 | trans | NA |
| Depressive symptoms | -0.0203 | 0.0101 | 0.0455 | Wald ratio | 1 | trans | NA |
| _...and 94 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3365_7_2` | Dkk-4 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_4 association rows across 3 traits (4 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Mean sphered cell volume (UKB data field 30270) | 5e-34 | rs113111764 | 1 | GCST90468089 | no MR -> candidate analysis |
| Mean reticulocyte volume (UKB data field 30260) | 3e-29 | rs113111764 | 2 | GCST90468088 | no MR -> candidate analysis |
| Dickkopf-related protein 4 levels | 3e-14 | rs77736087 | 1 | GCST90059943 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 120 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| osteoarthritis | 0.415 | — | common-variant locus | MR: beta=-0.137, p=0.0903 (trans) |
| Abnormality of the skeletal system | 0.077 | — | common-variant locus | no MR -> candidate analysis |
| tonsillitis | 0.076 | — | common-variant locus | no MR -> candidate analysis |
| ovarian dysfunction | 0.064 | — | common-variant locus | no MR -> candidate analysis |
| osteoarthritis, knee | 0.059 | — | common-variant locus | MR: beta=-0.137, p=0.0903 (trans) |
| Loss of consciousness | 0.038 | — | common-variant locus | no MR -> candidate analysis |

> Of the 6 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=4.4e-06, LOEUF=1.59 — LoF-tolerant |
| GWAS Catalog | 31 unique SNPs / 59 rows |
| ClinVar | 103 records; 5 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 120 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'DKK4'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 103 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 3 of 3 traits by best p-value, aggregated from 4 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9UBT3 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000104371/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/DKK4 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/DKK4 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=DKK4%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/DKK4 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:17:55  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
