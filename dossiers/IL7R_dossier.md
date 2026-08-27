# Protein Dossier — IL7R (Interleukin-7 receptor subunit alpha)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Inflammatory bowel disease | 0.104 | 0.0247 | 2.48e-05 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | 0.0948 | 0.0233 | 4.80e-05 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: asthma | 0.0574 | 0.0153 | 1.69e-04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hayfever or allergic rhinitis | 0.0784 | 0.0219 | 3.49e-04 | Wald ratio | 1 | cis | NA |
| Ulcerative colitis | 0.102 | 0.0309 | 9.04e-04 | Wald ratio | 1 | cis | NA |
| Crohn's disease | 0.0964 | 0.0298 | 0.00123 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | -0.0223 | 0.00746 | 0.00279 | Wald ratio | 1 | cis | NA |
| Height | -0.0198 | 0.00706 | 0.00511 | Wald ratio | 1 | cis | NA |
| ER-negative Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.0699 | 0.0268 | 0.00918 | Wald ratio | 1 | cis | NA |
| Juvenile idiopathic arthritis | 0.323 | 0.127 | 0.011 | Wald ratio | 1 | cis | NA |
| Lung cancer | -0.0971 | 0.041 | 0.018 | Wald ratio | 1 | cis | NA |
| Happiness | 0.0168 | 0.00714 | 0.0182 | Wald ratio | 1 | cis | NA |
| _...and 109 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5089_11_3` | IL-7 Ra | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_258 association rows across 144 traits (242 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating IL7R levels | 1e-4083 | rs11742270 | 4 | GCST90860451 | no MR -> candidate analysis |
| ICAM2/IL7R protein level ratio | 3e-3651 | rs6897932 | 1 | GCST90315117 | no MR -> candidate analysis |
| IL7R protein levels | 8e-206 | rs182158522 | 12 | GCST90469605 | no MR -> candidate analysis |
| Lymphocyte count | 3e-144 | rs11567699 | 7 | GCST90002320 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 1e-118 | rs11567701 | 2 | GCST90838669 | no MR -> candidate analysis |
| Atopic dermatitis | 3e-99 | rs10214273 | 6 | GCST90244787 | no MR -> candidate analysis |
| Lymphocyte count (UKB data field 30120) | 3e-86 | rs1053496 | 1 | GCST90468082 | no MR -> candidate analysis |
| Eosinophil count | 2e-66 | rs1961220 | 8 | GCST90002302 | no MR -> candidate analysis |
| Lymphocyte percentage of white cells | 1e-63 | rs11567701 | 2 | GCST90002389 | no MR -> candidate analysis |
| Lymphocyte percentage (UKB data field 30180) | 4e-61 | rs11567701 | 1 | GCST90468083 | no MR -> candidate analysis |
| Eczema | 2e-59 | rs6881706 | 3 | GCST007075 | MR: beta=0.0584, p=0.146 (cis) |
| Eosinophill percentage (UKB data field 30210) | 6e-53 | rs4594881 | 1 | GCST90468069 | no MR -> candidate analysis |
| _...and 132 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 872 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| immunodeficiency 104 | 0.889 | — | established (curated) | no MR -> candidate analysis |
| asthma | 0.957 | — | common-variant locus | MR: beta=0.0574, p=1.69e-04 (cis) |
| multiple sclerosis | 0.804 | — | common-variant locus | no MR -> candidate analysis |
| T-B+ severe combined immunodeficiency due to JAK3 deficiency | 0.959 | — | established (curated) | no MR -> candidate analysis |
| hypothyroidism | 0.935 | — | common-variant locus | MR: beta=0.0948, p=4.80e-05 (cis) |
| Omenn syndrome | 0.608 | — | established (curated) | no MR -> candidate analysis |
| allergic rhinitis | 0.904 | — | common-variant locus | MR: beta=0.0784, p=3.49e-04 (cis) |
| atopic eczema | 0.903 | — | common-variant locus | no MR -> candidate analysis |
| Eczematoid dermatitis | 0.897 | — | common-variant locus | no MR -> candidate analysis |
| primary biliary cholangitis | 0.894 | — | common-variant locus | no MR -> candidate analysis |
| allergic disease | 0.875 | — | common-variant locus | no MR -> candidate analysis |
| dermatitis | 0.866 | — | common-variant locus | no MR -> candidate analysis |
| severe combined immunodeficiency | 0.858 | — | established (curated) | no MR -> candidate analysis |
| skin disorder | 0.846 | — | common-variant locus | no MR -> candidate analysis |
| respiratory system disorder | 0.813 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **12 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=4e-11, LOEUF=1.06 — LoF-tolerant |
| GWAS Catalog | 124 unique SNPs / 323 rows |
| ClinVar | 635 records; 5 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 872 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'IL7R'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 635 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 144 traits by best p-value, aggregated from 258 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P16871 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000168685/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/IL7R — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/IL7R — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=IL7R%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/IL7R — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:16:54  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
