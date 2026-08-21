# Protein Dossier — DUSP13 (Dual specificity protein phosphatase 13B)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Cough on most days | -0.102 | 0.0337 | 0.00259 | Inverse variance weighted | 2 | cis | NA |
| Cough on most days | -0.102 | 0.0337 | 0.00259 | Inverse variance weighted | 2 | trans | NA |
| HDL cholesterol | 0.0478 | 0.016 | 0.00289 | Wald ratio | 1 | cis | NA |
| Childhood intelligence | 0.124 | 0.0431 | 0.00393 | Wald ratio | 1 | cis | NA |
| Sodium in urine | -0.0161 | 0.00584 | 0.00598 | Inverse variance weighted | 2 | cis | NA |
| Sodium in urine | -0.0161 | 0.00584 | 0.00598 | Inverse variance weighted | 2 | trans | NA |
| Diagnoses - main ICD10: R55 Syncope and collapse | -0.209 | 0.0782 | 0.0076 | Inverse variance weighted | 2 | cis | NA |
| Diagnoses - main ICD10: R55 Syncope and collapse | -0.209 | 0.0782 | 0.0076 | Inverse variance weighted | 2 | trans | NA |
| Creatinine (enzymatic) in urine | -0.0146 | 0.00568 | 0.0102 | Inverse variance weighted | 2 | cis | NA |
| Creatinine (enzymatic) in urine | -0.0146 | 0.00568 | 0.0102 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: emphysema or chronic bronchitis | -0.139 | 0.0593 | 0.0187 | Inverse variance weighted | 2 | cis | NA |
| Non-cancer illness code  self-reported: emphysema or chronic bronchitis | -0.139 | 0.0593 | 0.0187 | Inverse variance weighted | 2 | trans | NA |
| _...and 157 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_No GWAS Catalog associations mapped to this gene._

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 47 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| atrial fibrillation | 0.732 | — | common-variant locus | no MR -> candidate analysis |
| major depressive disorder | 0.683 | — | common-variant locus | MR: beta=-0.149, p=0.0372 (cis) |
| coronary artery disorder | 0.625 | — | common-variant locus | no MR -> candidate analysis |
| peripheral arterial disease | 0.625 | — | common-variant locus | no MR -> candidate analysis |
| smoking initiation | 0.574 | — | common-variant locus | no MR -> candidate analysis |
| insomnia | 0.55 | — | common-variant locus | no MR -> candidate analysis |
| diabetes mellitus | 0.082 | — | common-variant locus | no MR -> candidate analysis |
| atrial flutter | 0.058 | — | common-variant locus | no MR -> candidate analysis |
| type 2 diabetes mellitus | 0.047 | — | common-variant locus | no MR -> candidate analysis |
| hypertensive disorder | 0.037 | — | common-variant locus | no MR -> candidate analysis |
| coronary atherosclerosis | 0.033 | — | common-variant locus | no MR -> candidate analysis |

> Of the 11 rows above, **10 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | not available |
| GWAS Catalog | no mapped SNPs |
| ClinVar | no records |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 47 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'DUSP13'.
- **`gnomad`** — No gnomAD constraint data.
- **`gwas`** — No GWAS Catalog SNPs mapped to this gene.
- **`clinvar`** — No ClinVar records.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — No GWAS Catalog associations mapped to this gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9UII6 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000079393/associations — _Open Targets data release 26.06_

## Provenance

- Generated: 2026-08-14T02:21:02  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
