# Protein Dossier — FAM213A (Peroxiredoxin-like 2A)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Heel bone mineral density (BMD) T-score  automated | -0.074 | 0.0168 | 1.04e-05 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypopituitarism | 1.09 | 0.257 | 2.32e-05 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: asthma | 0.11 | 0.0326 | 6.90e-04 | Wald ratio | 1 | cis | NA |
| Urate | 0.0905 | 0.0293 | 0.002 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | 0.0325 | 0.0106 | 0.00223 | Wald ratio | 1 | cis | NA |
| Fractured or broken bones in last 5 years | 0.102 | 0.0366 | 0.00516 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Arm | 0.278 | 0.1 | 0.00534 | Wald ratio | 1 | cis | NA |
| Sleep duration | -0.0269 | 0.0101 | 0.00784 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K35 Acute appendicitis | 0.354 | 0.134 | 0.00808 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: osteoporosis | 0.212 | 0.0849 | 0.0127 | Wald ratio | 1 | cis | NA |
| Platelet count | 5.18 | 2.16 | 0.0163 | Wald ratio | 1 | cis | NA |
| Alcohol intake frequency | 0.046 | 0.0192 | 0.0164 | Wald ratio | 1 | cis | NA |
| _...and 100 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_No GWAS Catalog associations mapped to this gene._

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 102 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| kidney failure | 0.497 | — | common-variant locus | no MR -> candidate analysis |
| sunburn | 0.342 | — | common-variant locus | no MR -> candidate analysis |
| hypertensive disorder | 0.318 | — | common-variant locus | no MR -> candidate analysis |
| exfoliation syndrome | 0.147 | — | common-variant locus | no MR -> candidate analysis |
| heart failure | 0.144 | — | common-variant locus | no MR -> candidate analysis |
| glaucoma | 0.119 | — | common-variant locus | MR: beta=-0.134, p=0.288 (cis) |
| open-angle glaucoma | 0.092 | — | common-variant locus | no MR -> candidate analysis |

> Of the 7 rows above, **6 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Peroxiredoxin-like 2A) |
| gnomAD constraint | not available |
| GWAS Catalog | no mapped SNPs |
| ClinVar | no records |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 102 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'FAM213A' and resolved to 'Peroxiredoxin-like 2A' — confirm this is the intended target.
- **`gnomad`** — No gnomAD constraint data.
- **`gwas`** — No GWAS Catalog SNPs mapped to this gene.
- **`clinvar`** — No ClinVar records.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — No GWAS Catalog associations mapped to this gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9BRX8 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000122378/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3879824/ — _ChEMBL_37 (released 2026-05-01)_

## Provenance

- Generated: 2026-08-14T02:34:34  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
