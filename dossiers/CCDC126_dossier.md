# Protein Dossier — CCDC126 (Coiled-coil domain-containing protein 126)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: R07 Pain in throat and chest | 0.124 | 0.0346 | 3.33e-04 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M72 Fibroblastic disorders | 0.285 | 0.0908 | 0.00172 | Wald ratio | 1 | cis | NA |
| Schizophrenia | -0.113 | 0.0393 | 0.00387 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | -0.0206 | 0.00721 | 0.0043 | Wald ratio | 1 | cis | NA |
| Rheumatoid arthritis | -0.177 | 0.0622 | 0.00432 | Wald ratio | 1 | cis | NA |
| Neuroticism | -0.0291 | 0.0109 | 0.00766 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | -0.0196 | 0.0076 | 0.0101 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: deep venous thrombosis (dvt) | 0.125 | 0.0551 | 0.0231 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: malignant melanoma | -0.287 | 0.136 | 0.0346 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K20 Oesophagitis | 0.16 | 0.0761 | 0.0351 | Wald ratio | 1 | cis | NA |
| Hirschsprung's disease | -0.936 | 0.497 | 0.0594 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I30 Acute pericarditis | 0.578 | 0.315 | 0.0671 | Wald ratio | 1 | cis | NA |
| _...and 99 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_15 association rows across 15 traits (14 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Coiled-coil domain-containing protein 126 levels | 1e-140 | rs35121828 | 1 | GCST90246891 | no MR -> candidate analysis |
| Serum levels of protein CCDC126 | 1e-37 | rs227937 | 1 | GCST90089389 | no MR -> candidate analysis |
| Coiled-coil domain-containing protein 126 levels (CCDC126.63 | 7e-29 | rs227934 | 1 | GCST90240731 | no MR -> candidate analysis |
| Height (baseline) | 5e-23 | rs34576444 | 1 | GCST90565843 | no MR -> candidate analysis |
| Blood protein levels | 4e-19 | rs143669862 | 1 | GCST006585 | no MR -> candidate analysis |
| CR2 protein levels | 2e-16 | rs145235515 | 1 | GCST90468852 | no MR -> candidate analysis |
| Circulating CR2 levels | 3e-16 | rs13231199 | 1 | GCST90860456 | no MR -> candidate analysis |
| Alkaline phosphatase (UKB data field 30610) | 5e-16 | rs67998529 | 1 | GCST90468060 | no MR -> candidate analysis |
| FEV1 | 5e-15 | rs12700451 | 1 | GCST90270081 | MR: beta=-0.0196, p=0.0101 (cis) |
| Height | 6e-14 | rs34096175 | 1 | GCST007841 | no MR -> candidate analysis |
| Physical function (baseline) | 2e-11 | rs7786022 | 1 | GCST90565837 | no MR -> candidate analysis |
| Body shape phenotype PC2 | 8e-11 | rs6959005 | 1 | GCST90832990 | no MR -> candidate analysis |
| _...and 3 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 22 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| alcohol drinking | 0.361 | — | common-variant locus | no MR -> candidate analysis |
| insomnia | 0.309 | — | common-variant locus | no MR -> candidate analysis |
| diabetes mellitus | 0.226 | — | common-variant locus | no MR -> candidate analysis |
| neoplasm | 0.048 | — | common-variant locus | MR: beta=-0.0647, p=0.399 (cis) |
| schizophrenia | 0.039 | — | common-variant locus | MR: beta=-0.113, p=0.00387 (cis) |
| ovarian neoplasm | 0.035 | — | common-variant locus | no MR -> candidate analysis |
| skin aging | 0.032 | — | common-variant locus | no MR -> candidate analysis |

> Of the 7 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.27, LOEUF=0.901 — LoF-tolerant |
| GWAS Catalog | 48 unique SNPs / 96 rows |
| ClinVar | 68 records; 5 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 22 of 22 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CCDC126'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 68 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 15 of 15 traits by best p-value, aggregated from 15 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q96EE4 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000169193/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CCDC126 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CCDC126 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CCDC126%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CCDC126 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:30:08  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
