# Report 01: core classes

**From:** Anna **To:** Flo **Date:** 2026-11-09
**Terminal state: COMPLETE** (awaiting Flo's review; not self-accepted)

## Files created
- `pyproject.toml`, `src/sortsearch/__init__.py`, `counter.py`, `dataset.py`
- `sorters/`: `base.py bubble.py insertion.py selection.py recursive.py merge.py quick.py __init__.py`
- `searchers/`: `base.py linear.py binary.py recursive_searcher.py recursive_binary.py __init__.py`
- `tests/`: `test_counter.py test_dataset.py test_sorters.py test_searchers.py`
- README gained a "Run the tests" section; `PROVENANCE.md` updated.

## Commands and results
- `python3 -m pytest -q` in the worktree: 64 passed.
- Fresh `git clone -b anna/01-core-classes` from GitHub, then `pytest -q`: 64 passed (Python 3.12, pytest 9; the pytest config adds `src` to the path, so no install is needed).
- grep of `src`, `tests` and top-level `*.md` for home paths and host names: no hits.

## Acceptance test, item by item
1. Fresh-clone pytest passes: yes (above).
2. All five sorters on random, sorted, reversed, empty, one-element, all-duplicates (plus a mixed-duplicates case): correct, input unchanged, new list returned. `test_sorts_correctly_and_leaves_input_alone`.
3. Hand-worked counts for `[3, 1, 2]`, written as comments before each assertion (bubble 3 comparisons / 4 moves; insertion 3 / 4; selection 3 / 4). I also hand-worked merge (3 / 5) and quick (3 / 10) and insertion's best case. The code matched my hand counts on the first run.
4. Binary, recursive binary and linear agree over 200 seeded cases including absent targets (unique values). A second test shows the two binary searches also agree on lists with duplicates.
5. `QuickSort` on sorted input of 100 gives `max_depth` = **100 exactly**; `MergeSort` gives 8 (< 10). Why 100: the first call is depth 1, and the nested calls on 100, 99, ..., 1 elements make 100 levels. Calls on empty ranges are skipped on purpose, otherwise the answer would be 101.
6. Branch pushed; `git status --short` clean after the last code commit.

## Counting conventions chosen (the design left these open)
- Move = one write into a list position; a swap is 2.
- Bubble has no early exit (matches "bubble (full)" in the design table).
- Insertion counts each shift and each placement of the held value as a move, so best-case sorted input costs n-1 moves, not 0.
- Selection swaps only if the smallest value is not already in place.
- Merge counts every value written while merging; the final copy back into the caller's copy is not counted again.
- Searchers: one probe and one comparison per element looked at.

## Borrowed
Nothing. Written from scratch from `DESIGN.md`; I did not open the other repositories. `PROVENANCE.md` says so.

## Unsure or unfinished
- `Sorter.sort` raises `RuntimeError` if the result is unsorted. The design said only "checks"; I chose an exception over `assert` so it survives `python -O`.
- The merge recursion uses list slices (extra memory) for readability. Counts are unaffected.
- Python 3.9 compatibility was not run here (only 3.12); the code uses no syntax newer than 3.9, but that is unchecked.

## What I would change in DESIGN.md
- State the counting conventions above in the Counter table (what a "move" is for insertion and merge).
- Say that depth starts at 1 and that empty-range calls are not counted.
- Note that `RecursiveSorter` and `RecursiveSearcher` each carry their own copy of `_enter`; a shared helper would remove the duplication but add a third class to explain.
- Add `recursive_searcher.py` to the folder layout (it is a separate file, one class per file).

Code commit before this report: `33db462`.

## Update (after Flo's sidecar move)
Merged `origin/main` (sidecar move, `3b532e7`/`648132a`) into this branch and moved this report to `sidecar/reports/`. Per Jeremy, polish is skipped; the gaps above are the plain list.
