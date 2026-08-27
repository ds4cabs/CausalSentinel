# Protein Dossier — GAL (Germinal center-associated signaling and motility protein)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Glioma | -0.382 | 0.248 | 0.124 | Wald ratio | 1 | trans | NA |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_53 association rows across 34 traits (49 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Bone mineral density mean | 7e-77 | rs186637849 | 6 | GCST90321120 | no MR -> candidate analysis |
| Circulating GAL levels | 1e-55 | rs2012605 | 3 | GCST90860395 | no MR -> candidate analysis |
| Appendicular lean mass | 7e-53 | rs7129320 | 2 | GCST90000025 | no MR -> candidate analysis |
| GAL protein levels | 2e-50 | rs3018721 | 2 | GCST90469300 | no MR -> candidate analysis |
| Whole body water mass (UKB data field 23102) | 2e-44 | rs7129320 | 1 | GCST90468184 | no MR -> candidate analysis |
| Fracture | 8e-44 | rs35989399 | 1 | GCST006980 | no MR -> candidate analysis |
| Height | 1e-43 | rs2510396 | 5 | GCST007841 | no MR -> candidate analysis |
| Height (baseline) | 3e-41 | rs7102308 | 2 | GCST90565843 | no MR -> candidate analysis |
| Basal metabolic rate (UKB data field 23105) | 4e-39 | rs7129320 | 1 | GCST90468159 | no MR -> candidate analysis |
| Heel bone mineral density | 3e-38 | rs2510405 | 1 | GCST006433 | no MR -> candidate analysis |
| Ximenoylcarnitine (C26:1) levels | 2e-36 | rs2510374 | 1 | GCST90200149 | no MR -> candidate analysis |
| Cerotoylcarnitine (C26) levels | 2e-34 | rs112549564 | 3 | GCST90200136 | no MR -> candidate analysis |
| _...and 22 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1029 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| temporal lobe epilepsy | 0.608 | — | established (curated) | no MR -> candidate analysis |
| autosomal dominant epilepsy with auditory features | 0.674 | — | established (curated) | no MR -> candidate analysis |
| ankylosing spondylitis | 0.448 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.189 | — | common-variant locus | no MR -> candidate analysis |
| arthropathy | 0.169 | — | common-variant locus | no MR -> candidate analysis |
| non-autoimmune hemolytic anemia | 0.169 | — | common-variant locus | no MR -> candidate analysis |
| bone fracture | 0.138 | — | common-variant locus | no MR -> candidate analysis |
| hair color | 0.122 | — | common-variant locus | no MR -> candidate analysis |

> Of the 8 rows above, **8 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Galectin-9C) |
| gnomAD constraint | pLI=3.5e-05, LOEUF=1.39 — LoF-tolerant |
| GWAS Catalog | 132 unique SNPs / 208 rows |
| ClinVar | 90 records; 4 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | 3 clinical annotations across 6 drugs |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1029 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'GAL' and resolved to 'Galectin-9C' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 90 ClinVar records for this gene; it is a sample, not a rate.
- **`gwas_traits`** — Top 20 of 34 traits by best p-value, aggregated from 53 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q8N6F7 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000069482/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL6066211/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/GAL — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/GAL — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=GAL%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `pharmgkb`: https://www.pharmgkb.org/search?query=GAL — _ClinPGx clinicalAnnotation via https://api.clinpgx.org/v1/data_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/GAL — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:46:25  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
