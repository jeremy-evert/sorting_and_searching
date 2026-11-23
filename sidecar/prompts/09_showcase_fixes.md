# Prompt 09: make the showcase keep its promises

**From:** Jeremy (asked Anna directly, 2026-11-11) **To:** Anna **Follows:** `01` to `08`, and `TASKS.md`.

## Why
This repo is going to be shown to the Computer Science 2 class as a finished product with clean, refactored code, so students can think about what they want their own portfolios to look like. Anything the repo claims, it must deliver. If it promised something it cannot deliver, either deliver it or say plainly what it does.

## What to do
1. Make the code generate the plots and results from one command, and test that the promise holds.
2. Fix the claims in `README.md`, `BIG_O.md`, the home page and the report that `TASKS.md` marks as unchecked or overstated: the doubling-ratio definition, the quick-sort explanation (test it with more trials), what is counted, the search reference line (3n/4), alt text that describes what is drawn.
3. Check the numbers quoted in sentences, not only the tables.
4. Make `Sorter.sort` check that the output holds the same values as the input.
5. Add automated tests (CI) and the project's own checks to the repository.
6. Update `sidecar/DESIGN.md` and `AGENTS.md` where they disagree with the code.
7. Sweep the repository (files and history) for anything that should not be public, and report it. Do not rewrite history.

## Constraints
`AGENTS.md` applies. Own branch, nothing to `main`, stage files by name. No history rewrite, no branch deletion, no change to the license. Say "tests pass" only for tests run in this session.
