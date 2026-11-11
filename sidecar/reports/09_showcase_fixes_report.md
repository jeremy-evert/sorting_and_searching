# Report 09: make the showcase keep its promises

**Prompt:** `sidecar/prompts/09_showcase_fixes.md` **Branch:** `anna/09-showcase-fixes` (off `origin/main` at 11d62b6) **Terminal state:** HUMAN_GATE (merge, history rewrite and branch deletion are a person's decision). Not self-accepted.

## What changed
- **One command makes the results and plots.** `scripts/regenerate.py` runs the experiment, writes the CSVs, draws all 19 plots. `--check` rebuilds in a temporary folder and compares the CSVs byte for byte. `tests/test_results_reproducible.py` does the same inside pytest.
- **The README now says exactly what reproduces.** CSVs: byte for byte (tested). Plots: same data and curves; pixels can differ between matplotlib versions (I saw this: a newer matplotlib changed every committed PNG). Plot files now carry no matplotlib version metadata.
- **Search plot:** the reference line is 3n/4 (labelled "half the lookups miss"), with a test (`linear_reference`) and a caption on the home page.
- **`Sorter.sort`** also checks the output holds the same values as the input; two deliberately broken sorters (drops a value, invents a value) are rejected by tests.
- **`BIG_O.md`:** Big O is stated as an upper bound; the doubling ratio illustrates it. A "what exactly is counted" list was added (also a box on the home page). The plot names are no longer "planned". The word "exceptions" is gone from the home page.
- **Quick sort on random input, tested.** 500 lists per size (seeds 1000n to 1000n+499) give 2793.3 at n=320 and 6441.0 at n=640, ratio 2.31. The exact expected count for a first-item pivot, 2(n+1)H(n) - 4n, gives 2794.8 and 6464.6, ratio 2.313. So the 2.40 was five unlucky lists, and the remaining gap above 2.24 is lower-order terms. `tests/test_quick_sort_expectation.py` checks it (n=320 within 1%, plus a hand-worked n=3 case). The 5-trial table and its "NO" are unchanged.
- **Checkers say what they check.** `check_big_o.py` now also verifies a fixed list of numbers quoted in sentences in `BIG_O.md`, `docs/index.html` and `report/report.tex`; a test changes one and sees it fail. Its success line says other prose numbers are not checked. `check_site.py` says it checks structure, alt-text presence and local links only, not accuracy or external links.
- **Alt text** for the quick-sort image no longer describes an n log n curve that is not drawn; the searching alt text mentions the reference lines. I looked at the regenerated plots to write them.
- **Class diagram:** split into an at-a-glance overview (fits a phone), a sorter diagram, a searcher diagram, and a plain nested list. The two family diagrams still scroll sideways on a phone; the overview and the list do not.
- **`docs/report.pdf`:** Title, Author and Subject set; quick-sort paragraph updated; rebuilt with pdflatex. (The old PDF had blank metadata.)
- **DESIGN.md / AGENTS.md:** plotter interface, folder layout and `regenerate.py` match the code; "no global variables" now reads "no mutable module-level state; constants are fine".
- **CI:** `.github/workflows/tests.yml` runs pytest, `regenerate.py --check`, `check_big_o.py` and `check_site.py` on Python 3.9 and 3.11; README badge added.
- **Field Guide:** the root `Deciding_with_AI_Field_Guide_print.pdf` (an older version) was removed; `docs/Deciding_with_AI_Field_Guide_v1.0.3.pdf` (4 pages, supplied by Jeremy on 2026-11-10) replaces it, and the README link explains what it is.

## Commands run (in a fresh clone of the pushed branch, tip c43bb4c, Python 3.12)
```
pytest                               -> 90 passed in 4.12s
python scripts/regenerate.py --check -> OK: the CSVs match ... byte for byte, and all 19 plots were drawn.
python scripts/check_big_o.py        -> OK: both marked tables, and the listed numbers quoted in sentences, match the data.
python scripts/check_site.py         -> OK: six sections present, every image has alt text, every local image and link resolves.
```
I viewed the home page at 390 px wide in headless Chromium: the overview diagram and the list read fine; the family diagrams scroll sideways.

## Addendum (same day): from Monday's CS1 class on this repo
The CS1 recording shows this repo was the class's example of a public project with a sidecar, and that students will pick a project of their own on Wednesday and ask an agent "is it ready to go public?". Added: `docs/WHAT_IS_A_TEST.md` (real passing and failing pytest runs, linked from `AGENTS.md`, because the class had not seen unit tests), a pre-publish prompt in `sidecar/prompts/README.md`, and in `sidecar/README.md` what each of ledger and tasks owns plus a worked "what belongs in a sidecar" example using DESIGN.md (students debated this live). Their tasks were removed from `TASKS.md`. The class also found the class diagram an "eye chart" and could not scroll it sideways: the overview and list above address that.

## Public-safety sweep (read-only)
Current files and the contents of every commit: no home paths, tokens, keys or hostnames. PDF and PNG metadata clean. Author lines: 40 of 62 commits show a machine name (april 25, brandy 13, windows_desktop 2) and 23 show an institutional email address. I did not rewrite history. Decision for a person: `sidecar/questions/07_history_identity.md`.

## Not done, and why
- **CI (resolved).** The first GitHub run failed: Python 3.9 is not on the newest Ubuntu image, and fail-fast cancelled 3.11. Fixed by pinning `ubuntu-24.04` and `fail-fast: false`. The rerun passed on 3.9 and 3.11, including `regenerate.py --check`, so the CSVs also match byte for byte on those versions.
- **History rewrite** (author lines) and **deleting merged remote branches**: AGENTS.md says ask first.
- **Closing out prompts 06 and 07 and the ledger rows for them:** that is the reviewer's call.
- **Teaching items** (shell-sort "your turn" prompt, unit-test page, Field Guide map, pre-publish checklist): new content, not repairs to a promise; left in `TASKS.md`.
- **Decisions list** (CSV rounding, overlapping lines, the RecursiveSorter question): unchanged.
- Quick sort's own 'Try it' number (2.31 with a middle pivot) is quoted from earlier work and not machine-checked.
- Housekeeping: the removal of the old root PDF landed inside commit `c4328f5` rather than its own commit; an error in my staging, harmless.

## Final commit
c43bb4c on `anna/09-showcase-fixes`.
