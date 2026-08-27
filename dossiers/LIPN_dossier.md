# Protein Dossier — LIPN (Lipase member N)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Height | 0.00925 | 0.00315 | 0.00331 | Wald ratio | 1 | cis | NA |
| Alzheimer's disease | 0.0494 | 0.017 | 0.00371 | Wald ratio | 1 | cis | NA |
| Neo-neuroticism | 0.273 | 0.0995 | 0.00611 | Wald ratio | 1 | cis | NA |
| Small vessel disease | 0.0934 | 0.0372 | 0.0121 | Wald ratio | 1 | cis | NA |
| Neo-extraversion | -0.197 | 0.0796 | 0.0134 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K20 Oesophagitis | -0.0649 | 0.0278 | 0.0196 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: gout | -0.0526 | 0.0228 | 0.021 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M54 Dorsalgia | -0.0478 | 0.021 | 0.0229 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R55 Syncope and collapse | -0.0662 | 0.0292 | 0.0234 | Wald ratio | 1 | cis | NA |
| Sleep duration | 0.00451 | 0.00201 | 0.0249 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R10 Abdominal and pelvic pain | -0.0286 | 0.0128 | 0.0257 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: osteoarthritis | -0.0195 | 0.00879 | 0.0269 | Wald ratio | 1 | cis | NA |
| _...and 87 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_12 association rows across 8 traits (11 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Lipase member N levels | 1e-764 | rs10509554 | 3 | GCST90248295 | no MR -> candidate analysis |
| Lipase member N levels (LIPN.8097.77.3) | 7e-499 | rs10509554 | 2 | GCST90241809 | no MR -> candidate analysis |
| Serum levels of protein LIPN | 5e-178 | rs10509554 | 2 | GCST90090049 | no MR -> candidate analysis |
| Blood protein levels | 7e-104 | rs10509554 | 1 | GCST006585 | no MR -> candidate analysis |
| Lipase member N level in Chronic kidney disease with hyperte | 1e-77 | rs10509554 | 1 | GCST90238820 | no MR -> candidate analysis |
| Neuroendocrine secretory protein 55 protein levels (SomaScan | 1e-23 | rs10509554 | 1 | GCST90443255 | no MR -> candidate analysis |
| FASLG protein levels | 4e-16 | rs10509554 | 1 | GCST90469191 | no MR -> candidate analysis |
| Lobe attachment (rater-scored or self-reported) | 2e-6 | rs444386 | 1 | GCST005192 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 60 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| lamellar ichthyosis | 0.606 | — | established (curated) | no MR -> candidate analysis |
| arthropathy | 0.459 | — | common-variant locus | no MR -> candidate analysis |
| androgenetic alopecia | 0.045 | — | common-variant locus | no MR -> candidate analysis |
| malunion fracture | 0.04 | — | common-variant locus | no MR -> candidate analysis |
| adolescent idiopathic scoliosis | 0.035 | — | common-variant locus | no MR -> candidate analysis |

> Of the 5 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Carboxylic ester hydrolase LipN) |
| gnomAD constraint | pLI=1.3e-08, LOEUF=0.984 — LoF-tolerant |
| GWAS Catalog | 41 unique SNPs / 81 rows |
| ClinVar | 166 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 60 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'LIPN' and resolved to 'Carboxylic ester hydrolase LipN' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 166 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 8 of 8 traits by best p-value, aggregated from 12 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q5VXI9 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000204020/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4105751/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/LIPN — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/LIPN — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=LIPN%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/LIPN — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:35:39  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
