# Protein Dossier — CTGF (CCN family member 2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: K40 Inguinal hernia | 0.158 | 0.0435 | 2.85e-04 | Wald ratio | 1 | cis | NA |
| Haemoglobin concentration | -0.0943 | 0.0303 | 0.00186 | Wald ratio | 1 | cis | NA |
| Forced expiratory volume in 1-second (FEV1) | 0.0222 | 0.00719 | 0.00202 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | 0.019 | 0.00682 | 0.00539 | Wald ratio | 1 | cis | NA |
| Birth length | -0.0867 | 0.0331 | 0.00891 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: uterine fibroids | 0.151 | 0.0579 | 0.00915 | Wald ratio | 1 | cis | NA |
| Packed cell volume | -0.217 | 0.0836 | 0.00941 | Wald ratio | 1 | cis | NA |
| Vascular or heart problems diagnosed by doctor: Angina | -0.13 | 0.0532 | 0.0143 | Wald ratio | 1 | cis | NA |
| Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.0518 | 0.0212 | 0.0147 | Wald ratio | 1 | cis | NA |
| Height | 0.0235 | 0.00992 | 0.0177 | Wald ratio | 1 | cis | NA |
| Cough on most days | -0.113 | 0.048 | 0.0184 | Wald ratio | 1 | cis | NA |
| Transferrin | -0.0799 | 0.0351 | 0.023 | Wald ratio | 1 | cis | NA |
| _...and 84 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2975_19_2` | CTGF | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_No GWAS Catalog associations mapped to this gene._

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 3866 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| kyphomelic dysplasia | 0.684 | — | established (curated) | no MR -> candidate analysis |
| spondyloepimetaphyseal dysplasia, Li-Shao-Li type | 0.547 | — | established (curated) | no MR -> candidate analysis |
| vertebral column disorder | 0.463 | — | common-variant locus | no MR -> candidate analysis |
| cardiomyopathy | 0.44 | — | common-variant locus | no MR -> candidate analysis |
| enteritis | 0.401 | — | common-variant locus | no MR -> candidate analysis |
| aortic stenosis | 0.396 | — | common-variant locus | no MR -> candidate analysis |
| secondary malignant neoplasm | 0.387 | — | common-variant locus | no MR -> candidate analysis |
| Hyperhidrosis | 0.353 | — | common-variant locus | no MR -> candidate analysis |
| non-autoimmune hemolytic anemia | 0.334 | — | common-variant locus | no MR -> candidate analysis |
| pulmonary embolism | 0.25 | — | common-variant locus | MR: beta=0.102, p=0.226 (cis) |

> Of the 10 rows above, **9 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 1 known modulators (CCN family member 2) |
| gnomAD constraint | not available |
| GWAS Catalog | no mapped SNPs |
| ClinVar | no records |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 3866 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'CTGF' and resolved to 'CCN family member 2' — confirm this is the intended target.
- **`gnomad`** — No gnomAD constraint data.
- **`gwas`** — No GWAS Catalog SNPs mapped to this gene.
- **`clinvar`** — No ClinVar records.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — No GWAS Catalog associations mapped to this gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P29279 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000118523/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3712901/ — _ChEMBL_37 (released 2026-05-01)_

## Provenance

- Generated: 2026-08-14T02:09:24  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
