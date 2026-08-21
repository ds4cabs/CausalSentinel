# Protein Dossier — CCL5 (C-C motif chemokine 5)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Neo-agreeableness | -0.811 | 0.237 | 6.11e-04 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | 0.0309 | 0.00902 | 6.16e-04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertrophic cardiomyopathy (hcm  or  hocm) | 0.91 | 0.278 | 0.00107 | Wald ratio | 1 | cis | NA |
| Birth weight | 0.0364 | 0.0133 | 0.00616 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Wrist | 0.143 | 0.056 | 0.0106 | Wald ratio | 1 | cis | NA |
| Percent emphysema | 0.0749 | 0.0309 | 0.0155 | Wald ratio | 1 | cis | NA |
| Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0535 | 0.0231 | 0.0208 | Wald ratio | 1 | cis | NA |
| Autism | 0.243 | 0.105 | 0.021 | Wald ratio | 1 | cis | NA |
| Vascular or heart problems diagnosed by doctor: Angina | 0.104 | 0.0457 | 0.0225 | Wald ratio | 1 | cis | NA |
| Birth length | 0.0798 | 0.0379 | 0.0351 | Wald ratio | 1 | cis | NA |
| Sleep duration | -0.0145 | 0.00704 | 0.0394 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: arthritis (nos) | 0.18 | 0.0875 | 0.0395 | Wald ratio | 1 | cis | NA |
| _...and 102 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2523_31_3` | RANTES | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_11 association rows across 10 traits (11 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating CCL5 levels | 6e-179 | rs2107538 | 1 | GCST90860445 | no MR -> candidate analysis |
| CCL5 protein levels | 2e-169 | rs2107538 | 1 | GCST90468584 | no MR -> candidate analysis |
| Dynorphin A (1-17) levels | 7e-107 | rs2107538 | 1 | GCST90247380 | no MR -> candidate analysis |
| Delta-like protein 3 levels | 2e-73 | rs3817655 | 1 | GCST90247295 | no MR -> candidate analysis |
| C-C motif chemokine 5 levels | 2e-67 | rs7211393 | 2 | GCST90246920 | no MR -> candidate analysis |
| Blood protein levels | 5e-35 | rs2107538 | 1 | GCST006585 | no MR -> candidate analysis |
| Reticulocyte percentage (UKB data field 30240) | 1e-14 | rs41471045 | 1 | GCST90468101 | no MR -> candidate analysis |
| Reticulocyte count (UKB data field 30250) | 1e-14 | rs41471045 | 1 | GCST90468100 | no MR -> candidate analysis |
| CCL16 protein levels | 2e-12 | rs28914803 | 1 | GCST90468568 | no MR -> candidate analysis |
| C-C motif chemokine 5 (analyte X5480.49) levels | 2e-10 | rs1800825 | 1 | GCST90426363 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1352 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| poisoning | 0.261 | — | common-variant locus | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (C-C motif chemokine 5) |
| gnomAD constraint | pLI=0.085, LOEUF=1.16 — LoF-tolerant |
| GWAS Catalog | 84 unique SNPs / 165 rows |
| ClinVar | 28 records; 7 pathogenic in sample of 28 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1352 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'CCL5' and resolved to 'C-C motif chemokine 5' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 28 record(s) retrieved, NOT over all 28 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 10 of 10 traits by best p-value, aggregated from 11 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P13501 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000271503/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL1275217/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CCL5 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CCL5 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CCL5%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CCL5 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:38:34  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
