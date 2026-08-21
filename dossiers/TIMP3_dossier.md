# Protein Dossier — TIMP3 (Metalloproteinase inhibitor 3)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Myocardial infarction | -0.0389 | 0.0119 | 0.00111 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: anxiety or panic attacks | 0.0752 | 0.0231 | 0.00114 | Wald ratio | 1 | cis | NA |
| Coronary heart disease | -0.0328 | 0.0108 | 0.00234 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: B37 Candidiasis | 0.311 | 0.102 | 0.00236 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: malignant melanoma | 0.0781 | 0.0303 | 0.0101 | Wald ratio | 1 | cis | NA |
| Urate | 0.0161 | 0.00645 | 0.0124 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: muscle or soft tissue injuries | 0.0746 | 0.0317 | 0.0186 | Wald ratio | 1 | cis | NA |
| Subjective well being | 0.00967 | 0.0043 | 0.0244 | Wald ratio | 1 | cis | NA |
| Internalizing problems | -0.059 | 0.0269 | 0.0281 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: deep venous thrombosis (dvt) | 0.043 | 0.0196 | 0.0285 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: mania or bipolar disorder or manic depression | 0.111 | 0.0508 | 0.0292 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: arthritis (nos) | 0.0677 | 0.0311 | 0.0295 | Wald ratio | 1 | cis | NA |
| _...and 98 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2480_58_3` | TIMP-3 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_12 association rows across 6 traits (11 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| TIMP3 protein levels | 4e-68 | rs116959820 | 2 | GCST90470871 | no MR -> candidate analysis |
| Metalloproteinase inhibitor 3 levels | 2e-20 | rs242069 | 4 | GCST90161365 | no MR -> candidate analysis |
| Free Cholesterol to Cholesteryl Esters in Large HDL ratio | 4e-15 | rs117004633 | 1 | GCST90827800 | no MR -> candidate analysis |
| acne vulgaris | 1e-10 | rs135025 | 3 | GCST90092000 | no MR -> candidate analysis |
| Depression x environmental factor score interaction | 4e-8 | rs536631793 | 1 | GCST90102448 | no MR -> candidate analysis |
| Triglyceride levels | 2e-7 | rs1065314 | 1 | GCST008150 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1907 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Sorsby fundus dystrophy | 0.859 | — | established (curated) | no MR -> candidate analysis |
| Sorsby's fundus dystrophy | 0.489 | — | established (curated) | no MR -> candidate analysis |
| Retinal dystrophy | 0.851 | — | established (curated) | no MR -> candidate analysis |
| venous thromboembolism | 0.705 | — | common-variant locus | no MR -> candidate analysis |
| open-angle glaucoma | 0.685 | — | common-variant locus | no MR -> candidate analysis |
| glaucoma | 0.677 | — | common-variant locus | MR: beta=-0.0495, p=0.0501 (cis) |
| retinal disorder | 0.669 | — | established (curated) | no MR -> candidate analysis |
| acne | 0.667 | — | common-variant locus | no MR -> candidate analysis |
| cutaneous lupus erythematosus | 0.484 | — | common-variant locus | no MR -> candidate analysis |
| Cerebral arteriovenous malformation | 0.438 | — | established (curated) | no MR -> candidate analysis |
| stricture | 0.391 | — | common-variant locus | no MR -> candidate analysis |
| ductal breast carcinoma in situ | 0.344 | — | common-variant locus | no MR -> candidate analysis |
| age-related macular degeneration | 0.259 | — | common-variant locus | no MR -> candidate analysis |
| obesity disorder | 0.267 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.259 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **14 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Metalloproteinase inhibitor 3) |
| gnomAD constraint | pLI=0.7, LOEUF=0.606 — LoF-tolerant |
| GWAS Catalog | 110 unique SNPs / 254 rows |
| ClinVar | 302 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1907 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'TIMP3' and resolved to 'Metalloproteinase inhibitor 3' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 302 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 6 of 6 traits by best p-value, aggregated from 12 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P35625 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000100234/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL5465289/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/TIMP3 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/TIMP3 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=TIMP3%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/TIMP3 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:21:54  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
