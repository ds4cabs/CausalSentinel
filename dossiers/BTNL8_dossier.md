# Protein Dossier — BTNL8 (Butyrophilin-like protein 8)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Eye problems or disorders: Injury or trauma resulting in loss of vision | 0.301 | 0.0873 | 5.69e-04 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Diabetes related eye disease | 0.264 | 0.0889 | 0.00295 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Other bones | 0.0983 | 0.0354 | 0.00546 | Wald ratio | 1 | cis | NA |
| Packed cell volume | -0.187 | 0.0733 | 0.0108 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: pneumothorax | 0.633 | 0.251 | 0.0116 | Wald ratio | 1 | cis | NA |
| Cough on most days | -0.124 | 0.0521 | 0.0171 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code self-reported: pulmonary embolism (with or without) dvt | 0.173 | 0.0842 | 0.0394 | Wald ratio | 1 | cis | NA |
| Depressive symptoms | -0.0293 | 0.0147 | 0.0455 | Wald ratio | 1 | cis | NA |
| Fasting insulin | -0.026 | 0.0132 | 0.0486 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hyperthyroidism or thyrotoxicosis | -0.276 | 0.141 | 0.0493 | Wald ratio | 1 | cis | NA |
| Triglycerides | -0.0366 | 0.019 | 0.0545 | Wald ratio | 1 | cis | NA |
| Vascular or heart problems diagnosed by doctor: Angina | -0.107 | 0.0561 | 0.0564 | Wald ratio | 1 | cis | NA |
| _...and 90 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_30 association rows across 22 traits (20 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Butyrophilin-like protein 8 levels | 2e-60 | rs201210185 | 2 | GCST90246756 | no MR -> candidate analysis |
| Serum levels of protein BTNL8 | 5e-51 | rs2387717 | 1 | GCST90090457 | no MR -> candidate analysis |
| high density lipoprotein cholesterol (HDLC, mean, inv-norm t | 2e-43 | rs188238483 | 2 | GCST90475352 | no MR -> candidate analysis |
| high density lipoprotein cholesterol (HDLC, maximum, inv-nor | 4e-38 | rs188238483 | 2 | GCST90475348 | no MR -> candidate analysis |
| high density lipoprotein cholesterol (HDLC, minimm, inv-norm | 5e-36 | rs188238483 | 2 | GCST90475356 | no MR -> candidate analysis |
| FLT4 protein levels | 2e-17 | rs249356 | 2 | GCST90469252 | no MR -> candidate analysis |
| Butyrophilin-like protein 9 levels | 5e-17 | rs138692142 | 1 | GCST90246757 | no MR -> candidate analysis |
| High density lipoprotein cholesterol levels | 8e-17 | rs138692142 | 3 | GCST90239649 | no MR -> candidate analysis |
| Butyrophilin-like protein 8 level in Chronic kidney disease  | 2e-13 | rs34030001 | 1 | GCST90239160 | no MR -> candidate analysis |
| MEP1B protein levels | 2e-13 | rs576925502 | 1 | GCST90469888 | no MR -> candidate analysis |
| Apolipoprotein A levels (UKB data field 30630) | 7e-13 | rs188238483 | 1 | GCST90468061 | no MR -> candidate analysis |
| HDL cholesterol | 4e-10 | rs188238483 | 1 | GCST90018956 | MR: beta=-0.0132, p=0.497 (cis) |
| _...and 10 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 65 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| enteritis | 0.267 | — | common-variant locus | no MR -> candidate analysis |
| benign neoplasm of spinal cord | 0.203 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=6.4e-05, LOEUF=0.871 — LoF-tolerant |
| GWAS Catalog | 39 unique SNPs / 78 rows |
| ClinVar | 125 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 65 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'BTNL8'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 125 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 22 traits by best p-value, aggregated from 30 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q6UX41 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000113303/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/BTNL8 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/BTNL8 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=BTNL8%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/BTNL8 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:19:30  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
