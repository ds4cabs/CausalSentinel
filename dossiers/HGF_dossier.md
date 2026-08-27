# Protein Dossier — HGF (Hepatocyte growth factor)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: hypopituitarism | 1.03 | 0.312 | 9.90e-04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: retinal detachment | 0.481 | 0.16 | 0.00262 | Wald ratio | 1 | cis | NA |
| Age at menarche | 0.0978 | 0.0355 | 0.0058 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: osteoporosis | 0.24 | 0.0916 | 0.00879 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: G56 Mononeuropathies of upper limb | 0.222 | 0.0883 | 0.0118 | Wald ratio | 1 | cis | NA |
| Fasting insulin | -0.0412 | 0.0185 | 0.0263 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: basal cell carcinoma | 0.261 | 0.118 | 0.0264 | Wald ratio | 1 | cis | NA |
| HOMA-IR | -0.0515 | 0.0237 | 0.0297 | Wald ratio | 1 | cis | NA |
| ER-negative Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.144 | 0.0685 | 0.0353 | Wald ratio | 1 | cis | NA |
| Small vessel disease | 0.453 | 0.219 | 0.0389 | Wald ratio | 1 | cis | NA |
| Forearm bone mineral density | 0.181 | 0.0925 | 0.0501 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: joint disorder | 0.307 | 0.159 | 0.0534 | Wald ratio | 1 | cis | NA |
| _...and 84 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2681_23_2` | HGF | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_118 association rows across 67 traits (99 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating HGF levels (id: OID00522_OID20656) | 3e-81 | rs5745687 | 4 | GCST90859878 | no MR -> candidate analysis |
| Circulating HGF levels (id: OID00706_OID20656) | 5e-59 | rs5745687 | 4 | GCST90860049 | no MR -> candidate analysis |
| Circulating HGF levels (id: OID00803_OID20656) | 3e-56 | rs5745687 | 4 | GCST90860133 | no MR -> candidate analysis |
| HGF protein levels | 4e-52 | rs5745687 | 2 | GCST90469449 | no MR -> candidate analysis |
| Facial appearance | 3e-35 | rs28584384 | 1 | GCST90128425 | no MR -> candidate analysis |
| Hepatocyte growth factor levels | 9e-35 | rs554133413 | 12 | GCST90247875 | no MR -> candidate analysis |
| Sex hormone-binding globulin levels adjusted for BMI | 1e-32 | rs1229492 | 4 | GCST90012110 | no MR -> candidate analysis |
| Cerebrospinal fluid protein HGF levels | 3e-31 | rs10252734 | 1 | GCST90943462 | no MR -> candidate analysis |
| Sex hormone-binding globulin levels | 9e-27 | rs1229492 | 10 | GCST90012111 | no MR -> candidate analysis |
| Unsupervised deep imaging phenotypes (UDIP-FA) | 2e-20 | rs10252734 | 1 | GCST90860937 | no MR -> candidate analysis |
| Glycoprotein acetyls levels | 3e-20 | rs1229480 | 2 | GCST90501111 | no MR -> candidate analysis |
| Endothelial growth factor levels | 4e-19 | rs5745687 | 1 | GCST002731 | no MR -> candidate analysis |
| _...and 55 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 2009 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| hearing loss, autosomal recessive | 0.744 | — | established (curated) | no MR -> candidate analysis |
| prostate carcinoma | 0.53 | — | common-variant locus | no MR -> candidate analysis |
| kidney disorder | 0.59 | — | common-variant locus | no MR -> candidate analysis |
| Sensorineural hearing impairment | 0.559 | — | established (curated) | no MR -> candidate analysis |
| ovarian neoplasm | 0.499 | — | common-variant locus | no MR -> candidate analysis |

> Of the 5 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 20 known modulators (Hepatocyte growth factor receptor) |
| gnomAD constraint | pLI=1, LOEUF=0.456 — LoF-INTOLERANT |
| GWAS Catalog | 52 unique SNPs / 104 rows |
| ClinVar | 356 records; 3 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 2009 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'HGF' and resolved to 'Hepatocyte growth factor receptor' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 356 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 67 traits by best p-value, aggregated from 118 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P14210 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000019991/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3717/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/HGF — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/HGF — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=HGF%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/HGF — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:00:00  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
