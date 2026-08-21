# Protein Dossier — REG1A (Lithostathine-1-alpha)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: pernicious anaemia | 0.00121 | 0.000412 | 0.00326 | Inverse variance weighted | 2 | cis | NA |
| Non-cancer illness code  self-reported: pernicious anaemia | 0.00121 | 0.000412 | 0.00326 | Inverse variance weighted | 2 | trans | NA |
| Alcohol intake frequency | 0.0252 | 0.0109 | 0.0213 | Inverse variance weighted | 2 | cis | NA |
| Alcohol intake frequency | 0.0252 | 0.0109 | 0.0213 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: vitiligo | 0.000281 | 0.000126 | 0.0257 | Inverse variance weighted | 2 | cis | NA |
| Non-cancer illness code  self-reported: vitiligo | 0.000281 | 0.000126 | 0.0257 | Inverse variance weighted | 2 | trans | NA |
| Mean cell haemoglobin concentration | -0.0291 | 0.0132 | 0.0278 | Wald ratio | 1 | cis | NA |
| Mean cell haemoglobin | -0.0808 | 0.0396 | 0.0415 | Wald ratio | 1 | cis | NA |
| Internalizing problems | -0.174 | 0.0857 | 0.0427 | Wald ratio | 1 | cis | NA |
| ER-negative Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0692 | 0.0365 | 0.058 | Inverse variance weighted | 2 | cis | NA |
| ER-negative Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0692 | 0.0365 | 0.058 | Inverse variance weighted | 2 | trans | NA |
| Diagnoses - main ICD10: N40 Hyperplasia of prostate | -0.00135 | 0.000716 | 0.0586 | Inverse variance weighted | 2 | cis | NA |
| _...and 153 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_25 association rows across 14 traits (21 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating REG1A levels | 2e-379 | rs11126696 | 2 | GCST90860433 | no MR -> candidate analysis |
| REG1A protein levels | 2e-311 | rs76841471 | 5 | GCST90470447 | no MR -> candidate analysis |
| REG1B protein levels | 7e-207 | rs76841471 | 3 | GCST90470448 | no MR -> candidate analysis |
| Lithostathine-1-alpha levels | 2e-91 | rs76841471 | 4 | GCST90248306 | no MR -> candidate analysis |
| Lithostathine-1-beta levels | 2e-86 | rs11126696 | 2 | GCST90248307 | no MR -> candidate analysis |
| REG3A protein levels | 2e-37 | rs12990484 | 1 | GCST90470449 | no MR -> candidate analysis |
| Serum levels of protein REG1A | 3e-25 | rs76841471 | 1 | GCST90087370 | no MR -> candidate analysis |
| Cerebrospinal fluid protein REG1A levels | 3e-18 | rs76841471 | 1 | GCST90945040 | no MR -> candidate analysis |
| Lithostathine-1-beta (analyte X16770.3) levels | 1e-16 | rs76841471 | 1 | GCST90422860 | no MR -> candidate analysis |
| Cerebrospinal fluid protein REG1B levels | 2e-16 | rs11126696 | 1 | GCST90944880 | no MR -> candidate analysis |
| Progression free survival in epithelial ovarian cancer treat | 2e-6 | rs2070707 | 1 | GCST012474 | no MR -> candidate analysis |
| Complement factor H-related protein 2 levels | 4e-6 | rs205549 | 1 | GCST90026530 | no MR -> candidate analysis |
| _...and 2 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 404 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| focal segmental glomerulosclerosis | 0.195 | — | established (curated) | no MR -> candidate analysis |
| smoking initiation | 0.144 | — | common-variant locus | no MR -> candidate analysis |
| obesity disorder | 0.121 | — | common-variant locus | no MR -> candidate analysis |
| pyogenic granuloma | 0.121 | — | common-variant locus | no MR -> candidate analysis |
| substance abuse | 0.105 | — | common-variant locus | no MR -> candidate analysis |
| attention deficit-hyperactivity disorder | 0.105 | — | common-variant locus | no MR -> candidate analysis |

> Of the 6 rows above, **6 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=2.1e-07, LOEUF=1.41 — LoF-tolerant |
| GWAS Catalog | 55 unique SNPs / 110 rows |
| ClinVar | 44 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 404 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'REG1A'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 44 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 14 of 14 traits by best p-value, aggregated from 25 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P05451 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000115386/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/REG1A — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/REG1A — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=REG1A%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/REG1A — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:46:52  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
