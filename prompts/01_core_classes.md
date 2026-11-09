# Prompt 01: core classes

**From:** Flo (Foreman) **To:** Anna (builder) **Date:** 2026-11-09

## Where
Repo `sorting_and_searching` (public, `github.com/jeremy-evert/sorting_and_searching`). Branch `anna/01-core-classes` off `origin/main`. Work in a fresh worktree, not in a checkout that has other changes in it. Read `DESIGN.md` first; it is the plan.

## Why
This repo will be shown to a beginner programming class as an example of well-formed classes and clean inheritance. Step 1 builds the classes that everything else sits on. If these are clear and correct, the experiment, plots and home page are easy; if they are muddled, nothing after them can be fixed with polish.

## What to build
Everything under `src/sortsearch/` that `DESIGN.md` lists for: `Counter`, `DataSet`, `Sorter` and its five children (bubble, insertion, selection, merge, quick, with `RecursiveSorter` between `Sorter` and the last two), `Searcher` and its children (linear, binary, recursive binary, with `RecursiveSearcher`). One class per file. Plus `pyproject.toml`, a `tests/` file per module, and a README line saying how to run the tests.

You may reuse code from Jeremy's other repositories (the CS2 Beast `week_12/refactor_beast/src/` is a good start; also look at the CS1, Computer Architecture and DSCT repos) or write from scratch. Whatever you borrow, record it in `PROVENANCE.md` (what, from which repo and path, what you changed).

## Constraints
- Python 3.9 or newer. Standard library only for the classes; `pytest` for tests.
- No global variables. State is passed in.
- `Sorter.sort` copies its input and never mutates the caller's list.
- `QuickSort` uses the first element as its pivot, on purpose (see `DESIGN.md`).
- Docstring on every class and public method, one or two plain sentences. Names a beginner can read. No clever one-liners.
- Public repo: no secrets, no student data, no personal paths or hostnames in any file.
- Do not push to `main`. Push your branch. One commit per class or per tight group of files, with a plain message.

## Acceptance test
All of these must be true, and your report must show the output:
1. `pytest` passes from a fresh clone of your branch.
2. Every sorter returns a correctly sorted list for random, sorted, reversed, empty, one-element and all-duplicates inputs, and leaves the input untouched.
3. Hand-worked counts: for `[3, 1, 2]`, write the expected comparisons and moves for bubble, insertion and selection **by hand in the test, as comments**, and assert them. A test that only copies what the code prints doesn't count.
4. `BinarySearch` and `RecursiveBinarySearch` return the same index as each other, and the same as `LinearSearch`'s index when the target is unique, for 200 seeded random cases including absent targets.
5. `QuickSort` on sorted input of size 100 reaches `max_depth` of 100 (or one less; say which and why), and `MergeSort` stays under 10.
6. `git status --short` is clean after your final commit, and the branch is pushed.

## Report
Write `reports/01_core_classes_report.md` and commit it on the same branch. Include: files created, commands run with results, anything borrowed, anything you did not finish or were unsure about, the final commit hash, and what you would change in `DESIGN.md` now that you have built from it. Honesty about gaps is worth more than a tidy report.
