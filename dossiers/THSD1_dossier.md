# Protein Dossier — THSD1 (Thrombospondin type-1 domain-containing protein 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Myocardial infarction | -0.107 | 0.0372 | 0.00391 | Wald ratio | 1 | cis | NA |
| Coronary heart disease | -0.0962 | 0.0341 | 0.00477 | Wald ratio | 1 | cis | NA |
| Weight | 0.014 | 0.00712 | 0.0495 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hayfever or allergic rhinitis | 0.0596 | 0.0313 | 0.0567 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: mania or bipolar disorder or manic depression | 0.24 | 0.127 | 0.0585 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Other bones | -0.07 | 0.0377 | 0.0633 | Wald ratio | 1 | cis | NA |
| Cough on most days | 0.0704 | 0.0386 | 0.0683 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Cataract | 0.0743 | 0.0408 | 0.0687 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: joint disorder | 0.177 | 0.0999 | 0.0764 | Wald ratio | 1 | cis | NA |
| Forearm bone mineral density | -0.245 | 0.143 | 0.0853 | Wald ratio | 1 | cis | NA |
| Birth weight | 0.0211 | 0.0129 | 0.103 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R11 Nausea and vomiting | -0.286 | 0.178 | 0.107 | Wald ratio | 1 | cis | NA |
| _...and 42 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_4 association rows across 3 traits (4 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Thrombospondin type-1 domain-containing protein 1 levels | 3e-338 | rs41292808 | 2 | GCST90249866 | no MR -> candidate analysis |
| THSD1 protein levels | 4e-83 | rs149590732 | 1 | GCST90470859 | no MR -> candidate analysis |
| Thrombospondin type-1 domain-containing protein 1 levels (TH | 6e-33 | rs41292808 | 1 | GCST90243009 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 86 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| aneurysm, intracranial berry, 12 | 0.862 | — | established (curated) | no MR -> candidate analysis |
| lymphatic malformation 13 | 0.799 | — | established (curated) | no MR -> candidate analysis |
| Non-immune hydrops fetalis | 0.596 | — | established (curated) | no MR -> candidate analysis |
| Familial cerebral saccular aneurysm | 0.608 | — | established (curated) | no MR -> candidate analysis |
| Alzheimer disease | 0.396 | — | common-variant locus | no MR -> candidate analysis |
| aortic aneurysm | 0.195 | — | established (curated) | no MR -> candidate analysis |
| vascular dementia | 0.182 | — | established (curated) | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.041 | — | common-variant locus | no MR -> candidate analysis |
| cataract | 0.04 | — | common-variant locus | MR: beta=0.0743, p=0.0687 (cis) |
| trauma complication | 0.04 | — | common-variant locus | no MR -> candidate analysis |

> Of the 10 rows above, **9 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=4e-09, LOEUF=0.979 — LoF-tolerant |
| GWAS Catalog | 9 unique SNPs / 18 rows |
| ClinVar | 216 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 86 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'THSD1'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 216 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 3 of 3 traits by best p-value, aggregated from 4 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9NS62 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000136114/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/THSD1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/THSD1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=THSD1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/THSD1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T05:20:57  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
