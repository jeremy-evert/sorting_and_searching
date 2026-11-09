# Prompt 02: experiment manager and results

**From:** Flo (Foreman) **To:** Anna (builder) **Date:** 2026-11-09
**Follows:** `01_core_classes.md` and its report. Read that report first: it records anything in `DESIGN.md` that turned out different when built.

## Where
Repo `sorting_and_searching`. Branch `anna/02-manager-and-results`, **stacked on `anna/01-core-classes`** (create it from that branch's tip, after your 01 report says COMPLETE and 01 is pushed). If 01 is later changed in review, Flo will tell you to rebase. Fresh worktree, not a checkout with other changes in it.

## Why
Step 1 gave us correct classes. Step 2 turns them into evidence: one repeatable run that produces the numbers every later graph and claim rests on. If these numbers are not exactly repeatable, the Big O story on the home page can't be trusted, and a reader can't check it. The manager is also the one place where the whole design meets, so it is the best test of whether the classes from step 1 fit together cleanly. If you have to bend a step 1 class to make the manager work, that is a finding: report it, don't hide it.

## What to build
1. `src/sortsearch/manager.py`: `ExperimentManager` and the result dataclasses `SortRow(kind, algorithm, size, avg_comparisons, avg_moves, max_depth)` and `SearchRow(algorithm, size, avg_probes)`, plus `ExperimentResult` holding the two row lists. The manager receives its sorters, searchers, sizes, kinds and trial count through its constructor. It has no `print`, no file writing, no plotting.
2. **Sorting measurement:** for each kind (`random`, `sorted`, `reversed`), sorter and size, run 5 trials. Trial `t` of size `n` uses seed `n * 1000 + t`. Average the counts over the trials. Sizes: 10, 20, 40, 80, 160, 320, 640.
3. **Search measurement:** for each size, build one sorted list of `n` distinct values; make 200 targets, alternating present and absent; average probes per lookup for each searcher on the same targets.
4. `scripts/run_experiment.py`: builds the default manager, runs it, writes `results/sort_counts.csv` and `results/search_counts.csv` (long format, one row per row object, header row first). **LF line endings on every platform** (open with `newline=""`, set `lineterminator="\n"`); a previous project failed its own tests because of CRLF. Write a one-line log to `sidecar/runs/02_run.log`.
5. Commit the two CSV files. They are small, and the home page reads them.
6. Tests: `tests/test_manager.py` (and a test for the script's output). A tiny manager run (sizes 4 and 8, 2 trials) must finish in under a second.

## Constraints
Same as prompt 01 (Python 3.9+, no globals, plain names, docstrings, no secrets or personal paths, public repo, nothing to `main`). Standard library only, except `pytest`. No plotting in this step.

## Acceptance test
Your report must show the commands and output for each:
1. Run `scripts/run_experiment.py` twice; the `sha256sum` of both CSVs is **identical** across the runs.
2. Row counts: sort CSV has exactly 105 data rows (3 kinds x 5 sorters x 7 sizes); search CSV has exactly 21 (7 sizes x 3 searchers).
3. These exact values hold at size 640, and a test asserts each. They follow from the algorithms themselves, so they are not copied from the output:
   - bubble (full) comparisons = 204480 on all three kinds (n(n-1)/2)
   - selection comparisons = 204480 on all three kinds
   - insertion comparisons on sorted input = 639 (n-1)
   - quick sort comparisons on sorted input = 204480
   - merge sort comparisons <= 640 x 10 on every kind
   If a value disagrees, **stop and report which one and why; do not edit the test to match the code.** A disagreement may mean a bug in step 1, or a counting rule that `DESIGN.md` should state more clearly. Either is useful.
4. Binary and recursive binary search give identical `avg_probes` at every size.
5. `grep -c $'\r'` on both CSVs prints 0.
6. `git status --short` is clean and the branch is pushed.

## Report
Write `sidecar/reports/02_manager_and_results_report.md` on the branch: files, commands and their output, which acceptance items passed, any step 1 class you had to change and why, anything unfinished, the final commit hash, and one sentence on what prompt 03 (plots) will need from the result data that you did or did not provide. Terminal state COMPLETE / HUMAN_GATE / FAILED. Do not mark your own work accepted.
