# Archived cards — frozen historical outputs

**Current cards live one level up.** Everything in this folder is a *frozen exhibit*:
the exact output an earlier version of the agent produced, kept byte-identical so any
version-to-version comparison stays honest. Do not edit these files.

| Folder | What it is | Why it is kept |
|---|---|---|
| `v0.1_2026-07-13/` | The first card the Round-1+2 agent ever produced (PNPLA3 × MASLD), written entirely by the model | The "before" exhibit for every comparison in CHANGELOG.md: the MR row is a declared stub, the GWAS count reads "51 unique SNPs" (the tool had returned 52 and the true, pagination-fixed count is 114), and there is no caveat block, no provenance, no source versions. Same input under the current version: `../PNPLA3_MASLD_evidence_card.md` |

Conventions:
- **Folder name = version + date** (`v0.1_2026-07-13`); **file names are never changed**,
  so provenance stays obvious.
- Archived files are **byte-identical** to git history — verify anytime with
  `git show main:cards/PNPLA3_MASLD_causal_card.md`.
- Only milestone exhibits are archived here (artifacts the project's documentation
  points at). Everything else is retrievable from git and does not need a copy.
