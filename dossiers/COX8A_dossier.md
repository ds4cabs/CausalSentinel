# Protein Dossier — COX8A (Cytochrome c oxidase subunit 8A, mitochondrial)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Height | 0.0181 | 0.00617 | 0.00338 | Wald ratio | 1 | trans | NA |
| Neo-agreeableness | 0.359 | 0.132 | 0.00673 | Wald ratio | 1 | trans | NA |
| Heel bone mineral density (BMD) T-score  automated | 0.0138 | 0.00601 | 0.0221 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: I48 Atrial fibrillation and flutter | -0.112 | 0.0493 | 0.0228 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: pneumothorax | 0.357 | 0.164 | 0.0299 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: K60 Fissure and fistula of anal and rectal regions | -0.149 | 0.0803 | 0.063 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: J33 Nasal polyp | 0.111 | 0.0605 | 0.0666 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: I83 Varicose veins of lower extremities | -0.0611 | 0.0345 | 0.0761 | Wald ratio | 1 | trans | NA |
| Fractured bone site(s): Wrist | 0.0545 | 0.0314 | 0.0823 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: muscle or soft tissue injuries | 0.0863 | 0.0504 | 0.0869 | Wald ratio | 1 | trans | NA |
| Haemoglobin concentration | 0.0246 | 0.0145 | 0.0894 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: osteoporosis | -0.0661 | 0.0398 | 0.0972 | Wald ratio | 1 | trans | NA |
| _...and 84 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_7 association rows across 4 traits (7 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Systolic blood pressure | 9e-17 | rs4980515 | 3 | GCST006624 | MR: beta=0.0043, p=0.367 (trans) |
| Pulse pressure | 3e-16 | rs4980515 | 2 | GCST90310296 | no MR -> candidate analysis |
| Systolic blood pressure (MTAG) | 1e-12 | rs4980515 | 1 | GCST90449056 | no MR -> candidate analysis |
| Forced expiratory volume in 1 second (FEV1) | 3e-8 | rs11605797 | 1 | GCST90705070 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 217 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Isolated cytochrome C oxidase deficiency | 0.605 | — | established (curated) | no MR -> candidate analysis |
| leigh syndrome due to mitochondrial complex iv deficiency | 0.596 | — | established (curated) | no MR -> candidate analysis |
| mitochondrial complex IV deficiency, nuclear type 15 | 0.017 | — | established (curated) | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.0019, LOEUF=2.68 — LoF-tolerant |
| GWAS Catalog | 32 unique SNPs / 64 rows |
| ClinVar | 49 records; 5 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 217 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'COX8A'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 49 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 4 of 4 traits by best p-value, aggregated from 7 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P10176 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000176340/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/COX8A — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/COX8A — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=COX8A%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/COX8A — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:58:41  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
