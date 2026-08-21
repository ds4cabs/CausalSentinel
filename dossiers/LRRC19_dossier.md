# Protein Dossier — LRRC19 (Leucine-rich repeat-containing protein 19)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Forearm bone mineral density | 0.0556 | 0.02 | 0.00544 | Wald ratio | 1 | trans | NA |
| Total cholesterol | 0.0169 | 0.0067 | 0.0116 | Wald ratio | 1 | trans | NA |
| Red blood cell count | -0.00742 | 0.00309 | 0.0164 | Wald ratio | 1 | trans | NA |
| Neuroticism | -0.00928 | 0.00412 | 0.0244 | Wald ratio | 1 | trans | NA |
| Alzheimer's disease | 0.047 | 0.0217 | 0.0299 | Wald ratio | 1 | trans | NA |
| Serum cystatin C (eGFRcys) | -0.00505 | 0.00237 | 0.0331 | Wald ratio | 1 | trans | NA |
| Femoral neck bone mineral density | 0.0194 | 0.00954 | 0.0425 | Wald ratio | 1 | trans | NA |
| HDL cholesterol | 0.012 | 0.00619 | 0.0532 | Wald ratio | 1 | trans | NA |
| Internalizing problems | -0.0755 | 0.0417 | 0.07 | Wald ratio | 1 | trans | NA |
| High grade serous ovarian cancer | 0.036 | 0.0205 | 0.0785 | Wald ratio | 1 | trans | NA |
| Neo-openness to experience | 0.149 | 0.0895 | 0.095 | Wald ratio | 1 | trans | NA |
| Rheumatoid arthritis | 0.0314 | 0.0189 | 0.0964 | Wald ratio | 1 | trans | NA |
| _...and 35 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_1 association rows across 1 traits (0 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Emphysema annual change measurement in smokers (adjusted lun | 7e-6 | rs145997721 | 1 | GCST008477 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 68 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| sign or symptom | 0.06 | — | common-variant locus | no MR -> candidate analysis |
| sialadenitis | 0.049 | — | common-variant locus | no MR -> candidate analysis |
| aneurysm | 0.048 | — | common-variant locus | no MR -> candidate analysis |
| nephrotic syndrome | 0.035 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=8.9e-12, LOEUF=1.33 — LoF-tolerant |
| GWAS Catalog | 13 unique SNPs / 26 rows |
| ClinVar | 155 records; 5 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 68 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'LRRC19'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 155 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 1 of 1 traits by best p-value, aggregated from 1 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9H756 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000184434/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/LRRC19 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/LRRC19 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=LRRC19%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/LRRC19 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:38:21  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
