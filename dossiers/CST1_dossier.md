# Protein Dossier — CST1 (Cystatin-SN)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Iron | -0.078 | 0.019 | 3.92e-05 | Wald ratio | 1 | cis | NA |
| Transferrin Saturation | -0.0663 | 0.0191 | 5.34e-04 | Wald ratio | 1 | cis | NA |
| Pallidum volume | 10.6 | 3.57 | 0.00295 | Wald ratio | 1 | cis | NA |
| Serum cystatin C (eGFRcys) | -0.0103 | 0.00355 | 0.00373 | Wald ratio | 1 | cis | NA |
| Pulse rate | -0.0228 | 0.00822 | 0.00552 | Wald ratio | 1 | cis | NA |
| Diastolic blood pressure  automated reading | -0.0123 | 0.00477 | 0.0101 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: bladder problem (not cancer) | -0.184 | 0.0739 | 0.0127 | Wald ratio | 1 | cis | NA |
| Ischemic stroke | 0.0738 | 0.031 | 0.0174 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | 0.0142 | 0.00603 | 0.0183 | Wald ratio | 1 | cis | NA |
| Subjective well being | 0.0124 | 0.00532 | 0.0196 | Wald ratio | 1 | cis | NA |
| ER-positive Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.0333 | 0.0145 | 0.0219 | Wald ratio | 1 | cis | NA |
| Cigarettes smoked per day | 0.335 | 0.158 | 0.0344 | Wald ratio | 1 | cis | NA |
| _...and 109 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5459_33_3` | CYTN | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_44 association rows across 15 traits (43 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Cystatin-SN levels | 2e-346 | rs4260306 | 7 | GCST90247223 | no MR -> candidate analysis |
| Cystatin C levels | 2e-307 | rs13043045 | 5 | GCST90019504 | no MR -> candidate analysis |
| Cystatin-SA levels | 4e-265 | rs4260306 | 5 | GCST90247222 | no MR -> candidate analysis |
| Cerebrospinal fluid protein CST1 levels | 7e-244 | rs4383402 | 1 | GCST90944226 | no MR -> candidate analysis |
| Serum levels of protein CST1 | 4e-221 | rs4260306 | 3 | GCST90089041 | no MR -> candidate analysis |
| Serum levels of protein CST2 | 1e-145 | rs4260306 | 2 | GCST90088663 | no MR -> candidate analysis |
| Blood protein levels | 1e-115 | rs4260306 | 2 | GCST006585 | no MR -> candidate analysis |
| CST3/TFF3 protein level ratio | 9e-111 | rs6114264 | 1 | GCST90314299 | no MR -> candidate analysis |
| CST1 protein levels | 2e-82 | rs117730889 | 8 | GCST90468893 | no MR -> candidate analysis |
| Cystatin-D levels | 1e-22 | rs8115901 | 2 | GCST90161908 | no MR -> candidate analysis |
| CST5 protein levels | 7e-22 | rs147068635 | 3 | GCST90468895 | no MR -> candidate analysis |
| Cerebrospinal fluid biomarker levels | 1e-20 | rs4328700 | 1 | GCST004000 | no MR -> candidate analysis |
| _...and 3 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 150 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| alcohol drinking | 0.216 | — | common-variant locus | no MR -> candidate analysis |
| liver disorder | 0.166 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=8.4e-10, LOEUF=2.61 — LoF-tolerant |
| GWAS Catalog | 96 unique SNPs / 192 rows |
| ClinVar | 69 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 150 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CST1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 69 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 15 of 15 traits by best p-value, aggregated from 44 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P01037 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000170373/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CST1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CST1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CST1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CST1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:06:21  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
