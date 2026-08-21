# Protein Dossier — MGAT4B (Alpha-1,3-mannosyl-glycoprotein 4-beta-N-acetylglucosaminyltransferase B)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Weight | -0.024 | 0.00767 | 0.00178 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: deep venous thrombosis (dvt) | 0.151 | 0.0531 | 0.00461 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Diabetes related eye disease | 0.237 | 0.0888 | 0.00777 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: migraine | 0.116 | 0.0448 | 0.00979 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R14 Flatulence and related conditions | 0.542 | 0.223 | 0.015 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | -0.0205 | 0.00869 | 0.0184 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Glaucoma | -0.21 | 0.0906 | 0.0206 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R55 Syncope and collapse | 0.168 | 0.0785 | 0.0328 | Wald ratio | 1 | cis | NA |
| Myocardial infarction | 0.0967 | 0.0461 | 0.036 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hiatus hernia | -0.131 | 0.0653 | 0.0446 | Wald ratio | 1 | cis | NA |
| Pallidum volume | -15.5 | 8.35 | 0.0633 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: muscle or soft tissue injuries | 0.161 | 0.0882 | 0.0685 | Wald ratio | 1 | cis | NA |
| _...and 50 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_10 association rows across 7 traits (9 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Alpha-1,3-mannosyl-glycoprotein 4-beta-N-acetylglucosaminylt | 2e-198 | rs113756550 | 2 | GCST90248466 | no MR -> candidate analysis |
| Blood protein levels | 3e-62 | rs58413676 | 1 | GCST006585 | no MR -> candidate analysis |
| Alpha-1,3-mannosyl-glycoprotein 4-beta-N-acetylglucosaminylt | 2e-29 | rs73351608 | 1 | GCST90240236 | no MR -> candidate analysis |
| Monocyte count | 8e-21 | rs6883116 | 3 | GCST90002340 | no MR -> candidate analysis |
| Platelet count (UKB data field 30080) | 4e-12 | rs6883116 | 1 | GCST90468095 | no MR -> candidate analysis |
| Plateletcrit | 1e-10 | rs6883116 | 1 | GCST90002400 | no MR -> candidate analysis |
| Major depressive disorder | 6e-7 | rs272440 | 1 | GCST006041 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 105 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| neoplasm | 0.267 | — | common-variant locus | MR: beta=0.148, p=0.111 (cis) |
| Abnormality of the skeletal system | 0.079 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=3e-05, LOEUF=0.674 — LoF-tolerant |
| GWAS Catalog | 54 unique SNPs / 108 rows |
| ClinVar | 174 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 105 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'MGAT4B'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 174 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 7 of 7 traits by best p-value, aggregated from 10 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9UQ53 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000161013/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/MGAT4B — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/MGAT4B — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=MGAT4B%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/MGAT4B — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:47:33  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
