# Protein Dossier — EPHA1 (Ephrin type-A receptor 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: hypertrophic cardiomyopathy (hcm  or  hocm) | 0.691 | 0.193 | 3.39e-04 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: B37 Candidiasis | 0.503 | 0.156 | 0.00127 | Wald ratio | 1 | cis | NA |
| Eczema | -0.105 | 0.0374 | 0.00482 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M16 Coxarthrosis [arthrosis of hip] | 0.104 | 0.0395 | 0.0085 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hyperthyroidism or thyrotoxicosis | 0.134 | 0.0536 | 0.0124 | Wald ratio | 1 | cis | NA |
| Bipolar disorder | -0.123 | 0.0506 | 0.015 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: osteoporosis | 0.0926 | 0.0385 | 0.0162 | Wald ratio | 1 | cis | NA |
| Sleep duration | 0.00959 | 0.0041 | 0.0195 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: psoriasis | 0.101 | 0.0449 | 0.025 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Diabetes related eye disease | -0.17 | 0.0797 | 0.0329 | Wald ratio | 1 | cis | NA |
| Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0298 | 0.014 | 0.0332 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: gout | 0.0841 | 0.0406 | 0.0383 | Wald ratio | 1 | cis | NA |
| _...and 95 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3431_54_2` | EphA1 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_102 association rows across 63 traits (84 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Ephrin type-A receptor 1 levels | 4e-778 | rs4725617 | 8 | GCST90247471 | no MR -> candidate analysis |
| BTN2A1/EPHA1 protein level ratio | 1e-275 | rs11767557 | 1 | GCST90313542 | no MR -> candidate analysis |
| EPHA1/LTBR protein level ratio | 5e-248 | rs11767557 | 1 | GCST90314676 | no MR -> candidate analysis |
| EPHA1 protein levels | 3e-229 | rs75045569 | 3 | GCST90469129 | no MR -> candidate analysis |
| Blood protein levels | 2e-223 | rs4725617 | 1 | GCST006585 | no MR -> candidate analysis |
| Ephrin type-A receptor 1 levels (EPHA1.3431.54.2) | 9e-83 | rs4421280 | 1 | GCST90241065 | no MR -> candidate analysis |
| Ephrin type-A receptor 1 level in Chronic kidney disease wit | 1e-61 | rs4725617 | 1 | GCST90237377 | no MR -> candidate analysis |
| Serum levels of protein EPHA1 | 2e-60 | rs11767557 | 1 | GCST90088381 | no MR -> candidate analysis |
| Gamma glutamyltransferase levels (UKB data field 30730) | 4e-28 | rs34372369 | 2 | GCST90468070 | no MR -> candidate analysis |
| Liver enzyme levels (gamma-glutamyl transferase) | 4e-27 | rs34372369 | 1 | GCST90013407 | no MR -> candidate analysis |
| Gamma glutamyl transferase levels | 6e-27 | rs34372369 | 2 | GCST90428730 | no MR -> candidate analysis |
| Height | 4e-26 | rs34372369 | 1 | GCST90245848 | MR: beta=0.0083, p=0.16 (cis) |
| _...and 51 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 409 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Alzheimer disease | 0.824 | — | common-variant locus | no MR -> candidate analysis |
| pathological myopia | 0.394 | — | common-variant locus | no MR -> candidate analysis |
| late-onset Alzheimers disease | 0.379 | — | common-variant locus | no MR -> candidate analysis |
| response to xenobiotic stimulus | 0.25 | — | common-variant locus | no MR -> candidate analysis |
| bladder exstrophy | 0.195 | — | established (curated) | no MR -> candidate analysis |

> Of the 5 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Ephrin type-A receptor 1) |
| gnomAD constraint | pLI=3e-26, LOEUF=0.994 — LoF-tolerant |
| GWAS Catalog | 54 unique SNPs / 108 rows |
| ClinVar | 267 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 409 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'EPHA1' and resolved to 'Ephrin type-A receptor 1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 267 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 63 traits by best p-value, aggregated from 102 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P21709 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000146904/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL5810/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/EPHA1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/EPHA1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=EPHA1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/EPHA1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:26:40  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
