# Protein Dossier — NFASC (Neurofascin)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: I84 Haemorrhoids | 0.0917 | 0.0263 | 4.78e-04 | Inverse variance weighted | 2 | cis | NA |
| Diagnoses - main ICD10: I84 Haemorrhoids | 0.0917 | 0.0263 | 4.78e-04 | Inverse variance weighted | 2 | trans | NA |
| Neo-conscientiousness | 0.571 | 0.165 | 5.39e-04 | Wald ratio | 1 | cis | NA |
| Neuroticism | -0.0219 | 0.00691 | 0.00155 | Inverse variance weighted | 2 | cis | NA |
| Neuroticism | -0.0219 | 0.00691 | 0.00155 | Inverse variance weighted | 2 | trans | NA |
| Diagnoses - main ICD10: R10 Abdominal and pelvic pain | 0.0562 | 0.0204 | 0.00595 | Inverse variance weighted | 2 | cis | NA |
| Diagnoses - main ICD10: R10 Abdominal and pelvic pain | 0.0562 | 0.0204 | 0.00595 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: enlarged prostate | 0.0893 | 0.035 | 0.0108 | Inverse variance weighted | 2 | cis | NA |
| Non-cancer illness code  self-reported: enlarged prostate | 0.0893 | 0.035 | 0.0108 | Inverse variance weighted | 2 | trans | NA |
| Hippocampus volume | -23 | 9.19 | 0.0121 | Wald ratio | 1 | cis | NA |
| Ischemic stroke | -0.0832 | 0.034 | 0.0146 | Wald ratio | 1 | cis | NA |
| Childhood intelligence | 0.0579 | 0.026 | 0.0261 | Wald ratio | 1 | cis | NA |
| _...and 157 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_89 association rows across 52 traits (64 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating CNTN2 levels | 6e-1074 | rs12032559 | 5 | GCST90860318 | no MR -> candidate analysis |
| NFASC/PLXNB2 protein level ratio | 9e-821 | rs6657372 | 1 | GCST90315537 | no MR -> candidate analysis |
| Neurofascin levels | 8e-274 | rs6667532 | 1 | GCST90248666 | no MR -> candidate analysis |
| NFASC protein levels | 3e-125 | rs11806216 | 7 | GCST90470031 | no MR -> candidate analysis |
| Mean platelet thrombocyte volume (UKB data field 30100) | 3e-110 | rs10657459 | 3 | GCST90468087 | no MR -> candidate analysis |
| CNTN2 protein levels | 6e-106 | rs72753439 | 9 | GCST90468804 | no MR -> candidate analysis |
| Neurofascin levels (NFASC.7179.69.3) | 4e-100 | rs6667532 | 2 | GCST90242075 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 4e-59 | rs11240324 | 3 | GCST90838671 | no MR -> candidate analysis |
| Serum levels of protein NFASC | 2e-58 | rs6663324 | 2 | GCST90089710 | no MR -> candidate analysis |
| Mean platelet volume | 3e-58 | rs11240325 | 2 | GCST90002395 | MR: beta=-0.00427, p=0.0389 (cis) |
| Blood protein levels | 8e-37 | rs6663324 | 2 | GCST006585 | no MR -> candidate analysis |
| Platelet count (UKB data field 30080) | 1e-24 | rs11240325 | 2 | GCST90468095 | no MR -> candidate analysis |
| _...and 40 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 716 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| neurodevelopmental disorder with central and peripheral motor dysfunction | 0.851 | — | established (curated) | no MR -> candidate analysis |
| hereditary disease | 0.684 | — | established (curated) | no MR -> candidate analysis |
| risk-taking behaviour | 0.586 | — | common-variant locus | no MR -> candidate analysis |
| hair color | 0.533 | — | common-variant locus | no MR -> candidate analysis |
| dermatophytosis | 0.501 | — | common-variant locus | no MR -> candidate analysis |
| neoplasm | 0.396 | — | common-variant locus | MR: beta=-0.0684, p=0.116 (cis) |
| circadian rhythm | 0.385 | — | common-variant locus | no MR -> candidate analysis |
| spondylolisthesis | 0.327 | — | common-variant locus | no MR -> candidate analysis |
| musculoskeletal system disorder | 0.327 | — | common-variant locus | no MR -> candidate analysis |
| neuromuscular disease | 0.243 | — | established (curated) | no MR -> candidate analysis |

> Of the 10 rows above, **9 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1, LOEUF=0.376 — LoF-INTOLERANT |
| GWAS Catalog | 128 unique SNPs / 288 rows |
| ClinVar | 371 records; 4 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 716 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'NFASC'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 371 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 52 traits by best p-value, aggregated from 89 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O94856 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000163531/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/NFASC — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/NFASC — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=NFASC%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/NFASC — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:58:13  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
