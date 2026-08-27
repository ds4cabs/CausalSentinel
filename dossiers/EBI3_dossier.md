# Protein Dossier — EBI3 (Interleukin-27 subunit beta)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: Z09 Follow-up examination after treatment for conditions other than malignant neoplasms | 0.0575 | 0.0195 | 0.00315 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: chronic obstructive airways disease or copd | -0.124 | 0.0493 | 0.012 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: migraine | -0.0368 | 0.0152 | 0.0155 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Arm | 0.0564 | 0.0241 | 0.0194 | Wald ratio | 1 | cis | NA |
| Cough on most days | -0.0308 | 0.0134 | 0.0214 | Wald ratio | 1 | cis | NA |
| Forearm bone mineral density | 0.0362 | 0.0162 | 0.026 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code self-reported: pulmonary embolism (with or without) dvt | -0.0646 | 0.03 | 0.0314 | Wald ratio | 1 | cis | NA |
| Thyroid cancer | -0.176 | 0.0833 | 0.0345 | Wald ratio | 1 | cis | NA |
| 2hr glucose | 0.0419 | 0.02 | 0.0361 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: vitiligo | 0.247 | 0.122 | 0.0433 | Wald ratio | 1 | cis | NA |
| Cigarettes smoked per day | 0.162 | 0.0862 | 0.0605 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | 0.0524 | 0.0287 | 0.0674 | Wald ratio | 1 | cis | NA |
| _...and 104 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_24 association rows across 13 traits (24 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating EBI3_IL27 levels | 1e-1975 | rs4905 | 5 | GCST90859764 | no MR -> candidate analysis |
| Interleukin-27 subunit beta levels | 3e-1862 | rs353705 | 2 | GCST90248066 | no MR -> candidate analysis |
| Interleukin-27 levels | 6e-1169 | rs4905 | 4 | GCST90012017 | no MR -> candidate analysis |
| Interleukin-35 levels | 2e-222 | rs4740 | 1 | GCST90423778 | no MR -> candidate analysis |
| Interleukin-35 level in Chronic kidney disease with hyperten | 8e-163 | rs4740 | 1 | GCST90235456 | no MR -> candidate analysis |
| Interleukin-27 subunit beta level in Chronic kidney disease  | 1e-152 | rs4740 | 1 | GCST90233006 | no MR -> candidate analysis |
| Blood protein levels in cardiovascular risk | 5e-119 | rs4905 | 1 | GCST009731 | no MR -> candidate analysis |
| IL-27 levels in early pregnancy | 2e-94 | rs4905 | 1 | GCST90809109 | no MR -> candidate analysis |
| HemK methyltransferase family member 2 levels | 4e-64 | rs4740 | 2 | GCST90161266 | no MR -> candidate analysis |
| IL27B protein level (protein group normalized intensity) | 1e-63 | rs4740 | 1 | GCST90570739 | no MR -> candidate analysis |
| Calbindin protein levels (SomaScan ID:20533-39) | 2e-29 | rs353705 | 1 | GCST90438930 | no MR -> candidate analysis |
| YJU2 protein levels | 2e-16 | rs694443 | 1 | GCST90471089 | no MR -> candidate analysis |
| _...and 1 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 271 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| immune system disorder | 0.271 | — | common-variant locus | no MR -> candidate analysis |
| gangrene | 0.253 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Sequestosome-1) |
| gnomAD constraint | pLI=1.2e-06, LOEUF=1.31 — LoF-tolerant |
| GWAS Catalog | 70 unique SNPs / 140 rows |
| ClinVar | 77 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 271 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'EBI3' and resolved to 'Sequestosome-1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 77 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 13 of 13 traits by best p-value, aggregated from 24 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q14213 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000105246/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4295816/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/EBI3 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/EBI3 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=EBI3%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/EBI3 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:22:21  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
