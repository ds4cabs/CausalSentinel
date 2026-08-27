# Protein Dossier — CCL25 (C-C motif chemokine 25)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Height | -0.0828 | 0.0155 | 9.64e-08 | Wald ratio | 1 | trans | 0.00633 |
| Caudate volume | -34 | 9.89 | 5.90e-04 | Inverse variance weighted | 2 | trans | NA |
| Caudate volume | -34 | 9.89 | 5.90e-04 | Inverse variance weighted | 2 | cis | NA |
| Total cholesterol | -0.0663 | 0.0197 | 7.56e-04 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: hyperthyroidism or thyrotoxicosis | 0.00117 | 0.000372 | 0.00173 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: hyperthyroidism or thyrotoxicosis | 0.00117 | 0.000372 | 0.00173 | Inverse variance weighted | 2 | cis | NA |
| Ischemic stroke | -0.216 | 0.0844 | 0.0103 | Wald ratio | 1 | trans | NA |
| Pancreatic cancer | -0.604 | 0.254 | 0.0175 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: S76 Injury of muscle and tendon at hip and thigh level | 0.0002 | 9.2e-05 | 0.03 | Inverse variance weighted | 2 | trans | NA |
| Diagnoses - main ICD10: S76 Injury of muscle and tendon at hip and thigh level | 0.0002 | 9.2e-05 | 0.03 | Inverse variance weighted | 2 | cis | NA |
| Non-cancer illness code  self-reported: iron deficiency anaemia | -0.000682 | 0.000317 | 0.0312 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: iron deficiency anaemia | -0.000682 | 0.000317 | 0.0312 | Inverse variance weighted | 2 | cis | NA |
| _...and 162 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2705_5_2` | TECK | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_37 association rows across 13 traits (35 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating CCL25 levels | 5e-3726 | rs2032887 | 5 | GCST90859901 | no MR -> candidate analysis |
| C-C motif chemokine 25 levels | 4e-830 | rs2032887 | 9 | GCST90274768 | no MR -> candidate analysis |
| Blood protein levels | 1e-160 | rs77625270 | 2 | GCST006585 | no MR -> candidate analysis |
| C-C motif chemokine 25 levels (CCL25.2705.5.2) | 5e-114 | rs74959615 | 4 | GCST90240493 | no MR -> candidate analysis |
| CCL25 protein levels | 2e-89 | rs112560582 | 6 | GCST90468577 | no MR -> candidate analysis |
| Serum levels of protein CCL25 | 5e-80 | rs7259568 | 3 | GCST90088027 | no MR -> candidate analysis |
| TECK plasma levels | 2e-45 | rs2032887 | 1 | GCST90085778 | no MR -> candidate analysis |
| CCL25 levels | 1e-37 | rs2032887 | 2 | GCST90000446 | no MR -> candidate analysis |
| Cerebrospinal fluid protein CCL25 levels | 7e-22 | rs2032887 | 1 | GCST90943136 | no MR -> candidate analysis |
| Protein levels in obesity | 1e-15 | rs11671930 | 1 | GCST010196 | no MR -> candidate analysis |
| Rickets or osteomalacia (PheCode 261.41) | 2e-11 | rs184027577 | 1 | GCST90479911 | no MR -> candidate analysis |
| Alzheimer's disease or family history of Alzheimer's disease | 4e-8 | rs573469061 | 1 | GCST90624094 | no MR -> candidate analysis |
| _...and 1 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 293 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| vision disorder | 0.057 | — | common-variant locus | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.00033, LOEUF=1.1 — LoF-tolerant |
| GWAS Catalog | 71 unique SNPs / 141 rows |
| ClinVar | 26 records; 6 pathogenic in sample of 26 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 293 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CCL25'.
- **`clinvar`** — Pathogenic count is over the 26 record(s) retrieved, NOT over all 26 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 13 of 13 traits by best p-value, aggregated from 37 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O15444 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000131142/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CCL25 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CCL25 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CCL25%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CCL25 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:36:48  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: pharmgkb
