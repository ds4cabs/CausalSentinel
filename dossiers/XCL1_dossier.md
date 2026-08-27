# Protein Dossier — XCL1 (Lymphotactin)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Cancer code  self-reported: prostate cancer | -0.263 | 0.11 | 0.0169 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hiatus hernia | 0.0984 | 0.0425 | 0.0207 | Wald ratio | 1 | cis | NA |
| Urate | -0.0349 | 0.0156 | 0.0252 | Wald ratio | 1 | cis | NA |
| Happiness | 0.0192 | 0.00887 | 0.0306 | Wald ratio | 1 | cis | NA |
| Thalamus volume | 38.3 | 18.7 | 0.0404 | Wald ratio | 1 | cis | NA |
| Haemoglobin concentration | 0.0317 | 0.0161 | 0.0487 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | -0.204 | 0.106 | 0.0535 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | 0.0136 | 0.00713 | 0.0572 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R55 Syncope and collapse | -0.172 | 0.0908 | 0.0577 | Wald ratio | 1 | cis | NA |
| Sodium in urine | 0.0132 | 0.00702 | 0.0592 | Wald ratio | 1 | cis | NA |
| Hip osteoarthritis | 0.158 | 0.0838 | 0.0601 | Wald ratio | 1 | cis | NA |
| Weight | 0.0115 | 0.0063 | 0.0691 | Wald ratio | 1 | cis | NA |
| _...and 111 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4143_74_2` | Lymphotactin | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_70 association rows across 25 traits (63 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| XCL1 protein levels | 1e-191 | rs76683928 | 22 | GCST90471081 | no MR -> candidate analysis |
| Circulating XCL1 levels | 2e-120 | rs61801331 | 2 | GCST90859793 | no MR -> candidate analysis |
| DPT protein levels | 1e-65 | rs77143649 | 8 | GCST90469036 | no MR -> candidate analysis |
| neutrophil (fraction, minimum, inv-norm transformed) | 3e-21 | rs1337742 | 1 | GCST90479715 | no MR -> candidate analysis |
| Autoimmune hypothyroidism | 5e-21 | rs10753774 | 1 | GCST90837324 | no MR -> candidate analysis |
| neutrophil (fraction, mean, inv-norm transformed) | 1e-17 | rs1337742 | 1 | GCST90479714 | no MR -> candidate analysis |
| Hypothyroidism | 1e-15 | rs10753774 | 2 | GCST90627750 | MR: beta=0.0427, p=0.16 (cis) |
| Height | 2e-15 | rs6427140 | 2 | GCST90245848 | MR: beta=-0.0107, p=0.214 (cis) |
| white blood cell count (WBC, maximum, inv-norm transformed) | 3e-15 | rs1337742 | 1 | GCST90480723 | no MR -> candidate analysis |
| neutrophil (absolute count, maximum, inv-norm transformed) | 9e-14 | rs1337742 | 1 | GCST90479710 | no MR -> candidate analysis |
| Cytokine SCM-1 beta levels | 5e-13 | rs10753774 | 2 | GCST90249451 | no MR -> candidate analysis |
| Cerebrospinal fluid protein XCL1 levels | 1e-12 | rs10753774 | 1 | GCST90944069 | no MR -> candidate analysis |
| _...and 13 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 394 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| adolescent idiopathic scoliosis | 0.519 | — | common-variant locus | no MR -> candidate analysis |
| rhabdomyolysis | 0.482 | — | common-variant locus | no MR -> candidate analysis |
| gestational diabetes | 0.48 | — | common-variant locus | no MR -> candidate analysis |
| psoriasis | 0.379 | — | common-variant locus | MR: beta=-0.126, p=0.0995 (cis) |
| phlebitis | 0.302 | — | common-variant locus | no MR -> candidate analysis |
| Thrombophlebitis | 0.302 | — | common-variant locus | no MR -> candidate analysis |
| hypothyroidism | 0.299 | — | common-variant locus | MR: beta=0.0427, p=0.16 (cis) |
| streptococcal infection | 0.225 | — | common-variant locus | no MR -> candidate analysis |

> Of the 8 rows above, **6 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.01, LOEUF=1.61 — LoF-tolerant |
| GWAS Catalog | 103 unique SNPs / 178 rows |
| ClinVar | 48 records; 9 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 394 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'XCL1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 48 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 25 traits by best p-value, aggregated from 70 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P47992 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000143184/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/XCL1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/XCL1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=XCL1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/XCL1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:38:38  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
