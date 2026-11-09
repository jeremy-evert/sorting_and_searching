# Prompt 04: Big O explained, and checked against our numbers

**From:** Flo (Foreman) **To:** Anna (builder) **Date:** 2026-11-09
**Follows:** `01` and `02` (merged to `main`; the real result CSVs are in `results/`). Runs in parallel with `03` (plots, Hanna). You do not need her plots; refer to them by their planned names only.

## Where
Repo `sorting_and_searching`. Branch `anna/04-big-o` off `origin/main`. Fresh worktree. Read `DESIGN.md` ("Expectations") and `AGENTS.md` first.

## Why
The point of the project is that a reader can see **theory and measurement agree**, and understand why. Big O is usually taught as a symbol to memorize. Here every claim about growth is a statement you can check against a file. A beginner should finish `BIG_O.md` able to say what "n squared" means in terms of what happens when the list doubles, and to point at a number that proves it. If a prediction and a measurement disagree, that is the interesting part: explain it, don't hide it.

## What to write
1. `BIG_O.md`, plain language, for a first-year student. In this order:
   - What Big O is: how the work grows as the input grows, ignoring constants. Use the **doubling question**: if the list gets twice as long, how much more work? Roughly 2x for n, 4x for n squared, a little over 2x for n log n, +1 step for log n.
   - What we count and why not seconds (point to `DESIGN.md`).
   - A table of the five sorters on the three input kinds: predicted growth, and the **measured doubling ratio** (comparisons at size 640 divided by comparisons at size 320), side by side.
   - A table for the three searchers: predicted growth and measured probes at sizes 320 and 640.
   - For every row where measurement and prediction **differ noticeably**, a short plain explanation. Expect at least these to need one: insertion sort on sorted input (linear, not squared); quick sort on sorted input (squared, not n log n, because of the first-element pivot); linear search (about n/2, not n, because half the targets are present); merge sort's ratio slightly above 2.
   - A closing "what this means in practice": why the difference between n log n and n squared stops being academic at a million items (give the arithmetic).
   - A short glossary (4 to 8 terms) and a "try it" section: two changes a reader can make to the experiment and what they should expect to see.
2. `scripts/check_big_o.py`: reads `results/*.csv`, recomputes **every** number quoted in the two tables of `BIG_O.md`, and exits non-zero if any quoted number differs from the recomputed one. It should also print the tables, so you can paste them. Write the numbers into the Markdown so the script can find them (for example in table cells formatted the same way the script prints them).
3. `tests/test_check_big_o.py`: the script passes on the committed `BIG_O.md`; it fails (non-zero) when you change one quoted number in a temporary copy.
4. Add a one-line link to `BIG_O.md` in `README.md`.

## Constraints
`AGENTS.md` applies. Python 3.9+, standard library only. Do not change anything in `src/` or `results/`; if a number looks wrong, report it, don't "fix" it. Public repo: no secrets, hostnames, personal paths. Nothing to `main`; push your branch.

## Acceptance test
1. `python scripts/check_big_o.py` exits 0; show its output.
2. Change one quoted number in a copy of `BIG_O.md` and show the script exits non-zero.
3. `pytest` passes (all tests, not only yours); give the summary line.
4. Every "differs from prediction" row has an explanation, and your report lists which ones you found beyond the four named above, if any.
5. Someone who has never seen Big O can follow the doubling question section. Read it back once as that person and say in your report what you changed.
6. `git status --short` is clean and the branch is pushed.

## Report
`sidecar/reports/04_big_o_report.md`: files, commands with output, acceptance items, surprises in the data, gaps, final commit hash. Terminal state COMPLETE / HUMAN_GATE / FAILED. Do not mark your own work accepted. Standard: done enough to talk about.
