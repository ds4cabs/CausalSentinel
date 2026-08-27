# Protein Dossier — PRTN3 (Myeloblastin)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Heel bone mineral density (BMD) T-score  automated | -0.0199 | 0.00611 | 0.00116 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: chronic obstructive airways disease or copd | 0.207 | 0.066 | 0.00174 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K60 Fissure and fistula of anal and rectal regions | 0.15 | 0.0603 | 0.0127 | Wald ratio | 1 | cis | NA |
| ER-positive Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.0406 | 0.0172 | 0.0183 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: arthritis (nos) | -0.147 | 0.0631 | 0.0201 | Wald ratio | 1 | cis | NA |
| Cough on most days | -0.0541 | 0.0255 | 0.0336 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: osteoporosis | 0.0731 | 0.0352 | 0.0378 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R14 Flatulence and related conditions | 0.283 | 0.152 | 0.0629 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M23 Internal derangement of knee | -0.0566 | 0.0336 | 0.0918 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | 0.0861 | 0.0517 | 0.0957 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: ankylosing spondylitis | -0.177 | 0.108 | 0.101 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: malignant melanoma | -0.0893 | 0.0587 | 0.128 | Wald ratio | 1 | cis | NA |
| _...and 46 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3514_49_2` | Proteinase-3 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_84 association rows across 42 traits (81 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating PRTN3 levels | 1e-1200 | rs6510982 | 3 | GCST90859963 | no MR -> candidate analysis |
| MPO/PRTN3 protein level ratio | 3e-939 | rs12052108 | 1 | GCST90315492 | no MR -> candidate analysis |
| LCN2/PRTN3 protein level ratio | 7e-873 | rs12052108 | 1 | GCST90315307 | no MR -> candidate analysis |
| Myeloblastin levels | 2e-424 | rs6510982 | 13 | GCST90248550 | no MR -> candidate analysis |
| Circulating AZU1 levels | 4e-226 | rs138032111 | 3 | GCST90859945 | no MR -> candidate analysis |
| AZU1 protein levels | 2e-204 | rs138032111 | 2 | GCST90468408 | no MR -> candidate analysis |
| Myeloblastin levels (PRTN3.3514.49.2) | 8e-110 | rs10425544 | 5 | GCST90241987 | no MR -> candidate analysis |
| Neutrophil forward scatter | 2e-82 | rs7254911 | 1 | GCST90281224 | no MR -> candidate analysis |
| Neutrophil elastase levels | 2e-61 | rs10409474 | 1 | GCST90248653 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 2e-54 | rs76427287 | 1 | GCST90838669 | no MR -> candidate analysis |
| Neutrophil side scatter distribution width | 6e-54 | rs138303849 | 1 | GCST90281225 | no MR -> candidate analysis |
| Neutrophil side scatter | 6e-52 | rs76427287 | 1 | GCST90281222 | no MR -> candidate analysis |
| _...and 30 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 801 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| IgA glomerulonephritis | 0.283 | — | common-variant locus | no MR -> candidate analysis |
| anti-neutrophil antibody associated vasculitis | 0.259 | — | common-variant locus | no MR -> candidate analysis |
| stroke disorder | 0.18 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.18 | — | common-variant locus | no MR -> candidate analysis |
| pyogenic granuloma | 0.18 | — | common-variant locus | no MR -> candidate analysis |

> Of the 5 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Myeloblastin) |
| gnomAD constraint | pLI=1.3e-08, LOEUF=1.52 — LoF-tolerant |
| GWAS Catalog | 131 unique SNPs / 312 rows |
| ClinVar | 85 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 801 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'PRTN3' and resolved to 'Myeloblastin' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 85 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 42 traits by best p-value, aggregated from 84 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P24158 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000196415/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3900/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PRTN3 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PRTN3 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PRTN3%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PRTN3 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:38:37  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
