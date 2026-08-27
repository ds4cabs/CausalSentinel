# Protein Dossier — CHIC2 (Cysteine-rich hydrophobic domain-containing protein 2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Creatinine (enzymatic) in urine | -0.0295 | 0.0108 | 0.00648 | Wald ratio | 1 | trans | NA |
| Mean cell haemoglobin concentration | 0.0427 | 0.0161 | 0.008 | Wald ratio | 1 | trans | NA |
| IgA nephropathy | 1.05 | 0.396 | 0.0082 | Wald ratio | 1 | trans | NA |
| Serum cystatin C (eGFRcys) | 0.0224 | 0.00874 | 0.0105 | Wald ratio | 1 | trans | NA |
| Serum creatinine (eGFRcrea) | 0.00979 | 0.00385 | 0.0109 | Wald ratio | 1 | trans | NA |
| Urinary albumin-to-creatinine ratio | 0.0699 | 0.028 | 0.0124 | Wald ratio | 1 | trans | NA |
| Triglycerides | -0.0517 | 0.021 | 0.0136 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: anxiety or panic attacks | -0.341 | 0.141 | 0.0153 | Wald ratio | 1 | trans | NA |
| Fasting glucose | -0.0318 | 0.014 | 0.0229 | Wald ratio | 1 | trans | NA |
| Femoral neck bone mineral density | -0.0737 | 0.0348 | 0.0343 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: R10 Abdominal and pelvic pain | -0.132 | 0.0627 | 0.0356 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: osteoarthritis | -0.0859 | 0.0414 | 0.0378 | Wald ratio | 1 | trans | NA |
| _...and 113 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_10 association rows across 7 traits (6 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Red blood cell erythrocyte count (UKB data field 30010) | 3e-12 | rs370728588 | 1 | GCST90468098 | no MR -> candidate analysis |
| Corpus callosum posterior volume | 8e-9 | rs751410660 | 1 | GCST90281348 | no MR -> candidate analysis |
| Corpus callosum posterior subregion volume | 1e-8 | rs7674765 | 2 | GCST90728575 | no MR -> candidate analysis |
| Odor identification (fish) | 4e-8 | rs73252922 | 1 | GCST90628027 | no MR -> candidate analysis |
| Total corpus callosum volume | 4e-8 | rs10033247 | 1 | GCST90728576 | no MR -> candidate analysis |
| Post bronchodilator FEV1/FVC ratio | 1e-6 | rs192046469 | 3 | GCST003264 | no MR -> candidate analysis |
| Pregnancy loss in nulliparas | 2e-6 | rs60907021 | 1 | GCST90429686 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.007, LOEUF=0.847 — LoF-tolerant |
| GWAS Catalog | 51 unique SNPs / 94 rows |
| ClinVar | 39 records; 8 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 361 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CHIC2'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 39 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 7 of 7 traits by best p-value, aggregated from 10 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9UKJ5 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000109220/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CHIC2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CHIC2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CHIC2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CHIC2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:50:22  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
