# Protein Dossier — WFDC1 (WAP four-disulfide core domain protein 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Age at menarche | -0.0554 | 0.0166 | 8.30e-04 | Wald ratio | 1 | cis | NA |
| Microalbuminuria | -0.202 | 0.0643 | 0.0017 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hyperthyroidism or thyrotoxicosis | 0.176 | 0.0678 | 0.00921 | Wald ratio | 1 | cis | NA |
| Packed cell volume | -0.144 | 0.0592 | 0.0152 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Injury or trauma resulting in loss of vision | 0.179 | 0.076 | 0.0184 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: S76 Injury of muscle and tendon at hip and thigh level | 0.478 | 0.216 | 0.0265 | Wald ratio | 1 | cis | NA |
| Knee and hip osteoarthritis | -0.129 | 0.0585 | 0.0271 | Wald ratio | 1 | cis | NA |
| Invasive mucinous ovarian cancer | -0.251 | 0.114 | 0.0278 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | 0.0131 | 0.00599 | 0.029 | Wald ratio | 1 | cis | NA |
| Knee osteoarthritis | -0.171 | 0.0783 | 0.0294 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: high cholesterol | -0.0401 | 0.0195 | 0.0398 | Wald ratio | 1 | cis | NA |
| Systemic lupus erythematosus | -0.255 | 0.132 | 0.0539 | Wald ratio | 1 | cis | NA |
| _...and 91 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_21 association rows across 19 traits (11 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| WAP four-disulfide core domain protein 1 levels | 1e-212 | rs400345 | 2 | GCST90250205 | no MR -> candidate analysis |
| Serum levels of protein WFDC1 | 9e-98 | rs400345 | 1 | GCST90090626 | no MR -> candidate analysis |
| Blood protein levels | 6e-54 | rs400345 | 1 | GCST006585 | no MR -> candidate analysis |
| WAP four-disulfide core domain protein 1 level in Chronic ki | 3e-26 | rs400345 | 1 | GCST90239308 | no MR -> candidate analysis |
| Circulating SFTPD levels | 4e-23 | rs12919513 | 1 | GCST90859954 | no MR -> candidate analysis |
| WFDC1 protein levels | 7e-18 | rs62048609 | 1 | GCST90471074 | no MR -> candidate analysis |
| Cerebrospinal fluid protein WFDC1 levels | 3e-17 | rs12599383 | 1 | GCST90944063 | no MR -> candidate analysis |
| Height | 2e-13 | rs8063863 | 2 | GCST90245848 | MR: beta=0.0153, p=0.0769 (cis) |
| Gestational length in nulliparas | 4e-9 | rs2550487 | 1 | GCST90429687 | no MR -> candidate analysis |
| Gut microbial network clusters (Sienna (at 1 year) x Any Hou | 6e-8 | rs72802651 | 1 | GCST90569872 | no MR -> candidate analysis |
| Systolic blood pressure (alcohol consumption interaction) | 1e-7 | rs16963349 | 1 | GCST002307 | no MR -> candidate analysis |
| Metabolite levels | 4e-7 | rs9910 | 1 | GCST009391 | no MR -> candidate analysis |
| _...and 7 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 90 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| major salivary gland cancer | 0.459 | — | common-variant locus | no MR -> candidate analysis |
| musculoskeletal system disorder | 0.452 | — | common-variant locus | no MR -> candidate analysis |
| Vertigo | 0.389 | — | common-variant locus | no MR -> candidate analysis |
| neuroendocrine neoplasm | 0.055 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=8.1e-16, LOEUF=1.55 — LoF-tolerant |
| GWAS Catalog | 55 unique SNPs / 110 rows |
| ClinVar | 147 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 90 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'WFDC1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 147 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 19 of 19 traits by best p-value, aggregated from 21 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9HC57 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000103175/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/WFDC1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/WFDC1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=WFDC1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/WFDC1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:37:22  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
