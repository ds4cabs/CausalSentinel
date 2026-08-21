# Protein Dossier — CCNH (Cyclin-H)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Large vessel disease | -0.666 | 0.168 | 7.19e-05 | Wald ratio | 1 | cis | NA |
| Weight | -0.0385 | 0.011 | 4.83e-04 | Wald ratio | 1 | cis | NA |
| Height | -0.0503 | 0.0147 | 6.07e-04 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K43 Ventral hernia | 0.389 | 0.129 | 0.00263 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | 0.132 | 0.0487 | 0.00658 | Wald ratio | 1 | cis | NA |
| Alcohol intake frequency | -0.0486 | 0.0184 | 0.00847 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: depression | -0.152 | 0.0602 | 0.0113 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: H25 Senile cataract | 0.268 | 0.11 | 0.0154 | Wald ratio | 1 | cis | NA |
| Childhood intelligence | -0.153 | 0.065 | 0.0182 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | -0.0288 | 0.0125 | 0.021 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: arthritis (nos) | 0.255 | 0.113 | 0.0244 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I30 Acute pericarditis | 0.791 | 0.379 | 0.0369 | Wald ratio | 1 | cis | NA |
| _...and 101 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_8 association rows across 7 traits (5 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Height | 7e-32 | rs4421140 | 1 | GCST90245848 | MR: beta=-0.0503, p=6.07e-04 (cis) |
| Cyclin-H levels (CCNH.9848.22.3) | 1e-14 | rs2230641 | 1 | GCST90240828 | no MR -> candidate analysis |
| Chronotype | 4e-11 | rs66507804 | 1 | GCST007576 | no MR -> candidate analysis |
| Morningness | 1e-10 | rs66507804 | 1 | GCST007983 | no MR -> candidate analysis |
| Macular thickness | 4e-10 | rs13157168 | 1 | GCST006976 | no MR -> candidate analysis |
| PHQ score x Polysocial risk score (PsRS) interaction | 4e-6 | rs75661393 | 1 | GCST90451692 | no MR -> candidate analysis |
| Oligodendroglioma | 5e-6 | rs146974076 | 2 | GCST90296482 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 157 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| capillary malformation-arteriovenous malformation 1 | 0.933 | — | established (curated) | no MR -> candidate analysis |
| capillary malformation-arteriovenous malformation syndrome | 0.917 | — | established (curated) | no MR -> candidate analysis |
| Capillary malformation - arteriovenous malformation | 0.917 | — | established (curated) | no MR -> candidate analysis |
| Abnormality of the cardiovascular system | 0.893 | — | established (curated) | no MR -> candidate analysis |
| angioosteohypertrophic syndrome | 0.684 | — | established (curated) | no MR -> candidate analysis |
| hereditary disease | 0.559 | — | established (curated) | no MR -> candidate analysis |
| capillary infantile hemangioma | 0.559 | — | established (curated) | no MR -> candidate analysis |
| type 2 diabetes mellitus | 0.546 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.502 | — | common-variant locus | no MR -> candidate analysis |
| prostate carcinoma | 0.44 | — | common-variant locus | no MR -> candidate analysis |
| health study participation | 0.441 | — | common-variant locus | no MR -> candidate analysis |
| Wieacker-Wolff syndrome | 0.438 | — | established (curated) | no MR -> candidate analysis |
| Intellectual disability-developmental delay-contractures syndrome | 0.438 | — | established (curated) | no MR -> candidate analysis |
| smoking initiation | 0.404 | — | common-variant locus | no MR -> candidate analysis |
| ulcerative colitis | 0.388 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **15 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Cyclin-H) |
| gnomAD constraint | pLI=1.8e-08, LOEUF=0.999 — LoF-tolerant |
| GWAS Catalog | 26 unique SNPs / 52 rows |
| ClinVar | 1486 records; 8 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 157 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'CCNH' and resolved to 'Cyclin-H' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 1486 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 7 of 7 traits by best p-value, aggregated from 8 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P51946 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000134480/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2165/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CCNH — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CCNH — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CCNH%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CCNH — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:39:52  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
