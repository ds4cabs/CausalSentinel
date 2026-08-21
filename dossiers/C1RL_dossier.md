# Protein Dossier — C1RL (Complement C1r subcomponent-like protein)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Myocardial infarction | 0.153 | 0.0444 | 5.41e-04 | Wald ratio | 1 | cis | NA |
| Coronary heart disease | 0.118 | 0.0392 | 0.00249 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N20 Calculus of kidney and ureter | 0.227 | 0.0971 | 0.0195 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I84 Haemorrhoids | 0.126 | 0.0576 | 0.0289 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: basal cell carcinoma | 0.173 | 0.0897 | 0.0546 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: bladder problem (not cancer) | -0.367 | 0.201 | 0.0682 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: malignant melanoma | -0.27 | 0.155 | 0.0811 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: B37 Candidiasis | 0.541 | 0.315 | 0.0863 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: deep venous thrombosis (dvt) | 0.11 | 0.0646 | 0.0883 | Wald ratio | 1 | cis | NA |
| Rheumatoid arthritis | -0.109 | 0.0645 | 0.0899 | Wald ratio | 1 | cis | NA |
| Cough on most days | -0.0964 | 0.0571 | 0.0914 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: D25 Leiomyoma of uterus | -0.173 | 0.108 | 0.109 | Wald ratio | 1 | cis | NA |
| _...and 44 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_53 association rows across 39 traits (51 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Complement C1r subcomponent-like protein levels | 7e-333 | rs191448232 | 3 | GCST90246771 | no MR -> candidate analysis |
| Tyrosine-protein phosphatase non-receptor type 4 levels | 1e-209 | rs1126605 | 1 | GCST90250026 | no MR -> candidate analysis |
| Serum levels of protein SCGB1A1 | 4e-129 | rs1126605 | 1 | GCST90086346 | no MR -> candidate analysis |
| Catechol O-methyltransferase levels | 6e-112 | rs1126605 | 2 | GCST90247121 | no MR -> candidate analysis |
| Protocadherin-12 level in Chronic kidney disease with hypert | 2e-98 | rs1126605 | 1 | GCST90235819 | no MR -> candidate analysis |
| ZW10 interactor levels | 3e-77 | rs1126605 | 2 | GCST90423227 | no MR -> candidate analysis |
| NF-kappa-B inhibitor delta levels | 6e-67 | rs1126605 | 2 | GCST90248672 | no MR -> candidate analysis |
| Complement C1r subcomponent-like protein levels (C1RL.9348.1 | 6e-61 | rs191448232 | 2 | GCST90240769 | no MR -> candidate analysis |
| Ubiquitin-conjugating enzyme E2 D3 levels | 2e-55 | rs1126605 | 1 | GCST90250056 | no MR -> candidate analysis |
| Microfibrillar-associated protein 2 levels | 6e-52 | rs1126605 | 1 | GCST90248458 | no MR -> candidate analysis |
| EF-hand domain-containing protein D1 levels | 3e-46 | rs1126605 | 1 | GCST90247399 | no MR -> candidate analysis |
| Dynactin subunit 2 levels | 7e-46 | rs1126605 | 1 | GCST90247379 | no MR -> candidate analysis |
| _...and 27 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 607 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| coronary artery disorder | 0.125 | — | common-variant locus | no MR -> candidate analysis |

> Of the 1 rows above, **1 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.3e-09, LOEUF=1.33 — LoF-tolerant |
| GWAS Catalog | 102 unique SNPs / 213 rows |
| ClinVar | 153 records; 4 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 607 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'C1RL'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 153 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 39 traits by best p-value, aggregated from 53 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9NZP8 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000139178/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/C1RL — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/C1RL — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=C1RL%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/C1RL — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:21:33  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
