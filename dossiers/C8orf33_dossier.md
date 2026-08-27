# Protein Dossier — C8orf33 (UPF0488 protein C8orf33)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | 0.297 | 0.107 | 0.00535 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: pernicious anaemia | 0.387 | 0.153 | 0.0117 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: gout | -0.277 | 0.135 | 0.0398 | Wald ratio | 1 | trans | NA |
| Hirschsprung's disease | 1.48 | 0.723 | 0.04 | Wald ratio | 1 | trans | NA |
| Body fat | 0.054 | 0.0266 | 0.042 | Wald ratio | 1 | trans | NA |
| Neo-neuroticism | -0.903 | 0.462 | 0.0504 | Wald ratio | 1 | trans | NA |
| Neo-agreeableness | 0.577 | 0.298 | 0.0526 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: Z09 Follow-up examination after treatment for conditions other than malignant neoplasms | 0.154 | 0.0837 | 0.0658 | Wald ratio | 1 | trans | NA |
| Lung cancer | -0.166 | 0.0918 | 0.0701 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: hypertension | -0.0372 | 0.0211 | 0.0774 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: M72 Fibroblastic disorders | 0.231 | 0.131 | 0.0786 | Wald ratio | 1 | trans | NA |
| Large vessel disease | -0.29 | 0.169 | 0.0868 | Wald ratio | 1 | trans | NA |
| _...and 98 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_No GWAS Catalog associations mapped to this gene._

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 29 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| ulcerative colitis | 0.371 | — | common-variant locus | MR: beta=0.054, p=0.399 (trans) |
| placenta praevia | 0.155 | — | common-variant locus | no MR -> candidate analysis |
| metabolic dysfunction-associated steatotic liver disease | 0.037 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=6.7e-11, LOEUF=1.49 — LoF-tolerant |
| GWAS Catalog | 5 unique SNPs / 10 rows |
| ClinVar | 75 records; 12 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 29 of 29 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'C8orf33'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 75 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — No GWAS Catalog associations mapped to this gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9H7E9 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000182307/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/C8orf33 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/C8orf33 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=C8orf33%5Bgene%5D — _ClinVar build Build260809-1055.1_

## Provenance

- Generated: 2026-08-14T01:23:38  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
