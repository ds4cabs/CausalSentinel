# Protein Dossier — OSCAR (Osteoclast-associated immunoglobulin-like receptor)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Urinary albumin-to-creatinine ratio | 0.283 | 0.0942 | 0.0027 | Wald ratio | 1 | cis | NA |
| Microalbuminuria | 0.688 | 0.275 | 0.0124 | Wald ratio | 1 | cis | NA |
| Underlying (primary) cause of death: ICD10: E85.4 Organ-limited amyloidosis | 2.1 | 0.893 | 0.0189 | Wald ratio | 1 | cis | NA |
| Subjective well being | 0.0652 | 0.029 | 0.0244 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M54 Dorsalgia | 0.233 | 0.11 | 0.0333 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hiatus hernia | 0.196 | 0.0958 | 0.0409 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: migraine | 0.175 | 0.0859 | 0.0413 | Wald ratio | 1 | cis | NA |
| Cough on most days | 0.157 | 0.0774 | 0.042 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: gastro-oesophageal reflux (gord)  or  gastric reflux | -0.216 | 0.106 | 0.0424 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K35 Acute appendicitis | 0.367 | 0.182 | 0.0438 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: S66 Injury of muscle and tendon at wrist and hand level | 0.556 | 0.276 | 0.0441 | Wald ratio | 1 | cis | NA |
| Cigarettes smoked per day | -1.42 | 0.732 | 0.0524 | Wald ratio | 1 | cis | NA |
| _...and 83 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_21 association rows across 7 traits (21 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating OSCAR levels | 2e-729 | rs61742142 | 5 | GCST90859821 | no MR -> candidate analysis |
| OSCAR protein levels | 1e-275 | rs142964852 | 4 | GCST90470131 | no MR -> candidate analysis |
| VSTM1 protein levels | 4e-212 | rs35769057 | 5 | GCST90471055 | no MR -> candidate analysis |
| Osteoclast-associated immunoglobulin-like receptor levels | 3e-133 | rs61742142 | 3 | GCST90179316 | no MR -> candidate analysis |
| Cerebrospinal fluid protein OSCAR levels | 7e-118 | rs1657535 | 1 | GCST90944473 | no MR -> candidate analysis |
| Osteoclast-associated immunoglobulin-like receptor (analyte  | 8e-29 | rs1657535 | 1 | GCST90427450 | no MR -> candidate analysis |
| LILRB1 protein levels | 1e-18 | rs663569 | 2 | GCST90469776 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.3e-08, LOEUF=1.28 — LoF-tolerant |
| GWAS Catalog | 175 unique SNPs / 424 rows |
| ClinVar | 87 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 113 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'OSCAR'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 87 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 7 of 7 traits by best p-value, aggregated from 21 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q8IYS5 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000170909/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/OSCAR — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/OSCAR — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=OSCAR%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/OSCAR — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:10:06  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
