# Protein Dossier — QSOX1 (Sulfhydryl oxidase 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: enlarged prostate | 0.145 | 0.0449 | 0.00125 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: psoriasis | 0.134 | 0.05 | 0.00742 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: pneumothorax | 0.499 | 0.188 | 0.00796 | Wald ratio | 1 | cis | NA |
| Fracture resulting from simple fall | 0.04 | 0.0154 | 0.00961 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: L03 Cellulitis | -0.204 | 0.0834 | 0.0146 | Wald ratio | 1 | cis | NA |
| Invasive mucinous ovarian cancer | -0.271 | 0.118 | 0.0211 | Wald ratio | 1 | cis | NA |
| Intracranial volume | -1.15e+04 | 5.1e+03 | 0.0243 | Wald ratio | 1 | cis | NA |
| Pallidum volume | -11.3 | 5.07 | 0.026 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N40 Hyperplasia of prostate | 0.124 | 0.0559 | 0.0261 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R55 Syncope and collapse | 0.124 | 0.057 | 0.0292 | Wald ratio | 1 | cis | NA |
| Hearing difficulty or problems: Yes | 0.0221 | 0.0102 | 0.0312 | Wald ratio | 1 | cis | NA |
| Hip osteoarthritis | -0.151 | 0.0768 | 0.05 | Wald ratio | 1 | cis | NA |
| _...and 65 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_42 association rows across 29 traits (37 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| QSOX1 protein levels | 5e-132 | rs12094391 | 8 | GCST90470402 | no MR -> candidate analysis |
| Calponin-2 levels | 1e-118 | rs12371 | 1 | GCST90423340 | no MR -> candidate analysis |
| Serum levels of protein BAG5 | 1e-69 | rs12371 | 1 | GCST90087199 | no MR -> candidate analysis |
| Sulfhydryl oxidase 1 levels | 4e-68 | rs12371 | 1 | GCST90426591 | no MR -> candidate analysis |
| Sulfhydryl oxidase 1 levels (QSOX1.6217.23.3) | 1e-60 | rs12371 | 2 | GCST90242912 | no MR -> candidate analysis |
| TOR1AIP1 protein levels | 8e-43 | rs7556324 | 3 | GCST90470935 | no MR -> candidate analysis |
| BAG family molecular chaperone regulator 5 levels | 1e-41 | rs12371 | 1 | GCST90246648 | no MR -> candidate analysis |
| Serum levels of protein QSOX1 | 3e-27 | rs3767196 | 1 | GCST90089300 | no MR -> candidate analysis |
| ANGPTL1 protein levels | 2e-25 | rs115383570 | 1 | GCST90468302 | no MR -> candidate analysis |
| Serum levels of protein LILRB5 | 7e-23 | rs12371 | 1 | GCST90089622 | no MR -> candidate analysis |
| Serum levels of protein C17orf78 | 5e-20 | rs12371 | 1 | GCST90090227 | no MR -> candidate analysis |
| Uncharacterized protein C17orf78 levels (C17orf78.8545.14.3) | 7e-19 | rs12371 | 1 | GCST90243267 | no MR -> candidate analysis |
| _...and 17 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 2010 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| non-autoimmune hemolytic anemia | 0.512 | — | common-variant locus | no MR -> candidate analysis |
| knee fracture | 0.511 | — | common-variant locus | no MR -> candidate analysis |
| breast carcinoma | 0.031 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Sulfhydryl oxidase 1) |
| gnomAD constraint | pLI=8e-06, LOEUF=0.684 — LoF-tolerant |
| GWAS Catalog | 72 unique SNPs / 128 rows |
| ClinVar | 214 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 2010 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'QSOX1' and resolved to 'Sulfhydryl oxidase 1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 214 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 29 traits by best p-value, aggregated from 42 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O00391 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000116260/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4523117/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/QSOX1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/QSOX1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=QSOX1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/QSOX1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:44:30  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
