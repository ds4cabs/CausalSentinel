# Protein Dossier — AGRP (Agouti-related protein)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Height | -0.0536 | 0.00901 | 2.75e-09 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | 0.157 | 0.0273 | 8.84e-09 | Wald ratio | 1 | cis | NA |
| Heel bone mineral density (BMD) T-score  automated | 0.0426 | 0.00931 | 4.65e-06 | Wald ratio | 1 | cis | NA |
| Multiple sclerosis | -0.196 | 0.052 | 1.59e-04 | Wald ratio | 1 | cis | NA |
| Sodium in urine | -0.0246 | 0.00705 | 4.82e-04 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K60 Fissure and fistula of anal and rectal regions | 0.275 | 0.0812 | 7.23e-04 | Wald ratio | 1 | cis | NA |
| Subjective well being | 0.0329 | 0.00974 | 7.38e-04 | Wald ratio | 1 | cis | NA |
| Bipolar disorder | 0.212 | 0.067 | 0.00152 | Wald ratio | 1 | cis | NA |
| Forced vital capacity (FVC) | -0.018 | 0.00589 | 0.00225 | Wald ratio | 1 | cis | NA |
| Urate | -0.0451 | 0.0158 | 0.00443 | Wald ratio | 1 | cis | NA |
| Ferritin | -0.0773 | 0.0278 | 0.00535 | Wald ratio | 1 | cis | NA |
| Anorexia nervosa | -0.377 | 0.137 | 0.00608 | Wald ratio | 1 | cis | NA |
| _...and 106 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-2813_11_2` | ART | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_No GWAS Catalog associations mapped to this gene._

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 298 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Obesity | 0.195 | — | established (curated) | MR: beta=0.00996, p=0.164 (cis) |
| Abnormality of the skeletal system | 0.66 | — | common-variant locus | no MR -> candidate analysis |
| androgenetic alopecia | 0.329 | — | common-variant locus | no MR -> candidate analysis |
| poisoning | 0.289 | — | common-variant locus | no MR -> candidate analysis |
| hypothyroidism | 0.252 | — | common-variant locus | MR: beta=0.157, p=8.84e-09 (cis) |
| smoking behavior | 0.208 | — | common-variant locus | no MR -> candidate analysis |
| dermatophytosis | 0.113 | — | common-variant locus | no MR -> candidate analysis |

> Of the 7 rows above, **5 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=0.023, LOEUF=1.06 — LoF-tolerant |
| GWAS Catalog | 60 unique SNPs / 120 rows |
| ClinVar | 58 records; 5 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 298 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'AGRP'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 58 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — No GWAS Catalog associations mapped to this gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O00253 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000159723/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/AGRP — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/AGRP — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=AGRP%5Bgene%5D — _ClinVar build Build260809-1055.1_

## Provenance

- Generated: 2026-08-14T00:58:14  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
