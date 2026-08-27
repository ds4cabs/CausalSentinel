# Protein Dossier — CXCL1 (Growth-regulated alpha protein)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: G56 Mononeuropathies of upper limb | 0.0739 | 0.0268 | 0.00591 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | 0.009 | 0.00329 | 0.0062 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | 0.00807 | 0.00312 | 0.00962 | Wald ratio | 1 | cis | NA |
| Large vessel disease | 0.121 | 0.0532 | 0.0226 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: ankylosing spondylitis | 0.133 | 0.0632 | 0.0353 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K60 Fissure and fistula of anal and rectal regions | 0.105 | 0.0507 | 0.038 | Wald ratio | 1 | cis | NA |
| Depressive symptoms | -0.0107 | 0.00536 | 0.0455 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: arthritis (nos) | -0.0959 | 0.0482 | 0.0468 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: basal cell carcinoma | -0.0798 | 0.043 | 0.0636 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: Z09 Follow-up examination after treatment for conditions other than malignant neoplasms | 0.0535 | 0.0293 | 0.0682 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Glaucoma | 0.0533 | 0.0301 | 0.0768 | Wald ratio | 1 | cis | NA |
| Years of schooling | 0.00938 | 0.00536 | 0.0801 | Wald ratio | 1 | cis | NA |
| _...and 83 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2985_35_1` | Gro-a | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_95 association rows across 54 traits (91 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating CXCL1 levels (id: OID00404_OID20762) | 5e-1754 | rs2115691 | 2 | GCST90859766 | no MR -> candidate analysis |
| Circulating CXCL1 levels (id: OID00786_OID20762) | 6e-1709 | rs2115691 | 2 | GCST90860118 | no MR -> candidate analysis |
| Circulating CXCL1 levels (id: OID00496_OID20762) | 1e-1652 | rs2115691 | 2 | GCST90859853 | no MR -> candidate analysis |
| Growth-regulated alpha protein levels | 2e-1526 | rs3097411 | 9 | GCST90247816 | no MR -> candidate analysis |
| CXCL3/CXCL5 protein level ratio | 6e-1230 | rs352024 | 1 | GCST90314344 | no MR -> candidate analysis |
| CXCL1/CXCL5 protein level ratio | 2e-1218 | rs352024 | 1 | GCST90314343 | no MR -> candidate analysis |
| CCL5/CXCL5 protein level ratio | 1e-1011 | rs352024 | 1 | GCST90313701 | no MR -> candidate analysis |
| CXCL5/PPIB protein level ratio | 1e-899 | rs352024 | 1 | GCST90314352 | no MR -> candidate analysis |
| CXCL5/SERPINE1 protein level ratio | 3e-839 | rs352024 | 1 | GCST90314354 | no MR -> candidate analysis |
| CXCL5/SPARC protein level ratio | 4e-757 | rs352024 | 1 | GCST90314355 | no MR -> candidate analysis |
| CXCL5/PLXNA4 protein level ratio | 1e-717 | rs352024 | 1 | GCST90314351 | no MR -> candidate analysis |
| CXCL5/SDC4 protein level ratio | 1e-678 | rs352024 | 1 | GCST90314353 | no MR -> candidate analysis |
| _...and 42 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.0024, LOEUF=1.34 — LoF-tolerant |
| GWAS Catalog | 104 unique SNPs / 222 rows |
| ClinVar | 54 records; 5 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1109 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CXCL1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 54 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 54 traits by best p-value, aggregated from 95 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P09341 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000163739/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CXCL1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CXCL1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CXCL1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CXCL1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:13:13  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
