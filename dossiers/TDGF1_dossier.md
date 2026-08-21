# Protein Dossier — TDGF1 (Protein Cripto)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: gout | 0.0524 | 0.017 | 0.00206 | Wald ratio | 1 | cis | NA |
| Nucleus accumbens volume | -2.47 | 0.942 | 0.00864 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R14 Flatulence and related conditions | 0.189 | 0.074 | 0.0109 | Wald ratio | 1 | cis | NA |
| Bulimia nervosa | 0.0151 | 0.00605 | 0.0124 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | -0.00693 | 0.00277 | 0.0125 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: J33 Nasal polyp | -0.0819 | 0.0337 | 0.0151 | Wald ratio | 1 | cis | NA |
| Microalbuminuria | 0.0409 | 0.0174 | 0.0189 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: C61 Malignant neoplasm of prostate | -0.0657 | 0.028 | 0.019 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: prostate cancer | -0.0594 | 0.0266 | 0.0253 | Wald ratio | 1 | cis | NA |
| Neuroticism | 0.00605 | 0.00303 | 0.0455 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: gastro-oesophageal reflux (gord)  or  gastric reflux | 0.0197 | 0.0101 | 0.0505 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: osteoarthritis | -0.0139 | 0.00725 | 0.0558 | Wald ratio | 1 | cis | NA |
| _...and 93 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2672_60_1` | Cripto | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_No GWAS Catalog associations mapped to this gene._

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 280 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| midline interhemispheric variant of holoprosencephaly | 0.608 | — | established (curated) | no MR -> candidate analysis |
| lobar holoprosencephaly | 0.608 | — | established (curated) | no MR -> candidate analysis |
| microform holoprosencephaly | 0.608 | — | established (curated) | no MR -> candidate analysis |
| alobar holoprosencephaly | 0.608 | — | established (curated) | no MR -> candidate analysis |
| septopreoptic holoprosencephaly | 0.608 | — | established (curated) | no MR -> candidate analysis |
| semilobar holoprosencephaly | 0.608 | — | established (curated) | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.216 | — | common-variant locus | no MR -> candidate analysis |

> Of the 7 rows above, **7 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 1 known modulators (Protein Cripto) |
| gnomAD constraint | not available |
| GWAS Catalog | no mapped SNPs |
| ClinVar | no records |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 280 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'TDGF1' and resolved to 'Protein Cripto' — confirm this is the intended target.
- **`gnomad`** — No gnomAD constraint data.
- **`gwas`** — No GWAS Catalog SNPs mapped to this gene.
- **`clinvar`** — No ClinVar records.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — No GWAS Catalog associations mapped to this gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P13385 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000241186/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3713025/ — _ChEMBL_37 (released 2026-05-01)_

## Provenance

- Generated: 2026-08-14T05:18:20  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
