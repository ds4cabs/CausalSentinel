# Protein Dossier — CCL4 (C-C motif chemokine 4)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Ulcerative colitis | 0.179 | 0.0426 | 2.71e-05 | Wald ratio | 1 | trans | NA |
| Juvenile idiopathic arthritis | -0.74 | 0.19 | 1.02e-04 | Wald ratio | 1 | trans | NA |
| Inflammatory bowel disease | 0.117 | 0.0344 | 6.98e-04 | Wald ratio | 1 | trans | NA |
| Eye problems or disorders: Glaucoma | 0.121 | 0.0407 | 0.00291 | Inverse variance weighted | 2 | trans | NA |
| Eye problems or disorders: Glaucoma | 0.121 | 0.0407 | 0.00291 | Inverse variance weighted | 2 | cis | NA |
| Pulse rate | 0.0267 | 0.00957 | 0.0053 | Inverse variance weighted | 2 | trans | NA |
| Pulse rate | 0.0267 | 0.00957 | 0.0053 | Inverse variance weighted | 2 | cis | NA |
| Mean cell volume | -0.301 | 0.111 | 0.00674 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: R07 Pain in throat and chest | 0.0585 | 0.0228 | 0.0104 | Inverse variance weighted | 2 | trans | NA |
| Diagnoses - main ICD10: R07 Pain in throat and chest | 0.0585 | 0.0228 | 0.0104 | Inverse variance weighted | 2 | cis | NA |
| Non-cancer illness code  self-reported: vitiligo | 0.501 | 0.21 | 0.017 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: vitiligo | 0.501 | 0.21 | 0.017 | Inverse variance weighted | 2 | cis | NA |
| _...and 159 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_25 association rows across 21 traits (23 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| CCL3/CCL4 protein level ratio | 7e-1388 | rs1634517 | 1 | GCST90313697 | no MR -> candidate analysis |
| C-C motif chemokine 3 levels | 2e-320 | rs1634517 | 1 | GCST90012055 | no MR -> candidate analysis |
| CCL16 protein levels | 2e-200 | rs148048971 | 1 | GCST90468568 | no MR -> candidate analysis |
| Circulating CCL4 levels (id: OID00796_OID20695) | 2e-156 | rs200657610 | 1 | GCST90860128 | no MR -> candidate analysis |
| CCL4 protein levels | 2e-149 | rs1634513 | 1 | GCST90468583 | no MR -> candidate analysis |
| Circulating CCL4 levels (id: OID00498_OID20695) | 3e-140 | rs200657610 | 1 | GCST90859854 | no MR -> candidate analysis |
| CCL3 protein levels | 1e-91 | rs9709233 | 2 | GCST90468582 | no MR -> candidate analysis |
| C-C motif chemokine 3-like 1 levels | 6e-69 | rs149759822 | 1 | GCST90137673 | no MR -> candidate analysis |
| Circulating CCL16 levels | 3e-45 | rs550697938 | 1 | GCST90859998 | no MR -> candidate analysis |
| Circulating CCL18 levels | 1e-29 | rs1634508 | 1 | GCST90860473 | no MR -> candidate analysis |
| Beta-2-microglobulin level in Chronic kidney disease with hy | 6e-26 | rs9900984 | 1 | GCST90232921 | no MR -> candidate analysis |
| C-C motif chemokine 4-like levels | 8e-26 | rs1719205 | 1 | GCST90246919 | no MR -> candidate analysis |
| _...and 9 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.0041, LOEUF=1.39 — LoF-tolerant |
| GWAS Catalog | 113 unique SNPs / 267 rows |
| ClinVar | 41 records; 7 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 953 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CCL4'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 41 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 21 traits by best p-value, aggregated from 25 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P13236 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000275302/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CCL4 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CCL4 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CCL4%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CCL4 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:38:03  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
