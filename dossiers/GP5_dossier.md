# Protein Dossier — GP5 (Platelet glycoprotein V)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Mean platelet volume | -0.023 | 0.00548 | 2.63e-05 | Inverse variance weighted | 2 | trans | NA |
| Mean platelet volume | -0.023 | 0.00548 | 2.63e-05 | Inverse variance weighted | 2 | cis | NA |
| Platelet count | 8.65 | 2.11 | 4.19e-05 | Inverse variance weighted | 2 | trans | NA |
| Platelet count | 8.65 | 2.11 | 4.19e-05 | Inverse variance weighted | 2 | cis | NA |
| Non-cancer illness code  self-reported: osteoarthritis | 0.00916 | 0.00341 | 0.00716 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: osteoarthritis | 0.00916 | 0.00341 | 0.00716 | Inverse variance weighted | 2 | cis | NA |
| Non-cancer illness code  self-reported: psoriasis | -0.00353 | 0.00131 | 0.00718 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: psoriasis | -0.00353 | 0.00131 | 0.00718 | Inverse variance weighted | 2 | cis | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | 0.0065 | 0.00262 | 0.0131 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | 0.0065 | 0.00262 | 0.0131 | Inverse variance weighted | 2 | cis | NA |
| Sodium in urine | 0.0291 | 0.012 | 0.0151 | Inverse variance weighted | 2 | trans | NA |
| Sodium in urine | 0.0291 | 0.012 | 0.0151 | Inverse variance weighted | 2 | cis | NA |
| _...and 204 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_18 association rows across 11 traits (18 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| GP5 protein levels | 4e-68 | rs1466733 | 1 | GCST90469383 | no MR -> candidate analysis |
| Platelet count | 7e-28 | rs544985059 | 5 | GCST90662907 | MR: beta=8.65, p=4.19e-05 (trans) |
| Platelet distribution width | 8e-25 | rs1466733 | 2 | GCST90002401 | no MR -> candidate analysis |
| Platelet distribution width (UKB data field 30110) | 2e-23 | rs1466733 | 1 | GCST90468097 | no MR -> candidate analysis |
| Platelet glycoprotein V levels | 3e-22 | rs1466733 | 1 | GCST90247796 | no MR -> candidate analysis |
| Mean platelet volume | 1e-19 | rs1466733 | 3 | GCST90002349 | MR: beta=-0.023, p=2.63e-05 (trans) |
| Platelet count (UKB data field 30080) | 7e-18 | rs1466733 | 1 | GCST90468095 | no MR -> candidate analysis |
| mean platelet volume (MPV, maximum, inv-norm transformed) | 9e-18 | rs376133816 | 1 | GCST90479707 | no MR -> candidate analysis |
| Mean platelet thrombocyte volume (UKB data field 30100) | 1e-16 | rs10638925 | 1 | GCST90468087 | no MR -> candidate analysis |
| mean platelet volume (MPV, mean, inv-norm transformed) | 6e-16 | rs376133816 | 1 | GCST90479708 | no MR -> candidate analysis |
| mean platelet volume (MPV, minimum, inv-norm transformed) | 1e-11 | rs376133816 | 1 | GCST90479709 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 222 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| stroke disorder | 0.036 | — | common-variant locus | no MR -> candidate analysis |
| decubitus ulcer | 0.036 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.036 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=NA, LOEUF=NA — Constraint metrics missing; LoF tolerance cannot be judged. |
| GWAS Catalog | 46 unique SNPs / 92 rows |
| ClinVar | 135 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 222 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'GP5'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 135 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 11 of 11 traits by best p-value, aggregated from 18 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P40197 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000178732/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/GP5 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/GP5 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=GP5%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/GP5 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:52:15  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
