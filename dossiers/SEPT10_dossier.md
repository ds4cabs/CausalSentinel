# Protein Dossier — SEPT10 (Septin-10)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Childhood intelligence | -0.112 | 0.0368 | 0.00239 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: hypopituitarism | 0.579 | 0.223 | 0.0095 | Wald ratio | 1 | trans | NA |
| Body mass index (BMI) | 0.0178 | 0.00691 | 0.00982 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: R11 Nausea and vomiting | 0.224 | 0.0887 | 0.0115 | Wald ratio | 1 | trans | NA |
| Knee osteoarthritis | 0.208 | 0.0827 | 0.0119 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: I48 Atrial fibrillation and flutter | -0.203 | 0.0808 | 0.0121 | Wald ratio | 1 | trans | NA |
| Age at menarche | -0.0406 | 0.0165 | 0.014 | Wald ratio | 1 | trans | NA |
| Ischemic stroke | 0.109 | 0.0476 | 0.022 | Wald ratio | 1 | trans | NA |
| Sodium in urine | 0.0154 | 0.0068 | 0.024 | Wald ratio | 1 | trans | NA |
| Microalbuminuria | 0.127 | 0.0595 | 0.0326 | Wald ratio | 1 | trans | NA |
| Creatinine (enzymatic) in urine | 0.0141 | 0.00662 | 0.0331 | Wald ratio | 1 | trans | NA |
| Eye problems or disorders: Glaucoma | 0.108 | 0.052 | 0.0386 | Wald ratio | 1 | trans | NA |
| _...and 109 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_No GWAS Catalog associations mapped to this gene._

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 56 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| nutritional deficiency disease | 0.484 | — | common-variant locus | no MR -> candidate analysis |
| ocular hypotension | 0.265 | — | common-variant locus | no MR -> candidate analysis |
| stroke disorder | 0.262 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.262 | — | common-variant locus | no MR -> candidate analysis |
| placental abruption | 0.099 | — | common-variant locus | no MR -> candidate analysis |
| lung abscess | 0.094 | — | common-variant locus | no MR -> candidate analysis |
| bronchopneumonia | 0.094 | — | common-variant locus | no MR -> candidate analysis |
| esophageal ulcer | 0.051 | — | common-variant locus | no MR -> candidate analysis |

> Of the 8 rows above, **8 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | not available |
| GWAS Catalog | 1 unique SNPs / 2 rows |
| ClinVar | no records |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 56 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'SEPT10'.
- **`gnomad`** — No gnomAD constraint data.
- **`clinvar`** — No ClinVar records.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — No GWAS Catalog associations mapped to this gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9P0V9 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000186522/associations — _Open Targets data release 26.06_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/SEPT10 — _GWAS Catalog REST (live; release not exposed by this endpoint)_

## Provenance

- Generated: 2026-08-14T05:00:21  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
