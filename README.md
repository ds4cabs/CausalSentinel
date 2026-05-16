# CausalSentinel

[![GitHub Pages: live](https://img.shields.io/badge/GitHub_Pages-live-brightgreen?logo=github)](https://ds4cabs.github.io/CausalSentinel/)
![CABS: 2026](https://img.shields.io/badge/CABS-2026-6f42c1)
![status: MVP in progress](https://img.shields.io/badge/status-MVP_in_progress-f1c40f)
![type: Dossier Generator](https://img.shields.io/badge/type-Dossier_Generator-1f6feb)
![domain: Causal Inference](https://img.shields.io/badge/domain-Causal_Inference-0aa)

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
