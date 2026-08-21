# Protein Dossier — DEFB119 (Beta-defensin 119)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Squamous cell lung cancer | -0.676 | 0.125 | 6.44e-08 | Wald ratio | 1 | trans | 0.991 |
| Lung cancer | -0.423 | 0.0868 | 1.11e-06 | Wald ratio | 1 | trans | NA |
| Alcohol intake frequency | -0.0332 | 0.012 | 0.00568 | Inverse variance weighted | 2 | trans | NA |
| Alcohol intake frequency | -0.0332 | 0.012 | 0.00568 | Inverse variance weighted | 2 | trans | NA |
| High grade serous ovarian cancer | 0.184 | 0.0728 | 0.0114 | Wald ratio | 1 | trans | NA |
| Thyroid cancer | 1.19 | 0.482 | 0.0136 | Wald ratio | 1 | trans | NA |
| Eye problems or disorders: Diabetes related eye disease | -0.00475 | 0.00198 | 0.0165 | Inverse variance weighted | 2 | trans | NA |
| Eye problems or disorders: Diabetes related eye disease | -0.00475 | 0.00198 | 0.0165 | Inverse variance weighted | 2 | trans | NA |
| Age at menopause | 0.275 | 0.118 | 0.0196 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: R04 Haemorrhage from respiratory passages | -0.00138 | 0.000599 | 0.0209 | Inverse variance weighted | 2 | trans | NA |
| Diagnoses - main ICD10: R04 Haemorrhage from respiratory passages | -0.00138 | 0.000599 | 0.0209 | Inverse variance weighted | 2 | trans | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | -0.0016 | 0.000696 | 0.0215 | Inverse variance weighted | 2 | trans | NA |
| _...and 152 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_7 association rows across 7 traits (7 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating ENTPD6 levels (id: OID01322_OID20100) | 2e-48 | rs187219010 | 1 | GCST90860517 | no MR -> candidate analysis |
| Circulating ENTPD6 levels (id: OID01089_OID20100) | 2e-48 | rs187219010 | 1 | GCST90860303 | no MR -> candidate analysis |
| Liver enzyme levels (alkaline phosphatase) | 8e-20 | rs6119324 | 1 | GCST90013406 | no MR -> candidate analysis |
| CST7 protein levels | 4e-18 | rs147882083 | 1 | GCST90468897 | no MR -> candidate analysis |
| Serum alkaline phosphatase levels | 3e-15 | rs73108020 | 1 | GCST90018942 | no MR -> candidate analysis |
| Heel bone mineral density | 9e-10 | rs77241905 | 1 | GCST007066 | MR: beta=0.0133, p=0.206 (trans) |
| Mean corpuscular hemoglobin | 4e-8 | rs77241905 | 1 | GCST007068 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 16 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| hypertensive disorder | 0.085 | — | common-variant locus | no MR -> candidate analysis |
| response to xenobiotic stimulus | 0.065 | — | common-variant locus | no MR -> candidate analysis |
| adolescent idiopathic scoliosis | 0.057 | — | common-variant locus | no MR -> candidate analysis |
| crush injury | 0.053 | — | common-variant locus | no MR -> candidate analysis |
| gastric carcinoma | 0.051 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.044 | — | common-variant locus | no MR -> candidate analysis |

> Of the 6 rows above, **6 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.033, LOEUF=3.07 — LoF-tolerant |
| GWAS Catalog | 29 unique SNPs / 58 rows |
| ClinVar | 55 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 16 of 16 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'DEFB119'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 55 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 7 of 7 traits by best p-value, aggregated from 7 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q8N690 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000180483/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/DEFB119 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/DEFB119 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=DEFB119%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/DEFB119 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:16:03  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
