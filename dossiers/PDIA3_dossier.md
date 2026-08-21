# Protein Dossier — PDIA3 (Protein disulfide-isomerase A3)

**MR feasibility tier: A** — Published pQTL-MR estimates exist for this protein (retrieved below - not computed here).

## 1. Published MR estimates (retrieved, not computed)

| Outcome | beta | se | p | method | nSNP | cis/trans | coloc |
|---|---|---|---|---|---|---|---|
| Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.176 | 0.0423 | 3.20e-05 | Wald ratio | 1 | cis | NA |
| ER-positive Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.168 | 0.0505 | 8.79e-04 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K43 Ventral hernia | 0.512 | 0.156 | 0.00105 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: diverticular disease or diverticulitis | 0.367 | 0.112 | 0.00106 | Wald ratio | 1 | cis | NA |
| PGC cross-disorder traits | 0.245 | 0.0814 | 0.00258 | Wald ratio | 1 | cis | NA |
| Alcohol intake frequency | 0.0739 | 0.0249 | 0.00302 | Wald ratio | 1 | cis | NA |
| Schizophrenia | 0.205 | 0.0716 | 0.00429 | Wald ratio | 1 | cis | NA |
| ER-negative Breast cancer (Combined Oncoarray; iCOGS; GWAS meta analysis) | 0.209 | 0.0778 | 0.00732 | Wald ratio | 1 | cis | NA |
| Thyroid cancer | -1.48 | 0.553 | 0.00733 | Wald ratio | 1 | cis | NA |
| Diagnoses - main ICD10: K20 Oesophagitis | 0.318 | 0.126 | 0.0119 | Wald ratio | 1 | cis | NA |
| Non-cancer illness code  self-reported: anxiety or panic attacks | 0.278 | 0.112 | 0.013 | Wald ratio | 1 | cis | NA |
| Happiness | 0.05 | 0.0209 | 0.0166 | Wald ratio | 1 | cis | NA |
| _...and 103 more outcomes (see JSON)_ | | | | | | | |

## 2. pQTL instrument availability (Tier-B probe)

| Dataset | Trait | Author | Year |
|---|---|---|---|
| `prot-c-4719_58_2` | Protein disulfide isomerase A3 | Suhre K | 2019 |

## 3. GWAS Catalog results — traits with signal at this locus

_11 association rows across 11 traits (10 genome-wide significant rows). **Associations are loci, not causal claims**; the mapped gene at a locus is not necessarily the effector gene._

| Trait | best p | lead SNP | n assoc | study | MR status |
|---|---|---|---|---|---|
| Self-reported math ability (MTAG) | 1e-9 | rs3087657 | 1 | GCST006569 | no MR -> candidate analysis |
| Free cholesterol in IDL | 1e-9 | rs117519814 | 1 | GCST90827783 | no MR -> candidate analysis |
| Free cholesterol levels in IDL | 3e-9 | rs117519814 | 1 | GCST90092835 | no MR -> candidate analysis |
| Free cholesterol levels in large LDL | 4e-9 | rs117519814 | 1 | GCST90092860 | no MR -> candidate analysis |
| Cholesterol in IDL | 5e-9 | rs117519814 | 1 | GCST90827778 | no MR -> candidate analysis |
| Cholesterol levels in IDL | 1e-8 | rs117519814 | 1 | GCST90092831 | no MR -> candidate analysis |
| Free cholesterol in large LDL | 1e-8 | rs117519814 | 1 | GCST90827814 | no MR -> candidate analysis |
| Cholesteryl ester levels in IDL | 2e-8 | rs117519814 | 1 | GCST90092833 | no MR -> candidate analysis |
| Free cholesterol levels in LDL | 2e-8 | rs117519814 | 1 | GCST90092885 | no MR -> candidate analysis |
| Cholesteryl Esters in IDL | 2e-8 | rs117519814 | 1 | GCST90827780 | no MR -> candidate analysis |
| Aerodigestive squamous cell cancer (pleiotropy) | 4e-6 | rs8040336 | 1 | GCST012213 | no MR -> candidate analysis |

## 4. Phenome map — where this gene is a genetic locus, vs. where MR exists

