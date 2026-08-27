# Protein Dossier — ADH4 (All-trans-retinol dehydrogenase [NAD(+)] ADH4)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: B37 Candidiasis | 1.14 | 0.261 | 1.21e-05 | Wald ratio | 1 | cis | NA |
| Platelet count | 10.2 | 3.1 | 9.97e-04 | Wald ratio | 1 | cis | NA |
| Autism | 0.499 | 0.183 | 0.00656 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypopituitarism | 0.977 | 0.379 | 0.00996 | Wald ratio | 1 | cis | NA |
| Chronic kidney disease | -0.248 | 0.102 | 0.0148 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: psoriasis | 0.271 | 0.115 | 0.0185 | Wald ratio | 1 | cis | NA |
| Creatinine (enzymatic) in urine | -0.0341 | 0.0151 | 0.0241 | Wald ratio | 1 | cis | NA |
| HOMA-IR | -0.0955 | 0.0427 | 0.0252 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: depression | 0.124 | 0.0577 | 0.0321 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M54 Dorsalgia | 0.213 | 0.1 | 0.0332 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | 0.0289 | 0.0137 | 0.0344 | Wald ratio | 1 | cis | NA |
| Mean platelet volume | -0.0159 | 0.00764 | 0.0372 | Wald ratio | 1 | cis | NA |
| _...and 100 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_256 association rows across 173 traits (228 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| ADH4/GSTA1 protein level ratio | 1e-271 | rs2602836 | 1 | GCST90313191 | no MR -> candidate analysis |
| ACY1/ADH4 protein level ratio | 2e-191 | rs2602836 | 1 | GCST90313161 | no MR -> candidate analysis |
| ADH4/DCXR protein level ratio | 2e-189 | rs2602836 | 1 | GCST90313190 | no MR -> candidate analysis |
| ADH4/KRT18 protein level ratio | 7e-164 | rs2602836 | 1 | GCST90313192 | no MR -> candidate analysis |
| ADH4/SCLY protein level ratio | 3e-156 | rs2602836 | 1 | GCST90313195 | no MR -> candidate analysis |
| ADH4/RBP5 protein level ratio | 3e-149 | rs2602836 | 1 | GCST90313194 | no MR -> candidate analysis |
| ADH4/C19orf12 protein level ratio | 4e-142 | rs2602836 | 1 | GCST90313188 | no MR -> candidate analysis |
| ADH4/SORD protein level ratio | 2e-133 | rs2602836 | 1 | GCST90313196 | no MR -> candidate analysis |
| ADH4/KYNU protein level ratio | 5e-128 | rs2602836 | 1 | GCST90313193 | no MR -> candidate analysis |
| ADH4/CA5A protein level ratio | 3e-117 | rs2602836 | 1 | GCST90313189 | no MR -> candidate analysis |
| ADH4 protein levels | 2e-97 | rs1800759 | 1 | GCST90468244 | no MR -> candidate analysis |
| Alkaline phosphatase (UKB data field 30610) | 4e-86 | rs6822348 | 1 | GCST90468060 | no MR -> candidate analysis |
| _...and 161 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 135 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| ischemic stroke | 0.425 | — | common-variant locus | MR: beta=0.0904, p=0.387 (cis) |
| substance-related disorder | 0.424 | — | common-variant locus | no MR -> candidate analysis |
| coronary artery disorder | 0.422 | — | common-variant locus | no MR -> candidate analysis |
| venous thromboembolism | 0.355 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (All-trans-retinol dehydrogenase [NAD(+)] ADH4) |
| gnomAD constraint | pLI=4.7e-10, LOEUF=1.19 — LoF-tolerant |
| GWAS Catalog | 114 unique SNPs / 269 rows |
| ClinVar | 83 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 135 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'ADH4' and resolved to 'All-trans-retinol dehydrogenase [NAD(+)] ADH4' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 83 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 173 traits by best p-value, aggregated from 256 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P08319 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000198099/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2990/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/ADH4 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/ADH4 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=ADH4%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/ADH4 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T00:55:14  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
