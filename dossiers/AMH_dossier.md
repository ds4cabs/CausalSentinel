# Protein Dossier — AMH (Anti-Muellerian hormone)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Femoral neck bone mineral density | -0.108 | 0.0353 | 0.00216 | Wald ratio | 1 | trans | NA |
| Lumbar spine bone mineral density | -0.116 | 0.0411 | 0.00492 | Wald ratio | 1 | trans | NA |
| Height | 0.0372 | 0.0139 | 0.00724 | Wald ratio | 1 | trans | NA |
| Cough on most days | 0.129 | 0.0502 | 0.0104 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: R55 Syncope and collapse | -0.488 | 0.202 | 0.0157 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: gastro-oesophageal reflux (gord)  or  gastric reflux | -0.148 | 0.0624 | 0.0179 | Wald ratio | 1 | trans | NA |
| Age at menarche | 0.0554 | 0.0264 | 0.036 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: arthritis (nos) | 0.212 | 0.105 | 0.0429 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: L03 Cellulitis | 0.204 | 0.102 | 0.0454 | Wald ratio | 1 | trans | NA |
| Neuroticism | 0.0317 | 0.0158 | 0.0455 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: muscle or soft tissue injuries | -0.413 | 0.209 | 0.0487 | Wald ratio | 1 | trans | NA |
| Triglycerides | -0.0432 | 0.0222 | 0.0516 | Wald ratio | 1 | trans | NA |
| _...and 70 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4923_79_1` | MIS | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_3 association rows across 3 traits (3 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Anti-Mullerian hormone levels in pre-menopausal women | 8e-12 | rs10417628 | 1 | GCST90428625 | no MR -> candidate analysis |
| Anti-Mullerian hormone levels | 1e-11 | rs10417628 | 1 | GCST90104596 | no MR -> candidate analysis |
| Pulse pressure | 3e-8 | rs10407022 | 1 | GCST006022 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 761 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| persistent Mullerian duct syndrome | 0.9 | — | established (curated) | no MR -> candidate analysis |
| Persistent Müllerian duct syndrome | 0.864 | — | established (curated) | no MR -> candidate analysis |
| genetic non-acquired premature ovarian failure | 0.426 | — | established (curated) | no MR -> candidate analysis |
| hereditary disease | 0.318 | — | established (curated) | no MR -> candidate analysis |
| obesity disorder | 0.144 | — | common-variant locus | no MR -> candidate analysis |

> Of the 5 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.1e-15, LOEUF=1.53 — LoF-tolerant |
| GWAS Catalog | 100 unique SNPs / 202 rows |
| ClinVar | 311 records; 3 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 761 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'AMH'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 311 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 3 of 3 traits by best p-value, aggregated from 3 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P03971 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000104899/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/AMH — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/AMH — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=AMH%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/AMH — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:02:25  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
