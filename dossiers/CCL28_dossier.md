# Protein Dossier — CCL28 (C-C motif chemokine 28)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: K43 Ventral hernia | 0.31 | 0.0848 | 2.56e-04 | Inverse variance weighted | 2 | trans | NA |
| Diagnoses - main ICD10: K43 Ventral hernia | 0.31 | 0.0848 | 2.56e-04 | Inverse variance weighted | 2 | trans | NA |
| Height | 0.034 | 0.0121 | 0.00511 | Wald ratio | 1 | trans | NA |
| Systemic lupus erythematosus | 0.49 | 0.188 | 0.00927 | Wald ratio | 1 | trans | NA |
| PGC cross-disorder traits | -0.0983 | 0.0389 | 0.0116 | Inverse variance weighted | 2 | trans | NA |
| PGC cross-disorder traits | -0.0983 | 0.0389 | 0.0116 | Inverse variance weighted | 2 | trans | NA |
| Iron | 0.0992 | 0.0413 | 0.0163 | Wald ratio | 1 | trans | NA |
| Amygdala volume | -17.8 | 7.44 | 0.0171 | Inverse variance weighted | 2 | trans | NA |
| Amygdala volume | -17.8 | 7.44 | 0.0171 | Inverse variance weighted | 2 | trans | NA |
| Schizophrenia | -0.0795 | 0.0339 | 0.0189 | Inverse variance weighted | 2 | trans | NA |
| Schizophrenia | -0.0795 | 0.0339 | 0.0189 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: asthma | 0.0472 | 0.0204 | 0.0209 | Inverse variance weighted | 2 | trans | NA |
| _...and 159 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2890_59_2` | CCL28 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_30 association rows across 22 traits (21 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating CCL28 levels | 7e-27 | rs4866742 | 1 | GCST90859892 | no MR -> candidate analysis |
| GHR protein levels | 3e-21 | rs77860766 | 2 | GCST90469342 | no MR -> candidate analysis |
| C7 protein levels | 5e-18 | rs141365528 | 1 | GCST90468502 | no MR -> candidate analysis |
| CCL28 protein levels | 2e-17 | rs371029709 | 1 | GCST90468580 | no MR -> candidate analysis |
| High light scatter reticulocyte percentage (UKB data field 3 | 4e-17 | rs750583 | 1 | GCST90468077 | no MR -> candidate analysis |
| Red cell distribution width | 2e-16 | rs750583 | 2 | GCST90002369 | no MR -> candidate analysis |
| Red blood cell erythrocyte distribution width (UKB data fiel | 3e-16 | rs750583 | 1 | GCST90468099 | no MR -> candidate analysis |
| High light scatter reticulocyte percentage of red cells | 9e-14 | rs372212227 | 1 | GCST90002386 | no MR -> candidate analysis |
| High light scatter reticulocyte count | 1e-13 | rs372212227 | 1 | GCST90002385 | no MR -> candidate analysis |
| Immature fraction of reticulocytes | 8e-13 | rs372212227 | 1 | GCST90002387 | no MR -> candidate analysis |
| Self-reported math ability (MTAG) | 1e-12 | rs56206275 | 1 | GCST006569 | no MR -> candidate analysis |
| Self-reported math ability | 9e-11 | rs56206275 | 1 | GCST006573 | no MR -> candidate analysis |
| _...and 10 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 515 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| mathematical ability | 0.172 | — | common-variant locus | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.11, LOEUF=1.29 — LoF-tolerant |
| GWAS Catalog | 46 unique SNPs / 89 rows |
| ClinVar | 47 records; 7 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 515 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CCL28'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 47 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 22 traits by best p-value, aggregated from 30 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9NRJ3 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000151882/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CCL28 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CCL28 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CCL28%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CCL28 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:37:15  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
