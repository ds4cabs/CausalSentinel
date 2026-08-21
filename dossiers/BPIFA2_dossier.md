# Protein Dossier — BPIFA2 (BPI fold-containing family A member 2)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Non-cancer illness code  self-reported: mania or bipolar disorder or manic depression | 0.669 | 0.18 | 1.97e-04 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: N40 Hyperplasia of prostate | 0.386 | 0.124 | 0.00184 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R04 Haemorrhage from respiratory passages | 0.47 | 0.154 | 0.00224 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K60 Fissure and fistula of anal and rectal regions | 0.472 | 0.164 | 0.00405 | Wald ratio | 1 | cis | NA |
| Cancer code  self-reported: prostate cancer | 0.376 | 0.142 | 0.00795 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: L03 Cellulitis | 0.342 | 0.139 | 0.0142 | Wald ratio | 1 | cis | NA |
| ER-positive Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.134 | 0.0599 | 0.0255 | Wald ratio | 1 | cis | NA |
| Fracture resulting from simple fall | 0.0894 | 0.0417 | 0.0322 | Wald ratio | 1 | cis | NA |
| Creatinine (enzymatic) in urine | -0.0349 | 0.0165 | 0.0342 | Wald ratio | 1 | cis | NA |
| Systolic blood pressure  automated reading | 0.0359 | 0.0176 | 0.0409 | Wald ratio | 1 | cis | NA |
| Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | -0.103 | 0.0506 | 0.0412 | Wald ratio | 1 | cis | NA |
| Fractured bone site(s): Wrist | 0.177 | 0.104 | 0.0897 | Wald ratio | 1 | cis | NA |
| _...and 39 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_24 association rows across 16 traits (20 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Hair color | 1e-300 | rs117186940 | 1 | GCST007082 | no MR -> candidate analysis |
| BPIFB1 protein levels | 3e-140 | rs542213402 | 5 | GCST90468462 | no MR -> candidate analysis |
| Low tan response | 3e-104 | rs117186940 | 1 | GCST005897 | no MR -> candidate analysis |
| BPIFA2 protein levels | 1e-98 | rs6059134 | 4 | GCST90468461 | no MR -> candidate analysis |
| BPIFB2 protein levels | 4e-92 | rs13045604 | 2 | GCST90468463 | no MR -> candidate analysis |
| Hematological traits (multi-trait analysis) | 5e-16 | rs117186940 | 1 | GCST90838669 | no MR -> candidate analysis |
| BPI fold-containing family B member 1 levels | 4e-15 | rs76549422 | 1 | GCST90246734 | no MR -> candidate analysis |
| Height (baseline) | 6e-15 | rs117186940 | 1 | GCST90565843 | no MR -> candidate analysis |
| BPI fold-containing family A member 2 level in Chronic kidne | 9e-14 | rs6059143 | 1 | GCST90238042 | no MR -> candidate analysis |
| Mean corpuscular hemoglobin | 1e-12 | rs117186940 | 1 | GCST90002390 | no MR -> candidate analysis |
| Physical function (baseline) | 1e-10 | rs117052155 | 1 | GCST90565837 | no MR -> candidate analysis |
| Blood protein levels | 2e-8 | rs141715080 | 1 | GCST006585 | no MR -> candidate analysis |
| _...and 4 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 65 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| skin cancer | 0.459 | — | common-variant locus | no MR -> candidate analysis |
| cutaneous melanoma | 0.459 | — | common-variant locus | no MR -> candidate analysis |
| skin neoplasm | 0.459 | — | common-variant locus | no MR -> candidate analysis |
| Hashimoto thyroiditis | 0.06 | — | common-variant locus | no MR -> candidate analysis |

> Of the 4 rows above, **4 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | pLI=3.6e-06, LOEUF=1.13 — LoF-tolerant |
| GWAS Catalog | 58 unique SNPs / 116 rows |
| ClinVar | 62 records; 1 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 65 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'BPIFA2'.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 62 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 16 of 16 traits by best p-value, aggregated from 24 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q96DR5 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000131050/associations — _Open Targets data release 26.06_
- `gnomad`: https://gnomad.broadinstitute.org/gene/BPIFA2 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/BPIFA2 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=BPIFA2%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/BPIFA2 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T01:18:22  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
