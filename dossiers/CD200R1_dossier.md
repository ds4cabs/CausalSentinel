# Protein Dossier — CD200R1 (Cell surface glycoprotein CD200 receptor 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: asthma | 0.15 | 0.0336 | 8.51e-06 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypopituitarism | 0.979 | 0.319 | 0.00215 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I80 Phlebitis and thrombophlebitis | 0.415 | 0.138 | 0.00255 | Wald ratio | 1 | cis | NA |
| Eczema | 0.288 | 0.0972 | 0.00307 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: pernicious anaemia | 0.477 | 0.164 | 0.00369 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I48 Atrial fibrillation and flutter | 0.285 | 0.1 | 0.00444 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hayfever or allergic rhinitis | 0.133 | 0.0502 | 0.00834 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: basal cell carcinoma | 0.286 | 0.111 | 0.00971 | Wald ratio | 1 | cis | NA |
| Serum creatinine (eGFRcrea) | 0.0125 | 0.00523 | 0.0168 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: pneumothorax | 0.795 | 0.355 | 0.0253 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R07 Pain in throat and chest | 0.114 | 0.0555 | 0.04 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: S76 Injury of muscle and tendon at hip and thigh level | 0.743 | 0.366 | 0.0424 | Wald ratio | 1 | cis | NA |
| _...and 94 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5103_30_3` | MO2R1 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_37 association rows across 22 traits (34 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating CD200R1 levels | 4e-3173 | rs79556290 | 3 | GCST90859738 | no MR -> candidate analysis |
| CD200R1 protein levels | 1e-270 | rs4682447 | 4 | GCST90468605 | no MR -> candidate analysis |
| Cell surface glycoprotein CD200 receptor 1 levels | 4e-174 | rs77561169 | 3 | GCST90059915 | no MR -> candidate analysis |
| Cerebrospinal fluid protein CD200R1 levels | 5e-59 | rs57891445 | 1 | GCST90943148 | no MR -> candidate analysis |
| Neurological blood protein biomarker levels | 2e-30 | rs79834152 | 2 | GCST008478 | no MR -> candidate analysis |
| Atopic dermatitis | 5e-29 | rs6808249 | 2 | GCST90244787 | no MR -> candidate analysis |
| Eosinophil percentage of white cells | 9e-23 | rs35297201 | 1 | GCST90002382 | no MR -> candidate analysis |
| Eosinophil count | 2e-22 | rs12494693 | 4 | GCST90002381 | no MR -> candidate analysis |
| Height | 9e-21 | rs7432373 | 1 | GCST90245848 | MR: beta=-0.0239, p=0.162 (cis) |
| CD200 protein levels | 2e-19 | rs1488193 | 1 | GCST90468606 | no MR -> candidate analysis |
| Eosinophill count (UKB data field 30150) | 4e-19 | rs12494693 | 1 | GCST90468068 | no MR -> candidate analysis |
| Circulating CD200 levels | 6e-18 | rs55664715 | 1 | GCST90859700 | no MR -> candidate analysis |
| _...and 10 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 294 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| asthma | 0.667 | — | common-variant locus | MR: beta=0.15, p=8.51e-06 (cis) |
| atopic eczema | 0.668 | — | common-variant locus | no MR -> candidate analysis |
| hypothyroidism | 0.669 | — | common-variant locus | MR: beta=0.0725, p=0.209 (cis) |
| dermatitis | 0.667 | — | common-variant locus | no MR -> candidate analysis |
| Eczematoid dermatitis | 0.55 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.466 | — | common-variant locus | no MR -> candidate analysis |
| corneal neovascularization | 0.134 | — | common-variant locus | no MR -> candidate analysis |
| device complication | 0.12 | — | common-variant locus | no MR -> candidate analysis |

> Of the 8 rows above, **6 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=8.7e-09, LOEUF=1.07 — LoF-tolerant |
| GWAS Catalog | 50 unique SNPs / 100 rows |
| ClinVar | 89 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 294 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CD200R1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 89 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 22 traits by best p-value, aggregated from 37 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q8TD46 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000163606/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CD200R1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CD200R1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CD200R1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CD200R1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:41:06  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
