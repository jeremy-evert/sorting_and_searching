# Report 06: clarity pass

**Branch:** `claude/06-clarity-pass`  
**State:** FAILED (verification and commit blocked; not reviewed or accepted)

## Review and changes

Read the Python files in `src/sortsearch/` and `tests/`, and reports 01–04. The changes are limited to documentation: `src/sortsearch/sorters/merge.py` now says the final copy is not counted again, and `src/sortsearch/manager.py` distinguishes averages from maximum depth. No expected test numbers or algorithm statements were changed. The hardest point to make clear was which recursive calls count toward depth: the implementations differ on empty ranges.

`sidecar/DESIGN.md` now records the counting conventions, depth behavior, searcher file, target generation, maximum-over-trials depth, and mixed-search workload. `sidecar/TASKS.md` records those design updates while leaving prompt 06 open because its verification and commit are unfinished. This update follows the current owner's request, which supersedes the original prompt's instruction to list design discrepancies without editing the design. The task file's earlier request to say empty calls are not counted was inaccurate: quick sort skips them, merge sort counts its initial empty-list call, and recursive binary search counts empty-range calls. The design now reflects the code rather than repeating that claim.

## Proposed, not done

- Clarify the searching plot's `n/2 reference` label for hits; the mixed workload averages about `3n/4` for linear search. Changing the plot is outside this clarity pass.
- Consider whether recursive binary search should count empty-range calls. Changing it would alter depth counts, so the existing behavior remains.
- Other design drift remains: the class diagram describes a different Plotter interface, and the layout omits `results_io.py`. These were not among the requested task-list updates.

## Evidence and acceptance

- `git fetch`: succeeded.
- `.\.venv\Scripts\python.exe -m pytest -q`: could not start; Windows reported `Unable to create process ... The file cannot be accessed by the system.` Both `py -0p` and `python --version` failed with the same access error. Baseline and final tests therefore were not run; there is no test/code disagreement to assess.
- `Get-FileHash results/*.csv -Algorithm SHA256`, before changes:
  - `results/search_counts.csv`: `67754990ea4b864f5ed17bb9007d7f918317538be00a38207b34d505b5176fa8`
  - `results/sort_counts.csv`: `734a22d519fd703c6481dc25bacb9d0828d11e3570387477995bcd0831bc1ab5`
- The experiment could not be run without Python, so neither requested run nor post-run hashes are available. The existing `sidecar/runs/02_run.log` was preserved; its SHA-256 is `aa34dafb1c6b76ba1e8834886478f2571fd154a9402b29c59d9dc3361e47d662`.
- `git diff --check`: no output before this report.
- `git add src/sortsearch/manager.py src/sortsearch/sorters/merge.py sidecar/DESIGN.md sidecar/TASKS.md`: failed: `fatal: Unable to create .../.git/index.lock: Permission denied`. The configured sandbox makes `.git` read-only. No commit or push was made; the starting commit remains `0b06546`.
- The requested sidecar design and task updates necessarily depart from the original prompt's limited diff acceptance item. The pre-existing untracked run log also prevents a clean status and remains untouched.

## Remaining work

Run the baseline/final tests and experiment hash comparison in an environment that can execute Python, preserve the run log when running the experiment, then review the diff, finish the task and ledger entries, commit, and push the branch in an environment that permits Git metadata writes. A final commit hash cannot be supplied until that succeeds.

FAILED
