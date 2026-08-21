# Protein Dossier — C17orf78 (Uncharacterized protein C17orf78)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: enlarged prostate | 0.248 | 0.0733 | 7.33e-04 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: pneumothorax | 0.772 | 0.269 | 0.00407 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: psoriasis | 0.23 | 0.0823 | 0.00528 | Wald ratio | 1 | trans | NA |
| Fracture resulting from simple fall | 0.0709 | 0.027 | 0.00859 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: N40 Hyperplasia of prostate | 0.214 | 0.0927 | 0.0211 | Wald ratio | 1 | trans | NA |
| Invasive mucinous ovarian cancer | -0.489 | 0.212 | 0.0211 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: R55 Syncope and collapse | 0.214 | 0.0945 | 0.0238 | Wald ratio | 1 | trans | NA |
| Intracranial volume | -2.07e+04 | 9.19e+03 | 0.0243 | Wald ratio | 1 | trans | NA |
| Pallidum volume | -20.3 | 9.12 | 0.026 | Wald ratio | 1 | trans | NA |
| Hearing difficulty or problems: Yes | 0.0394 | 0.0181 | 0.0298 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: L03 Cellulitis | -0.403 | 0.19 | 0.0338 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: hypertrophic cardiomyopathy (hcm  or  hocm) | 0.807 | 0.411 | 0.0496 | Wald ratio | 1 | trans | NA |
| _...and 65 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_1 association rows across 1 traits (0 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Retinal nerve fibre layer (RNFL) thickness | 9e-7 | rs34232224 | 1 | GCST90554824 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 19 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Abnormality of the skeletal system | 0.232 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of the integument | 0.146 | — | common-variant locus | no MR -> candidate analysis |
| insomnia | 0.146 | — | common-variant locus | no MR -> candidate analysis |
| secondary malignant neoplasm | 0.12 | — | common-variant locus | no MR -> candidate analysis |
| intracranial hemorrhage | 0.096 | — | common-variant locus | no MR -> candidate analysis |
| alcohol drinking | 0.059 | — | common-variant locus | no MR -> candidate analysis |

> Of the 6 rows above, **6 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.3e-08, LOEUF=1.17 — LoF-tolerant |
| GWAS Catalog | 32 unique SNPs / 60 rows |
| ClinVar | 158 records; 21 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 19 of 19 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'C17orf78'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 158 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 1 of 1 traits by best p-value, aggregated from 1 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q8N4C9 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000278505/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/C17orf78 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/C17orf78 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=C17orf78%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/C17orf78 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:19:55  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
