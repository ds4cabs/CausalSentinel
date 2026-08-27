# Archived cards — frozen historical outputs

**The current cards live one level up.** Everything here is a *frozen exhibit*: the exact
output an earlier version produced, kept byte-identical so version-to-version comparison
stays honest. Do not edit these files.

The yardstick for every upgrade in this project is **identical input, compared output**.
These folders are what makes that checkable rather than asserted.

| Version | One line | Read |
|---|---|---|
| [`v0.1_2026-07-13/`](v0.1_2026-07-13/) | MR was a placeholder and the model wrote the entire card | [what it got wrong](v0.1_2026-07-13/README.md) |
| [`v0.2_2026-08-14/`](v0.2_2026-08-14/) | The model stops writing the card; MR becomes real retrieval; the validator can fail a run | [why these four](v0.2_2026-08-14/README.md) |
| *current* | Tissue-resolved eQTLs, instrument provenance, and a mechanism class for sign inversion | [`../`](..) and [CHANGELOG](../../CHANGELOG.md) |

## Conventions

- **Folder name = version + date** (`v0.2_2026-08-14`). **File names never change**, so a
  card's identity is stable across versions.
- Archived files are **byte-identical to git history** — verify with
  `git show <commit>:cards/<file>`.
- **Only exhibits the documentation points at are archived.** Everything else is in git
  and does not need a copy. The current version is never archived; it is one level up.
- Each version folder carries a `README.md` saying what that version was, what it got
  wrong, and where each defect was fixed.
