# Protein Dossier — RNPEP (Aminopeptidase B)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Diagnoses - main ICD10: I80 Phlebitis and thrombophlebitis | 0.26 | 0.0828 | 0.0017 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: R10 Abdominal and pelvic pain | -0.12 | 0.0397 | 0.00245 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: polio  or  poliomyelitis | 0.513 | 0.173 | 0.00292 | Wald ratio | 1 | cis | NA |
| Knee osteoarthritis | -0.257 | 0.0876 | 0.00337 | Wald ratio | 1 | cis | NA |
| Knee and hip osteoarthritis | -0.182 | 0.0637 | 0.00421 | Wald ratio | 1 | cis | NA |
| Neo-extraversion | 0.649 | 0.237 | 0.00615 | Wald ratio | 1 | cis | NA |
| Eye problems or disorders: Glaucoma | 0.132 | 0.0535 | 0.0136 | Wald ratio | 1 | cis | NA |
| Paget's disease | -0.415 | 0.176 | 0.0184 | Wald ratio | 1 | cis | NA |
| Height | 0.0202 | 0.00889 | 0.023 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hayfever or allergic rhinitis | 0.0636 | 0.0281 | 0.0236 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: hiatus hernia | -0.122 | 0.0541 | 0.0248 | Wald ratio | 1 | cis | NA |
| Fasting proinsulin | -0.0458 | 0.0208 | 0.0273 | Wald ratio | 1 | cis | NA |
| _...and 110 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

_No prot-* pQTL GWAS dataset found for this protein (matched by UniProt accession and symbol)._

## 3. GWAS Catalog results — traits with signal at this locus

_23 association rows across 18 traits (20 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Urine X-10457 levels in chronic kidney disease | 5e-162 | rs16849483 | 1 | GCST90266149 | no MR -> candidate analysis |
| Aminopeptidase B levels | 7e-122 | rs11810017 | 3 | GCST90246493 | no MR -> candidate analysis |
| BCHE protein levels | 2e-84 | rs12059693 | 1 | GCST90468429 | no MR -> candidate analysis |
| Serum levels of protein RNPEP | 2e-69 | rs4630172 | 4 | GCST90086949 | no MR -> candidate analysis |
| Urinary metabolite levels in chronic kidney disease | 1e-56 | rs56768485 | 1 | GCST009733 | no MR -> candidate analysis |
| Blood protein levels | 4e-42 | rs59698324 | 1 | GCST006585 | no MR -> candidate analysis |
| Cholinesterase levels | 1e-17 | rs56768485 | 1 | GCST90247015 | no MR -> candidate analysis |
| Butyrylcholinesterase levels | 9e-16 | rs4950806 | 1 | GCST001207 | no MR -> candidate analysis |
| Cerebrospinal fluid metabolite X-10457 levels | 1e-15 | rs16849483 | 1 | GCST90318292 | no MR -> candidate analysis |
| Metabolite peak levels (QI8492) | 1e-15 | rs28419585 | 1 | GCST90178387 | no MR -> candidate analysis |
| Aminopeptidase B level in Chronic kidney disease with hypert | 1e-12 | rs3820439 | 1 | GCST90233427 | no MR -> candidate analysis |
| Plasma prolylglycine levels in chronic kidney disease | 2e-11 | rs6691690 | 1 | GCST90265874 | no MR -> candidate analysis |
| _...and 6 more traits (see JSON)_ | | | | | |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 122 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| obstructive sleep apnea syndrome | 0.434 | — | common-variant locus | no MR -> candidate analysis |
| external ear disorder | 0.334 | — | common-variant locus | no MR -> candidate analysis |

> Of the 2 rows above, **2 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Aminopeptidase B) |
| gnomAD constraint | pLI=3e-16, LOEUF=1.01 — LoF-tolerant |
| GWAS Catalog | 73 unique SNPs / 146 rows |
| ClinVar | 138 records; 2 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 122 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'RNPEP' and resolved to 'Aminopeptidase B' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 138 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 18 of 18 traits by best p-value, aggregated from 23 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/Q9H4A4 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000176393/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2432/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/RNPEP — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/RNPEP — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=RNPEP%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/RNPEP — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:51:55  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
