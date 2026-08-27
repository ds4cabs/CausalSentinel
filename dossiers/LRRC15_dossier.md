# Protein Dossier — LRRC15 (Leucine-rich repeat-containing protein 15)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: gastro-oesophageal reflux (gord)  or  gastric reflux | 0.0923 | 0.0283 | 0.00112 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: pernicious anaemia | 0.282 | 0.0904 | 0.00181 | Wald ratio | 1 | cis | NA |
| Sleep duration | 0.0127 | 0.00503 | 0.0117 | Wald ratio | 1 | cis | NA |
| Potassium in urine | -0.0158 | 0.00654 | 0.0161 | Wald ratio | 1 | cis | NA |
| Ovarian cancer | 0.0918 | 0.0389 | 0.0184 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: H25 Senile cataract | -0.215 | 0.092 | 0.0194 | Wald ratio | 1 | cis | NA |
| Happiness | 0.0159 | 0.008 | 0.0471 | Wald ratio | 1 | cis | NA |
| Knee osteoarthritis | -0.159 | 0.0802 | 0.0472 | Wald ratio | 1 | cis | NA |
| Packed cell volume | -0.154 | 0.083 | 0.0641 | Wald ratio | 1 | cis | NA |
| Forearm bone mineral density | -0.0718 | 0.0415 | 0.0837 | Wald ratio | 1 | cis | NA |
| Creatinine (enzymatic) in urine | -0.0106 | 0.00617 | 0.0866 | Wald ratio | 1 | cis | NA |
| Amyotrophic lateral sclerosis | -0.0921 | 0.0538 | 0.087 | Wald ratio | 1 | cis | NA |
| _...and 69 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_18 association rows across 10 traits (17 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Leucine-rich repeat-containing protein 15 levels | 2e-178 | rs34461611 | 3 | GCST90248316 | no MR -> candidate analysis |
| Leucine-rich repeat-containing protein 15 levels (LRRC15.655 | 6e-54 | rs57514363 | 2 | GCST90241775 | no MR -> candidate analysis |
| Serum levels of protein LRRC15 | 1e-41 | rs6762627 | 1 | GCST90089496 | no MR -> candidate analysis |
| Blood protein levels | 1e-27 | rs923931 | 5 | GCST006585 | no MR -> candidate analysis |
| Serum levels of protein CPN2 | 1e-19 | rs34234514 | 1 | GCST90089412 | no MR -> candidate analysis |
| von Willebrand factor A domain-containing protein 2 levels | 9e-13 | rs10698992 | 1 | GCST90250199 | no MR -> candidate analysis |
| 3-hydroxyanthranilate 3,4-dioxygenase levels | 3e-12 | rs11925692 | 1 | GCST90162457 | no MR -> candidate analysis |
| Carboxypeptidase N subunit 2 levels | 4e-12 | rs34234514 | 2 | GCST90246881 | no MR -> candidate analysis |
| Symbolic dysfunction (PheCode 292.12) | 3e-11 | rs529517393 | 1 | GCST90480741 | no MR -> candidate analysis |
| Circulating TNFRSF11B levels (id: OID00479_OID20735) | 1e-6 | rs115983293 | 1 | GCST90859839 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 148 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Atypical behavior | 0.073 | — | common-variant locus | no MR -> candidate analysis |
| gram-negative bacterial infections | 0.043 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Leucine-rich repeat-containing protein 15) |
| gnomAD constraint | pLI=0.0067, LOEUF=2.44 — LoF-tolerant |
| GWAS Catalog | 47 unique SNPs / 94 rows |
| ClinVar | 177 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 3 clinical annotations across 3 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 148 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'LRRC15' and resolved to 'Leucine-rich repeat-containing protein 15' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 177 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 10 of 10 traits by best p-value, aggregated from 18 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q8TF66 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000172061/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4295907/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/LRRC15 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/LRRC15 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=LRRC15%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=LRRC15 — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/LRRC15 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:38:10  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
