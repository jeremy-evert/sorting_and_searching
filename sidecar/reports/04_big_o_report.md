# Report 04: Big O write-up

**From:** Anna **To:** Flo **Date:** 2026-11-09
**Terminal state: COMPLETE** (not self-accepted). Standard: done enough to talk about.

## Files
`BIG_O.md`, `scripts/check_big_o.py`, `tests/test_check_big_o.py`, one-line link added to `README.md`, this report. Branch `anna/04-big-o` off `origin/main` (a4b573d), in its own worktree. Nothing in `src/`, `results/` or plotter files was touched.

## Acceptance
1. **`python scripts/check_big_o.py` exits 0: PASS.** It prints both tables, ends with `OK: every quoted number matches the data.` (tables are in `BIG_O.md`).
2. **Changed number fails: PASS.** Copy of `BIG_O.md` with the first `204480.0` changed to `204481.0`: output ends `FAILED: 2 mismatched line(s).`, exit code 1. Also covered by tests (sort number, search number, missing tables).
3. **`pytest -q`: `74 passed in 0.59s`** (all tests, run this session).
4. **Every differing row explained: PASS.** See below for rows beyond the four named.
5. **Read back as a beginner:** I added the definition "n = number of items, 2n = twice as long" at the very start of the doubling section (it assumed n was known), and added that Big O is a statement about the ratio, not the exact count. No other change.
6. `git diff --check` clean; `git status --short` empty after the last commit; branch pushed.

## How the check works
The tables in `BIG_O.md` sit between `<!-- sort-table:start -->`/`end` and `search-table` markers. The script recomputes the two tables from the CSVs and requires every line to match exactly, in both directions. It checks the **tables only**: numbers quoted in prose (204480, 319/639, 481.25, 7.87 to 8.88, 2.40, 2.31, the million-item arithmetic) are not machine-checked. I hand-checked them against the data and the arithmetic.

## Surprises in the data (beyond the four named)
- **Linear search is 3n/4, not n/2.** The prompt said "about n/2, because half the targets are present". Half the lookups hit (n/2) and half miss (n), so the average is 3n/4: 249.50 vs 240 predicted at 320, 481.25 vs 480 at 640. I wrote 3n/4 in the doc and table. `DESIGN.md` says "about n/2 for hits, n for misses", which is consistent, but its table row could confuse; worth a line there.
- **Quick sort on random input** has a measured ratio of 2.40 against 2.24 predicted, so the script marks it "NO" (my tolerance is 5%). Explained in the doc as lower-order terms plus only 5 trials. Not a bug as far as I can tell, but I did not run more trials to confirm.
- **Binary search sits about 0.45 probes under log2 n** (7.87 vs 8.32 at 320). Explained as hits being found before the last halving.
- Bubble and selection have identical comparison counts on all inputs; mentioned in the doc.
- Merge ratios are 2.23 to 2.29, all within 5% of 2.24, so they show "yes". I still explained "slightly above 2" as asked.
- Try-it experiment 2 (middle pivot) was actually run in a scratch subclass: sorted-input comparisons 2058 at 320 and 4747 at 640, ratio 2.31. I first wrote 2.2 in the text, then corrected to the measured value.

## Gaps
- Prose numbers are not machine-checked (above).
- Plot names (`plots/sorting_*.png`, `plots/searching.png`) are Hanna's planned names; I did not verify them against her branch. The doc says "planned".
- "Agrees" uses a 5% tolerance I chose.
- Only comparisons are tabulated for sorting; moves and depth are not in the tables.
- Try-it experiment 1 (larger sizes) was not run; the recursion-limit remark is from reasoning, not a run.
- `DESIGN.md` was not edited (not asked).
- Python 3.9 still untested (ran on 3.12).

Final code commit: `12a8e51` (this report is committed on top of it).
