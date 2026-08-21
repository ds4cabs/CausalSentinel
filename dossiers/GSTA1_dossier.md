# Protein Dossier — GSTA1 (Glutathione S-transferase A1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Haemoglobin concentration | 0.0505 | 0.0135 | 1.77e-04 | Wald ratio | 1 | cis | NA |
| Serum creatinine (eGFRcrea) | -0.00746 | 0.00221 | 7.53e-04 | Wald ratio | 1 | cis | NA |
| LDL cholesterol | -0.0414 | 0.0125 | 9.41e-04 | Wald ratio | 1 | cis | NA |
| Platelet count | -3 | 0.949 | 0.0016 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K35 Acute appendicitis | 0.21 | 0.0684 | 0.00215 | Wald ratio | 1 | cis | NA |
| Microalbuminuria | 0.135 | 0.0505 | 0.00766 | Wald ratio | 1 | cis | NA |
| Total cholesterol | -0.0327 | 0.0123 | 0.00766 | Wald ratio | 1 | cis | NA |
| HDL cholesterol | 0.0301 | 0.0115 | 0.00921 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R07 Pain in throat and chest | 0.0598 | 0.0246 | 0.0149 | Wald ratio | 1 | cis | NA |
| Creatinine (enzymatic) in urine | 0.0135 | 0.00559 | 0.0155 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | -0.0112 | 0.00479 | 0.0193 | Wald ratio | 1 | cis | NA |
| Potassium in urine | 0.0138 | 0.00593 | 0.0202 | Wald ratio | 1 | cis | NA |
| _...and 110 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_64 association rows across 48 traits (64 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| ADH4/GSTA1 protein level ratio | 5e-1386 | rs6917325 | 1 | GCST90313191 | no MR -> candidate analysis |
| GSTA1/KRT18 protein level ratio | 3e-968 | rs6917325 | 1 | GCST90314993 | no MR -> candidate analysis |
| ACY1/GSTA1 protein level ratio | 9e-957 | rs6917325 | 1 | GCST90313163 | no MR -> candidate analysis |
| DCXR/GSTA1 protein level ratio | 1e-918 | rs6917325 | 1 | GCST90314437 | no MR -> candidate analysis |
| GSTA1/RBP5 protein level ratio | 1e-875 | rs6917325 | 1 | GCST90314995 | no MR -> candidate analysis |
| AGXT/GSTA1 protein level ratio | 1e-721 | rs6917325 | 1 | GCST90313206 | no MR -> candidate analysis |
| GSTA1/SULT2A1 protein level ratio | 1e-701 | rs6917325 | 1 | GCST90314996 | no MR -> candidate analysis |
| GSTA3/KRT18 protein level ratio | 9e-598 | rs6917325 | 1 | GCST90314997 | no MR -> candidate analysis |
| CA5A/GSTA1 protein level ratio | 1e-589 | rs6917325 | 1 | GCST90313591 | no MR -> candidate analysis |
| GSTA1/PBLD protein level ratio | 4e-586 | rs6917325 | 1 | GCST90314994 | no MR -> candidate analysis |
| FBP1/GSTA1 protein level ratio | 6e-564 | rs6917325 | 1 | GCST90314786 | no MR -> candidate analysis |
| CANT1/GSTA1 protein level ratio | 2e-539 | rs6917325 | 1 | GCST90313616 | no MR -> candidate analysis |
| _...and 36 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 266 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| familial hyperlipidemia | 0.214 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.07 | — | common-variant locus | no MR -> candidate analysis |
| type 2 diabetes mellitus | 0.058 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Glutathione S-transferase A1) |
| gnomAD constraint | pLI=5.2e-09, LOEUF=1.52 — LoF-tolerant |
| GWAS Catalog | 100 unique SNPs / 200 rows |
| ClinVar | 51 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 5 clinical annotations across 7 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 266 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'GSTA1' and resolved to 'Glutathione S-transferase A1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 51 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 20 of 48 traits by best p-value, aggregated from 64 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P08263 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000243955/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3409/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/GSTA1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/GSTA1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=GSTA1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=GSTA1 — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/GSTA1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:55:23  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
