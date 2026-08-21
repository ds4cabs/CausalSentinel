# Protein Dossier — CD48 (CD48 antigen)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Eye problems or disorders: Diabetes related eye disease | 0.303 | 0.0894 | 6.97e-04 | Wald ratio | 1 | cis | NA |
| Alcohol intake frequency | 0.0432 | 0.0138 | 0.00178 | Wald ratio | 1 | cis | NA |
| Weight | 0.0203 | 0.00826 | 0.0141 | Wald ratio | 1 | cis | NA |
| Happiness | 0.0281 | 0.0116 | 0.0154 | Wald ratio | 1 | cis | NA |
| Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0686 | 0.0288 | 0.0172 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M16 Coxarthrosis [arthrosis of hip] | -0.221 | 0.0982 | 0.0248 | Wald ratio | 1 | cis | NA |
| Sodium in urine | 0.0205 | 0.00921 | 0.0258 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: pernicious anaemia | 0.288 | 0.132 | 0.0293 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N40 Hyperplasia of prostate | 0.178 | 0.0821 | 0.03 | Wald ratio | 1 | cis | NA |
| ER-positive Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0728 | 0.0345 | 0.0349 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K80 Cholelithiasis | 0.117 | 0.0582 | 0.0452 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: bladder problem (not cancer) | -0.363 | 0.184 | 0.0481 | Wald ratio | 1 | cis | NA |
| _...and 62 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3292_75_1` | CD48 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_50 association rows across 28 traits (48 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating CD48 levels | 9e-1653 | rs10908797 | 3 | GCST90860011 | no MR -> candidate analysis |
| Circulating SLAMF7 levels | 1e-821 | rs66692283 | 2 | GCST90859745 | no MR -> candidate analysis |
| SLAM family member 7 levels | 1e-169 | rs2090756 | 3 | GCST90249565 | no MR -> candidate analysis |
| CD48 protein levels | 8e-135 | rs1503851 | 7 | GCST90468635 | no MR -> candidate analysis |
| SLAMF7 protein levels | 4e-90 | rs111287847 | 6 | GCST90470651 | no MR -> candidate analysis |
| CD48 antigen levels | 2e-50 | rs1980606 | 5 | GCST90246944 | no MR -> candidate analysis |
| Serum levels of protein SLAMF7 | 3e-44 | rs3845628 | 1 | GCST90089059 | no MR -> candidate analysis |
| LY9 protein levels | 4e-39 | rs71639027 | 2 | GCST90469824 | no MR -> candidate analysis |
| Serum levels of protein CD48 | 9e-35 | rs140833109 | 2 | GCST90088294 | no MR -> candidate analysis |
| Cerebrospinal fluid protein CD48 levels | 2e-32 | rs10489637 | 1 | GCST90944166 | no MR -> candidate analysis |
| CD48 antigen levels (CD48.3292.75.1) | 1e-25 | rs12124234 | 1 | GCST90240643 | no MR -> candidate analysis |
| Circulating TNFRSF10C levels | 1e-22 | rs11584616 | 1 | GCST90859942 | no MR -> candidate analysis |
| _...and 16 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 289 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Decreased total leukocyte count | 0.466 | — | common-variant locus | no MR -> candidate analysis |
| multiple sclerosis | 0.036 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=4.7e-07, LOEUF=1.32 — LoF-tolerant |
| GWAS Catalog | 117 unique SNPs / 256 rows |
| ClinVar | 71 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 289 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CD48'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 71 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 28 traits by best p-value, aggregated from 50 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P09326 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000117091/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CD48 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CD48 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CD48%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CD48 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:43:14  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
