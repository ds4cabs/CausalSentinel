# Protein Dossier — NDC80 (Kinetochore protein NDC80 homolog)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: M72 Fibroblastic disorders | 0.378 | 0.125 | 0.00248 | Wald ratio | 1 | trans | NA |
| Eye problems or disorders: Glaucoma | 0.246 | 0.0865 | 0.00443 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: retinal detachment | 0.43 | 0.154 | 0.00512 | Wald ratio | 1 | trans | NA |
| Neuroticism | 0.043 | 0.0172 | 0.0124 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: hypertension | 0.0522 | 0.0213 | 0.0142 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: depression | 0.115 | 0.0485 | 0.0178 | Wald ratio | 1 | trans | NA |
| Sodium in urine | 0.0297 | 0.013 | 0.0217 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: R11 Nausea and vomiting | 0.346 | 0.153 | 0.0234 | Wald ratio | 1 | trans | NA |
| Squamous cell lung cancer | -0.308 | 0.137 | 0.0245 | Wald ratio | 1 | trans | NA |
| Non-cancer illness code  self-reported: migraine | 0.148 | 0.0659 | 0.0248 | Wald ratio | 1 | trans | NA |
| Intracranial volume | -2.29e+04 | 1.03e+04 | 0.0256 | Wald ratio | 1 | trans | NA |
| Diagnoses - main ICD10: I80 Phlebitis and thrombophlebitis | 0.318 | 0.144 | 0.0267 | Wald ratio | 1 | trans | NA |
| _...and 78 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_4 association rows across 4 traits (0 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Tinnitus | 5e-7 | rs145362852 | 1 | GCST90267564 | no MR -> candidate analysis |
| PR interval in Tripanosoma cruzi seropositivity | 2e-6 | rs182046301 | 1 | GCST002279 | no MR -> candidate analysis |
| Vaginal microbiome relative abundance (s_Aerococcus christen | 4e-6 | rs78805937 | 1 | GCST90027005 | no MR -> candidate analysis |
| Plasma neurofilament light levels | 6e-6 | rs764064487 | 1 | GCST90837205 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 197 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| alcohol drinking | 0.525 | — | common-variant locus | no MR -> candidate analysis |
| bronchial disorder | 0.348 | — | common-variant locus | no MR -> candidate analysis |
| Abnormality of the skeletal system | 0.346 | — | common-variant locus | no MR -> candidate analysis |
| Tietze syndrome | 0.337 | — | common-variant locus | no MR -> candidate analysis |
| heart conduction disease | 0.335 | — | common-variant locus | no MR -> candidate analysis |
| hemorrhage | 0.335 | — | common-variant locus | no MR -> candidate analysis |
| gastric ulcer | 0.335 | — | common-variant locus | no MR -> candidate analysis |
| ulcerative colitis | 0.332 | — | common-variant locus | no MR -> candidate analysis |
| neuroendocrine neoplasm | 0.332 | — | common-variant locus | no MR -> candidate analysis |
| nerve plexus disorder | 0.332 | — | common-variant locus | no MR -> candidate analysis |
| pneumonitis | 0.332 | — | common-variant locus | no MR -> candidate analysis |
| ovarian neoplasm | 0.332 | — | common-variant locus | no MR -> candidate analysis |
| aortic disorder | 0.332 | — | common-variant locus | no MR -> candidate analysis |
| chronic ulcer of skin | 0.332 | — | common-variant locus | no MR -> candidate analysis |
| placental abruption | 0.332 | — | common-variant locus | no MR -> candidate analysis |

> Of the 15 rows above, **15 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Kinetochore protein NDC80 homolog) |
| gnomAD constraint | pLI=2e-18, LOEUF=0.944 — LoF-tolerant |
| GWAS Catalog | 22 unique SNPs / 44 rows |
| ClinVar | 224 records; 3 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 197 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'NDC80' and resolved to 'Kinetochore protein NDC80 homolog' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 224 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 4 of 4 traits by best p-value, aggregated from 4 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/O14777 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000080986/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL5660/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/NDC80 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/NDC80 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=NDC80%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/NDC80 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T03:57:09  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
