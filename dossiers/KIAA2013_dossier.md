# Protein Dossier — KIAA2013 (Uncharacterized protein KIAA2013)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Neuroblastoma | -0.814 | 0.242 | 7.49e-04 | Wald ratio | 1 | cis | NA |
| Alzheimer's disease | 0.287 | 0.0882 | 0.00113 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M17 Gonarthrosis [arthrosis of knee] | 0.234 | 0.0781 | 0.00267 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: high cholesterol | 0.092 | 0.0336 | 0.00616 | Wald ratio | 1 | cis | NA |
| Birth length | -0.151 | 0.0562 | 0.00715 | Wald ratio | 1 | cis | NA |
| Vascular or heart problems diagnosed by doctor: Angina | 0.173 | 0.0645 | 0.00746 | Wald ratio | 1 | cis | NA |
| Platelet count | -6.07 | 2.33 | 0.00901 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: G47 Sleep disorders | 0.32 | 0.132 | 0.0149 | Wald ratio | 1 | cis | NA |
| Rheumatoid arthritis | 0.166 | 0.0699 | 0.0176 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Injury or trauma resulting in loss of vision | 0.313 | 0.133 | 0.0184 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | 0.117 | 0.054 | 0.0306 | Wald ratio | 1 | cis | NA |
| 2hr glucose | 0.23 | 0.107 | 0.0309 | Wald ratio | 1 | cis | NA |
| _...and 98 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_15 association rows across 14 traits (12 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating NTproBNP levels (id: OID01214_OID20125) | 2e-113 | rs9787387 | 1 | GCST90860419 | no MR -> candidate analysis |
| Circulating NTproBNP levels (id: OID00455_OID20125) | 3e-106 | rs9787387 | 1 | GCST90859816 | no MR -> candidate analysis |
| Circulating NTproBNP levels (id: OID00131_OID20125) | 1e-92 | rs9787387 | 1 | GCST90859652 | no MR -> candidate analysis |
| Systolic blood pressure x alcohol consumption interaction (2 | 1e-15 | rs71647019 | 1 | GCST006434 | no MR -> candidate analysis |
| Systolic blood pressure | 2e-15 | rs71647020 | 1 | GCST90132903 | no MR -> candidate analysis |
| Diastolic blood pressure x alcohol consumption interaction ( | 6e-15 | rs71647020 | 1 | GCST006166 | no MR -> candidate analysis |
| Hypertension | 9e-13 | rs12738237 | 2 | GCST90446531 | no MR -> candidate analysis |
| Other cerebral degenerations (PheCode 331) | 3e-11 | rs551075790 | 1 | GCST90480007 | no MR -> candidate analysis |
| Height | 5e-10 | rs2639453 | 1 | GCST90245844 | MR: beta=0.0135, p=0.424 (cis) |
| Alzheimer's disease | 9e-10 | rs6682554 | 1 | GCST90558104 | MR: beta=0.287, p=0.00113 (cis) |
| ICD10 O13: Gestational hypertension | 3e-9 | rs143439093 | 1 | GCST90454232 | no MR -> candidate analysis |
| Red blood cell folate levels | 5e-8 | rs2639453 | 1 | GCST007580 | no MR -> candidate analysis |
| _...and 2 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 12 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Alzheimer disease | 0.431 | — | common-variant locus | no MR -> candidate analysis |
| Cerebral degeneration | 0.062 | — | common-variant locus | no MR -> candidate analysis |
| esophageal ulcer | 0.044 | — | common-variant locus | no MR -> candidate analysis |
| osteoarthritis | 0.04 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.0051, LOEUF=0.728 — LoF-tolerant |
| GWAS Catalog | 119 unique SNPs / 324 rows |
| ClinVar | 158 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 12 of 12 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'KIAA2013'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 158 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 14 of 14 traits by best p-value, aggregated from 15 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q8IYS2 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000116685/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/KIAA2013 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/KIAA2013 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=KIAA2013%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/KIAA2013 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:21:40  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
