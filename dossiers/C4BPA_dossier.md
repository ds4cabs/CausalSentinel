# Protein Dossier — C4BPA (C4b-binding protein alpha chain)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Rheumatoid arthritis | 0.158 | 0.0498 | 0.00155 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: muscle or soft tissue injuries | 0.249 | 0.0806 | 0.00205 | Wald ratio | 1 | cis | NA |
| Forearm bone mineral density | -0.154 | 0.0537 | 0.00418 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hiatus hernia | 0.142 | 0.0496 | 0.00427 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertrophic cardiomyopathy (hcm  or  hocm) | 0.821 | 0.297 | 0.00568 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Glaucoma | -0.241 | 0.0932 | 0.00973 | Wald ratio | 1 | cis | NA |
| Platelet count | 3.48 | 1.42 | 0.0141 | Wald ratio | 1 | cis | NA |
| Lumbar spine bone mineral density | -0.073 | 0.0301 | 0.0152 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R55 Syncope and collapse | 0.183 | 0.0773 | 0.0178 | Wald ratio | 1 | cis | NA |
| Myocardial infarction | 0.0804 | 0.0341 | 0.0183 | Wald ratio | 1 | cis | NA |
| Anorexia nervosa | 0.255 | 0.111 | 0.0212 | Wald ratio | 1 | cis | NA |
| Low grade serous ovarian cancer | -0.414 | 0.18 | 0.0212 | Wald ratio | 1 | cis | NA |
| _...and 101 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_63 association rows across 45 traits (60 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| C4b-binding protein alpha chain levels | 1e-151 | rs34101855 | 1 | GCST90246784 | no MR -> candidate analysis |
| CD55 protein levels | 1e-105 | rs72742944 | 1 | GCST90468637 | no MR -> candidate analysis |
| Serum levels of protein S100A5 | 2e-83 | rs4844573 | 2 | GCST90087838 | no MR -> candidate analysis |
| Killer cell lectin-like receptor subfamily G member 2 levels | 2e-59 | rs2808467 | 1 | GCST90248210 | no MR -> candidate analysis |
| Protein S100-A5 levels (S100A5.14222.68.3) | 1e-58 | rs17020993 | 2 | GCST90242509 | no MR -> candidate analysis |
| Serum levels of protein C4BPA | 3e-50 | rs11120218 | 1 | GCST90090695 | no MR -> candidate analysis |
| Blood protein levels | 9e-45 | rs11120218 | 4 | GCST006585 | no MR -> candidate analysis |
| Platelet distribution width (UKB data field 30110) | 8e-39 | rs11120218 | 1 | GCST90468097 | no MR -> candidate analysis |
| CR1 protein levels | 9e-36 | rs12064010 | 3 | GCST90468851 | no MR -> candidate analysis |
| C1q-related factor levels | 2e-34 | rs4266889 | 1 | GCST90246765 | no MR -> candidate analysis |
| Mean platelet volume | 1e-31 | rs12074166 | 4 | GCST90002346 | MR: beta=0.00606, p=0.104 (cis) |
| C4BPA protein levels | 8e-30 | rs11120218 | 2 | GCST90453101 | no MR -> candidate analysis |
| _...and 33 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 394 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| venous thromboembolism | 0.637 | — | common-variant locus | no MR -> candidate analysis |
| Thromboembolism | 0.503 | — | common-variant locus | no MR -> candidate analysis |
| deep vein thrombosis | 0.393 | — | common-variant locus | no MR -> candidate analysis |
| age-related macular degeneration | 0.083 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.001, LOEUF=0.656 — LoF-tolerant |
| GWAS Catalog | 80 unique SNPs / 165 rows |
| ClinVar | 122 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 394 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'C4BPA'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 122 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 45 traits by best p-value, aggregated from 63 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P04003 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000123838/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/C4BPA — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/C4BPA — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=C4BPA%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/C4BPA — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:22:26  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
