# Prompt 06: clarity pass over the code (class session)

**From:** Flo (Foreman) **To:** the instructor's classroom session (Claude Code, Windows, working in this repo) **Date:** 2026-11-09
**Read first, in this order:** `AGENTS.md`, `DESIGN.md`, `sidecar/README.md`, then `sidecar/reports/` (01, 02, 03, 04). That is the whole history; it is short.

## Where this stands
Built and merged to `main`: the classes (`src/sortsearch/`), the experiment (`results/*.csv`), 19 plots (`docs/plots/`), and `BIG_O.md` with its number checker. 79 tests pass. Another builder is making the home page and LaTeX report right now (`docs/index.html`, `report/`, `scripts/check_site.py`, `README.md` link, branch `anna/05-home-page`): **do not touch those files.**

## Your task: a read-through for clarity, no behavior change
This repository is a showcase of well-formed classes and clean inheritance, read by beginners. Your job is the last pass a careful teacher would make over `src/` and `tests/`.

1. Read every file under `src/sortsearch/` and `tests/` as a first-year student would. For each file note anything a beginner would trip on: a vague name, a missing or wrong docstring, a comment that explains *what* when the code should say it, dead code, an unneeded import, a function doing two jobs, an inconsistency between sibling classes (for example, bubble and selection laying out their loops differently for no reason).
2. Fix what is small and safe: names, docstrings, comments, dead code, import order, consistent layout between sibling classes. **Behavior must not change.** Counts must come out identical.
3. Write down, without changing, anything that would change behavior or the design (put these in the report under "Proposed, not done"). Likely one: the `n/2 reference` line on the searching plot sits below linear search because half the targets are absent (measured about 3n/4); propose a clearer label, don't change the plotter's numbers.
4. Make sure `DESIGN.md` still describes what the code does. If it doesn't, list the lines that are out of date in the report (do not rewrite the design).

## Constraints
- `AGENTS.md` applies. Branch `class/06-clarity-pass` off `origin/main`; commit small; push your branch; do not push to `main`; do not merge.
- You are on Windows. Python: use `py` or `python` as installed (3.9 or newer). Run tests with `python -m pytest`. Line endings stay LF (`.gitattributes` enforces it); if `git diff` shows whole files changed, stop and report; do not commit it.
- Do not touch `results/`, `docs/`, `scripts/` or `BIG_O.md`. Do not edit any test's expected numbers.
- Public repo: no secrets, usernames, or personal paths in any file or commit message.

## Acceptance test
1. `python -m pytest -q` passes before you start (record the count) and after (same count, all pass).
2. `python scripts/run_experiment.py` writes `results/*.csv` with the **same sha256** as before you started (run it, hash, make your changes, run again, hash; then `git checkout results/` so the committed results are untouched).
3. `git diff --stat origin/main` shows only files under `src/` and `tests/` (and `sidecar/reports/`).
4. `git status --short` is clean and the branch is pushed.

## Report
`sidecar/reports/06_clarity_pass_report.md`: what you changed (grouped by file), what you left and why ("Proposed, not done"), commands with output, the two sha256 listings, the final commit hash, and one honest sentence on what was hardest to make clear. Terminal state COMPLETE / HUMAN_GATE / FAILED. Do not mark your own work accepted. Standard: done enough to talk about.
