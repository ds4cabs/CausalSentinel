# Protein Dossier — TEPSIN (AP-4 complex accessory subunit Tepsin)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: asthma | -0.127 | 0.0416 | 0.00224 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: depression | -0.167 | 0.0639 | 0.00881 | Wald ratio | 1 | cis | NA |
| Clear cell ovarian cancer | 0.685 | 0.278 | 0.0136 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: D25 Leiomyoma of uterus | 0.201 | 0.0951 | 0.0342 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: S76 Injury of muscle and tendon at hip and thigh level | 0.716 | 0.348 | 0.0395 | Wald ratio | 1 | cis | NA |
| Potassium in urine | -0.0261 | 0.0132 | 0.0486 | Wald ratio | 1 | cis | NA |
| Birth weight | -0.0381 | 0.0201 | 0.0577 | Wald ratio | 1 | cis | NA |
| Eczema | -0.258 | 0.136 | 0.0587 | Wald ratio | 1 | cis | NA |
| Ovarian cancer | 0.142 | 0.0783 | 0.0699 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Cataract | 0.115 | 0.0637 | 0.07 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | 0.0193 | 0.0107 | 0.0709 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | 0.0922 | 0.053 | 0.0821 | Wald ratio | 1 | cis | NA |
| _...and 49 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_5 association rows across 3 traits (2 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| AP-4 complex accessory subunit tepsin levels | 6e-24 | rs61745945 | 1 | GCST90246531 | no MR -> candidate analysis |
| AP-4 complex accessory subunit tepsin levels (ENTHD2.7947.19 | 6e-19 | rs61745945 | 1 | GCST90240305 | no MR -> candidate analysis |
| Frontotemporal dementia | 8e-7 | rs906175; rs2659030; rs2725391; rs969413; rs1048775; rs9319617; rs2255166 | 3 | GCST002960 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 31 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| obesity disorder | 0.086 | — | common-variant locus | no MR -> candidate analysis |
| response to xenobiotic stimulus | 0.05 | — | common-variant locus | no MR -> candidate analysis |
| hypertensive disorder | 0.05 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=5.2e-18, LOEUF=1.31 — LoF-tolerant |
| GWAS Catalog | 49 unique SNPs / 98 rows |
| ClinVar | 45 records; 4 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 31 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'TEPSIN'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 45 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 3 of 3 traits by best p-value, aggregated from 5 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q96N21 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000167302/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/TEPSIN — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/TEPSIN — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=TEPSIN%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/TEPSIN — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:18:48  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
