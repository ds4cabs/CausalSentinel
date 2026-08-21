# Protein Dossier — TNC (Tenascin)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Body mass index (BMI) | -0.0121 | 0.00389 | 0.00196 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K80 Cholelithiasis | -0.0848 | 0.0295 | 0.00408 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertrophic cardiomyopathy (hcm  or  hocm) | 0.415 | 0.188 | 0.0272 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I80 Phlebitis and thrombophlebitis | -0.146 | 0.0663 | 0.0275 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | -0.113 | 0.052 | 0.0303 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: iron deficiency anaemia | 0.103 | 0.0482 | 0.0331 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: osteoarthritis | 0.0266 | 0.0127 | 0.0359 | Wald ratio | 1 | cis | NA |
| Pulse rate | -0.0137 | 0.00687 | 0.0459 | Wald ratio | 1 | cis | NA |
| Fracture resulting from simple fall | -0.0197 | 0.0105 | 0.0593 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M16 Coxarthrosis [arthrosis of hip] | 0.0577 | 0.0306 | 0.0594 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R04 Haemorrhage from respiratory passages | -0.113 | 0.0608 | 0.0627 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: L03 Cellulitis | -0.0873 | 0.0474 | 0.0655 | Wald ratio | 1 | cis | NA |
| _...and 55 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4155_3_2` | Tenascin | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_106 association rows across 65 traits (94 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Tenascin levels | 4e-1960 | rs1138545 | 11 | GCST90249798 | no MR -> candidate analysis |
| Tenascin (analyte X4155.3) levels | 3e-910 | rs1138545 | 1 | GCST90425965 | no MR -> candidate analysis |
| Chymotrypsin-like elastase family member 1 levels | 3e-579 | rs1138545 | 3 | GCST90247434 | no MR -> candidate analysis |
| Prolargin levels (PRELP.5675.6.3) | 2e-489 | rs1138545 | 2 | GCST90242391 | no MR -> candidate analysis |
| Tenascin (analyte X5675.6) levels | 2e-388 | rs1138545 | 1 | GCST90426445 | no MR -> candidate analysis |
| Blood protein levels | 2e-333 | rs72758637 | 6 | GCST006585 | no MR -> candidate analysis |
| Serum levels of protein TNC | 4e-299 | rs7021589 | 2 | GCST90088611 | no MR -> candidate analysis |
| Serum levels of protein CETP | 4e-294 | rs7029844 | 1 | GCST90089679 | no MR -> candidate analysis |
| Serum levels of protein CELA1 | 1e-258 | rs7029844 | 1 | GCST90089284 | no MR -> candidate analysis |
| Circulating TNC levels | 3e-213 | rs34810955 | 2 | GCST90860463 | no MR -> candidate analysis |
| Tenascin (analyte X7131.207) levels | 2e-193 | rs1138545 | 1 | GCST90426927 | no MR -> candidate analysis |
| Height | 2e-176 | rs1250023 | 7 | GCST90245848 | no MR -> candidate analysis |
| _...and 53 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1002 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| autosomal dominant nonsyndromic hearing loss | 0.787 | — | established (curated) | no MR -> candidate analysis |
| deafness | 0.832 | — | established (curated) | no MR -> candidate analysis |
| osteoarthritis, hip | 0.846 | — | common-variant locus | no MR -> candidate analysis |
| Dupuytren Contracture | 0.723 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.713 | — | common-variant locus | no MR -> candidate analysis |
| total hip arthroplasty | 0.709 | — | common-variant locus | no MR -> candidate analysis |
| medical procedure | 0.635 | — | common-variant locus | no MR -> candidate analysis |
| osteoarthritis, knee | 0.631 | — | common-variant locus | no MR -> candidate analysis |
| osteoarthritis | 0.593 | — | common-variant locus | MR: beta=0.0266, p=0.0359 (cis) |
| vein disorder | 0.594 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.573 | — | common-variant locus | no MR -> candidate analysis |
| lymphatic system disorder | 0.555 | — | common-variant locus | no MR -> candidate analysis |
| Varicose veins | 0.553 | — | common-variant locus | MR: beta=-0.0404, p=0.153 (cis) |
| asthma | 0.499 | — | common-variant locus | MR: beta=0.0102, p=0.346 (cis) |
| total joint arthroplasty | 0.512 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **12 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 4 known modulators (Tenascin) |
| gnomAD constraint | pLI=3.2e-15, LOEUF=0.631 — LoF-tolerant |
| GWAS Catalog | 128 unique SNPs / 275 rows |
| ClinVar | 691 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1002 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'TNC' and resolved to 'Tenascin' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 691 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 65 traits by best p-value, aggregated from 106 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P24821 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000041982/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3712856/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/TNC — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/TNC — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=TNC%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/TNC — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:24:58  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
