# Protein Dossier — SEMG1 (Semenogelin-1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Birth weight | 0.0754 | 0.0196 | 1.15e-04 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: R07 Pain in throat and chest | -0.187 | 0.0667 | 0.00496 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: asthma | -0.105 | 0.0384 | 0.00608 | Wald ratio | 1 | trans | NA |
| Femoral neck bone mineral density | 0.104 | 0.0406 | 0.0101 | Wald ratio | 1 | trans | NA |
| Amygdala volume | -36.7 | 14.6 | 0.0122 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | -0.16 | 0.0646 | 0.0133 | Wald ratio | 1 | trans | NA |
| Eye problems or disorders: Injury or trauma resulting in loss of vision | 0.294 | 0.123 | 0.0164 | Wald ratio | 1 | trans | NA |
| Eczema | 0.228 | 0.114 | 0.0448 | Wald ratio | 1 | trans | NA |
| Fractured or broken bones in last 5 years | 0.0719 | 0.0358 | 0.0448 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: M23 Internal derangement of knee | 0.142 | 0.0723 | 0.049 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: I83 Varicose veins of lower extremities | -0.203 | 0.107 | 0.0576 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: K44 Diaphragmatic hernia | 0.15 | 0.0857 | 0.0793 | Wald ratio | 1 | trans | NA |
| _...and 67 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_6 association rows across 4 traits (5 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Serum levels of protein PI3 | 5e-45 | rs6104052 | 1 | GCST90088842 | no MR -> candidate analysis |
| Blood protein levels | 5e-32 | rs6104052 | 1 | GCST006585 | no MR -> candidate analysis |
| WFDC12 protein levels | 5e-21 | rs2746994 | 3 | GCST90471073 | no MR -> candidate analysis |
| Bipolar disorder | 3e-6 | rs190905111 | 1 | GCST008103 | MR: beta=0.198, p=0.343 (trans) |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.022, LOEUF=1.35 — LoF-tolerant |
| GWAS Catalog | 53 unique SNPs / 106 rows |
| ClinVar | 87 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 70 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'SEMG1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 87 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 4 of 4 traits by best p-value, aggregated from 6 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P04279 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000124233/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/SEMG1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/SEMG1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=SEMG1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/SEMG1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:59:59  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
