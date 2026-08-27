# Protein Dossier — CCL18 (C-C motif chemokine 18)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: G47 Sleep disorders | -0.181 | 0.0712 | 0.0108 | Wald ratio | 1 | cis | NA |
| Rheumatoid arthritis | -0.0717 | 0.0282 | 0.0109 | Wald ratio | 1 | cis | NA |
| Eczema | 0.0805 | 0.0317 | 0.011 | Wald ratio | 1 | cis | NA |
| Neo-openness to experience | -0.317 | 0.128 | 0.0136 | Wald ratio | 1 | cis | NA |
| Amyotrophic lateral sclerosis | 0.0786 | 0.0323 | 0.0149 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Wrist | -0.0803 | 0.035 | 0.022 | Wald ratio | 1 | cis | NA |
| Pallidum volume | -7.87 | 3.44 | 0.0222 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: J33 Nasal polyp | -0.168 | 0.0783 | 0.0317 | Wald ratio | 1 | cis | NA |
| Forearm bone mineral density | 0.0581 | 0.0285 | 0.0417 | Wald ratio | 1 | cis | NA |
| Alzheimer's disease | 0.0558 | 0.0287 | 0.0519 | Wald ratio | 1 | cis | NA |
| Intracranial volume | -6.54e+03 | 3.46e+03 | 0.0585 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R11 Nausea and vomiting | -0.158 | 0.0851 | 0.063 | Wald ratio | 1 | cis | NA |
| _...and 82 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3044_3_2` | PARC | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_89 association rows across 43 traits (85 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating CCL18 levels | 9e-1471 | rs2015086 | 2 | GCST90860473 | no MR -> candidate analysis |
| ANG/CCL18 protein level ratio | 7e-1018 | rs56683451 | 1 | GCST90313258 | no MR -> candidate analysis |
| CCL18/RARRES2 protein level ratio | 2e-1001 | rs56683451 | 1 | GCST90313690 | no MR -> candidate analysis |
| CCL18/TFPI protein level ratio | 4e-986 | rs56683451 | 1 | GCST90313691 | no MR -> candidate analysis |
| C-C motif chemokine 18 levels | 2e-635 | rs2015086 | 10 | GCST90246906 | no MR -> candidate analysis |
| Circulating CCL23 levels (id: OID00530_OID20693) | 3e-360 | rs712046 | 1 | GCST90859884 | no MR -> candidate analysis |
| C-C motif chemokine 3 levels | 2e-314 | rs2015086 | 5 | GCST90246917 | no MR -> candidate analysis |
| CCL16 protein levels | 1e-299 | rs117259529 | 1 | GCST90468568 | no MR -> candidate analysis |
| Circulating CCL14 levels | 4e-296 | rs854466 | 2 | GCST90860489 | no MR -> candidate analysis |
| Circulating CCL23 levels (id: OID00811_OID20693) | 8e-263 | rs712046 | 1 | GCST90860141 | no MR -> candidate analysis |
| CCL15 protein levels | 3e-260 | rs117759380 | 5 | GCST90468567 | no MR -> candidate analysis |
| Serum levels of protein CCL18 | 4e-237 | rs854469 | 2 | GCST90088203 | no MR -> candidate analysis |
| _...and 31 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.0041, LOEUF=1.64 — LoF-tolerant |
| GWAS Catalog | 167 unique SNPs / 409 rows |
| ClinVar | 27 records; 11 pathogenic in sample of 27 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 520 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CCL18'.
- **`clinvar`** — Pathogenic count is over the 27 record(s) retrieved, NOT over all 27 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 20 of 43 traits by best p-value, aggregated from 89 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P55774 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000275385/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CCL18 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CCL18 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CCL18%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CCL18 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:32:48  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: pharmgkb
