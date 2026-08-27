# Protein Dossier — CCL21 (C-C motif chemokine 21)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Total cholesterol | 0.0646 | 0.013 | 6.98e-07 | Wald ratio | 1 | trans | NA |
| LDL cholesterol | 0.0646 | 0.0133 | 1.30e-06 | Wald ratio | 1 | trans | NA |
| Age at menopause | -0.181 | 0.0494 | 2.46e-04 | Wald ratio | 1 | trans | NA |
| Height | 0.028 | 0.00774 | 2.98e-04 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: high cholesterol | 0.0548 | 0.016 | 6.46e-04 | Wald ratio | 1 | trans | NA |
| HOMA-IR | 0.028 | 0.00988 | 0.00461 | Wald ratio | 1 | trans | NA |
| Lung adenocarcinoma | -0.222 | 0.0789 | 0.00493 | Wald ratio | 1 | trans | NA |
| Iron | -0.0697 | 0.0254 | 0.00602 | Wald ratio | 1 | trans | NA |
| Triglycerides | 0.0319 | 0.012 | 0.00787 | Wald ratio | 1 | trans | NA |
| HOMA-B | 0.0214 | 0.00807 | 0.00798 | Wald ratio | 1 | trans | NA |
| Serum creatinine (eGFRcrea) | 0.0056 | 0.00214 | 0.00891 | Wald ratio | 1 | trans | NA |
| Paget's disease | -0.375 | 0.145 | 0.00995 | Wald ratio | 1 | trans | NA |
| _...and 109 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2516_57_3` | 6Ckine | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_34 association rows across 23 traits (31 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| CCL27 protein levels | 1e-67 | rs10814133 | 1 | GCST90468579 | no MR -> candidate analysis |
| CCL21 protein levels | 2e-55 | rs10814138 | 1 | GCST90468573 | no MR -> candidate analysis |
| Circulating CCL21 levels | 2e-54 | rs10814138 | 1 | GCST90860611 | no MR -> candidate analysis |
| Circulating CCL19 levels (id: OID00513_OID21030) | 1e-50 | rs10972202 | 1 | GCST90859869 | no MR -> candidate analysis |
| Circulating CCL19 levels (id: OID00794_OID21030) | 1e-29 | rs10972202 | 1 | GCST90860126 | no MR -> candidate analysis |
| CCL19 protein levels | 2e-29 | rs11574915 | 1 | GCST90468571 | no MR -> candidate analysis |
| COVID-19 hospitalization or rheumatoid arthritis (MTAG) | 3e-19 | rs10972201 | 1 | GCST90255368 | no MR -> candidate analysis |
| C-C motif chemokine 19 levels | 8e-18 | rs11574915 | 1 | GCST90274765 | no MR -> candidate analysis |
| Rheumatoid arthritis (rheumatoid factor and/or anti-cyclic c | 6e-16 | rs2812378 | 2 | GCST90132225 | no MR -> candidate analysis |
| Rheumatoid arthritis | 2e-15 | rs11574914 | 10 | GCST002318 | no MR -> candidate analysis |
| Height | 3e-13 | rs10124246 | 1 | GCST90245844 | MR: beta=0.028, p=2.98e-04 (trans) |
| Lymphocyte count | 1e-12 | rs11574914 | 1 | GCST90002320 | no MR -> candidate analysis |
| _...and 11 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 926 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| rheumatoid arthritis | 0.809 | — | common-variant locus | no MR -> candidate analysis |
| autoimmune disease | 0.54 | — | common-variant locus | no MR -> candidate analysis |
| ulcerative colitis | 0.541 | — | common-variant locus | MR: beta=-0.0239, p=0.47 (trans) |
| Crohn disease | 0.541 | — | common-variant locus | no MR -> candidate analysis |
| psoriasis | 0.541 | — | common-variant locus | no MR -> candidate analysis |
| ankylosing spondylitis | 0.541 | — | common-variant locus | no MR -> candidate analysis |
| sclerosing cholangitis | 0.541 | — | common-variant locus | no MR -> candidate analysis |
| COVID-19 | 0.304 | — | common-variant locus | no MR -> candidate analysis |

> Of the 8 rows above, **7 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.00066, LOEUF=1.18 — LoF-tolerant |
| GWAS Catalog | 59 unique SNPs / 118 rows |
| ClinVar | 103 records; 8 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 926 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CCL21'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 103 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 20 of 23 traits by best p-value, aggregated from 34 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O00585 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000137077/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CCL21 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CCL21 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CCL21%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CCL21 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:34:25  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: pharmgkb
