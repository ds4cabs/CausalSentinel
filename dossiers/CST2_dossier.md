# Protein Dossier — CST2 (Cystatin-SA)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Iron | -0.0855 | 0.0208 | 3.92e-05 | Wald ratio | 1 | cis | NA |
| Transferrin Saturation | -0.0726 | 0.021 | 5.34e-04 | Wald ratio | 1 | cis | NA |
| Pallidum volume | 11.6 | 3.92 | 0.00295 | Wald ratio | 1 | cis | NA |
| Serum cystatin C (eGFRcys) | -0.0113 | 0.00389 | 0.00373 | Wald ratio | 1 | cis | NA |
| Pulse rate | -0.025 | 0.00901 | 0.00552 | Wald ratio | 1 | cis | NA |
| Diastolic blood pressure  automated reading | -0.0134 | 0.00523 | 0.0101 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: bladder problem (not cancer) | -0.204 | 0.0827 | 0.0138 | Wald ratio | 1 | cis | NA |
| Ischemic stroke | 0.0808 | 0.034 | 0.0174 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | 0.0156 | 0.00661 | 0.0183 | Wald ratio | 1 | cis | NA |
| Subjective well being | 0.0136 | 0.00583 | 0.0196 | Wald ratio | 1 | cis | NA |
| ER-positive Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.0365 | 0.0159 | 0.0219 | Wald ratio | 1 | cis | NA |
| Cigarettes smoked per day | 0.367 | 0.173 | 0.0344 | Wald ratio | 1 | cis | NA |
| _...and 109 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4324_33_2` | CYTT | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_56 association rows across 17 traits (50 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating CST5 levels | 9e-3177 | rs35275385 | 2 | GCST90859850 | no MR -> candidate analysis |
| Cystatin-D levels | 8e-500 | rs4642010 | 7 | GCST90247217 | no MR -> candidate analysis |
| Cystatin C levels | 1e-349 | rs6106728 | 4 | GCST90019504 | no MR -> candidate analysis |
| Cystatin C plasma levels | 9e-306 | rs6106728 | 1 | GCST90100559 | no MR -> candidate analysis |
| CST5 protein levels | 2e-251 | rs150230325 | 21 | GCST90468895 | no MR -> candidate analysis |
| CST1 protein levels | 6e-68 | rs73093347 | 9 | GCST90468893 | no MR -> candidate analysis |
| Cystatin D levels | 5e-34 | rs57922873 | 1 | GCST90000456 | no MR -> candidate analysis |
| Protein quantitative trait loci | 3e-19 | rs4387871 | 1 | GCST010900 | no MR -> candidate analysis |
| Cystatin-SN levels | 2e-15 | rs7270053 | 2 | GCST90162410 | no MR -> candidate analysis |
| Carbonic anhydrase 12 protein levels (SomaScan ID:3803-10) | 9e-10 | rs6049191 | 1 | GCST90442950 | no MR -> candidate analysis |
| Bone mineral density mean | 2e-8 | rs150080077 | 1 | GCST90321120 | no MR -> candidate analysis |
| Gut microbiome abundance (class Bacteroides sp. 8 (at 1 year | 5e-7 | rs72490828 | 1 | GCST90568892 | no MR -> candidate analysis |
| _...and 5 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 97 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| alcohol drinking | 0.067 | — | common-variant locus | no MR -> candidate analysis |
| liver disorder | 0.055 | — | common-variant locus | no MR -> candidate analysis |
| ovarian dysfunction | 0.055 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.2e-13, LOEUF=2.7 — LoF-tolerant |
| GWAS Catalog | 101 unique SNPs / 218 rows |
| ClinVar | 77 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 97 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CST2'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 77 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 17 of 17 traits by best p-value, aggregated from 56 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P09228 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000170369/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CST2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CST2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CST2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CST2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:06:35  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