_Top diseases by Open Targets association (of 384 total). **Associations are loci, not causal claims.** The causal-status column is a four-state triage per pair: **established (curated)** = a curated clinical assertion exists (ClinGen/G2P/GEL/Orphanet/ClinVar — any validity level, MR adds little); **exploratory rare-variant signal** = ExWAS burden evidence without curation — a candidate NEW gene-disease relationship; **common-variant locus** = GWAS signal, classic pQTL-MR territory; **multi-layer** = burden+GWAS together, an allelic-series candidate (the strongest causal setup). Burden estimand is carrier-vs-noncarrier, not per-SD MR._

| Disease | genetic assoc. | burden (ExWAS) | causal status | MR status |
|---|---|---|---|---|
| Intellectual disability | 0.426 | — | established (curated) | no MR -> candidate analysis |
| cancer | 0.299 | — | common-variant locus | MR: beta=0.176, p=3.20e-05 (cis) |
| autoimmune thyroid disease | 0.3 | — | common-variant locus | no MR -> candidate analysis |
| celiac disease | 0.3 | — | common-variant locus | no MR -> candidate analysis |
| mathematical ability | 0.287 | — | common-variant locus | no MR -> candidate analysis |
| type 2 diabetes mellitus | 0.233 | — | common-variant locus | no MR -> candidate analysis |
| diabetes mellitus | 0.214 | — | common-variant locus | no MR -> candidate analysis |

> Of the 7 rows above, **6 have no MR estimate in this resource**. Across all retrieved diseases for this gene: 0 exploratory rare-variant signal(s), 0 multi-layer (allelic-series candidate) pair(s). Final triage still belongs to a statistical geneticist.

## 5. Downstream annotation (druggability & safety preview)

| Layer | Result |
|---|---|
| ChEMBL druggability | 0 known modulators (Protein disulfide-isomerase A3) |
| gnomAD constraint | pLI=1, LOEUF=0.427 — LoF-INTOLERANT |
| GWAS Catalog | 30 unique SNPs / 60 rows |
| ClinVar | 125 records; 0 pathogenic in sample of 30 |
| PharmGKB/ClinPGx | no annotations |

## Caveats declared by the tools

- **`phenome`** — Top 30 of 384 associated diseases by overall score. genetic_association aggregates GWAS common-variant AND rare-variant evidence. These are ASSOCIATIONS (loci), not causal claims.
- **`chembl`** — ChEMBL target matched by text search on 'PDIA3' and resolved to 'Protein disulfide-isomerase A3' — confirm this is the intended target.
- **`clinvar`** — Pathogenic count is over the 30 record(s) retrieved, NOT over all 125 ClinVar records for this gene; it is a sample, not a rate.
- **`pharmgkb`** — No PharmGKB/ClinPGx clinical annotations (gene may not be a pharmacogene).
- **`gwas_traits`** — Top 11 of 11 traits by best p-value, aggregated from 11 association rows. These are GWAS ASSOCIATIONS (loci), not causal claims; mapped genes at a locus are not necessarily the effector gene.

## Sources

- `uniprot`: https://www.uniprot.org/uniprotkb/P30101 — _UniProt release 2026_02 (10-June-2026)_
- `mr_outcomes`: https://epigraphdb.org/pqtl/ — _EpiGraphDB pQTL MR (Zheng et al., Nat Genet 2020) — pre-computed two-sample MR; retrieved, not computed by this agent; EpiGraphDB build 1.0, pQTL dataset v3.0_
- `phenome`: https://platform.opentargets.org/target/ENSG00000167004/associations — _Open Targets data release 26.06_
- `chembl`: https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL4296001/ — _ChEMBL_37 (released 2026-05-01)_
- `gnomad`: https://gnomad.broadinstitute.org/gene/PDIA3 — _gnomAD constraint via GraphQL API (reference genome GRCh38)_
- `gwas`: https://www.ebi.ac.uk/gwas/genes/PDIA3 — _GWAS Catalog REST (live; release not exposed by this endpoint)_
- `clinvar`: https://www.ncbi.nlm.nih.gov/clinvar/?term=PDIA3%5Bgene%5D — _ClinVar build Build260809-1055.1_
- `gwas_traits`: https://www.ebi.ac.uk/gwas/genes/PDIA3 — _GWAS Catalog search API (live; release not exposed)_

## Provenance

- Generated: 2026-08-14T04:15:59  ·  Tier: A
- Fully mechanical: every cell above is rendered from tool return values. No language model wrote any part of this dossier.
- MR estimates, where present, are retrieved from published work (EpiGraphDB pQTL, Zheng et al. Nat Genet 2020); nothing is computed here.
- Tool errors this run: none
