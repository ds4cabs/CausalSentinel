# Protein Dossier — LILRA4 (Leukocyte immunoglobulin-like receptor subfamily A member 4)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Potassium in urine | -0.0268 | 0.00821 | 0.00111 | Inverse variance weighted | 2 | cis | NA |
| Potassium in urine | -0.0268 | 0.00821 | 0.00111 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: polio  or  poliomyelitis | 0.525 | 0.191 | 0.00593 | Inverse variance weighted | 2 | cis | NA |
| Non-cancer illness code  self-reported: polio  or  poliomyelitis | 0.525 | 0.191 | 0.00593 | Inverse variance weighted | 2 | trans | NA |
| Diagnoses - main ICD10: I30 Acute pericarditis | 0.643 | 0.263 | 0.0145 | Inverse variance weighted | 2 | cis | NA |
| Diagnoses - main ICD10: I30 Acute pericarditis | 0.643 | 0.263 | 0.0145 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: anxiety or panic attacks | -0.198 | 0.0857 | 0.0207 | Inverse variance weighted | 2 | cis | NA |
| Non-cancer illness code  self-reported: anxiety or panic attacks | -0.198 | 0.0857 | 0.0207 | Inverse variance weighted | 2 | trans | NA |
| Gallbladder cancer | 2.78 | 1.37 | 0.043 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M72 Fibroblastic disorders | -0.311 | 0.155 | 0.044 | Inverse variance weighted | 2 | cis | NA |
| Diagnoses - main ICD10: M72 Fibroblastic disorders | -0.311 | 0.155 | 0.044 | Inverse variance weighted | 2 | trans | NA |
| Diagnoses - main ICD10: I80 Phlebitis and thrombophlebitis | 0.195 | 0.0985 | 0.0473 | Inverse variance weighted | 2 | cis | NA |
| _...and 145 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_48 association rows across 28 traits (44 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating LAIR1 levels | 3e-545 | rs59862055 | 1 | GCST90860669 | no MR -> candidate analysis |
| LAIR1 protein levels | 6e-202 | rs73061003 | 5 | GCST90469728 | no MR -> candidate analysis |
| Leukocyte immunoglobulin-like receptor subfamily A member 4  | 3e-198 | rs2241384 | 4 | GCST90248298 | no MR -> candidate analysis |
| LILRA3 protein levels | 2e-158 | rs542875167 | 5 | GCST90469772 | no MR -> candidate analysis |
| LILRB5 protein levels | 1e-38 | rs73938664 | 5 | GCST90469779 | no MR -> candidate analysis |
| High density lipoprotein cholesterol levels | 2e-28 | rs17634081 | 1 | GCST90019510 | no MR -> candidate analysis |
| Apolipoprotein A1 levels | 4e-25 | rs17634081 | 1 | GCST90019495 | no MR -> candidate analysis |
| LILRB2 protein levels | 4e-22 | rs78469793 | 5 | GCST90469777 | no MR -> candidate analysis |
| Leukocyte immunoglobulin-like receptor subfamily A member 4  | 3e-21 | rs2241384 | 1 | GCST90241789 | no MR -> candidate analysis |
| Serum levels of protein LILRA4 | 1e-19 | rs2241384 | 1 | GCST90090112 | no MR -> candidate analysis |
| LAIR2 protein levels | 2e-17 | rs59862055 | 1 | GCST90469729 | no MR -> candidate analysis |
| LILRB1 protein levels | 5e-17 | rs56374127 | 1 | GCST90469776 | no MR -> candidate analysis |
| _...and 16 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 81 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Abnormality of the gastrointestinal tract | 0.21 | — | common-variant locus | no MR -> candidate analysis |
| disease of peritoneum | 0.21 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 1 known modulators (Leukocyte immunoglobulin-like receptor subfamily A member 4) |
| gnomAD constraint | pLI=2.4e-18, LOEUF=1.3 — LoF-tolerant |
| GWAS Catalog | 196 unique SNPs / 532 rows |
| ClinVar | 125 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 81 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'LILRA4' and resolved to 'Leukocyte immunoglobulin-like receptor subfamily A member 4' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 125 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 28 traits by best p-value, aggregated from 48 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P59901 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000239961/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4804246/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/LILRA4 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/LILRA4 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=LILRA4%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/LILRA4 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:32:59  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
