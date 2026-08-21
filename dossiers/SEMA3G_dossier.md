# Protein Dossier — SEMA3G (Semaphorin-3G)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| HDL cholesterol | 0.0845 | 0.0182 | 3.61e-06 | Wald ratio | 1 | cis | NA |
| Triglycerides | -0.0689 | 0.0175 | 8.28e-05 | Wald ratio | 1 | cis | NA |
| Age at menarche | 0.093 | 0.0296 | 0.0017 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M17 Gonarthrosis [arthrosis of knee] | -0.373 | 0.123 | 0.00246 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: emphysema or chronic bronchitis | 0.226 | 0.0804 | 0.00483 | Wald ratio | 1 | cis | NA |
| Height | 0.0409 | 0.0149 | 0.00596 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: G56 Mononeuropathies of upper limb | -0.341 | 0.126 | 0.00687 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | -0.0309 | 0.0116 | 0.00746 | Wald ratio | 1 | cis | NA |
| Lung cancer | -0.191 | 0.0849 | 0.0246 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: uterine fibroids | -0.279 | 0.126 | 0.0267 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I30 Acute pericarditis | 0.774 | 0.349 | 0.0268 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: osteoarthritis | -0.0938 | 0.0426 | 0.0275 | Wald ratio | 1 | cis | NA |
| _...and 107 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_14 association rows across 11 traits (14 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Semaphorin-3G levels | 4e-107 | rs2016575 | 2 | GCST90249487 | no MR -> candidate analysis |
| Serum levels of protein SEMA3G | 9e-20 | rs13091025 | 1 | GCST90089104 | no MR -> candidate analysis |
| Apolipoprotein A levels (UKB data field 30630) | 6e-18 | rs82825 | 1 | GCST90468061 | no MR -> candidate analysis |
| Semaphorin-3G levels (SEMA3G.5628.21.3) | 2e-17 | rs2016575 | 1 | GCST90242746 | no MR -> candidate analysis |
| Metabolic syndrome | 2e-14 | rs2016575 | 2 | GCST90444487 | no MR -> candidate analysis |
| Waist circumference adjusted for body mass index | 7e-14 | rs62257614 | 2 | GCST009867 | no MR -> candidate analysis |
| Calcium levels | 1e-10 | rs648514 | 1 | GCST90018951 | no MR -> candidate analysis |
| Cholesteryl Esters to Total Lipids in Very Large HDL percent | 1e-10 | rs82825 | 1 | GCST90501297 | no MR -> candidate analysis |
| Intelligence | 4e-9 | rs648514 | 1 | GCST90264174 | no MR -> candidate analysis |
| Waist-to-hip ratio adjusted for BMI | 4e-9 | rs62257614 | 1 | GCST009858 | no MR -> candidate analysis |
| Fluid intelligence score (baseline) | 2e-8 | rs661777 | 1 | GCST90565842 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 129 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| diverticular disease | 0.446 | — | common-variant locus | MR: beta=-0.191, p=0.0552 (cis) |
| hypertrophic cardiomyopathy | 0.271 | — | common-variant locus | no MR -> candidate analysis |
| gastroesophageal reflux disease | 0.21 | — | common-variant locus | no MR -> candidate analysis |
| esophageal disorder | 0.188 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.1e-19, LOEUF=0.991 — LoF-tolerant |
| GWAS Catalog | 104 unique SNPs / 260 rows |
| ClinVar | 408 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 129 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'SEMA3G'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 408 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 11 of 11 traits by best p-value, aggregated from 14 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9NS98 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000010319/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/SEMA3G — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/SEMA3G — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=SEMA3G%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/SEMA3G — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:58:55  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
