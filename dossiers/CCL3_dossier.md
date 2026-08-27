# Protein Dossier — CCL3 (C-C motif chemokine 3)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Neo-openness to experience | -0.413 | 0.149 | 0.00567 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Injury or trauma resulting in loss of vision | -0.228 | 0.0826 | 0.00583 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: G47 Sleep disorders | -0.197 | 0.0801 | 0.0141 | Wald ratio | 1 | cis | NA |
| HDL cholesterol | 0.0231 | 0.0104 | 0.0258 | Wald ratio | 1 | cis | NA |
| Amyotrophic lateral sclerosis | 0.0795 | 0.0368 | 0.0308 | Wald ratio | 1 | cis | NA |
| Pallidum volume | -8.4 | 3.94 | 0.0331 | Wald ratio | 1 | cis | NA |
| Underlying (primary) cause of death: ICD10: E85.4 Organ-limited amyloidosis | 1.08 | 0.505 | 0.0332 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: J33 Nasal polyp | -0.188 | 0.0885 | 0.0341 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I84 Haemorrhoids | 0.0621 | 0.0303 | 0.0403 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: L03 Cellulitis | -0.131 | 0.0638 | 0.0404 | Wald ratio | 1 | cis | NA |
| Alzheimer's disease | 0.0689 | 0.0337 | 0.0412 | Wald ratio | 1 | cis | NA |
| Eczema | 0.0722 | 0.0363 | 0.0466 | Wald ratio | 1 | cis | NA |
| _...and 78 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3040_59_1` | MIP-1a | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_30 association rows across 23 traits (28 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating CCL3 levels (id: OID00532_OID20610) | 1e-972 | rs1719126 | 2 | GCST90859886 | no MR -> candidate analysis |
| Circulating CCL3 levels (id: OID00440_OID20610) | 3e-934 | rs1719126 | 2 | GCST90859800 | no MR -> candidate analysis |
| Circulating CCL3 levels (id: OID00813_OID20610) | 1e-679 | rs1719126 | 2 | GCST90860143 | no MR -> candidate analysis |
| Macrophage inflammatory protein 1a levels | 1e-202 | rs8951 | 1 | GCST90274825 | no MR -> candidate analysis |
| CCL16 protein levels | 2e-200 | rs148048971 | 2 | GCST90468568 | no MR -> candidate analysis |
| Circulating CCL4 levels (id: OID00796_OID20695) | 2e-156 | rs200657610 | 1 | GCST90860128 | no MR -> candidate analysis |
| CCL4 protein levels | 2e-149 | rs1634513 | 1 | GCST90468583 | no MR -> candidate analysis |
| Circulating CCL4 levels (id: OID00498_OID20695) | 3e-140 | rs200657610 | 1 | GCST90859854 | no MR -> candidate analysis |
| C-C motif chemokine 3-like 1 levels | 6e-69 | rs149759822 | 1 | GCST90137673 | no MR -> candidate analysis |
| CCL14 protein levels | 5e-50 | rs8073437 | 1 | GCST90468566 | no MR -> candidate analysis |
| CCL18 protein levels | 4e-48 | rs1879917 | 2 | GCST90468570 | no MR -> candidate analysis |
| CCL3 protein levels | 2e-45 | rs764872 | 3 | GCST90428428 | no MR -> candidate analysis |
| _...and 11 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.015, LOEUF=1.46 — LoF-tolerant |
| GWAS Catalog | 137 unique SNPs / 335 rows |
| ClinVar | 34 records; 7 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1124 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CCL3'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 34 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 23 traits by best p-value, aggregated from 30 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P10147 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000277632/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CCL3 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CCL3 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CCL3%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CCL3 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:37:32  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
