# CausalSentinel

[![CABS: ds4cabs](https://img.shields.io/badge/CABS-ds4cabs-1f4b99?logo=github)](https://github.com/ds4cabs)
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
Python, **`google-genai`** (Gemini SDK; the older `google-generativeai` is deprecated),
requests, python-dotenv, DuckDB (Round 3), matplotlib (Round 3).

## Getting Started (Round 1)

**Prerequisites:** Python 3.10+, and a free Gemini API key in `../.env` as `GEMINI_API_KEY`
(see `.env.example`). The `.env` file lives one level up and is never committed.

```bash
# 1) create and activate an isolated environment
python -m venv .venv
.venv\Scripts\activate            # Windows  (macOS/Linux: source .venv/bin/activate)

# 2) install dependencies
pip install -r requirements.txt

# 3) test a single tool on its own (no Gemini key needed)
python tools\uniprot.py

# 4) run the full agent -> writes a card to cards/
python agent.py --protein PNPLA3 --disease MASLD
```

Output: `cards/PNPLA3_MASLD_causal_card.md` (+ `.json`).

**Architecture.** `agent.py` reads `system_prompt.md`, registers the tools in `tools/`
with Gemini, and runs automatic function calling: the model decides which tools to call,
the SDK executes them, and the model synthesizes one cited causal card.

**Tools (Round 1):** `get_uniprot_dossier` (UniProt), `get_target_disease_evidence`
(Open Targets), `get_chembl_modulators` (ChEMBL), and a stubbed `get_mr_result`
(real Mendelian randomization from R -> DuckDB lands in Round 3).

## Notes
This project is the cohort's causal evidence reference implementation with strong
variant-level rigor. Built in rounds (each ships); Round 1 = a 3-tool card end to end.
