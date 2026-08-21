# Protein Dossier — HAVCR1 (Hepatitis A virus cellular receptor 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: L03 Cellulitis | 0.18 | 0.0489 | 2.31e-04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: high cholesterol | 0.0379 | 0.0137 | 0.00556 | Wald ratio | 1 | cis | NA |
| Thyroid cancer | 0.448 | 0.184 | 0.0148 | Wald ratio | 1 | cis | NA |
| Total cholesterol | 0.0265 | 0.0111 | 0.0167 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: psoriasis | 0.103 | 0.0447 | 0.0217 | Wald ratio | 1 | cis | NA |
| Endometrioid ovarian cancer | -0.145 | 0.0636 | 0.0224 | Wald ratio | 1 | cis | NA |
| Triglycerides | 0.0233 | 0.0102 | 0.0228 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: enlarged prostate | -0.113 | 0.0504 | 0.0244 | Wald ratio | 1 | cis | NA |
| Parkinson's disease | 0.195 | 0.0889 | 0.0283 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: depression | 0.0453 | 0.0207 | 0.0285 | Wald ratio | 1 | cis | NA |
| Knee osteoarthritis | 0.127 | 0.0579 | 0.0286 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K43 Ventral hernia | -0.202 | 0.0974 | 0.0379 | Wald ratio | 1 | cis | NA |
| _...and 104 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_973 association rows across 522 traits (953 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating HAVCR1 levels (id: OID00426_OID21422) | 2e-2307 | rs6555821 | 5 | GCST90859787 | no MR -> candidate analysis |
| Circulating HAVCR1 levels (id: OID01075_OID21422) | 2e-1545 | rs6555821 | 4 | GCST90860291 | no MR -> candidate analysis |
| AMBP/HAVCR1 protein level ratio | 2e-1335 | rs6863148 | 1 | GCST90313254 | no MR -> candidate analysis |
| Kidney injury molecule 1 levels | 4e-817 | rs6555820 | 3 | GCST90012041 | no MR -> candidate analysis |
| T-cell immunoglobulin and mucin domain-containing protein 4  | 1e-363 | rs6882076 | 3 | GCST90422671 | no MR -> candidate analysis |
| Circulating TIMD4 levels | 2e-323 | rs4704826 | 3 | GCST90860495 | no MR -> candidate analysis |
| Total cholesterol levels | 5e-247 | rs6874202 | 31 | GCST90239673 | no MR -> candidate analysis |
| LDL cholesterol levels x alcohol consumption (regular vs non | 5e-226 | rs10066168 | 2 | GCST008078 | no MR -> candidate analysis |
| Non-HDL cholesterol levels | 7e-184 | rs6874202 | 3 | GCST90239667 | no MR -> candidate analysis |
| Hepatitis A virus cellular receptor 1 levels | 4e-175 | rs6878069 | 3 | GCST90247868 | no MR -> candidate analysis |
| Low density lipoprotein cholesterol levels | 8e-156 | rs6874202 | 21 | GCST90239655 | no MR -> candidate analysis |
| Low-density lipoprotein levels | 4e-147 | rs6882076 | 2 | GCST90662892 | no MR -> candidate analysis |
| _...and 510 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 556 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| metabolic disease | 0.75 | — | common-variant locus | no MR -> candidate analysis |
| familial hyperlipidemia | 0.477 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.415 | — | common-variant locus | no MR -> candidate analysis |
| self-injurious ideation | 0.295 | — | common-variant locus | no MR -> candidate analysis |
| hypothyroidism | 0.142 | — | common-variant locus | MR: beta=0.0181, p=0.43 (cis) |

> Of the 5 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=8.1e-13, LOEUF=1.42 — LoF-tolerant |
| GWAS Catalog | 109 unique SNPs / 256 rows |
| ClinVar | 103 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 556 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'HAVCR1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 103 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 522 traits by best p-value, aggregated from 973 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q96D42 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000113249/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/HAVCR1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/HAVCR1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=HAVCR1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/HAVCR1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:57:57  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
