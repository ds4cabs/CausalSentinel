# Protein Dossier — ENTPD1 (Ectonucleoside triphosphate diphosphohydrolase 1)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: K57 Diverticular disease of intestine | 0.207 | 0.0674 | 0.00214 | Wald ratio | 1 | cis | NA |
| Transferrin Saturation | -0.142 | 0.0484 | 0.00336 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: diverticular disease or diverticulitis | 0.234 | 0.0885 | 0.00823 | Wald ratio | 1 | cis | NA |
| Iron | -0.124 | 0.048 | 0.00954 | Wald ratio | 1 | cis | NA |
| Total cholesterol | -0.0633 | 0.0247 | 0.0103 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Cataract | 0.138 | 0.0561 | 0.014 | Wald ratio | 1 | cis | NA |
| Fracture resulting from simple fall | 0.0699 | 0.029 | 0.0157 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: vaginal prolapse or uterine prolapse | 0.282 | 0.122 | 0.0209 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: joint disorder | 0.294 | 0.13 | 0.0241 | Wald ratio | 1 | cis | NA |
| HOMA-IR | 0.0419 | 0.0196 | 0.0321 | Wald ratio | 1 | cis | NA |
| Large vessel disease | 0.344 | 0.17 | 0.0423 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertension | 0.0388 | 0.0192 | 0.0434 | Wald ratio | 1 | cis | NA |
| _...and 89 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3182_38_2` | CD39 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_169 association rows across 93 traits (158 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| CD39+ activated CD4 regulatory T cell %activated CD4 regulat | 1e-897 | rs4539246 | 3 | GCST90001490 | no MR -> candidate analysis |
| CD39+ CD4+ T cell %CD4+ T cell | 7e-738 | rs10736092 | 1 | GCST90001659 | no MR -> candidate analysis |
| CD39+ CD4+ T cell %T cell | 5e-712 | rs10736092 | 1 | GCST90001658 | no MR -> candidate analysis |
| CD39 on CD39+ activated CD4 regulatory T cell | 1e-700 | rs4918960 | 3 | GCST90002030 | no MR -> candidate analysis |
| CD39 on CD39+ secreting CD4 regulatory T cell | 1e-700 | rs10882655 | 2 | GCST90002031 | no MR -> candidate analysis |
| CD39 on CD39+ CD4+ T cell | 1e-700 | rs10882655 | 3 | GCST90002032 | no MR -> candidate analysis |
| CD39+ secreting CD4 regulatory T cell %secreting CD4 regulat | 4e-631 | rs2861152 | 3 | GCST90001496 | no MR -> candidate analysis |
| CD39+ secreting CD4 regulatory T cell %CD4 regulatory T cell | 5e-630 | rs7088584 | 3 | GCST90001497 | no MR -> candidate analysis |
| CD39+ CD8+ T cell %T cell | 3e-607 | rs10736092 | 2 | GCST90001670 | no MR -> candidate analysis |
| CD39+ CD4+ T cell Absolute Count | 1e-605 | rs7088584 | 2 | GCST90001660 | no MR -> candidate analysis |
| CD39+ CD8+ T cell %CD8+ T cell | 1e-583 | rs4917715 | 2 | GCST90001671 | no MR -> candidate analysis |
| CD39+ CD8+ T cell Absolute Count | 2e-574 | rs10748649 | 2 | GCST90001672 | no MR -> candidate analysis |
| _...and 81 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 1060 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Autosomal recessive spastic paraplegia type 64 | 0.816 | — | established (curated) | no MR -> candidate analysis |
| hereditary spastic paraplegia 64 | 0.891 | — | established (curated) | no MR -> candidate analysis |
| diverticular disease | 0.59 | — | common-variant locus | MR: beta=0.207, p=0.00214 (cis) |
| placental abruption | 0.547 | — | common-variant locus | no MR -> candidate analysis |
| dementia | 0.458 | — | common-variant locus | no MR -> candidate analysis |
| hereditary disease | 0.316 | — | established (curated) | no MR -> candidate analysis |
| hereditary spastic paraplegia | 0.31 | — | established (curated) | no MR -> candidate analysis |
| Global developmental delay | 0.195 | — | established (curated) | no MR -> candidate analysis |
| microcephaly | 0.195 | — | established (curated) | no MR -> candidate analysis |
| polymicrogyria | 0.195 | — | established (curated) | no MR -> candidate analysis |

> Of the 10 rows above, **9 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Ectonucleoside triphosphate diphosphohydrolase 1) |
| gnomAD constraint | pLI=3.1e-06, LOEUF=0.774 — LoF-tolerant |
| GWAS Catalog | 103 unique SNPs / 219 rows |
| ClinVar | 309 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 1060 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'ENTPD1' and resolved to 'Ectonucleoside triphosphate diphosphohydrolase 1' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 309 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 93 traits by best p-value, aggregated from 169 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P49961 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000138185/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL5722/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/ENTPD1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/ENTPD1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=ENTPD1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/ENTPD1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:26:08  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
