# Protein Dossier — MED1 (Methyl-CpG-binding domain protein 4)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Pancreatic cancer | 0.176 | 0.115 | 0.125 | Wald ratio | 1 | trans | NA |
| Melanoma | -0.152 | 0.184 | 0.407 | Wald ratio | 1 | trans | NA |
| Intracranial volume | -3.37e+03 | 4.6e+03 | 0.463 | Wald ratio | 1 | trans | NA |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3891_56_1` | MBD4 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_36 association rows across 31 traits (32 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Hematological traits (multi-trait analysis) | 4e-95 | rs145835664 | 1 | GCST90838669 | no MR -> candidate analysis |
| Estimated glomerular filtration rate (creatinine) | 4e-48 | rs55722796 | 1 | GCST90103634 | no MR -> candidate analysis |
| Circulating EPCAM levels | 2e-26 | rs4795369 | 1 | GCST90859956 | no MR -> candidate analysis |
| Asthma (childhood onset) | 8e-23 | rs145835664 | 1 | GCST009841 | no MR -> candidate analysis |
| EPCAM protein levels | 4e-22 | rs4795369 | 1 | GCST90469126 | no MR -> candidate analysis |
| Neutrophil-to-lymphocyte ratio | 5e-20 | rs145835664 | 4 | GCST90866310 | no MR -> candidate analysis |
| SLC51B protein levels | 2e-19 | rs4795369 | 1 | GCST90470664 | no MR -> candidate analysis |
| Blood urea nitrogen (BUN, maximum, inv-norm transformed) | 3e-17 | rs12943928 | 1 | GCST90479524 | no MR -> candidate analysis |
| Drinks per week | 6e-16 | rs55722796 | 1 | GCST90243989 | no MR -> candidate analysis |
| White blood cell count | 9e-16 | rs72825193 | 1 | GCST007070 | no MR -> candidate analysis |
| Asthma | 2e-14 | rs146644295 | 1 | GCST008916 | no MR -> candidate analysis |
| Creatinine levels | 2e-14 | rs4795361 | 2 | GCST90827754 | no MR -> candidate analysis |
| _...and 19 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 784 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| asthma | 0.355 | — | common-variant locus | no MR -> candidate analysis |
| coronary atherosclerosis | 0.097 | — | common-variant locus | no MR -> candidate analysis |
| systolic heart failure | 0.086 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Methyl-CpG-binding domain protein 4) |
| gnomAD constraint | pLI=1, LOEUF=0.21 — LoF-INTOLERANT |
| GWAS Catalog | 112 unique SNPs / 234 rows |
| ClinVar | 194 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 784 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'MED1' and resolved to 'Methyl-CpG-binding domain protein 4' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 194 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 31 traits by best p-value, aggregated from 36 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O95243 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000125686/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL5723573/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/MED1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/MED1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=MED1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/MED1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:45:49  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
