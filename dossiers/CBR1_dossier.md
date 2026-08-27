# Protein Dossier — CBR1 (Carbonyl reductase [NADPH] 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Fractured bone site(s): Wrist | -0.233 | 0.0662 | 4.39e-04 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M23 Internal derangement of knee | 0.115 | 0.0439 | 0.00855 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: emphysema or chronic bronchitis | -0.194 | 0.0773 | 0.0121 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: kidney stone or ureter stone or bladder stone | -0.232 | 0.106 | 0.0278 | Wald ratio | 1 | cis | NA |
| Sleep duration | -0.0124 | 0.0057 | 0.0293 | Wald ratio | 1 | cis | NA |
| Primary sclerosing cholangitis  | -0.18 | 0.0848 | 0.0334 | Wald ratio | 1 | cis | NA |
| Hearing difficulty or problems: Yes | 0.0261 | 0.0123 | 0.034 | Wald ratio | 1 | cis | NA |
| Weight | -0.0133 | 0.00645 | 0.0394 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K57 Diverticular disease of intestine | -0.116 | 0.058 | 0.0451 | Wald ratio | 1 | cis | NA |
| Nucleus accumbens volume | 6.63 | 3.4 | 0.0514 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K29 Gastritis and duodenitis | 0.0818 | 0.0437 | 0.061 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R07 Pain in throat and chest | 0.0563 | 0.0308 | 0.0681 | Wald ratio | 1 | cis | NA |
| _...and 63 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_3 association rows across 3 traits (2 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Height | 7e-24 | rs2835266 | 1 | GCST90245848 | no MR -> candidate analysis |
| C-reactive protein levels | 2e-9 | rs2156407 | 1 | GCST90029070 | no MR -> candidate analysis |
| Acetone levels | 1e-5 | rs41540212 | 1 | GCST90492713 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 713 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| mitral valve prolapse | 0.309 | — | common-variant locus | no MR -> candidate analysis |
| osteoporosis | 0.191 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.189 | — | common-variant locus | no MR -> candidate analysis |
| Left bundle branch block | 0.188 | — | common-variant locus | no MR -> candidate analysis |
| femoral neck fracture | 0.174 | — | common-variant locus | no MR -> candidate analysis |
| facial morphology | 0.162 | — | common-variant locus | no MR -> candidate analysis |
| Burkitt lymphoma | 0.161 | — | common-variant locus | no MR -> candidate analysis |
| musculoskeletal system disorder | 0.156 | — | common-variant locus | no MR -> candidate analysis |
| stomach disorder | 0.155 | — | common-variant locus | no MR -> candidate analysis |
| migraine disorder | 0.143 | — | common-variant locus | no MR -> candidate analysis |
| bone disorder | 0.142 | — | common-variant locus | no MR -> candidate analysis |
| arthropathy | 0.129 | — | common-variant locus | no MR -> candidate analysis |

> Of the 12 rows above, **12 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Carbonyl reductase [NADPH] 1) |
| gnomAD constraint | pLI=9.4e-05, LOEUF=1.71 — LoF-tolerant |
| GWAS Catalog | 47 unique SNPs / 94 rows |
| ClinVar | 131 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 4 clinical annotations across 5 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 713 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'CBR1' and resolved to 'Carbonyl reductase [NADPH] 1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 131 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 3 of 3 traits by best p-value, aggregated from 3 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P16152 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000159228/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL5586/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CBR1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CBR1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CBR1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=CBR1 — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CBR1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:29:35  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
