# Protein Dossier — MMP1 (Interstitial collagenase)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: K20 Oesophagitis | 0.201 | 0.0595 | 7.43e-04 | Inverse variance weighted | 2 | trans | NA |
| Diagnoses - main ICD10: K20 Oesophagitis | 0.201 | 0.0595 | 7.43e-04 | Inverse variance weighted | 2 | cis | NA |
| Fractured bone site(s): Arm | 0.192 | 0.0597 | 0.00128 | Inverse variance weighted | 2 | trans | NA |
| Fractured bone site(s): Arm | 0.192 | 0.0597 | 0.00128 | Inverse variance weighted | 2 | cis | NA |
| ER-negative Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0912 | 0.0338 | 0.00689 | Inverse variance weighted | 2 | trans | NA |
| ER-negative Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0912 | 0.0338 | 0.00689 | Inverse variance weighted | 2 | cis | NA |
| Non-cancer illness code  self-reported: diverticular disease or diverticulitis | 0.128 | 0.0598 | 0.0318 | Inverse variance weighted | 2 | trans | NA |
| Non-cancer illness code  self-reported: diverticular disease or diverticulitis | 0.128 | 0.0598 | 0.0318 | Inverse variance weighted | 2 | cis | NA |
| Intracranial volume | 1.3e+04 | 6.16e+03 | 0.0343 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R14 Flatulence and related conditions | 0.425 | 0.205 | 0.0383 | Inverse variance weighted | 2 | trans | NA |
| Diagnoses - main ICD10: R14 Flatulence and related conditions | 0.425 | 0.205 | 0.0383 | Inverse variance weighted | 2 | cis | NA |
| Non-cancer illness code  self-reported: anxiety or panic attacks | 0.101 | 0.056 | 0.0709 | Inverse variance weighted | 2 | trans | NA |
| _...and 85 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4924_32_1` | MMP-1 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_17 association rows across 7 traits (17 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| MMP10 protein levels | 1e-94 | rs657043 | 4 | GCST90469915 | no MR -> candidate analysis |
| Serum levels of protein MMP10 | 5e-71 | rs17885595 | 3 | GCST90090215 | no MR -> candidate analysis |
| MMP1 protein levels | 2e-57 | rs139018071 | 5 | GCST90469919 | no MR -> candidate analysis |
| MMP12 protein levels | 2e-48 | rs470747 | 1 | GCST90469916 | no MR -> candidate analysis |
| Interstitial collagenase levels | 2e-46 | rs17879749 | 2 | GCST90248110 | no MR -> candidate analysis |
| Blood protein levels | 1e-42 | rs17878931 | 1 | GCST006585 | no MR -> candidate analysis |
| Cerebrospinal fluid protein MMP1 levels | 4e-17 | rs17879749 | 1 | GCST90944430 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1160 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| ovarian dysfunction | 0.541 | — | common-variant locus | no MR -> candidate analysis |
| poisoning | 0.512 | — | common-variant locus | no MR -> candidate analysis |
| response to xenobiotic stimulus | 0.512 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 5 known modulators (Interstitial collagenase) |
| gnomAD constraint | pLI=2.6e-18, LOEUF=1.3 — LoF-tolerant |
| GWAS Catalog | 153 unique SNPs / 386 rows |
| ClinVar | 172 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1160 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'MMP1' and resolved to 'Interstitial collagenase' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 172 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 7 of 7 traits by best p-value, aggregated from 17 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P03956 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000196611/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL332/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/MMP1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/MMP1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=MMP1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/MMP1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:49:26  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
