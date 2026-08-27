# Protein Dossier — REG4 (Regenerating islet-derived protein 4)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: I30 Acute pericarditis | 1.02 | 0.256 | 6.44e-05 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K60 Fissure and fistula of anal and rectal regions | 0.335 | 0.124 | 0.00715 | Wald ratio | 1 | cis | NA |
| Lumbar spine bone mineral density | -0.122 | 0.0512 | 0.0169 | Wald ratio | 1 | cis | NA |
| Eczema | -0.276 | 0.125 | 0.0275 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N92 Excessive  frequent and irregular menstruation | 0.146 | 0.0698 | 0.0366 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: polio  or  poliomyelitis | 0.544 | 0.281 | 0.0528 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: L03 Cellulitis | -0.367 | 0.194 | 0.0584 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hayfever or allergic rhinitis | 0.082 | 0.0438 | 0.0613 | Wald ratio | 1 | cis | NA |
| Hearing difficulty or problems: Yes | 0.0352 | 0.0192 | 0.0665 | Wald ratio | 1 | cis | NA |
| ER-positive Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.086 | 0.0477 | 0.0715 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: D25 Leiomyoma of uterus | -0.226 | 0.13 | 0.0832 | Wald ratio | 1 | cis | NA |
| Diastolic blood pressure  automated reading | -0.0204 | 0.0118 | 0.0836 | Wald ratio | 1 | cis | NA |
| _...and 43 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_32 association rows across 20 traits (28 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Circulating REG4 levels | 1e-181 | rs79795228 | 3 | GCST90860391 | no MR -> candidate analysis |
| REG4 protein levels | 4e-163 | rs79795228 | 2 | GCST90470451 | no MR -> candidate analysis |
| X-18922 levels | 7e-51 | rs1163548 | 3 | GCST90245656 | no MR -> candidate analysis |
| Regenerating islet-derived protein 4 levels | 3e-38 | rs58163904 | 3 | GCST90421303 | no MR -> candidate analysis |
| Acetone levels | 1e-24 | rs2582783 | 3 | GCST90501095 | no MR -> candidate analysis |
| Serum uric acid levels | 9e-24 | rs150147865 | 2 | GCST90018977 | no MR -> candidate analysis |
| Urate levels (UKB data field 30880) | 3e-18 | rs150147865 | 1 | GCST90468107 | no MR -> candidate analysis |
| DNA methylation-estimated granulocyte proportions | 2e-16 | rs4659238 | 1 | GCST90014293 | no MR -> candidate analysis |
| Regenerating islet-derived protein 4 levels (REG4.11102.22.3 | 1e-15 | rs79795228 | 2 | GCST90242614 | no MR -> candidate analysis |
| X-21736 levels | 1e-13 | rs1163548 | 2 | GCST90245691 | no MR -> candidate analysis |
| ACP6 protein levels | 6e-13 | rs34595089 | 1 | GCST90468204 | no MR -> candidate analysis |
| Plasma X-18922 levels in chronic kidney disease | 8e-12 | rs12132674 | 1 | GCST90266465 | no MR -> candidate analysis |
| _...and 8 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 194 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| cutaneous lupus erythematosus | 0.457 | — | common-variant locus | no MR -> candidate analysis |
| pneumonia | 0.395 | — | common-variant locus | no MR -> candidate analysis |
| fungal lung infectious disease | 0.395 | — | common-variant locus | no MR -> candidate analysis |

> Of the 3 rows above, **3 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=9.7e-05, LOEUF=1.09 — LoF-tolerant |
| GWAS Catalog | 78 unique SNPs / 156 rows |
| ClinVar | 56 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 194 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'REG4'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 56 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 20 traits by best p-value, aggregated from 32 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9BYZ8 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000134193/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/REG4 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/REG4 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=REG4%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/REG4 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:47:18  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
