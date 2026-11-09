# Report 02: manager and results

**From:** Anna **To:** Flo **Date:** 2026-11-09
**Terminal state: COMPLETE** (not self-accepted). Per Jeremy: done enough to talk about, no polish.

## Files
`src/sortsearch/manager.py` (ExperimentManager, SortRow, SearchRow, ExperimentResult), `scripts/run_experiment.py`, `tests/test_manager.py`, `results/sort_counts.csv`, `results/search_counts.csv`. Branch `anna/02-manager-and-results`, stacked on `anna/01-core-classes` (tip `f01c335`, which includes the sidecar merge).

## Acceptance
1. **Identical hashes across two runs: PASS.**
   ```
   67754990ea4b864f5ed17bb9007d7f918317538be00a38207b34d505b5176fa8  results/search_counts.csv
   734a22d519fd703c6481dc25bacb9d0828d11e3570387477995bcd0831bc1ab5  results/sort_counts.csv
   ```
   (same output after both runs)
2. **Row counts: PASS.** 106 lines in sort CSV (105 data + header), 22 in search CSV (21 + header); also asserted in a test.
3. **Exact values at 640: PASS, no disagreement.** bubble and selection comparisons are 204480.0 on all three kinds; insertion sorted 639.0; quick sorted 204480.0; merge is 5182.8 / 2880.0 / 3136.0 (random / sorted / reversed), all <= 6400. Asserted in `test_exact_values_at_640` against n(n-1)/2, not against output.
4. **Binary and recursive binary identical avg_probes at every size: PASS** (`test_binary_pair_probes_identical`).
5. **`grep -c $'\r'` on both CSVs: 0 and 0. PASS.** A test checks LF on a small run too.
6. **Clean and pushed:** see final commit below; `git status --short` was run after the last commit.

`pytest`: 70 passed (0.57 s). The tiny 4/8 run is asserted to finish in under a second.

## Step 1 classes changed
None.

## Gaps, plainly
- `sidecar/runs/02_run.log` is written by the script but **not committed**: the repo's `.gitignore` ignores `*.log`. I did not force-add it or edit `.gitignore`. Flo/Jeremy: say if you want it tracked.
- Averages are written as raw floats (e.g. `5182.8`, `204480.0`); no rounding rule was set.
- `max_depth` in a sort row is the maximum over trials, not an average (prompt gave no rule). Search rows have no depth column, as specified.
- Search targets: even-valued list (0, 2, ..., 2(n-1)); present targets drawn with a seeded RNG (seed = n), absent targets are odd numbers. Choices of mine, since the prompt left them open; worth one line in `DESIGN.md`.
- Python 3.9 still unchecked (ran on 3.12).

## For prompt 03 (plots)
The CSVs give per-size averages for every kind/algorithm and per-size average probes per searcher; they do not include the fitted Big O constant, per-trial spread, or max_depth for searchers, so the plotter must compute fits itself.

Final code commit: `36f3d55` (this report is committed on top of it).
