# Protein Dossier — TIMP4 (Metalloproteinase inhibitor 4)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: hypothyroidism or myxoedema | -0.144 | 0.0332 | 1.43e-05 | Wald ratio | 1 | cis | NA |
| Lumbar spine bone mineral density | -0.076 | 0.0238 | 0.00143 | Wald ratio | 1 | cis | NA |
| Type 2 diabetes | 0.119 | 0.0393 | 0.00249 | Wald ratio | 1 | cis | NA |
| Schizophrenia | -0.0885 | 0.0294 | 0.00258 | Wald ratio | 1 | cis | NA |
| Hearing difficulty or problems: Yes | 0.0312 | 0.0108 | 0.00392 | Wald ratio | 1 | cis | NA |
| Happiness | -0.0218 | 0.00799 | 0.00646 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: anxiety or panic attacks | -0.177 | 0.0668 | 0.00813 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: uterine fibroids | 0.122 | 0.0463 | 0.00836 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: G47 Sleep disorders | -0.286 | 0.114 | 0.012 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: depression | -0.0682 | 0.0285 | 0.0168 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Other bones | 0.0629 | 0.0264 | 0.0173 | Wald ratio | 1 | cis | NA |
| Serum cystatin C (eGFRcys) | -0.012 | 0.0053 | 0.0233 | Wald ratio | 1 | cis | NA |
| _...and 107 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_No GWAS Catalog associations mapped to this gene._

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 634 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| type 2 diabetes mellitus | 0.573 | — | common-variant locus | no MR -> candidate analysis |
| acne | 0.529 | — | common-variant locus | no MR -> candidate analysis |
| myeloid leukemia | 0.505 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of skin pigmentation | 0.473 | — | common-variant locus | no MR -> candidate analysis |
| hypothyroidism | 0.45 | — | common-variant locus | MR: beta=-0.144, p=1.43e-05 (cis) |
| myxedema | 0.386 | — | common-variant locus | no MR -> candidate analysis |
| atrial fibrillation | 0.356 | — | common-variant locus | no MR -> candidate analysis |
| ACPA-positive rheumatoid arthritis | 0.283 | — | common-variant locus | no MR -> candidate analysis |
| hemorrhagic disease | 0.273 | — | common-variant locus | no MR -> candidate analysis |
| hyperlipidemia | 0.254 | — | common-variant locus | no MR -> candidate analysis |
| Hypercholesterolemia | 0.252 | — | common-variant locus | MR: beta=-0.0188, p=0.176 (cis) |
| metabolic disease | 0.249 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.237 | — | common-variant locus | no MR -> candidate analysis |
| diabetes mellitus | 0.212 | — | common-variant locus | no MR -> candidate analysis |
| thrombocytopenia 4 | 0.207 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **13 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=2e-10, LOEUF=1.41 — LoF-tolerant |
| GWAS Catalog | 104 unique SNPs / 232 rows |
| ClinVar | 88 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 634 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'TIMP4'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 88 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — No GWAS Catalog associations mapped to this gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q99727 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000157150/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/TIMP4 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/TIMP4 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=TIMP4%5Bgene%5D — _ClinVar build Build260809-1055.1_

## Provenance

- Generated: 2026-08-14T05:22:09  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
