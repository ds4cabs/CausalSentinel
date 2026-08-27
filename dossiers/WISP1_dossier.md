# Protein Dossier — WISP1 (CCN family member 4)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Rheumatoid arthritis | -0.142 | 0.0374 | 1.46e-04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | -0.0754 | 0.0255 | 0.00304 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hyperthyroidism or thyrotoxicosis | -0.172 | 0.0737 | 0.0194 | Wald ratio | 1 | cis | NA |
| ER-negative Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0655 | 0.0288 | 0.0227 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | -0.00898 | 0.00435 | 0.039 | Wald ratio | 1 | cis | NA |
| Hearing difficulty or problems: Yes | 0.0179 | 0.009 | 0.0463 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: osteoporosis | -0.0915 | 0.0468 | 0.0505 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: pernicious anaemia | 0.161 | 0.0839 | 0.0542 | Wald ratio | 1 | cis | NA |
| Serum cystatin C (eGFRcys) | -0.00821 | 0.0043 | 0.0563 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | -0.00838 | 0.00459 | 0.0679 | Wald ratio | 1 | cis | NA |
| Urate | 0.0235 | 0.0131 | 0.0733 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N92 Excessive  frequent and irregular menstruation | 0.0619 | 0.0348 | 0.0752 | Wald ratio | 1 | cis | NA |
| _...and 97 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3057_55_1` | WISP-1 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_No GWAS Catalog associations mapped to this gene._

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 488 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| hypothyroidism | 0.769 | — | common-variant locus | MR: beta=-0.0754, p=0.00304 (cis) |
| Graves disease | 0.738 | — | common-variant locus | no MR -> candidate analysis |
| rheumatoid arthritis | 0.656 | — | common-variant locus | MR: beta=-0.142, p=1.46e-04 (cis) |
| myxedema | 0.656 | — | common-variant locus | no MR -> candidate analysis |
| thyrotoxicosis | 0.591 | — | common-variant locus | MR: beta=-0.172, p=0.0194 (cis) |
| autoimmune disease | 0.525 | — | common-variant locus | no MR -> candidate analysis |
| hyperthyroidism | 0.525 | — | common-variant locus | MR: beta=-0.172, p=0.0194 (cis) |
| respiratory system disorder | 0.509 | — | common-variant locus | no MR -> candidate analysis |
| hypotensive disorder | 0.482 | — | common-variant locus | no MR -> candidate analysis |
| ovarian neoplasm | 0.293 | — | common-variant locus | no MR -> candidate analysis |
| Back pain | 0.23 | — | common-variant locus | no MR -> candidate analysis |

> Of the 11 rows above, **7 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | not available |
| GWAS Catalog | no mapped SNPs |
| ClinVar | no records |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 488 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'WISP1'.
- **`gnomad`** — No gnomAD constraint data.
- **`gwas`** — No GWAS Catalog SNPs mapped to this gene.
- **`clinvar`** — No ClinVar records.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — No GWAS Catalog associations mapped to this gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O95388 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000104415/associations — _Open Targets data release 26.06_

## Provenance

- Generated: 2026-08-14T05:38:15  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
