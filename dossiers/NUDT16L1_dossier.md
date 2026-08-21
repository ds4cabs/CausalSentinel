# Protein Dossier — NUDT16L1 (Tudor-interacting repair regulator protein)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: N81 Female genital prolapse | -0.185 | 0.0786 | 0.0186 | Wald ratio | 1 | trans | NA |
| Fasting proinsulin | -0.0765 | 0.0353 | 0.0303 | Wald ratio | 1 | trans | NA |
| Urate | 0.0618 | 0.0288 | 0.0321 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: R55 Syncope and collapse | -0.216 | 0.104 | 0.0367 | Wald ratio | 1 | trans | NA |
| Alcohol intake frequency | -0.0223 | 0.0115 | 0.0517 | Wald ratio | 1 | trans | NA |
| LDL cholesterol | 0.0491 | 0.0253 | 0.0522 | Wald ratio | 1 | trans | NA |
| Hippocampus volume | 31.4 | 16.2 | 0.0523 | Wald ratio | 1 | trans | NA |
| Cancer code  self-reported: prostate cancer | 0.149 | 0.0789 | 0.0585 | Wald ratio | 1 | trans | NA |
| Forced vital capacity (FVC) | 0.012 | 0.00637 | 0.0598 | Wald ratio | 1 | trans | NA |
| Total cholesterol | 0.0465 | 0.0247 | 0.06 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: ankylosing spondylitis | 0.224 | 0.119 | 0.0608 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: S66 Injury of muscle and tendon at wrist and hand level | 0.28 | 0.151 | 0.0635 | Wald ratio | 1 | trans | NA |
| _...and 80 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_5 association rows across 4 traits (5 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Height | 1e-89 | rs841217 | 2 | GCST90245848 | no MR -> candidate analysis |
| Physical function (baseline) | 3e-15 | rs841217 | 1 | GCST90565837 | no MR -> candidate analysis |
| Body size (confirmatory factor analysis Factor 21) | 3e-12 | rs841217 | 1 | GCST90309355 | no MR -> candidate analysis |
| Gamma glutamyl transferase levels | 5e-10 | rs841219 | 1 | GCST90428730 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 65 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| systemic inflammatory response syndrome | 0.049 | — | common-variant locus | no MR -> candidate analysis |
| type 2 diabetes mellitus | 0.036 | — | common-variant locus | no MR -> candidate analysis |
| diabetes mellitus | 0.036 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Tudor-interacting repair regulator protein) |
| gnomAD constraint | pLI=9.6e-08, LOEUF=1.61 — LoF-tolerant |
| GWAS Catalog | 60 unique SNPs / 120 rows |
| ClinVar | 93 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 65 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'NUDT16L1' and resolved to 'Tudor-interacting repair regulator protein' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 93 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 4 of 4 traits by best p-value, aggregated from 5 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9BRJ7 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000168101/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL5724605/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/NUDT16L1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/NUDT16L1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=NUDT16L1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/NUDT16L1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:07:22  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
