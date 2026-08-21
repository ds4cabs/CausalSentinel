# Protein Dossier — CD300A (CMRF35-like molecule 8)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diastolic blood pressure  automated reading | -0.0199 | 0.00707 | 0.00479 | Wald ratio | 1 | cis | NA |
| Years of schooling | 0.0322 | 0.0115 | 0.00511 | Wald ratio | 1 | cis | NA |
| Systolic blood pressure  automated reading | -0.0194 | 0.00706 | 0.00602 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypopituitarism | 0.55 | 0.23 | 0.0169 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: D25 Leiomyoma of uterus | 0.128 | 0.0538 | 0.0174 | Wald ratio | 1 | cis | NA |
| Fasting glucose | -0.0253 | 0.011 | 0.0219 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K80 Cholelithiasis | -0.123 | 0.0546 | 0.0237 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R04 Haemorrhage from respiratory passages | 0.179 | 0.0808 | 0.0263 | Wald ratio | 1 | cis | NA |
| Ferritin | -0.0563 | 0.0269 | 0.0363 | Wald ratio | 1 | cis | NA |
| Primary sclerosing cholangitis  | -0.2 | 0.0966 | 0.0381 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: emphysema or chronic bronchitis | 0.111 | 0.0536 | 0.0386 | Wald ratio | 1 | cis | NA |
| Hirschsprung's disease | -0.795 | 0.388 | 0.0402 | Wald ratio | 1 | cis | NA |
| _...and 95 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_51 association rows across 29 traits (47 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating CD300C levels | 2e-1141 | rs1171197 | 4 | GCST90859659 | no MR -> candidate analysis |
| CD300C/HAVCR2 protein level ratio | 7e-1127 | rs1171196 | 1 | GCST90313789 | no MR -> candidate analysis |
| CD300C/NBL1 protein level ratio | 5e-982 | rs1171196 | 1 | GCST90313792 | no MR -> candidate analysis |
| CD300C/MANSC1 protein level ratio | 3e-963 | rs1171196 | 1 | GCST90313791 | no MR -> candidate analysis |
| CD300C/FOLR2 protein level ratio | 1e-950 | rs1171196 | 1 | GCST90313787 | no MR -> candidate analysis |
| CD300C/CLEC14A protein level ratio | 3e-838 | rs1171196 | 1 | GCST90313786 | no MR -> candidate analysis |
| CD300C/GOLM2 protein level ratio | 9e-805 | rs1171196 | 1 | GCST90313788 | no MR -> candidate analysis |
| CMRF35-like molecule 8 levels | 1e-360 | rs2272111 | 4 | GCST90247074 | no MR -> candidate analysis |
| CD300C protein levels | 2e-254 | rs577654240 | 6 | GCST90468620 | no MR -> candidate analysis |
| CMRF35-like molecule 6 levels | 2e-139 | rs62087200 | 5 | GCST90247072 | no MR -> candidate analysis |
| CD300A protein levels | 3e-94 | rs750453552 | 2 | GCST90468619 | no MR -> candidate analysis |
| Serum levels of protein CD300A | 4e-84 | rs2272111 | 2 | GCST90089106 | no MR -> candidate analysis |
| _...and 17 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 161 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| injury | 0.432 | — | common-variant locus | MR: beta=0.145, p=0.0638 (cis) |
| non-autoimmune hemolytic anemia | 0.065 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.8e-05, LOEUF=0.936 — LoF-tolerant |
| GWAS Catalog | 71 unique SNPs / 142 rows |
| ClinVar | 84 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 161 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'CD300A'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 84 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 29 traits by best p-value, aggregated from 51 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9UGN4 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000167851/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/CD300A — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/CD300A — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=CD300A%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/CD300A — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:41:34  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
