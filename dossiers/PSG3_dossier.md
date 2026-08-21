# Protein Dossier — PSG3 (Pregnancy-specific beta-1-glycoprotein 3)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Clear cell ovarian cancer | -0.209 | 0.0663 | 0.00163 | Wald ratio | 1 | cis | NA |
| Femoral neck bone mineral density | -0.0234 | 0.0122 | 0.0555 | Wald ratio | 1 | cis | NA |
| Eczema | 0.056 | 0.0296 | 0.0583 | Wald ratio | 1 | cis | NA |
| Rheumatoid arthritis | 0.0601 | 0.0376 | 0.11 | Wald ratio | 1 | cis | NA |
| Bulimia nervosa | 0.0276 | 0.0184 | 0.134 | Wald ratio | 1 | cis | NA |
| Forearm bone mineral density | 0.0349 | 0.0241 | 0.148 | Wald ratio | 1 | cis | NA |
| Intracranial volume | -3.98e+03 | 3.11e+03 | 0.2 | Wald ratio | 1 | cis | NA |
| Depressive symptoms | -0.00767 | 0.00613 | 0.211 | Wald ratio | 1 | cis | NA |
| Myocardial infarction | -0.0208 | 0.0167 | 0.211 | Wald ratio | 1 | cis | NA |
| Coronary heart disease | -0.0185 | 0.0154 | 0.228 | Wald ratio | 1 | cis | NA |
| Thalamus volume | -12 | 10 | 0.231 | Wald ratio | 1 | cis | NA |
| Lung cancer | -0.0339 | 0.0289 | 0.242 | Wald ratio | 1 | cis | NA |
| _...and 9 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_8 association rows across 5 traits (8 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| CEACAM1 protein levels | 3e-32 | rs147492478 | 1 | GCST90468692 | no MR -> candidate analysis |
| Low density lipoprotein cholesterol levels | 2e-17 | rs538657595 | 2 | GCST90239658 | no MR -> candidate analysis |
| PSG1 protein levels | 1e-16 | rs141072282 | 1 | GCST90470353 | no MR -> candidate analysis |
| Non-HDL cholesterol levels | 3e-11 | rs538657595 | 2 | GCST90239670 | no MR -> candidate analysis |
| Total cholesterol levels | 1e-10 | rs538657595 | 2 | GCST90239676 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 75 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| intestinal impaction | 0.416 | — | common-variant locus | no MR -> candidate analysis |
| venous thromboembolism | 0.093 | — | common-variant locus | no MR -> candidate analysis |
| Alzheimer disease | 0.055 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=8.2e-26, LOEUF=1.59 — LoF-tolerant |
| GWAS Catalog | 22 unique SNPs / 44 rows |
| ClinVar | 162 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 75 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'PSG3'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 162 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 5 of 5 traits by best p-value, aggregated from 8 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q16557 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000221826/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PSG3 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PSG3 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PSG3%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PSG3 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:39:36  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
