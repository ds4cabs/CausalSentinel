# Protein Dossier — SFRP4 (Secreted frizzled-related protein 4)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: M16 Coxarthrosis [arthrosis of hip] | 0.288 | 0.075 | 1.24e-04 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | 0.0557 | 0.0155 | 3.10e-04 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K60 Fissure and fistula of anal and rectal regions | 0.392 | 0.121 | 0.00125 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | -0.0272 | 0.00979 | 0.00552 | Wald ratio | 1 | cis | NA |
| Potassium in urine | -0.0326 | 0.0121 | 0.00714 | Wald ratio | 1 | cis | NA |
| Creatinine (enzymatic) in urine | -0.027 | 0.0114 | 0.0178 | Wald ratio | 1 | cis | NA |
| Cough on most days | -0.173 | 0.0734 | 0.0182 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N81 Female genital prolapse | 0.184 | 0.0836 | 0.0281 | Wald ratio | 1 | cis | NA |
| Fractured or broken bones in last 5 years | -0.0887 | 0.0407 | 0.0295 | Wald ratio | 1 | cis | NA |
| Hearing difficulty or problems: Yes | 0.0423 | 0.0197 | 0.0322 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I83 Varicose veins of lower extremities | -0.219 | 0.105 | 0.037 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K43 Ventral hernia | 0.284 | 0.138 | 0.0396 | Wald ratio | 1 | cis | NA |
| _...and 67 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_373 association rows across 88 traits (356 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Height | 2e-277 | rs6963134 | 25 | GCST90245848 | no MR -> candidate analysis |
| Estimated bone mineral density | 2e-229 | rs10235021 | 6 | GCST90726625 | no MR -> candidate analysis |
| Heel bone mineral density | 2e-215 | rs6973667 | 27 | GCST007066 | MR: beta=0.0557, p=3.10e-04 (cis) |
| Dupuytren's disease | 2e-176 | rs2044830 | 9 | GCST90301252 | no MR -> candidate analysis |
| SFRP4 protein levels | 3e-175 | rs75207237 | 2 | GCST90470611 | no MR -> candidate analysis |
| Contracture of palmar fascia [Dupuytren's disease] (PheCode  | 5e-143 | rs74335252 | 2 | GCST90480521 | no MR -> candidate analysis |
| Secreted frizzled-related protein 4 levels | 5e-50 | rs75207237 | 2 | GCST90249517 | no MR -> candidate analysis |
| Bone density (confirmatory factor analysis Factor 19) | 1e-41 | rs939666 | 1 | GCST90309353 | no MR -> candidate analysis |
| Standing height (UKB data field 50) | 3e-38 | rs1403987 | 1 | GCST90468178 | no MR -> candidate analysis |
| Lumbar spine bone mineral density | 4e-38 | rs6959212 | 2 | GCST001482 | MR: beta=0.0378, p=0.401 (cis) |
| Height (baseline) | 1e-34 | rs1524065 | 9 | GCST90565843 | no MR -> candidate analysis |
| Fasciitis (PheCode 728.7) | 5e-32 | rs6965376 | 2 | GCST90476244 | no MR -> candidate analysis |
| _...and 76 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 691 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Pyle disease | 0.792 | — | established (curated) | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.7e-06, LOEUF=0.963 — LoF-tolerant |
| GWAS Catalog | 211 unique SNPs / 388 rows |
| ClinVar | 202 records; 5 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 691 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'SFRP4'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 202 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 88 traits by best p-value, aggregated from 373 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q6FHJ7 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000106483/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/SFRP4 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/SFRP4 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=SFRP4%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/SFRP4 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:03:48  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
