# Protein Dossier — CD5L (CD5 antigen-like)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: diverticular disease or diverticulitis | 0.215 | 0.0665 | 0.00124 | Wald ratio | 1 | cis | NA |
| Large vessel disease | -0.338 | 0.122 | 0.00557 | Wald ratio | 1 | cis | NA |
| Ischemic stroke | -0.152 | 0.0575 | 0.00828 | Wald ratio | 1 | cis | NA |
| Neuroblastoma | -0.379 | 0.154 | 0.0139 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: osteoarthritis | -0.0767 | 0.0314 | 0.0144 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: B37 Candidiasis | 0.588 | 0.247 | 0.0171 | Wald ratio | 1 | cis | NA |
| Depressive symptoms | -0.0246 | 0.0105 | 0.0196 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hyperthyroidism or thyrotoxicosis | -0.33 | 0.144 | 0.0217 | Wald ratio | 1 | cis | NA |
| Total cholesterol | -0.0414 | 0.0182 | 0.0233 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C61 Malignant neoplasm of prostate | 0.195 | 0.0883 | 0.0273 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | 0.0241 | 0.0112 | 0.0315 | Wald ratio | 1 | cis | NA |
| Small vessel disease | -0.261 | 0.129 | 0.0435 | Wald ratio | 1 | cis | NA |
| _...and 89 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3293_2_4` | CD5L | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_62 association rows across 29 traits (56 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| CD5L protein levels | 3e-193 | rs2765501 | 5 | GCST90468640 | no MR -> candidate analysis |
| CD5 antigen-like levels | 2e-166 | rs2765501 | 5 | GCST90246946 | no MR -> candidate analysis |
| FCRL3 protein levels | 7e-144 | rs11264843 | 17 | GCST90469207 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 2e-91 | rs2765496 | 3 | GCST90838667 | no MR -> candidate analysis |
| Circulating FCRL3 levels | 7e-83 | rs112278796 | 1 | GCST90860213 | no MR -> candidate analysis |
| Blood protein levels | 2e-82 | rs2765496 | 4 | GCST006585 | no MR -> candidate analysis |
| Neutrophil count | 1e-59 | rs927698 | 1 | GCST90101731 | no MR -> candidate analysis |
| Serum levels of protein FCRL1 | 5e-59 | rs2777817 | 1 | GCST90089174 | no MR -> candidate analysis |
| White blood cell count | 5e-49 | rs927698 | 1 | GCST90101726 | no MR -> candidate analysis |
| FCRL1 protein levels | 2e-32 | rs4971116 | 5 | GCST90469205 | no MR -> candidate analysis |
| C1QA protein levels | 4e-30 | rs2765501 | 1 | GCST90468485 | no MR -> candidate analysis |
| Serum levels of protein CD5L | 2e-24 | rs2765501 | 1 | GCST90088295 | no MR -> candidate analysis |
| _...and 17 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 537 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| functional neutrophil defect | 0.572 | — | common-variant locus | no MR -> candidate analysis |
| Dysmetria | 0.35 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=2.6e-13, LOEUF=1.25 — LoF-tolerant |
| GWAS Catalog | 100 unique SNPs / 180 rows |
| ClinVar | 63 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 537 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CD5L'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 63 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 29 traits by best p-value, aggregated from 62 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O43866 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000073754/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CD5L — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CD5L — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CD5L%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CD5L — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:44:00  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
