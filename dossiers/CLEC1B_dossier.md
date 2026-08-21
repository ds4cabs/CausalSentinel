# Protein Dossier — CLEC1B (C-type lectin domain family 1 member B)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: N40 Hyperplasia of prostate | 0.122 | 0.0509 | 0.0162 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I80 Phlebitis and thrombophlebitis | 0.163 | 0.0689 | 0.018 | Wald ratio | 1 | cis | NA |
| Neo-openness to experience | -0.349 | 0.158 | 0.0271 | Wald ratio | 1 | cis | NA |
| Hirschsprung's disease | 0.614 | 0.278 | 0.0272 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: arthritis (nos) | 0.121 | 0.0564 | 0.0316 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K57 Diverticular disease of intestine | 0.0728 | 0.0361 | 0.0436 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: osteoporosis | -0.0984 | 0.0489 | 0.0442 | Wald ratio | 1 | cis | NA |
| Type 2 diabetes | 0.0586 | 0.0295 | 0.0468 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertrophic cardiomyopathy (hcm  or  hocm) | 0.486 | 0.256 | 0.0582 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: deep venous thrombosis (dvt) | 0.0685 | 0.0365 | 0.0606 | Wald ratio | 1 | cis | NA |
| Birth length | -0.0423 | 0.0226 | 0.0617 | Wald ratio | 1 | cis | NA |
| Parkinson's disease | -0.171 | 0.0926 | 0.0645 | Wald ratio | 1 | cis | NA |
| _...and 85 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4332_6_2` | CLC1B | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_45 association rows across 39 traits (44 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Blood protein levels | 1e-553 | rs7970682 | 2 | GCST006585 | no MR -> candidate analysis |
| CLEC1B/SNAP29 protein level ratio | 3e-234 | rs581949 | 1 | GCST90314103 | no MR -> candidate analysis |
| CLEC1B/EGF protein level ratio | 1e-180 | rs581949 | 1 | GCST90314089 | no MR -> candidate analysis |
| CLEC1B/MPIG6B protein level ratio | 3e-175 | rs581949 | 1 | GCST90314098 | no MR -> candidate analysis |
| CLEC1B/PPP1R2 protein level ratio | 2e-150 | rs581949 | 1 | GCST90314101 | no MR -> candidate analysis |
| CLEC1B/PLXNA4 protein level ratio | 3e-150 | rs581949 | 1 | GCST90314100 | no MR -> candidate analysis |
| CLEC1B/TXNDC5 protein level ratio | 8e-137 | rs581949 | 1 | GCST90314105 | no MR -> candidate analysis |
| CD69/CLEC1B protein level ratio | 5e-132 | rs76016091 | 1 | GCST90313869 | no MR -> candidate analysis |
| CLEC1B/MGLL protein level ratio | 3e-129 | rs581949 | 1 | GCST90314097 | no MR -> candidate analysis |
| CLEC1B/F11R protein level ratio | 4e-129 | rs581949 | 1 | GCST90314090 | no MR -> candidate analysis |
| Circulating CLEC1B levels | 3e-125 | rs659928 | 2 | GCST90859682 | no MR -> candidate analysis |
| CLEC1B/RWDD1 protein level ratio | 3e-119 | rs581949 | 1 | GCST90314102 | no MR -> candidate analysis |
| _...and 27 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_No genetically-associated diseases retrieved from Open Targets._

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=2.4e-09, LOEUF=1.35 — LoF-tolerant |
| GWAS Catalog | 72 unique SNPs / 141 rows |
| ClinVar | 96 records; 5 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 576 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CLEC1B'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 96 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 39 traits by best p-value, aggregated from 45 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9P126 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000165682/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CLEC1B — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CLEC1B — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CLEC1B%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CLEC1B — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:52:49  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
