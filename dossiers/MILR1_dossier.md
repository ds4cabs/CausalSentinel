# Protein Dossier — MILR1 (Allergin-1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Body mass index (BMI) | 0.0268 | 0.0103 | 0.00934 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: R04 Haemorrhage from respiratory passages | 0.279 | 0.11 | 0.0112 | Wald ratio | 1 | trans | NA |
| Lung cancer | -0.178 | 0.0733 | 0.0152 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: J33 Nasal polyp | 0.258 | 0.118 | 0.0281 | Wald ratio | 1 | trans | NA |
| Underlying (primary) cause of death: ICD10: E85.4 Organ-limited amyloidosis | 1.61 | 0.736 | 0.0283 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: K20 Oesophagitis | 0.189 | 0.0869 | 0.0298 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: bone disorder | 0.342 | 0.161 | 0.0336 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: kidney stone or ureter stone or bladder stone | 0.202 | 0.0962 | 0.0357 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: M17 Gonarthrosis [arthrosis of knee] | 0.132 | 0.0653 | 0.0432 | Wald ratio | 1 | trans | NA |
| Weight | 0.0179 | 0.0091 | 0.0493 | Wald ratio | 1 | trans | NA |
| Lung adenocarcinoma | -0.211 | 0.111 | 0.0587 | Wald ratio | 1 | trans | NA |
| Fractured bone site(s): Wrist | -0.161 | 0.0871 | 0.0652 | Wald ratio | 1 | trans | NA |
| _...and 68 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_33 association rows across 31 traits (30 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating MILR1 levels | 2e-754 | rs138176943 | 1 | GCST90860202 | no MR -> candidate analysis |
| MILR1 protein levels | 2e-56 | rs536767372 | 1 | GCST90469907 | no MR -> candidate analysis |
| Cerebrospinal fluid protein MILR1 levels | 3e-35 | rs138176943 | 1 | GCST90942449 | no MR -> candidate analysis |
| Sex hormone-binding globulin levels adjusted for BMI and hee | 4e-28 | rs17650301 | 1 | GCST90399398 | no MR -> candidate analysis |
| Height | 2e-27 | rs113252144 | 1 | GCST007841 | no MR -> candidate analysis |
| Sex hormone-binding globulin levels and heel estimated bone  | 3e-26 | rs17650301 | 1 | GCST90399396 | no MR -> candidate analysis |
| Mitochondrial DNA heteroplasmy (chrM:16183:A:AC case-only he | 5e-25 | rs17850455 | 1 | GCST90268483 | no MR -> candidate analysis |
| Standing height (UKB data field 50) | 6e-25 | rs113252144 | 1 | GCST90468178 | no MR -> candidate analysis |
| Heel bone mineral density | 3e-23 | rs17650301 | 3 | GCST007066 | no MR -> candidate analysis |
| Estimated bone mineral density | 4e-22 | rs17650301 | 1 | GCST90726625 | no MR -> candidate analysis |
| Height (baseline) | 6e-22 | rs113252144 | 1 | GCST90565843 | no MR -> candidate analysis |
| Age at menopause | 6e-20 | rs17650301 | 1 | GCST007079 | no MR -> candidate analysis |
| _...and 19 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 163 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| progressive external ophthalmoplegia with mitochondrial DNA deletions, autosomal dominant 4 | 0.833 | — | established (curated) | no MR -> candidate analysis |
| mitochondrial dna depletion syndrome 16B (neuroophthalmic type) | 0.699 | — | established (curated) | no MR -> candidate analysis |
| mitochondrial DNA depletion syndrome 16 (hepatic type) | 0.534 | — | established (curated) | no MR -> candidate analysis |
| hereditary spastic paraplegia | 0.278 | — | established (curated) | no MR -> candidate analysis |
| asthma | 0.087 | — | common-variant locus | MR: beta=-0.0402, p=0.182 (trans) |

> Of the 5 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=2.8e-15, LOEUF=2.26 — LoF-tolerant |
| GWAS Catalog | 47 unique SNPs / 80 rows |
| ClinVar | 586 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 163 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'MILR1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 586 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 31 traits by best p-value, aggregated from 33 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q7Z6M3 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000271605/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/MILR1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/MILR1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=MILR1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/MILR1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:48:35  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
