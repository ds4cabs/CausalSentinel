# Protein Dossier — SPOCK2 (Testican-2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: pneumothorax | 0.866 | 0.245 | 4.03e-04 | Wald ratio | 1 | cis | NA |
| Neuroticism | 0.0459 | 0.0138 | 8.58e-04 | Wald ratio | 1 | cis | NA |
| Lung adenocarcinoma | -0.355 | 0.116 | 0.0023 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: ankylosing spondylitis | 0.414 | 0.142 | 0.00352 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M23 Internal derangement of knee | -0.245 | 0.0962 | 0.011 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M17 Gonarthrosis [arthrosis of knee] | -0.246 | 0.103 | 0.0173 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: enlarged prostate | 0.168 | 0.0806 | 0.0371 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M16 Coxarthrosis [arthrosis of hip] | 0.164 | 0.0788 | 0.0372 | Wald ratio | 1 | cis | NA |
| Schizophrenia | 0.101 | 0.0491 | 0.0398 | Wald ratio | 1 | cis | NA |
| Endometrioid ovarian cancer | 0.253 | 0.134 | 0.0594 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: asthma | -0.0604 | 0.033 | 0.0674 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: D12 Benign neoplasm of colon  rectum  anus and anal canal | 0.148 | 0.0812 | 0.0676 | Wald ratio | 1 | cis | NA |
| _...and 108 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-5491_12_3` | Testican-2 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_39 association rows across 29 traits (30 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| ACAN protein levels | 3e-242 | rs11000138 | 1 | GCST90468196 | no MR -> candidate analysis |
| Circulating ACAN levels | 2e-120 | rs61852248 | 1 | GCST90860590 | no MR -> candidate analysis |
| Testican-2 levels | 3e-104 | rs1245540 | 4 | GCST90426371 | no MR -> candidate analysis |
| Testican-2 levels (SPOCK2.5491.12.3) | 3e-19 | rs1245540 | 1 | GCST90242987 | no MR -> candidate analysis |
| Aortic stenosis | 5e-18 | rs1245518 | 5 | GCST90837544 | no MR -> candidate analysis |
| Thoracic or lumbosacral neuritis or radiculitis, unspecified | 1e-17 | rs1245512 | 2 | GCST90480572 | no MR -> candidate analysis |
| Blood protein levels | 3e-17 | rs1245547 | 1 | GCST006585 | no MR -> candidate analysis |
| Back pain (PheCode 760) | 5e-16 | rs1245527 | 1 | GCST90480570 | no MR -> candidate analysis |
| Osteoarthritis (with total hip replacement) | 6e-14 | rs7895905 | 1 | GCST90566802 | no MR -> candidate analysis |
| VSIR protein levels | 8e-14 | rs542440927 | 1 | GCST90471053 | no MR -> candidate analysis |
| Displacement of intervertebral disc (PheCode 722.1) | 3e-13 | rs11000138 | 1 | GCST90480510 | no MR -> candidate analysis |
| Circulating SFTPD levels | 5e-13 | rs1245555 | 1 | GCST90859954 | no MR -> candidate analysis |
| _...and 17 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 144 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Back pain | 0.559 | — | common-variant locus | no MR -> candidate analysis |
| osteoarthritis, knee | 0.535 | — | common-variant locus | no MR -> candidate analysis |
| Pain | 0.366 | — | common-variant locus | MR: beta=0.0797, p=0.107 (cis) |
| radiculitis | 0.216 | — | common-variant locus | no MR -> candidate analysis |
| arthropathy | 0.153 | — | common-variant locus | no MR -> candidate analysis |
| vertebral column disorder | 0.11 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.1 | — | common-variant locus | no MR -> candidate analysis |
| Intervertebral Disc Displacement | 0.061 | — | common-variant locus | no MR -> candidate analysis |
| osteoarthritis, hip | 0.055 | — | common-variant locus | MR: beta=0.14, p=0.29 (cis) |
| musculoskeletal system disorder | 0.049 | — | common-variant locus | no MR -> candidate analysis |
| spinal cord injury | 0.047 | — | common-variant locus | no MR -> candidate analysis |

> Of the 11 rows above, **9 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=9.2e-09, LOEUF=0.847 — LoF-tolerant |
| GWAS Catalog | 60 unique SNPs / 120 rows |
| ClinVar | 91 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 144 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'SPOCK2'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 91 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 29 traits by best p-value, aggregated from 39 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q92563 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000107742/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/SPOCK2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/SPOCK2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=SPOCK2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/SPOCK2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:13:22  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
