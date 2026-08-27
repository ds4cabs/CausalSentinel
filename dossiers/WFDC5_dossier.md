# Protein Dossier — WFDC5 (WAP four-disulfide core domain protein 5)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Height | 0.0742 | 0.017 | 1.31e-05 | Wald ratio | 1 | cis | NA |
| Eczema | 0.447 | 0.105 | 2.18e-05 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Diabetes related eye disease | 0.415 | 0.117 | 3.74e-04 | Wald ratio | 1 | cis | NA |
| Neuroblastoma | -0.814 | 0.25 | 0.00113 | Wald ratio | 1 | cis | NA |
| Weight | 0.0336 | 0.012 | 0.005 | Wald ratio | 1 | cis | NA |
| Neuroticism | -0.0568 | 0.0218 | 0.00932 | Wald ratio | 1 | cis | NA |
| Mean platelet volume | -0.0135 | 0.00568 | 0.0171 | Wald ratio | 1 | cis | NA |
| Lung cancer | 0.231 | 0.0976 | 0.0179 | Wald ratio | 1 | cis | NA |
| Ischemic stroke | 0.223 | 0.0956 | 0.0199 | Wald ratio | 1 | cis | NA |
| Melanoma | -0.745 | 0.329 | 0.0234 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: S76 Injury of muscle and tendon at hip and thigh level | 0.766 | 0.343 | 0.0257 | Wald ratio | 1 | cis | NA |
| Triglycerides | 0.0581 | 0.0271 | 0.0319 | Wald ratio | 1 | cis | NA |
| _...and 95 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_12 association rows across 10 traits (12 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| LY6D/WFDC12 protein level ratio | 5e-1373 | rs2157361 | 1 | GCST90315346 | no MR -> candidate analysis |
| KLK8/WFDC12 protein level ratio | 3e-1335 | rs2157361 | 1 | GCST90315259 | no MR -> candidate analysis |
| CDSN/WFDC12 protein level ratio | 6e-1322 | rs2157361 | 1 | GCST90313999 | no MR -> candidate analysis |
| LGALS7_LGALS7B/WFDC12 protein level ratio | 2e-1206 | rs2157361 | 1 | GCST90315317 | no MR -> candidate analysis |
| Serum levels of protein WISP2 | 2e-128 | rs760365325 | 1 | GCST90089393 | no MR -> candidate analysis |
| WFDC12 protein levels | 7e-60 | rs534712611 | 2 | GCST90471073 | no MR -> candidate analysis |
| Antileukoproteinase levels | 1e-30 | rs916311 | 1 | GCST90246475 | no MR -> candidate analysis |
| Cerebrospinal fluid protein WFDC12 levels | 2e-10 | rs6104016 | 1 | GCST90944064 | no MR -> candidate analysis |
| Bipolar disorder | 6e-9 | rs6130764 | 2 | GCST011102 | no MR -> candidate analysis |
| Eye color (hue) | 2e-8 | rs17422688 | 1 | GCST007456 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 16 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| type 2 diabetes mellitus | 0.259 | — | common-variant locus | no MR -> candidate analysis |
| bipolar disorder | 0.047 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=8.9e-06, LOEUF=1.47 — LoF-tolerant |
| GWAS Catalog | 61 unique SNPs / 122 rows |
| ClinVar | 32 records; 8 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 16 of 16 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'WFDC5'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 32 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 10 of 10 traits by best p-value, aggregated from 12 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q8TCV5 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000175121/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/WFDC5 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/WFDC5 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=WFDC5%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/WFDC5 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:37:34  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
