# Protein Dossier — MENT (Protein MENT)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: R10 Abdominal and pelvic pain | -0.415 | 0.133 | 0.00176 | Wald ratio | 1 | cis | NA |
| Weight | -0.0443 | 0.0157 | 0.00469 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | -0.0434 | 0.0177 | 0.0144 | Wald ratio | 1 | cis | NA |
| Sodium in urine | -0.0425 | 0.0175 | 0.0152 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: small intestine or small bowel cancer | 0.92 | 0.399 | 0.0211 | Wald ratio | 1 | cis | NA |
| Creatinine (enzymatic) in urine | -0.0387 | 0.017 | 0.023 | Wald ratio | 1 | cis | NA |
| Lumbar spine bone mineral density | 0.153 | 0.0673 | 0.0231 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Other bones | -0.209 | 0.0962 | 0.0295 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: high cholesterol | -0.112 | 0.0539 | 0.0379 | Wald ratio | 1 | cis | NA |
| Pallidum volume | -33 | 16.4 | 0.044 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: chronic obstructive airways disease or copd | 0.419 | 0.211 | 0.0474 | Wald ratio | 1 | cis | NA |
| Fracture resulting from simple fall | 0.0818 | 0.0419 | 0.051 | Wald ratio | 1 | cis | NA |
| _...and 64 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_No GWAS Catalog associations mapped to this gene._

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 34 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| obesity disorder | 0.321 | — | common-variant locus | no MR -> candidate analysis |
| type 2 diabetes mellitus | 0.074 | — | common-variant locus | no MR -> candidate analysis |
| basal cell carcinoma | 0.057 | — | common-variant locus | MR: beta=0.204, p=0.19 (cis) |
| non-melanoma skin carcinoma | 0.057 | — | common-variant locus | no MR -> candidate analysis |
| response to xenobiotic stimulus | 0.033 | — | common-variant locus | no MR -> candidate analysis |
| hypertensive disorder | 0.033 | — | common-variant locus | no MR -> candidate analysis |

> Of the 6 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | not available |
| GWAS Catalog | no mapped SNPs |
| ClinVar | no records |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 34 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'MENT'.
- **`gnomad`** — No gnomAD constraint data.
- **`gwas`** — No GWAS Catalog SNPs mapped to this gene.
- **`clinvar`** — No ClinVar records.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — No GWAS Catalog associations mapped to this gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9BUN1 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000143443/associations — _Open Targets data release 26.06_

## Provenance

- Generated: 2026-08-14T03:46:02  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
