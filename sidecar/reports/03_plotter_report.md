# Prompt 03: plotter and Big O overlays

**Terminal state: COMPLETE**

## Work completed

- Added `src/sortsearch/results_io.py` with immutable `SortRow` and `SearchRow` readers for the prompt-02 CSV schema. The search reader accepts the actual `recursive binary` label.
- Added `src/sortsearch/plotter.py` for sorting comparisons, fitted Big O overlays with visible over-25% disagreement marks, and searching probe curves with `n/2` and `log2 n` references. The plotter only uses row objects supplied to its constructor.
- Added `scripts/make_plots.py`, which accepts `--results` and `--out` and writes all 19 requested figures.
- Added deterministic CSV fixtures for 105 sorting rows and 21 searching rows, including the real spaced search label, plus plotter tests.
- Added the `plots` optional dependency in `pyproject.toml`; the `test` extra includes matplotlib so the plot tests work with the repository's normal test install.

## Checks and output

Installed the optional packages in a temporary environment with `python3 -m pip install -e '.[test]'`.

`python -m pytest -q`:

```text
.....                                                                    [100%]
5 passed
```

`python scripts/make_plots.py --results tests/fixtures --out /tmp/plots_check`:

```text
Wrote 19 PNGs to /tmp/plots_check
19
```

Fetched `origin/anna/02-manager-and-results` and read its CSV files without adding them to this branch. Confirmed sort labels are `bubble`, `insertion`, `selection`, `merge`, and `quick`; the third search label is `recursive binary`. Ran the same plot command with those two real CSV files supplied from a temporary directory:

```text
Wrote 19 PNGs to /tmp/plotter-real-plots
19
```

The real prompt-02 CSVs work without code changes. No prompt-02 result files were committed here.

Cloned the pushed branch into a clean temporary checkout, installed `.[test]`, and ran:

```text
python -m pytest -q
.....                                                                    [100%]
5 passed

python scripts/make_plots.py --results tests/fixtures --out /tmp/ss-hanna-03-clone2-plots
Wrote 19 PNGs to /tmp/ss-hanna-03-clone2-plots
19

git status --short --branch
## hanna/03-plotter...origin/hanna/03-plotter
```

`git diff --check` completed with no output.

## Figure inspection

Opened these four generated figures from the real prompt-02 CSVs:

- `sorting_random.png`: the quadratic series rise faster than merge and quick sort; the full-name legend is readable. Bubble and selection have identical comparison values, so their traces coincide.
- `bigo_merge_random.png`: the fitted `n log n` prediction follows measured merge-sort points; no point is marked as more than 25% off.
- `bigo_quick_sorted.png`: the measured points follow the fitted quadratic curve for sorted input, as expected for the first-element pivot.
- `searching.png`: linear search rises above the `n/2` reference, while binary searches stay near the logarithmic reference. Binary and recursive-binary measurements coincide, so one trace partially covers the other.

The coincident traces are a visible limitation of these real measurements; the legend still names both algorithms. I left the data unaltered and did not add plot polish beyond distinct colors and markers.

## Remaining gaps

- Coincident algorithm measurements overlap in the combined charts, as noted above.
- No site page or `BIG_O.md` integration was part of this prompt.

Implementation commit: `db816d8` (`Fix sorting plot indentation`), following `9c9b4d7` (`Build sorting and searching plots`). Branch `hanna/03-plotter` was pushed to origin. This report does not mark the work accepted.
