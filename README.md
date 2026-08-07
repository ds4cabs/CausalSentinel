# CausalSentinel

[![CABS: ds4cabs](https://img.shields.io/badge/CABS-ds4cabs-1f4b99?logo=github)](https://github.com/ds4cabs)
[![GitHub Pages: live](https://img.shields.io/badge/GitHub_Pages-live-brightgreen?logo=github)](https://ds4cabs.github.io/CausalSentinel/)
![CABS: 2026](https://img.shields.io/badge/CABS-2026-6f42c1)
![status: MVP in progress](https://img.shields.io/badge/status-MVP_in_progress-f1c40f)
![type: Dossier Generator](https://img.shields.io/badge/type-Dossier_Generator-1f6feb)
![domain: Causal Inference](https://img.shields.io/badge/domain-Causal_Inference-0aa)

**Interns:** Shucheng Cao (CausalSentinel core), Natalie Huang (OpenSentinel sub-project)
**Project Type:** Dossier Generator

## Overview
Give it a protein and a disease. It decides which public databases to query, queries them,
and writes one **target evidence card**: a short, sourced argument ending in a go / no-go,
where every number is traceable to the tool that returned it.

The hard part is not fetching from eight databases. It is making the output something a
reviewer can *falsify* — so the design puts the model where it can do least damage:

| | Written by |
|---|---|
| Evidence table, caveats, sources, provenance | **rendered mechanically from tool output** — the model never touches them |
| Verdict line + reasoning paragraph | the model — then **checked against tool output**, and the run fails if a claim has no source |

## What it does and does not do

- **It retrieves published Mendelian randomization estimates** (EpiGraphDB pQTL resource,
  Zheng et al. *Nat Genet* 2020) — beta, se, p, method, cis/trans instrument, Steiger
  direction, colocalization probability where available.
- **It does not compute MR or colocalization.** No instrument selection, no harmonisation.
  Every estimate is labelled `computed_here: false`.
- **Coverage is partial and the card says so.** Proteins with no plasma pQTL instrument
  return "not available" — which means *no estimate*, not *no effect*.
- **Where no GWAS was ever run, no agent can help.** That data still has to be generated
  by a human. This is the line between a tool and the science.

## Core tools (8, all live)

| Tool | Source | Answers |
|---|---|---|
| `get_mr_result` | EpiGraphDB pQTL MR | is there a *published* causal estimate for this protein → disease? |
| `get_target_disease_evidence` | Open Targets | how strongly is this target associated with this disease? |
| `get_uniprot_dossier` | UniProt | what is this protein and where does it act? |
| `get_chembl_modulators` | ChEMBL | is it already druggable, and by what? |
| `get_clinvar_variants` | ClinVar (NCBI) | are there clinically classified variants? |
| `get_gnomad_constraint` | gnomAD | is it LoF-intolerant — i.e. a *safety warning*? |
| `get_gwas_catalog` | GWAS Catalog | how much genetic signal maps to the locus? |
| `get_pharmgkb_drug_gene` | PharmGKB / ClinPGx | any pharmacogenomic relationships? |

Each tool reports its `source_release` (UniProt release, ClinVar build, ChEMBL version,
Open Targets data release, EpiGraphDB build), so a card is reproducible rather than merely
timestamped.

## Tech Stack
Python, **`google-genai`** (Gemini SDK; the older `google-generativeai` is deprecated),
requests, python-dotenv.

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
python tools\mr.py                 # PCSK9, IL6R, PNPLA3 — including an honest "no estimate"

# 4) run the agent on one pair -> writes a card to cards/
python agent.py --protein PCSK9 --disease "high cholesterol"

# 5) or run the benchmark set (10 pairs chosen to exercise different branches)
python agent.py --batch pairs_benchmark.txt

# 6) validator regression tests (19 cases, no network, no key)
python test_validator.py
```

Output: `cards/PCSK9_high-cholesterol_evidence_card.md` (+ `.json`). The `.json` carries
the **full tool ledger** — every call, its arguments and its verbatim return — so any card
can be re-derived and diffed. *The JSON is the record; the markdown is the readable view.*

### Architecture

```
agent.py          orchestrates: wrap tools -> model calls them -> render -> validate
  ledger.py       captures every tool call's arguments and verbatim return value
  render.py       builds table + caveats + sources + provenance FROM the ledger
  validate_card.py  fails the run if the model's prose outruns the ledger
  tools/*.py      one database wrapper each; one public function returning a dict
  system_prompt.md  the agent's rules
```

Gemini's automatic function calling normally executes tools *inside* the SDK, so the caller
never sees what came back and the card is whatever the model remembers. `ledger.py` wraps
each tool so the return values survive — which is what makes deterministic rendering and
validation possible at all.

### What the validator catches

Fabricated numbers (compared **numerically**, tolerant of honest rounding and of "over N" /
"nearly N" bounds), fabricated rsIDs and accessions, unsupported qualitative claims
("FDA-approved", "monoclonal antibody", "small-molecule"), **causal language when the MR
tool returned no estimate**, and any claim that this agent performed MR itself.

On the 10-pair benchmark it currently rejects 3 cards — each for a real defect, not a false
alarm. Run `test_validator.py` after any change to it.

## OpenSentinel (Natalie Huang)

A companion, beginner-scoped sub-project in this repo: a **drug-comparison agent**.
Given two drug names, it pulls molecular properties (PubChem) and adverse-event data
(openFDA FAERS), then uses Gemini to summarize the key differences in a Streamlit UI —
a fast, sourced answer to "how do these two drugs actually differ?"

Full scope, timeline, and stretch goals: [`MVP_Natalie.md`](MVP_Natalie.md).
Tracking issue: [#10](https://github.com/ds4cabs/CausalSentinel/issues/10).

## Notes
This project is the cohort's causal evidence reference implementation with strong
variant-level rigor. Built in rounds (each ships); Round 1 = a 3-tool card end to end.
