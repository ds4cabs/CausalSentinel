# Protein Dossier — NMRAL1 (NmrA-like family domain-containing protein 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: L03 Cellulitis | -0.517 | 0.179 | 0.00381 | Wald ratio | 1 | cis | NA |
| Squamous cell lung cancer | 0.271 | 0.104 | 0.00876 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: migraine | 0.108 | 0.0479 | 0.0234 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K29 Gastritis and duodenitis | -0.149 | 0.0696 | 0.0318 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K80 Cholelithiasis | -0.161 | 0.0758 | 0.0336 | Wald ratio | 1 | cis | NA |
| Type 2 diabetes | -0.422 | 0.211 | 0.0453 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: B37 Candidiasis | 0.534 | 0.283 | 0.0589 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: H25 Senile cataract | -0.256 | 0.139 | 0.0648 | Wald ratio | 1 | cis | NA |
| ER-negative Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0932 | 0.0514 | 0.0698 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: asthma | -0.0474 | 0.0271 | 0.08 | Wald ratio | 1 | cis | NA |
| Body mass index (BMI) | 0.0155 | 0.0092 | 0.0922 | Wald ratio | 1 | cis | NA |
| Birth weight | -0.0249 | 0.0151 | 0.0992 | Wald ratio | 1 | cis | NA |
| _...and 56 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_13 association rows across 11 traits (10 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| NmrA-like family domain-containing protein 1 levels | 4e-602 | rs11557236 | 2 | GCST90248696 | no MR -> candidate analysis |
| HMOX2 protein levels | 8e-60 | rs3747585 | 1 | GCST90469466 | no MR -> candidate analysis |
| Circulating HMOX2 levels | 4e-59 | rs4785966 | 1 | GCST90860742 | no MR -> candidate analysis |
| NmrA-like family domain-containing protein 1 levels (NMRAL1. | 2e-28 | rs11557236 | 1 | GCST90242124 | no MR -> candidate analysis |
| Pulse pressure | 5e-14 | rs6500609 | 1 | GCST90310296 | no MR -> candidate analysis |
| Systolic blood pressure | 1e-13 | rs6500609 | 1 | GCST90310294 | no MR -> candidate analysis |
| Migraine | 2e-10 | rs12598836 | 2 | GCST90102553 | MR: beta=0.108, p=0.0234 (cis) |
| Knee osteoarthritis | 5e-9 | rs6500609 | 1 | GCST90034523 | no MR -> candidate analysis |
| Hair color | 5e-8 | rs4424915 | 1 | GCST007082 | no MR -> candidate analysis |
| Waist circumference adjusted for body mass index | 6e-7 | rs190275219 | 1 | GCST008161 | no MR -> candidate analysis |
| Astrocytoma (high-grade) | 9e-6 | rs11557236 | 1 | GCST90296478 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 219 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| osteoarthritis, knee | 0.307 | — | common-variant locus | no MR -> candidate analysis |
| hypertensive disorder | 0.258 | — | common-variant locus | no MR -> candidate analysis |
| schizophrenia | 0.22 | — | common-variant locus | no MR -> candidate analysis |
| migraine disorder | 0.154 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (NmrA-like family domain-containing protein 1) |
| gnomAD constraint | pLI=6.5e-13, LOEUF=1.56 — LoF-tolerant |
| GWAS Catalog | 93 unique SNPs / 184 rows |
| ClinVar | 121 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 219 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'NMRAL1' and resolved to 'NmrA-like family domain-containing protein 1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 121 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 11 of 11 traits by best p-value, aggregated from 13 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9HBL8 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000153406/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4802017/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/NMRAL1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/NMRAL1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=NMRAL1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/NMRAL1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:59:52  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
