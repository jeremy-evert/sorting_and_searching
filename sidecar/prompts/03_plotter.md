# Prompt 03: plotter and Big O overlays

**From:** Flo (Foreman) **To:** Hanna (builder, Codex) **Date:** 2026-11-09
**Runs in parallel with** prompt 02. You do not wait for it: you build against the result **file format**, which prompt 02 fixes, and a small hand-made sample of it.

## Where
Repo `sorting_and_searching`. Branch `hanna/03-plotter` off `origin/main`. Fresh worktree. Read `DESIGN.md` (especially "Expectations") and `sidecar/prompts/02_manager_and_results.md` (section 2 to 4) before you start.

## The contract you build against
Prompt 02 writes two CSV files with a header row and LF line endings:

- `results/sort_counts.csv`: `kind,algorithm,size,avg_comparisons,avg_moves,max_depth`
  - `kind` is `random`, `sorted` or `reversed`.
  - `algorithm` is one of `bubble`, `insertion`, `selection`, `merge`, `quick`.
  - `size` is 10, 20, 40, 80, 160, 320, 640.
- `results/search_counts.csv`: `algorithm,size,avg_probes`
  - `algorithm` is `linear`, `binary`, `recursive_binary`.

Make a small sample of both in `tests/fixtures/` (the real sizes, plausible numbers you work out from the formulas in `DESIGN.md`, not random). Your tests use the fixtures. When prompt 02 lands, the real files must work with no code change; say in your report whether you checked that.

## Why
The plots are the picture the whole project is shown through: a reader should see in ten seconds that bubble sort bends upward and merge sort stays nearly straight, and see where the measurements agree with theory and where they don't. A graph that is hard to read has failed even if the numbers are right.

## What to build
1. `src/sortsearch/plotter.py`: class `Plotter` with `__init__(self, sort_rows, search_rows)` taking the row lists (build small `SortRow` and `SearchRow` readers in `src/sortsearch/results_io.py` that load the CSVs; the manager's result dataclasses from prompt 02 may not exist yet, so define the reader's rows yourself and keep them the same field names). `Plotter` never runs experiments and never reads files itself.
2. Methods writing PNGs (matplotlib, `Agg` backend) into a directory passed in:
   - `plot_sorting(kind, path)`: one figure per input kind, one line per sorter, comparisons against size, with log-log axes.
   - `plot_big_o(algorithm, kind, path)`: measured points for one algorithm and one input kind, plus the prediction curve from the table in `DESIGN.md`: `c * f(n)` where `f` is `n`, `n log n` or `n squared`, and `c` is one constant fit by least squares to the measured points. Title says what was predicted and what was measured. Mark visibly when the two disagree by more than 25% anywhere.
   - `plot_searching(path)`: probes per lookup against size for the three searchers, plus `n/2` and `log2 n` reference curves.
3. `scripts/make_plots.py`: reads the two CSVs, writes everything to `docs/plots/` with names `sorting_<kind>.png`, `bigo_<algorithm>_<kind>.png`, `searching.png`.
4. Tests (`tests/test_plotter.py`): files are written, are valid PNGs (check the 8-byte signature), and the least-squares fit returns the constant exactly for synthetic data that is exactly `3 * n * log2(n)`. A test also asserts the 25% disagreement flag turns on for a deliberately wrong prediction.

## Constraints
Python 3.9+. `matplotlib` and `pytest` are the only third-party packages; add `matplotlib` to `pyproject.toml` as an optional `plots` extra. Readable colors: no two lines the same color in one figure, and a legend that names algorithms in full. Axis labels in plain words ("input size n", "comparisons"). No global state. Public repo: no secrets or personal paths. Do not push to `main`; push your branch.

## Acceptance test
1. `pytest` passes from a fresh clone of your branch.
2. `python scripts/make_plots.py --results tests/fixtures --out /tmp/plots_check` (adapt the flags you define) writes 3 sorting figures, one Big O figure for each of the 5 algorithms on each of 3 kinds (15), and `searching.png`: **19 PNGs**.
3. Open at least four of the PNGs and look at them. Your report says what you saw, including anything that looked wrong and how you fixed it.
4. `git status --short` is clean and the branch is pushed.

## Report
`sidecar/reports/03_plotter_report.md`: files, commands with output, the four figures you inspected and what you saw, whether you ran against real prompt-02 data, what you couldn't verify, the final commit hash. Terminal state COMPLETE / HUMAN_GATE / FAILED. Do not mark your own work accepted.
