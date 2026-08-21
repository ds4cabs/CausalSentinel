# Protein Dossier — SPINK6 (Serine protease inhibitor Kazal-type 6)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Serum cystatin C (eGFRcys) | -0.0104 | 0.00359 | 0.00379 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: bone disorder | 0.187 | 0.0776 | 0.0158 | Wald ratio | 1 | cis | NA |
| Lumbar spine bone mineral density | 0.0374 | 0.0169 | 0.0272 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: gout | -0.0861 | 0.0399 | 0.0308 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Diabetes related eye disease | 0.107 | 0.0501 | 0.0325 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypopituitarism | 0.362 | 0.17 | 0.0335 | Wald ratio | 1 | cis | NA |
| Type 2 diabetes | 0.0371 | 0.0186 | 0.0457 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hyperthyroidism or thyrotoxicosis | -0.112 | 0.0568 | 0.049 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R55 Syncope and collapse | 0.0786 | 0.0428 | 0.0661 | Wald ratio | 1 | cis | NA |
| Urate | 0.017 | 0.00945 | 0.0719 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: psoriasis | 0.069 | 0.0383 | 0.0719 | Wald ratio | 1 | cis | NA |
| Chronic kidney disease | 0.0492 | 0.0274 | 0.073 | Wald ratio | 1 | cis | NA |
| _...and 92 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_2 association rows across 2 traits (2 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Blood protein levels | 2e-210 | rs10038416 | 1 | GCST006585 | no MR -> candidate analysis |
| SPINK6 protein levels | 1e-132 | rs74607481 | 1 | GCST90470725 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.2e-05, LOEUF=1.76 — LoF-tolerant |
| GWAS Catalog | 40 unique SNPs / 80 rows |
| ClinVar | 33 records; 10 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 47 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'SPINK6'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 33 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 2 of 2 traits by best p-value, aggregated from 2 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q6UWN8 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000178172/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/SPINK6 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/SPINK6 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=SPINK6%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/SPINK6 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:12:21  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
