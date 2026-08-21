# Protein Dossier — HNRNPC (Heterogeneous nuclear ribonucleoproteins C1/C2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Height | 0.0326 | 0.0111 | 0.00338 | Wald ratio | 1 | trans | NA |
| Neo-agreeableness | 0.647 | 0.239 | 0.00673 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: pneumothorax | 0.572 | 0.249 | 0.0214 | Wald ratio | 1 | trans | NA |
| Heel bone mineral density (BMD) T-score  automated | 0.0248 | 0.0108 | 0.0221 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: I48 Atrial fibrillation and flutter | -0.212 | 0.099 | 0.0322 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: J33 Nasal polyp | 0.192 | 0.101 | 0.0585 | Wald ratio | 1 | trans | NA |
| Fractured bone site(s): Wrist | 0.0962 | 0.0544 | 0.0768 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: muscle or soft tissue injuries | 0.15 | 0.0857 | 0.0791 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: I83 Varicose veins of lower extremities | -0.113 | 0.0657 | 0.0853 | Wald ratio | 1 | trans | NA |
| Haemoglobin concentration | 0.0443 | 0.0261 | 0.0894 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: K60 Fissure and fistula of anal and rectal regions | -0.288 | 0.171 | 0.0925 | Wald ratio | 1 | trans | NA |
| Packed cell volume | 0.149 | 0.09 | 0.0984 | Wald ratio | 1 | trans | NA |
| _...and 84 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_9 association rows across 7 traits (7 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Height | 2e-48 | rs8016099 | 2 | GCST90245848 | MR: beta=0.0326, p=0.00338 (trans) |
| C-reactive protein levels | 2e-10 | rs11156891 | 2 | GCST90029070 | no MR -> candidate analysis |
| C-reactive protein levels (MTAG) | 1e-9 | rs12589290 | 1 | GCST90179146 | no MR -> candidate analysis |
| Height (baseline) | 4e-9 | rs59988950 | 1 | GCST90565843 | no MR -> candidate analysis |
| Albumin levels | 9e-9 | rs35141059 | 1 | GCST90662901 | no MR -> candidate analysis |
| Bipolar disorder | 2e-6 | rs17197037 | 1 | GCST001135 | MR: beta=0.185, p=0.183 (trans) |
| Trauma exposure | 7e-6 | rs111571004 | 1 | GCST009982 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 432 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| intellectual developmental disorder, autosomal dominant 74 | 0.718 | — | established (curated) | no MR -> candidate analysis |
| complex neurodevelopmental disorder | 0.608 | — | established (curated) | no MR -> candidate analysis |
| hereditary disease | 0.308 | — | established (curated) | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Heterogeneous nuclear ribonucleoproteins C1/C2) |
| gnomAD constraint | pLI=1, LOEUF=0.233 — LoF-INTOLERANT |
| GWAS Catalog | 32 unique SNPs / 63 rows |
| ClinVar | 121 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 432 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'HNRNPC' and resolved to 'Heterogeneous nuclear ribonucleoproteins C1/C2' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 121 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 7 of 7 traits by best p-value, aggregated from 9 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P07910 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000092199/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2216742/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/HNRNPC — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/HNRNPC — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=HNRNPC%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/HNRNPC — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:01:20  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
