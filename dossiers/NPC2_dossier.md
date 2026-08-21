# Protein Dossier — NPC2 (NPC intracellular cholesterol transporter 2)

**MR feasibility tier: C** — No plasma pQTL found (accession + symbol match). Standard plasma pQTL MR is not currently feasible; gene-level genetic evidence below is the honest preview.

## 1. Published MR estimates (retrieved, not computed)

_None in the EpiGraphDB pQTL resource. Absence of an estimate is not evidence of no effect._

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_23 association rows across 18 traits (22 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Height | 2e-108 | rs7156302 | 1 | GCST90245848 | no MR -> candidate analysis |
| Cathepsin H levels (CTSH.8465.52.3) | 4e-30 | rs140130028 | 2 | GCST90240624 | no MR -> candidate analysis |
| Refractive error | 7e-25 | rs73294488 | 3 | GCST010002 | no MR -> candidate analysis |
| NPC2 protein levels | 3e-23 | rs113587712 | 1 | GCST90470068 | no MR -> candidate analysis |
| ENTPD5 protein levels | 7e-18 | rs149199515 | 1 | GCST90469121 | no MR -> candidate analysis |
| Circulating LTBP2 levels | 5e-17 | rs117743573 | 1 | GCST90860485 | no MR -> candidate analysis |
| Lung function (FEV1) | 7e-14 | rs7144263 | 1 | GCST90244092 | no MR -> candidate analysis |
| Serum levels of protein CTSH | 2e-13 | rs10873267 | 1 | GCST90088501 | no MR -> candidate analysis |
| Primary open angle glaucoma (multi-trait analysis) | 2e-12 | rs73294447 | 1 | GCST90310211 | no MR -> candidate analysis |
| Primary open angle glaucoma (MTAG) | 1e-11 | rs73294447 | 1 | GCST90310210 | no MR -> candidate analysis |
| Type 2 diabetes | 8e-11 | rs8008540 | 2 | GCST010555 | no MR -> candidate analysis |
| Spherical equivalent | 3e-10 | rs73294470 | 1 | GCST010378 | no MR -> candidate analysis |
| _...and 6 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1507 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Niemann-Pick disease, type C2 | 0.938 | — | established (curated) | no MR -> candidate analysis |
| Niemann-Pick disease type C | 0.85 | — | established (curated) | no MR -> candidate analysis |
| hereditary disease | 0.81 | — | established (curated) | no MR -> candidate analysis |
| Niemann-Pick disease | 0.559 | — | established (curated) | no MR -> candidate analysis |
| open-angle glaucoma | 0.686 | — | common-variant locus | no MR -> candidate analysis |
| glaucoma | 0.678 | — | common-variant locus | no MR -> candidate analysis |
| Niemann-Pick disease, type C1 | 0.654 | — | established (curated) | no MR -> candidate analysis |
| Niemann-Pick disease type C, severe early infantile neurologic onset | 0.608 | — | established (curated) | no MR -> candidate analysis |
| Niemann-Pick disease type C, adult neurologic onset | 0.608 | — | established (curated) | no MR -> candidate analysis |
| Niemann-Pick disease type C, severe perinatal form | 0.608 | — | established (curated) | no MR -> candidate analysis |
| Niemann-Pick disease type C, juvenile neurologic onset | 0.608 | — | established (curated) | no MR -> candidate analysis |
| Niemann-Pick disease type C, late infantile neurologic onset | 0.608 | — | established (curated) | no MR -> candidate analysis |
| refractive error | 0.491 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of refraction | 0.483 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.434 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **15 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=7e-05, LOEUF=1.29 — LoF-tolerant |
| GWAS Catalog | 85 unique SNPs / 170 rows |
| ClinVar | 330 records; 4 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1507 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'NPC2'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 330 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 18 of 18 traits by best p-value, aggregated from 23 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P61916 — _UniProt release 2026_02 (10-June-2026)_
- `phenome`: https://platform.opentargets.org/target/ENSG00000119655/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/NPC2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/NPC2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=NPC2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/NPC2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:01:12  ·  Tier: C
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: mr_outcomes
