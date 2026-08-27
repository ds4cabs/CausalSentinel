# Protein Dossier — ADGRE2 (Adhesion G protein-coupled receptor E2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: D25 Leiomyoma of uterus | 0.265 | 0.0606 | 1.24e-05 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K44 Diaphragmatic hernia | 0.16 | 0.0611 | 0.00879 | Wald ratio | 1 | cis | NA |
| Neo-extraversion | -0.822 | 0.352 | 0.0195 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: B37 Candidiasis | 0.553 | 0.266 | 0.0376 | Wald ratio | 1 | cis | NA |
| Height | 0.0313 | 0.0155 | 0.0432 | Wald ratio | 1 | cis | NA |
| Birth weight | -0.0293 | 0.0152 | 0.0532 | Wald ratio | 1 | cis | NA |
| Neo-conscientiousness | -0.67 | 0.347 | 0.0532 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K29 Gastritis and duodenitis | 0.0957 | 0.0526 | 0.0688 | Wald ratio | 1 | cis | NA |
| Low grade serous ovarian cancer | 0.353 | 0.2 | 0.0782 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: Z09 Follow-up examination after treatment for conditions other than malignant neoplasms | 0.114 | 0.0651 | 0.0807 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: sleep apnoea | 0.227 | 0.131 | 0.082 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | -0.24 | 0.138 | 0.0823 | Wald ratio | 1 | cis | NA |
| _...and 92 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4546_27_3` | EMR2 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_11 association rows across 10 traits (4 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Adhesion G protein-coupled receptor E2 levels | 2e-339 | rs9305048 | 2 | GCST90426071 | no MR -> candidate analysis |
| Protein quantitative trait loci (liver) | 2e-8 | rs117617387 | 1 | GCST011427 | no MR -> candidate analysis |
| Height | 2e-8 | rs2732796 | 1 | GCST90245844 | MR: beta=0.0313, p=0.0432 (cis) |
| Peak concentration of apixaban | 5e-8 | rs553498034 | 1 | GCST90271720 | no MR -> candidate analysis |
| Plasma androstenedione levels in resected early stage-recept | 1e-7 | rs57712673 | 1 | GCST004363 | no MR -> candidate analysis |
| 2-hydroxypalmitate levels in elite athletes | 3e-7 | rs3795033 | 1 | GCST90133637 | no MR -> candidate analysis |
| Major depressive disorder | 1e-6 | rs112610420 | 1 | GCST005547 | no MR -> candidate analysis |
| Vaginal microbiome MetaCyc pathway (PWY-7007|methyl ketone b | 1e-6 | rs4808487 | 1 | GCST90026898 | no MR -> candidate analysis |
| Response to gabapentin in female chronic pelvic pain (side-e | 2e-6 | rs11666594 | 1 | GCST90428069 | no MR -> candidate analysis |
| Parkinson's disease motor subtype (tremor to postural instab | 3e-6 | rs538015403 | 1 | GCST90000015 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 154 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| vibratory urticaria | 0.688 | — | established (curated) | no MR -> candidate analysis |
| autosomal dominant vibratory urticaria | 0.545 | — | established (curated) | no MR -> candidate analysis |
| Genetic visceral malformation of the liver, biliary tract, pancreas or spleen | 0.267 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.9e-23, LOEUF=0.988 — LoF-tolerant |
| GWAS Catalog | 30 unique SNPs / 58 rows |
| ClinVar | 701 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 154 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'ADGRE2'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 701 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 10 of 10 traits by best p-value, aggregated from 11 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9UHX3 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000127507/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/ADGRE2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/ADGRE2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=ADGRE2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/ADGRE2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T00:54:54  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
