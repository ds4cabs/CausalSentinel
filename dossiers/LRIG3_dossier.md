# Protein Dossier — LRIG3 (Leucine-rich repeats and immunoglobulin-like domains protein 3)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: hypopituitarism | 0.903 | 0.316 | 0.00431 | Wald ratio | 1 | cis | NA |
| Hip osteoarthritis | -0.358 | 0.136 | 0.00834 | Wald ratio | 1 | cis | NA |
| Mean cell haemoglobin concentration | 0.0582 | 0.0221 | 0.00836 | Wald ratio | 1 | cis | NA |
| Cardioembolic stroke | 0.395 | 0.166 | 0.0173 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: bone disorder | 0.435 | 0.184 | 0.0182 | Wald ratio | 1 | cis | NA |
| Ischemic stroke | 0.191 | 0.0837 | 0.0228 | Wald ratio | 1 | cis | NA |
| Years of schooling | -0.0324 | 0.0151 | 0.0321 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Wrist | 0.158 | 0.0786 | 0.0439 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I48 Atrial fibrillation and flutter | 0.2 | 0.1 | 0.0465 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hayfever or allergic rhinitis | 0.0915 | 0.0482 | 0.0576 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: M16 Coxarthrosis [arthrosis of hip] | -0.252 | 0.14 | 0.073 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: S66 Injury of muscle and tendon at wrist and hand level | 0.401 | 0.228 | 0.0789 | Wald ratio | 1 | cis | NA |
| _...and 82 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-3322_52_2` | LRIG3 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_47 association rows across 37 traits (36 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Leucine-rich repeats and immunoglobulin-like domains protein | 9e-50 | rs144365133 | 4 | GCST90137846 | no MR -> candidate analysis |
| Serum levels of protein LRIG3 | 5e-29 | rs11172775 | 2 | GCST90088314 | no MR -> candidate analysis |
| LRIG3 protein levels | 3e-28 | rs17619704 | 1 | GCST90469795 | no MR -> candidate analysis |
| Blood protein levels | 2e-26 | rs76158750 | 1 | GCST006585 | no MR -> candidate analysis |
| Leucine-rich repeats and immunoglobulin-like domains protein | 9e-20 | rs144365133 | 1 | GCST90237314 | no MR -> candidate analysis |
| GLIPR1 protein levels | 9e-18 | rs138919132 | 1 | GCST90469357 | no MR -> candidate analysis |
| Osteoarthritis (with total hip replacement) | 5e-15 | rs17120227 | 2 | GCST90566802 | no MR -> candidate analysis |
| Leucine-rich repeats and immunoglobulin-like domains protein | 5e-14 | rs11172791 | 1 | GCST90241785 | no MR -> candidate analysis |
| INHBC protein levels | 3e-13 | rs117621242 | 1 | GCST90469615 | no MR -> candidate analysis |
| Osteoarthritis (hip) | 4e-13 | rs79056043 | 2 | GCST90566798 | MR: beta=-0.358, p=0.00834 (cis) |
| Physical function (baseline) | 7e-13 | rs990887 | 1 | GCST90565837 | no MR -> candidate analysis |
| Smoking initiation | 3e-12 | rs10877196 | 2 | GCST90243985 | no MR -> candidate analysis |
| _...and 25 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 558 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| osteoarthritis, hip | 0.761 | — | common-variant locus | MR: beta=-0.358, p=0.00834 (cis) |
| total hip arthroplasty | 0.686 | — | common-variant locus | no MR -> candidate analysis |
| smoking initiation | 0.652 | — | common-variant locus | no MR -> candidate analysis |
| esophageal disorder | 0.555 | — | common-variant locus | no MR -> candidate analysis |
| osteoarthritis | 0.548 | — | common-variant locus | MR: beta=-0.358, p=0.00834 (cis) |
| cholesteatoma of middle ear | 0.503 | — | common-variant locus | no MR -> candidate analysis |

> Of the 6 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=1.1e-16, LOEUF=0.804 — LoF-tolerant |
| GWAS Catalog | 33 unique SNPs / 65 rows |
| ClinVar | 174 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 558 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'LRIG3'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 174 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 20 of 37 traits by best p-value, aggregated from 47 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q6UXM1 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000139263/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/LRIG3 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/LRIG3 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=LRIG3%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/LRIG3 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:36:56  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
