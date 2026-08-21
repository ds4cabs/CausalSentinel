# Protein Dossier — PTGDS (Prostaglandin-H2 D-isomerase)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: mania or bipolar disorder or manic depression | 0.503 | 0.148 | 7.02e-04 | Wald ratio | 1 | cis | NA |
| Putamen volume | -91.5 | 32.4 | 0.00469 | Wald ratio | 1 | cis | NA |
| Depressive symptoms | 0.0556 | 0.0202 | 0.00596 | Wald ratio | 1 | cis | NA |
| Large vessel disease | -0.532 | 0.199 | 0.00743 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: enlarged prostate | 0.189 | 0.0871 | 0.0303 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: psoriasis | 0.201 | 0.0949 | 0.0347 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: depression | -0.117 | 0.0567 | 0.0385 | Wald ratio | 1 | cis | NA |
| Cigarettes smoked per day | -1.54 | 0.764 | 0.0438 | Wald ratio | 1 | cis | NA |
| Cough on most days | -0.142 | 0.0725 | 0.0498 | Wald ratio | 1 | cis | NA |
| HDL cholesterol | 0.0374 | 0.0197 | 0.0578 | Wald ratio | 1 | cis | NA |
| Creatinine (enzymatic) in urine | -0.0219 | 0.0117 | 0.0602 | Wald ratio | 1 | cis | NA |
| Ischemic stroke | -0.159 | 0.0904 | 0.0794 | Wald ratio | 1 | cis | NA |
| _...and 94 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_No GWAS Catalog associations mapped to this gene._

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 467 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| keratoconus | 0.525 | — | common-variant locus | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 1 known modulators (Prostaglandin-H2 D-isomerase) |
| gnomAD constraint | pLI=4.3e-06, LOEUF=1.07 — LoF-tolerant |
| GWAS Catalog | 85 unique SNPs / 174 rows |
| ClinVar | 129 records; 6 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 467 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'PTGDS' and resolved to 'Prostaglandin-H2 D-isomerase' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 129 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — No GWAS Catalog associations mapped to this gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P41222 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000107317/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3430865/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PTGDS — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PTGDS — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PTGDS%5Bgene%5D — _ClinVar build Build260809-1055.1_

## Provenance

- Generated: 2026-08-14T04:40:43  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
