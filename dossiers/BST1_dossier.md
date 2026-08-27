# Protein Dossier — BST1 (ADP-ribosyl cyclase/cyclic ADP-ribose hydrolase 2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | -0.116 | 0.0317 | 2.41e-04 | Wald ratio | 1 | cis | NA |
| Celiac disease | 0.0548 | 0.0181 | 0.00247 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: sleep apnoea | -0.142 | 0.0494 | 0.00391 | Wald ratio | 1 | cis | NA |
| Alcohol intake frequency | -0.00999 | 0.0035 | 0.00433 | Wald ratio | 1 | cis | NA |
| Happiness | 0.00764 | 0.00294 | 0.0094 | Wald ratio | 1 | cis | NA |
| Weight | -0.00531 | 0.00209 | 0.0111 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R35 Polyuria | 0.0837 | 0.0349 | 0.0166 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: emphysema or chronic bronchitis | 0.0442 | 0.0196 | 0.0242 | Wald ratio | 1 | cis | NA |
| Lumbar spine bone mineral density | -0.0184 | 0.00854 | 0.0316 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: Z09 Follow-up examination after treatment for conditions other than malignant neoplasms | -0.0424 | 0.0201 | 0.0349 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | -0.00494 | 0.00237 | 0.0369 | Wald ratio | 1 | cis | NA |
| Crohn's disease | 0.0249 | 0.0121 | 0.0395 | Wald ratio | 1 | cis | NA |
| _...and 67 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4535_50_2` | BST1 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_88 association rows across 36 traits (77 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating BST1 levels | 3e-5695 | rs2302465 | 1 | GCST90860619 | no MR -> candidate analysis |
| ADP-ribosyl cyclase/cyclic ADP-ribose hydrolase 2 levels | 3e-2219 | rs73224660 | 17 | GCST90246747 | no MR -> candidate analysis |
| ADP-ribosyl cyclase/cyclic ADP-ribose hydrolase 2 levels (BS | 2e-744 | rs73224660 | 2 | GCST90240204 | no MR -> candidate analysis |
| 3-methylcytidine levels | 7e-661 | rs113618320 | 4 | GCST90200682 | no MR -> candidate analysis |
| Blood protein levels | 9e-630 | rs16892260 | 1 | GCST006585 | no MR -> candidate analysis |
| BST1 protein levels | 6e-274 | rs2302465 | 16 | GCST90453272 | no MR -> candidate analysis |
| Cerebrospinal fluid protein BST1 levels | 4e-253 | rs4263397 | 1 | GCST90944133 | no MR -> candidate analysis |
| Circulating CD38 levels | 7e-245 | rs868763 | 5 | GCST90859672 | no MR -> candidate analysis |
| Protein quantitative trait loci | 1e-134 | rs73224659 | 1 | GCST010900 | no MR -> candidate analysis |
| Metabolite levels (3-methylcytidine) | 5e-120 | rs2302465 | 1 | GCST90300548 | no MR -> candidate analysis |
| Urine 3-methylcytidine levels in chronic kidney disease | 2e-85 | rs113618320 | 1 | GCST90264561 | no MR -> candidate analysis |
| Plasma X-21283 levels in chronic kidney disease | 4e-70 | rs55735476 | 1 | GCST90266479 | no MR -> candidate analysis |
| _...and 24 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 192 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Parkinson disease | 0.853 | — | common-variant locus | no MR -> candidate analysis |
| Lewy body dementia | 0.505 | — | common-variant locus | no MR -> candidate analysis |
| cataract | 0.152 | 0.152 | exploratory rare-variant signal | MR: beta=0.0156, p=0.221 (cis) |
| drug-induced dyskinesia | 0.152 | 0.152 | exploratory rare-variant signal | no MR -> candidate analysis |
| conduct disorder | 0.112 | — | common-variant locus | no MR -> candidate analysis |
| phototoxic dermatitis | 0.052 | — | common-variant locus | no MR -> candidate analysis |
| diverticular disease | 0.044 | — | common-variant locus | no MR -> candidate analysis |
| risk-taking behaviour | 0.043 | — | common-variant locus | no MR -> candidate analysis |
| alopecia areata | 0.039 | — | common-variant locus | no MR -> candidate analysis |

> Of the 9 rows above, **8 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 2 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (ADP-ribosyl cyclase/cyclic ADP-ribose hydrolase 2) |
| gnomAD constraint | pLI=5.7e-20, LOEUF=1.53 — LoF-tolerant |
| GWAS Catalog | 108 unique SNPs / 226 rows |
| ClinVar | 132 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 1 clinical annotations across 1 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 192 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'BST1' and resolved to 'ADP-ribosyl cyclase/cyclic ADP-ribose hydrolase 2' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 132 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 20 of 36 traits by best p-value, aggregated from 88 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q10588 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000109743/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL5169147/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/BST1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/BST1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=BST1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=BST1 — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/BST1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:18:57  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
