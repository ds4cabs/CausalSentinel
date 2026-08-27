# Protein Dossier — CEL (Bile salt-activated lipase)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: N92 Excessive  frequent and irregular menstruation | 0.183 | 0.0584 | 0.00167 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: chronic obstructive airways disease or copd | 0.364 | 0.122 | 0.00273 | Wald ratio | 1 | cis | NA |
| Glioma | 0.663 | 0.233 | 0.00441 | Wald ratio | 1 | cis | NA |
| Sleep duration | -0.0206 | 0.00783 | 0.00837 | Wald ratio | 1 | cis | NA |
| 2hr glucose | 0.204 | 0.0861 | 0.0176 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | -0.03 | 0.0129 | 0.0205 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K57 Diverticular disease of intestine | 0.142 | 0.0615 | 0.0209 | Wald ratio | 1 | cis | NA |
| Caudate volume | 44.9 | 20.6 | 0.0295 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: emphysema or chronic bronchitis | 0.147 | 0.0754 | 0.0504 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: sleep apnoea | 0.273 | 0.141 | 0.0531 | Wald ratio | 1 | cis | NA |
| Small vessel disease | 0.299 | 0.161 | 0.0631 | Wald ratio | 1 | cis | NA |
| Invasive mucinous ovarian cancer | 0.323 | 0.184 | 0.0792 | Wald ratio | 1 | cis | NA |
| _...and 83 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_12 association rows across 11 traits (12 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Bile salt-activated lipase levels | 1e-44 | rs2075733 | 2 | GCST90427924 | no MR -> candidate analysis |
| ALPI protein levels | 1e-25 | rs141668780 | 1 | GCST90468285 | no MR -> candidate analysis |
| ABO protein levels | 4e-22 | rs551202309 | 1 | GCST90468191 | no MR -> candidate analysis |
| PLA2G1B protein levels | 2e-17 | rs116842520 | 1 | GCST90470246 | no MR -> candidate analysis |
| Type 1 diabetes | 4e-17 | rs541856133 | 1 | GCST90014023 | no MR -> candidate analysis |
| KIRREL2 protein levels | 2e-14 | rs526855 | 1 | GCST90469690 | no MR -> candidate analysis |
| Alkaline phosphatase (UKB data field 30610) | 3e-14 | rs577793545 | 1 | GCST90468060 | no MR -> candidate analysis |
| Serum levels of protein CEL | 1e-12 | rs509064 | 1 | GCST90090829 | no MR -> candidate analysis |
| CUZD1 protein levels | 3e-12 | rs75294797 | 1 | GCST90468919 | no MR -> candidate analysis |
| VWF protein levels | 7e-12 | rs142810361 | 1 | GCST90471065 | no MR -> candidate analysis |
| CD34 protein levels | 9e-12 | rs139744322 | 1 | GCST90468626 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 239 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| MODY | 0.788 | — | established (curated) | no MR -> candidate analysis |
| maturity-onset diabetes of the young | 0.608 | — | established (curated) | no MR -> candidate analysis |
| hereditary disease | 0.318 | — | established (curated) | no MR -> candidate analysis |
| monogenic diabetes | 0.246 | — | established (curated) | no MR -> candidate analysis |
| type 2 diabetes mellitus | 0.195 | — | established (curated) | no MR -> candidate analysis |

> Of the 5 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Bile salt-activated lipase) |
| gnomAD constraint | pLI=2e-09, LOEUF=0.893 — LoF-tolerant |
| GWAS Catalog | 169 unique SNPs / 384 rows |
| ClinVar | 486 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 239 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'CEL' and resolved to 'Bile salt-activated lipase' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 486 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 11 of 11 traits by best p-value, aggregated from 12 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P19835 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000170835/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3219/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CEL — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CEL — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CEL%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CEL — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:47:00  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
