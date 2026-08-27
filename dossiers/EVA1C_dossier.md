# Protein Dossier — EVA1C (Protein eva-1 homolog C)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: K80 Cholelithiasis | 0.00245 | 0.000697 | 4.40e-04 | Inverse variance weighted | 2 | cis | NA |
| Diagnoses - main ICD10: K80 Cholelithiasis | 0.00245 | 0.000697 | 4.40e-04 | Inverse variance weighted | 2 | trans | NA |
| Hippocampus volume | -86.6 | 28.3 | 0.0022 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | 0.00567 | 0.00214 | 0.00817 | Inverse variance weighted | 2 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | 0.00567 | 0.00214 | 0.00817 | Inverse variance weighted | 2 | trans | NA |
| Hearing difficulty or problems: Yes | -0.0054 | 0.00219 | 0.0134 | Inverse variance weighted | 2 | cis | NA |
| Hearing difficulty or problems: Yes | -0.0054 | 0.00219 | 0.0134 | Inverse variance weighted | 2 | trans | NA |
| Neo-extraversion | -1.2 | 0.492 | 0.0146 | Wald ratio | 1 | cis | NA |
| Diastolic blood pressure  automated reading | 0.0112 | 0.00495 | 0.0233 | Inverse variance weighted | 2 | cis | NA |
| Diastolic blood pressure  automated reading | 0.0112 | 0.00495 | 0.0233 | Inverse variance weighted | 2 | trans | NA |
| Thalamus volume | -85.1 | 37.7 | 0.024 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M72 Fibroblastic disorders | 0.000812 | 0.000363 | 0.0254 | Inverse variance weighted | 2 | cis | NA |
| _...and 178 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_30 association rows across 21 traits (16 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Protein eva-1 homolog C levels | 8e-35 | rs34028712 | 1 | GCST90248935 | no MR -> candidate analysis |
| Height | 2e-25 | rs9982003 | 3 | GCST90245848 | MR: beta=-0.0246, p=0.0822 (cis) |
| Serum levels of protein EVA1C | 4e-18 | rs59652870 | 1 | GCST90090356 | no MR -> candidate analysis |
| Blood protein levels | 2e-12 | rs6517101 | 1 | GCST006585 | no MR -> candidate analysis |
| Protein eva-1 homolog C levels (EVA1C.7008.13.3) | 6e-12 | rs6517101 | 1 | GCST90242442 | no MR -> candidate analysis |
| Gamma glutamyl transferase levels | 7e-11 | rs78732220 | 2 | GCST90662899 | no MR -> candidate analysis |
| Systolic blood pressure (MTAG) | 5e-10 | rs2833834 | 1 | GCST90449056 | no MR -> candidate analysis |
| Systolic blood pressure | 8e-10 | rs11701033 | 4 | GCST90310294 | no MR -> candidate analysis |
| Liver enzyme levels (gamma-glutamyl transferase) | 1e-9 | rs35933282 | 1 | GCST90013407 | no MR -> candidate analysis |
| Height (baseline) | 2e-9 | rs8127011 | 1 | GCST90565843 | no MR -> candidate analysis |
| Gamma glutamyl transpeptidase | 1e-8 | rs35933282 | 1 | GCST90018954 | no MR -> candidate analysis |
| Intraocular pressure | 3e-8 | rs77135980 | 1 | GCST010376 | no MR -> candidate analysis |
| _...and 9 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 62 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Abnormality of the skeletal system | 0.779 | — | common-variant locus | no MR -> candidate analysis |
| glaucoma | 0.457 | — | common-variant locus | MR: beta=0.00322, p=0.139 (cis) |
| aortic valve stenosis | 0.416 | — | common-variant locus | no MR -> candidate analysis |
| tympanic membrane disorder | 0.397 | — | common-variant locus | no MR -> candidate analysis |
| ovarian neoplasm | 0.052 | — | common-variant locus | no MR -> candidate analysis |
| mixed connective tissue disease | 0.043 | — | common-variant locus | no MR -> candidate analysis |
| male infertility | 0.039 | — | common-variant locus | no MR -> candidate analysis |
| squamous cell carcinoma | 0.034 | — | common-variant locus | no MR -> candidate analysis |

> Of the 8 rows above, **7 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.00017, LOEUF=0.769 — LoF-tolerant |
| GWAS Catalog | 26 unique SNPs / 52 rows |
| ClinVar | 138 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 62 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'EVA1C'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 138 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 21 traits by best p-value, aggregated from 30 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P58658 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000166979/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/EVA1C — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/EVA1C — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=EVA1C%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/EVA1C — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:29:58  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
