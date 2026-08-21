# Protein Dossier — B3GALTL (Beta-1,3-glucosyltransferase)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Heel bone mineral density (BMD) T-score  automated | -0.0582 | 0.0133 | 1.24e-05 | Wald ratio | 1 | cis | NA |
| Pallidum volume | 28.6 | 8.4 | 6.58e-04 | Wald ratio | 1 | cis | NA |
| Sodium in urine | 0.0334 | 0.0101 | 9.85e-04 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hypertrophic cardiomyopathy (hcm  or  hocm) | 0.951 | 0.312 | 0.00226 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: retinal detachment | 0.378 | 0.125 | 0.00257 | Wald ratio | 1 | cis | NA |
| Diastolic blood pressure  automated reading | 0.0312 | 0.0105 | 0.00313 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R07 Pain in throat and chest | 0.119 | 0.0408 | 0.00355 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: depression | 0.109 | 0.0381 | 0.00428 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: I80 Phlebitis and thrombophlebitis | 0.302 | 0.113 | 0.00747 | Wald ratio | 1 | cis | NA |
| Neo-extraversion | 0.859 | 0.335 | 0.0104 | Wald ratio | 1 | cis | NA |
| ER-positive Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.0838 | 0.0327 | 0.0105 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: Z09 Follow-up examination after treatment for conditions other than malignant neoplasms | 0.177 | 0.0706 | 0.0124 | Wald ratio | 1 | cis | NA |
| _...and 106 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_No GWAS Catalog associations mapped to this gene._

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 2491 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Peters plus syndrome | 0.848 | — | established (curated) | no MR -> candidate analysis |
| hereditary disease | 0.801 | — | established (curated) | no MR -> candidate analysis |
| age-related macular degeneration | 0.738 | — | common-variant locus | no MR -> candidate analysis |
| major depressive disorder | 0.732 | — | common-variant locus | no MR -> candidate analysis |
| COVID-19 | 0.687 | — | common-variant locus | no MR -> candidate analysis |
| mathematical ability | 0.623 | — | common-variant locus | no MR -> candidate analysis |
| insomnia | 0.561 | — | common-variant locus | no MR -> candidate analysis |
| health study participation | 0.516 | — | common-variant locus | no MR -> candidate analysis |
| wet macular degeneration | 0.501 | — | common-variant locus | no MR -> candidate analysis |
| risk-taking behaviour | 0.501 | — | common-variant locus | no MR -> candidate analysis |
| atrophic macular degeneration | 0.501 | — | common-variant locus | no MR -> candidate analysis |
| arthropathy | 0.486 | — | common-variant locus | no MR -> candidate analysis |
| Vertigo | 0.486 | — | common-variant locus | no MR -> candidate analysis |
| type 2 diabetes mellitus | 0.48 | — | common-variant locus | no MR -> candidate analysis |
| mental disorder | 0.475 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **15 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | **not available** — no ChEMBL target (undrugged) |
| gnomAD constraint | not available |
| GWAS Catalog | 1 unique SNPs / 1 rows |
| ClinVar | no records |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 2491 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — No ChEMBL target for 'B3GALTL'.
- **`gnomad`** — No gnomAD constraint data.
- **`clinvar`** — No ClinVar records.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — No GWAS Catalog associations mapped to this gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q6Y288 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000187676/associations — _Open Targets data release 26.06_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/B3GALTL — _GWAS Catalog REST (live; release not exposed by this endpoint)_

## Provenance

- Generated: 2026-08-14T01:13:51  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
