# Protein Dossier — GLRX2 (Glutaredoxin-2, mitochondrial)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Potassium in urine | -0.0247 | 0.00725 | 6.44e-04 | Wald ratio | 1 | cis | NA |
| Creatinine (enzymatic) in urine | -0.0219 | 0.00683 | 0.00135 | Wald ratio | 1 | cis | NA |
| Eczema | 0.427 | 0.163 | 0.00886 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: bladder problem (not cancer) | 0.188 | 0.0782 | 0.0164 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R14 Flatulence and related conditions | 0.462 | 0.196 | 0.0185 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: retinal detachment | 0.234 | 0.0997 | 0.0191 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M16 Coxarthrosis [arthrosis of hip] | -0.153 | 0.0697 | 0.0282 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: polio  or  poliomyelitis | 0.389 | 0.194 | 0.0447 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Injury or trauma resulting in loss of vision | 0.154 | 0.0806 | 0.0562 | Wald ratio | 1 | cis | NA |
| Weight | -0.0111 | 0.00631 | 0.0791 | Wald ratio | 1 | cis | NA |
| Primary sclerosing cholangitis  | -0.233 | 0.136 | 0.0863 | Wald ratio | 1 | cis | NA |
| Invasive mucinous ovarian cancer | 0.204 | 0.123 | 0.0973 | Wald ratio | 1 | cis | NA |
| _...and 44 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_15 association rows across 12 traits (15 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| HCLS1/TRIAP1 protein level ratio | 8e-285 | rs148212596 | 1 | GCST90315044 | no MR -> candidate analysis |
| FXN/TRIAP1 protein level ratio | 1e-277 | rs148212596 | 1 | GCST90314899 | no MR -> candidate analysis |
| HTRA2/TRIAP1 protein level ratio | 2e-255 | rs148212596 | 1 | GCST90315099 | no MR -> candidate analysis |
| TMSB10/TRIAP1 protein level ratio | 1e-235 | rs148212596 | 1 | GCST90315924 | no MR -> candidate analysis |
| GFER/TRIAP1 protein level ratio | 3e-212 | rs148212596 | 1 | GCST90314921 | no MR -> candidate analysis |
| NUCB2/TRIAP1 protein level ratio | 3e-196 | rs148212596 | 1 | GCST90315577 | no MR -> candidate analysis |
| Glutaredoxin-2, mitochondrial levels | 2e-153 | rs148212596 | 3 | GCST90247745 | no MR -> candidate analysis |
| DCTN1/TRIAP1 protein level ratio | 5e-142 | rs148212596 | 1 | GCST90314434 | no MR -> candidate analysis |
| HEXIM1/TRIAP1 protein level ratio | 3e-126 | rs148212596 | 1 | GCST90315054 | no MR -> candidate analysis |
| TRIAP1 protein levels | 2e-90 | rs148212596 | 2 | GCST90470963 | no MR -> candidate analysis |
| Cerebrospinal fluid protein GLRX2 levels | 9e-51 | rs148212596 | 1 | GCST90943425 | no MR -> candidate analysis |
| Glutaredoxin-2, mitochondrial levels (GLRX2.12486.8.3) | 4e-41 | rs148212596 | 1 | GCST90241278 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 157 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| hypertensive disorder | 0.186 | — | common-variant locus | no MR -> candidate analysis |
| essential hypertension | 0.148 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.00065, LOEUF=1.19 — LoF-tolerant |
| GWAS Catalog | 14 unique SNPs / 28 rows |
| ClinVar | 48 records; 5 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 157 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'GLRX2'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 48 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 12 of 12 traits by best p-value, aggregated from 15 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9NS18 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000023572/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/GLRX2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/GLRX2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=GLRX2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/GLRX2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:49:55  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
