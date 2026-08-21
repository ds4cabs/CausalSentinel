# Protein Dossier — CNTN1 (Contactin-1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: B37 Candidiasis | 0.000447 | 0.000149 | 0.0028 | Inverse variance weighted | 2 | trans | NA |
| Diagnoses - main ICD10: B37 Candidiasis | 0.000447 | 0.000149 | 0.0028 | Inverse variance weighted | 2 | cis | NA |
| Parkinson's disease | 0.385 | 0.146 | 0.00825 | Wald ratio | 1 | trans | NA |
| Body mass index (BMI) | 0.0159 | 0.00692 | 0.0211 | Inverse variance weighted | 2 | trans | NA |
| Body mass index (BMI) | 0.0159 | 0.00692 | 0.0211 | Inverse variance weighted | 2 | cis | NA |
| Pancreatic cancer | -0.303 | 0.141 | 0.0308 | Inverse variance weighted | 2 | trans | NA |
| Pancreatic cancer | -0.303 | 0.141 | 0.0308 | Inverse variance weighted | 2 | cis | NA |
| Non-cancer illness code  self-reported: enlarged prostate | -0.00163 | 0.000808 | 0.0439 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: enlarged prostate | -0.00163 | 0.000808 | 0.0439 | Inverse variance weighted | 2 | cis | NA |
| Amyotrophic lateral sclerosis | 0.0996 | 0.0507 | 0.0495 | Inverse variance weighted | 2 | trans | NA |
| Amyotrophic lateral sclerosis | 0.0996 | 0.0507 | 0.0495 | Inverse variance weighted | 2 | cis | NA |
| Diagnoses - main ICD10: S76 Injury of muscle and tendon at hip and thigh level | -0.000286 | 0.00015 | 0.0561 | Inverse variance weighted | 2 | trans | NA |
| _...and 158 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2974_61_2` | contactin-1 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_83 association rows across 43 traits (49 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating CNTN1 levels | 3e-344 | rs11177623 | 9 | GCST90859934 | no MR -> candidate analysis |
| CNTN1 protein levels | 2e-258 | rs3904168 | 13 | GCST90468803 | no MR -> candidate analysis |
| CNTN1/EGFR protein level ratio | 2e-177 | rs1965163 | 1 | GCST90314162 | no MR -> candidate analysis |
| ALCAM/CNTN1 protein level ratio | 6e-177 | rs1965163 | 1 | GCST90313235 | no MR -> candidate analysis |
| Contactin-1 levels | 7e-64 | rs12811939 | 6 | GCST90247122 | no MR -> candidate analysis |
| Parkinson's disease | 2e-27 | rs1442190 | 4 | GCST002455 | MR: beta=0.385, p=0.00825 (trans) |
| RELT-like protein 1 levels | 7e-17 | rs7299744 | 1 | GCST90422123 | no MR -> candidate analysis |
| Serum levels of protein CNTN1 | 2e-12 | rs11177623 | 1 | GCST90088159 | no MR -> candidate analysis |
| Blood protein levels | 1e-11 | rs11177623 | 1 | GCST006585 | no MR -> candidate analysis |
| Precordial pain (PheCode 418.1) | 5e-11 | rs150785851 | 1 | GCST90480142 | no MR -> candidate analysis |
| Gut microbial network clusters (Salmon (at 1 year) x Househo | 8e-11 | rs117742571 | 2 | GCST90569451 | no MR -> candidate analysis |
| Total PHF-tau (SNP x SNP interaction) | 5e-10 | rs10082977 x rs10754859 | 1 | GCST010340 | no MR -> candidate analysis |
| _...and 31 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 910 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Compton-North congenital myopathy | 0.902 | — | established (curated) | no MR -> candidate analysis |
| Congenital lethal myopathy, Compton-North type | 0.608 | — | established (curated) | no MR -> candidate analysis |
| Parkinson disease | 0.555 | — | common-variant locus | no MR -> candidate analysis |
| urinary system disorder | 0.536 | — | common-variant locus | no MR -> candidate analysis |
| escherichia coli infection | 0.485 | — | common-variant locus | no MR -> candidate analysis |
| exostosis | 0.417 | — | common-variant locus | no MR -> candidate analysis |
| Hypercholesterolemia | 0.32 | — | common-variant locus | MR: beta=-0.0207, p=0.0587 (trans) |
| hereditary disease | 0.318 | — | established (curated) | no MR -> candidate analysis |
| retinal disorder | 0.317 | — | common-variant locus | no MR -> candidate analysis |
| Precordial pain | 0.311 | — | common-variant locus | no MR -> candidate analysis |
| inflammatory bowel disease | 0.22 | — | common-variant locus | no MR -> candidate analysis |
| cervical carcinoma | 0.214 | — | common-variant locus | no MR -> candidate analysis |
| arthropathy | 0.203 | — | common-variant locus | no MR -> candidate analysis |
| Crohn disease | 0.198 | — | common-variant locus | no MR -> candidate analysis |

> Of the 14 rows above, **13 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Contactin-1) |
| gnomAD constraint | pLI=1, LOEUF=0.394 — LoF-INTOLERANT |
| GWAS Catalog | 109 unique SNPs / 182 rows |
| ClinVar | 752 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 910 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'CNTN1' and resolved to 'Contactin-1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 752 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 43 traits by best p-value, aggregated from 83 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q12860 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000018236/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL6067142/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CNTN1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CNTN1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CNTN1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CNTN1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:55:23  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
