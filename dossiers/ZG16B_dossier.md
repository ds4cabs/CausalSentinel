# Protein Dossier — ZG16B (Pancreatic adenocarcinoma up-regulated factor)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Age at menopause | -0.321 | 0.128 | 0.0124 | Wald ratio | 1 | cis | NA |
| Fractured or broken bones in last 5 years | -0.146 | 0.0604 | 0.0154 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Other bones | -0.221 | 0.0913 | 0.0155 | Wald ratio | 1 | cis | NA |
| Pulse rate | 0.0681 | 0.0293 | 0.0204 | Wald ratio | 1 | cis | NA |
| Hip osteoarthritis | -0.397 | 0.191 | 0.0374 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: prostate cancer | 0.306 | 0.147 | 0.0382 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: S66 Injury of muscle and tendon at wrist and hand level | 0.537 | 0.265 | 0.0428 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K40 Inguinal hernia | 0.17 | 0.0866 | 0.0491 | Wald ratio | 1 | cis | NA |
| Squamous cell lung cancer | -0.382 | 0.206 | 0.0635 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R04 Haemorrhage from respiratory passages | 0.318 | 0.175 | 0.069 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: deep venous thrombosis (dvt) | -0.293 | 0.163 | 0.0734 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hayfever or allergic rhinitis | 0.109 | 0.0617 | 0.0758 | Wald ratio | 1 | cis | NA |
| _...and 88 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_8 association rows across 7 traits (7 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Zymogen granule protein 16 homolog B levels | 6e-238 | rs9925556 | 2 | GCST90427325 | no MR -> candidate analysis |
| IL32 protein levels | 2e-19 | rs12445599 | 1 | GCST90469591 | no MR -> candidate analysis |
| LEG1 protein levels | 2e-15 | rs9925556 | 1 | GCST90469753 | no MR -> candidate analysis |
| Serum levels of protein ZG16B | 2e-13 | rs2190809 | 1 | GCST90090120 | no MR -> candidate analysis |
| LPO protein levels | 3e-13 | rs56411639 | 1 | GCST90469789 | no MR -> candidate analysis |
| Blood protein levels | 1e-8 | rs2190809 | 1 | GCST006585 | no MR -> candidate analysis |
| Stuttering | 5e-6 | rs767749192 | 1 | GCST90707227 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 97 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| stroke disorder | 0.145 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.145 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.00058, LOEUF=2.08 — LoF-tolerant |
| GWAS Catalog | 45 unique SNPs / 90 rows |
| ClinVar | 94 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 97 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'ZG16B'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 94 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 7 of 7 traits by best p-value, aggregated from 8 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q96DA0 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000162078/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/ZG16B — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/ZG16B — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=ZG16B%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/ZG16B — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:39:35  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
