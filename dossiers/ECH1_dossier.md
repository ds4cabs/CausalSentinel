# Protein Dossier — ECH1 (Delta(3,5)-Delta(2,4)-dienoyl-CoA isomerase, mitochondrial)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: kidney stone or ureter stone or bladder stone | 0.199 | 0.0686 | 0.00368 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N40 Hyperplasia of prostate | -0.298 | 0.105 | 0.00444 | Wald ratio | 1 | cis | NA |
| Type 2 diabetes | -0.295 | 0.11 | 0.00766 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: uterine fibroids | -0.17 | 0.071 | 0.0167 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I80 Phlebitis and thrombophlebitis | -0.342 | 0.156 | 0.029 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: L03 Cellulitis | 0.151 | 0.0709 | 0.0333 | Wald ratio | 1 | cis | NA |
| Potassium in urine | -0.0158 | 0.00748 | 0.0347 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hiatus hernia | -0.113 | 0.0543 | 0.0382 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M17 Gonarthrosis [arthrosis of knee] | 0.0981 | 0.0482 | 0.042 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I30 Acute pericarditis | 0.512 | 0.275 | 0.0631 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: prostate cancer | -0.191 | 0.106 | 0.0715 | Wald ratio | 1 | cis | NA |
| Amygdala volume | -13.3 | 7.64 | 0.0823 | Wald ratio | 1 | cis | NA |
| _...and 59 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_10 association rows across 9 traits (9 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Delta(3,5)-Delta(2,4)-dienoyl-CoA isomerase, mitochondrial l | 1e-282 | rs2229259 | 1 | GCST90247247 | no MR -> candidate analysis |
| LGALS4 protein levels | 5e-48 | rs28496951 | 2 | GCST90469762 | no MR -> candidate analysis |
| Serum levels of protein ECH1 | 6e-42 | rs2229259 | 1 | GCST90087134 | no MR -> candidate analysis |
| Blood protein levels | 2e-33 | rs4802890 | 1 | GCST006585 | no MR -> candidate analysis |
| Enoyl-CoA delta isomerase 2, mitochondrial levels | 4e-22 | rs4802890 | 1 | GCST90247387 | no MR -> candidate analysis |
| Circulating LGALS4 levels | 4e-17 | rs10426289 | 1 | GCST90859971 | no MR -> candidate analysis |
| platelet count (mean, inv-norm transformed) | 9e-15 | rs11671711 | 1 | GCST90480651 | no MR -> candidate analysis |
| Diffuse plaques (SNP x SNP interaction) | 3e-9 | rs11671711 x rs8122161 | 1 | GCST010341 | no MR -> candidate analysis |
| TNFB levels | 4e-6 | rs2287953 | 1 | GCST90503395 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 103 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| alcohol drinking | 0.326 | — | common-variant locus | no MR -> candidate analysis |
| urolithiasis | 0.326 | — | common-variant locus | no MR -> candidate analysis |
| decubitus ulcer | 0.182 | — | common-variant locus | no MR -> candidate analysis |
| dementia | 0.163 | — | common-variant locus | no MR -> candidate analysis |
| neurodegenerative disease | 0.131 | — | common-variant locus | no MR -> candidate analysis |

> Of the 5 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Delta(3,5)-Delta(2,4)-dienoyl-CoA isomerase, mitochondrial) |
| gnomAD constraint | pLI=4.9e-09, LOEUF=1.1 — LoF-tolerant |
| GWAS Catalog | 61 unique SNPs / 122 rows |
| ClinVar | 87 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 103 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'ECH1' and resolved to 'Delta(3,5)-Delta(2,4)-dienoyl-CoA isomerase, mitochondrial' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 87 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 9 of 9 traits by best p-value, aggregated from 10 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q13011 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000104823/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4523284/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/ECH1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/ECH1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=ECH1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/ECH1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:22:56  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
