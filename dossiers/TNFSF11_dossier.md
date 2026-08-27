# Protein Dossier — TNFSF11 (Tumor necrosis factor ligand superfamily member 11)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Iron | -0.122 | 0.045 | 0.00679 | Wald ratio | 1 | trans | NA |
| Autism | 0.337 | 0.129 | 0.009 | Wald ratio | 1 | trans | NA |
| Urinary albumin-to-creatinine ratio | 0.0545 | 0.0268 | 0.042 | Wald ratio | 1 | trans | NA |
| Ferritin | -0.085 | 0.0423 | 0.0444 | Wald ratio | 1 | trans | NA |
| Hirschsprung's disease | 1.23 | 0.616 | 0.0455 | Wald ratio | 1 | trans | NA |
| Intracranial volume | 1.26e+04 | 6.44e+03 | 0.0504 | Wald ratio | 1 | trans | NA |
| Ischemic stroke | 0.143 | 0.0755 | 0.0585 | Wald ratio | 1 | trans | NA |
| Age at menarche | 0.0455 | 0.0251 | 0.07 | Wald ratio | 1 | trans | NA |
| Chronic kidney disease | 0.123 | 0.0682 | 0.0719 | Wald ratio | 1 | trans | NA |
| Transferrin Saturation | -0.0809 | 0.045 | 0.0722 | Wald ratio | 1 | trans | NA |
| Bulimia nervosa | 0.0545 | 0.0318 | 0.0865 | Wald ratio | 1 | trans | NA |
| Subjective well being | 0.0227 | 0.0136 | 0.0956 | Wald ratio | 1 | trans | NA |
| _...and 30 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2917_3_2` | sRANKL | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_87 association rows across 56 traits (76 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Alkaline phosphatase (UKB data field 30610) | 1e-45 | rs665632 | 2 | GCST90468060 | no MR -> candidate analysis |
| Circulating SOST levels | 3e-31 | rs138818878 | 5 | GCST90860381 | no MR -> candidate analysis |
| Estimated bone mineral density | 5e-28 | rs117543324 | 2 | GCST90726625 | no MR -> candidate analysis |
| Serum alkaline phosphatase levels | 5e-26 | rs9533177 | 5 | GCST90018722 | no MR -> candidate analysis |
| Heel bone mineral density | 1e-24 | rs138818878 | 6 | GCST007066 | no MR -> candidate analysis |
| Eosinophill percentage (UKB data field 30210) | 1e-23 | rs9525630 | 1 | GCST90468069 | no MR -> candidate analysis |
| DXA-Bone mineral density (lumbar spine) | 5e-23 | rs78667121 | 1 | GCST90568448 | no MR -> candidate analysis |
| DXA-Bone mineral density (spine) (UKB data field 23234) | 5e-23 | rs78667121 | 1 | GCST90568454 | no MR -> candidate analysis |
| SOST protein levels | 6e-23 | rs138818878 | 3 | GCST90470711 | no MR -> candidate analysis |
| Serum sclerostin levels | 6e-23 | rs34136735 | 2 | GCST90320249 | no MR -> candidate analysis |
| DXA-Bone mineral density (trunk) (UKB data field 23241) | 2e-20 | rs78667121 | 1 | GCST90568456 | no MR -> candidate analysis |
| Total body bone mineral density | 1e-19 | rs116926994 | 5 | GCST005348 | no MR -> candidate analysis |
| _...and 44 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 2890 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| osteoporosis | 0.759 | — | common-variant locus | no MR -> candidate analysis |
| autosomal recessive osteopetrosis 2 | 0.84 | — | established (curated) | no MR -> candidate analysis |
| Autosomal recessive malignant osteopetrosis | 0.608 | — | established (curated) | no MR -> candidate analysis |
| bone disorder | 0.499 | — | established (curated) | no MR -> candidate analysis |
| hypothyroidism | 0.839 | — | common-variant locus | no MR -> candidate analysis |
| osteoarthritis, knee | 0.728 | — | common-variant locus | no MR -> candidate analysis |
| myxedema | 0.685 | — | common-variant locus | no MR -> candidate analysis |
| lichen planus | 0.658 | — | common-variant locus | no MR -> candidate analysis |
| Crohn disease | 0.626 | — | common-variant locus | no MR -> candidate analysis |
| primary biliary cholangitis | 0.618 | — | common-variant locus | no MR -> candidate analysis |
| Nasal polyposis | 0.642 | — | common-variant locus | no MR -> candidate analysis |
| skeletal system disorder | 0.649 | — | common-variant locus | no MR -> candidate analysis |
| autoimmune thyroid disease | 0.644 | — | common-variant locus | no MR -> candidate analysis |
| rheumatoid arthritis | 0.51 | — | common-variant locus | MR: beta=-0.09, p=0.256 (trans) |
| juvenile idiopathic arthritis | 0.551 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **14 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 1 known modulators (Tumor necrosis factor ligand superfamily member 11) |
| gnomAD constraint | pLI=0.66, LOEUF=0.604 — LoF-tolerant |
| GWAS Catalog | 106 unique SNPs / 177 rows |
| ClinVar | 323 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 1 clinical annotations across 2 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 2890 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'TNFSF11' and resolved to 'Tumor necrosis factor ligand superfamily member 11' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 323 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 20 of 56 traits by best p-value, aggregated from 87 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O14788 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000120659/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2364162/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/TNFSF11 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/TNFSF11 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=TNFSF11%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=TNFSF11 — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/TNFSF11 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:27:06  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
