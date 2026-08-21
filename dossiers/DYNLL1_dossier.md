# Protein Dossier — DYNLL1 (Dynein light chain 1, cytoplasmic)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: J33 Nasal polyp | 0.395 | 0.134 | 0.00323 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: S76 Injury of muscle and tendon at hip and thigh level | 0.82 | 0.315 | 0.00921 | Wald ratio | 1 | trans | NA |
| Fracture resulting from simple fall | 0.0838 | 0.0326 | 0.0103 | Wald ratio | 1 | trans | NA |
| Vascular or heart problems diagnosed by doctor: Angina | -0.25 | 0.0977 | 0.0105 | Wald ratio | 1 | trans | NA |
| Eye problems or disorders: Glaucoma | -0.37 | 0.168 | 0.0277 | Wald ratio | 1 | trans | NA |
| Happiness | 0.0363 | 0.0166 | 0.0293 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: D25 Leiomyoma of uterus | 0.201 | 0.098 | 0.0406 | Wald ratio | 1 | trans | NA |
| Sleep duration | -0.0212 | 0.0105 | 0.043 | Wald ratio | 1 | trans | NA |
| Cancer code  self-reported: small intestine or small bowel cancer | 0.718 | 0.357 | 0.0441 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: R07 Pain in throat and chest | -0.136 | 0.0689 | 0.0481 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: hyperthyroidism or thyrotoxicosis | 0.232 | 0.126 | 0.0657 | Wald ratio | 1 | trans | NA |
| Low grade serous ovarian cancer | -0.584 | 0.325 | 0.0721 | Wald ratio | 1 | trans | NA |
| _...and 52 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3881_49_2` | DLC8 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_30 association rows across 23 traits (30 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| High light scatter reticulocyte percentage of red cells | 2e-83 | rs4767902 | 3 | GCST004612 | no MR -> candidate analysis |
| High light scatter reticulocyte count | 5e-78 | rs11352199 | 2 | GCST004611 | no MR -> candidate analysis |
| Reticulocyte fraction of red cells | 9e-68 | rs11352199 | 2 | GCST004619 | no MR -> candidate analysis |
| Reticulocyte count | 4e-66 | rs4767902 | 2 | GCST004622 | no MR -> candidate analysis |
| Immature fraction of reticulocytes | 6e-60 | rs558163981 | 2 | GCST004628 | no MR -> candidate analysis |
| Mean spheric corpuscular volume | 2e-52 | rs1167688 | 1 | GCST90002397 | no MR -> candidate analysis |
| Mean corpuscular volume | 2e-37 | rs1167688 | 1 | GCST90002392 | no MR -> candidate analysis |
| C-reactive protein levels (MTAG) | 9e-34 | rs34179846 | 1 | GCST90179146 | no MR -> candidate analysis |
| C-reactive protein levels | 4e-33 | rs34179846 | 1 | GCST90019499 | no MR -> candidate analysis |
| Mean reticulocyte volume | 4e-33 | rs1167688 | 1 | GCST90002396 | no MR -> candidate analysis |
| Telomere length (principal component 1) | 4e-32 | rs111260157 | 1 | GCST90435144 | no MR -> candidate analysis |
| Mean platelet thrombocyte volume (UKB data field 30100) | 5e-27 | rs572586515 | 2 | GCST90468087 | no MR -> candidate analysis |
| _...and 11 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 510 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| coenzyme q10 deficiency, primary, 9 | 0.547 | — | established (curated) | no MR -> candidate analysis |
| mathematical ability | 0.224 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Dynein light chain 1, cytoplasmic) |
| gnomAD constraint | pLI=0.66, LOEUF=0.767 — LoF-tolerant |
| GWAS Catalog | 108 unique SNPs / 228 rows |
| ClinVar | 23 records; 15 pathogenic in sample of 23 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 510 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'DYNLL1' and resolved to 'Dynein light chain 1, cytoplasmic' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 23 record(s) retrieved, NOT over all 23 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 23 traits by best p-value, aggregated from 30 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P63167 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000088986/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL5725118/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/DYNLL1 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/DYNLL1 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=DYNLL1%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/DYNLL1 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T02:21:37  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
