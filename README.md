# CausalSentinel

**Intern:** Shucheng Cao
**Project Type:** Dossier Generator

## Overview
CausalSentinel is a causal evidence engine that builds target-disease causal cards by combining genetic causality, protein dossiers, pharmacology, clinical variants, population constraint, and pharmacogenomics.

## Deliverable
- CLI causal card generator for protein + disease pairs
- Markdown dossier with causal verdict, MR evidence, colocalization, and safety context
- Output includes JSON metadata and plots for causal evidence

## Core Tools
- IEU OpenGWAS / pre-computed MR
- UniProt
- Open Targets
- ChEMBL
- ClinVar
- gnomAD
- GWAS Catalog
- PharmGKB

## Tech Stack
Python, `google-generativeai`, DuckDB, requests, pandas, matplotlib

## Notes
This project is the cohort’s causal evidence reference implementation with strong variant-level rigor.
