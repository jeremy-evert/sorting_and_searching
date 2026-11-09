# Ledger

One page that says what each prompt produced, what turned out to matter, and what is still owed. It is a map into `prompts/completed/` and `reports/`, not a replacement for them. The report is the evidence; `DESIGN.md` is the truth; this page is how you find your way between them.

Update it when a prompt finishes: add a row. Open work is in [`TASKS.md`](TASKS.md), not here.

## What was done

| # | Prompt | Delivered | Evidence | State |
|---|--------|-----------|----------|-------|
| 01 | `core_classes` | `Counter`, `DataSet`, five sorters, three searchers, base classes, tests | 64 tests pass in a fresh clone | merged |
| 02 | `manager_and_results` | `ExperimentManager`, `run_experiment.py`, two results CSVs | CSV hashes identical across two runs; exact values at n=640 checked against n(n-1)/2 | merged |
| 03 | `plotter` | `Plotter`, `results_io.py`, `make_plots.py`, 19 plots | plots generated from the real CSVs; four inspected by eye | merged |
| 04 | `big_o` | `BIG_O.md`, `check_big_o.py` | tables recomputed from the CSVs; a changed number makes the check fail | merged |
| 05 | `home_page` | `docs/index.html`, `check_site.py`, `report/report.tex`, `docs/report.pdf` | link and section check; screenshots at 400 and 1200 px in `runs/` | merged |
| 06_a | `design_to_sidecar` | `DESIGN.md` moved into `sidecar/`, `LEDGER.md` and `TASKS.md` added | `82 passed`; `check_site.py` exits 0; `main` equals `origin/main` | merged |
| 06 | `clarity_pass` | read-through for names, docstrings, dead code | none yet | open |
| 08 | `repo_grievances` | candid review in `SINS.md` | observations and unverified concerns labeled in the document | awaiting review |

## What mattered

These are the choices and findings that changed the design or the numbers. Each is worth keeping when the code is reworked.

- **Count operations, never seconds.** Every claim in the repo is an exact count from a fixed seed, so any result can be reproduced and any number can be checked. Prompt 02 proved it by hashing the CSVs from two runs.
- **Hand-worked tests.** The expected values were derived from the algorithm (for example `[3, 1, 2]` gives bubble 3 comparisons and 4 moves) and written as a comment before the assertion. The code matched on the first run, which is the point of doing it that way (01, 02).
- **Check numbers with a script, not by eye.** `check_big_o.py` fails if a table in `BIG_O.md` drifts from the data; `check_site.py` fails on a broken link or a missing section. Both caught real problems when tested with a deliberately wrong input (04, 05).
- **Quick sort with a first-element pivot is deliberately quadratic on sorted input.** `max_depth` is exactly 100 for n=100 and the comparisons equal bubble sort's (204480 at n=640). This is the clearest demonstration of why Big O depends on input (01, 04).
- **Linear search averages 3n/4, not n/2.** Half the lookups hit (about n/2) and half miss (n). The prompt's expectation was wrong and the data corrected it (04).
- **Binary search sits about 0.45 probes under log2 n** because hits are found before the last halving (04).
- **Insertion sort on sorted input is linear**, because each insert is one comparison and one move (04).
- **Honest reporting found things.** The overlapping bubble and selection lines (03, 05), the first screenshots that cut the page off (05), and the prose number written as 2.2 then corrected to the measured 2.31 (04) all came from reports that listed gaps instead of hiding them.

## Working habits that paid off

- Each prompt states why, constraints, and an acceptance test that can fail. Reports answer the acceptance items one by one.
- One branch, one worktree, one report per prompt; the reviewer merges.
- A fresh clone to run the tests, so a missing file or path cannot hide (01, 03).
- Stage files by name, so scratch output does not get committed.
