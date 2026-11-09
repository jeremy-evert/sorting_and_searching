# Report 05: home page and LaTeX report

**From:** Anna **To:** Flo **Date:** 2026-11-09
**Terminal state: COMPLETE** (not self-accepted). Standard: done enough to talk about.

## Files
`docs/index.html`, `scripts/check_site.py`, `tests/test_check_site.py`, `report/report.tex`, `docs/report.pdf` (built), `sidecar/runs/05_home_400px.png`, `sidecar/runs/05_home_1200px.png`, README link to the published page. Branch `anna/05-home-page` off `origin/main` (8649f51). Nothing in `src/`, `results/` or `BIG_O.md` changed.

## Acceptance
1. **`python scripts/check_site.py` exits 0: PASS.** Output: `OK: six sections present, every image and local link resolves.` It also fails on sections out of order, missing alt text, and external scripts, stylesheets or images. Links to this repo's GitHub pages are mapped back to files and checked, because GitHub Pages serves only `docs/`, so links into `src/` must be absolute GitHub URLs. Three tests cover it.
2. **Screenshots: done** with headless Chromium at 400 and 1200 px wide, 5200 px tall (full page).
   - 1200 px: two headline plots side by side, two surprise plots side by side, readable diagram, table of code links. **First pass found two bugs, both fixed:** the diagram's note text ran into the MergeSort box and into the RecursiveBinarySearch box. I moved the notes and made the diagram taller.
   - 400 px: single column, plots scale to width, text readable, no page-level horizontal scroll. The class diagram is wider than the screen, so it scrolls sideways inside its own box (deliberate `min-width`); on a phone the right-hand part of the diagram is off-screen until you scroll it. Left as is.
   - My first screenshots were only 2600 px tall and cut the page off; retaken at 5200.
3. **Every number on the page is in BIG_O.md or the CSVs: PASS** by script over the visible text: 1, 2, 4, 320, 640, 204480, 639. Not in that scan: alt text on the plots says "about 481 probes" (BIG_O has 481.25) and "near 9" (8.88). Both are roundings of quoted numbers.
4. **pytest: `82 passed in 3.52s`.** Run in a scratch virtualenv with matplotlib installed. On the system Python, `pytest` stops at collecting `tests/test_plotter.py` because matplotlib is not installed (`ModuleNotFoundError`); that is Hanna's step-03 dependency, not new.
5. `git diff --check` clean; tree clean after the last commit; branch pushed (see hash).

## PDF
Built with `pdflatex` (installed here), 3 pages, no overfull boxes. Includes the sorting and searching figures, both tables generated from the same functions `check_big_o.py` uses, and a discussion. `report/` holds only the `.tex`; build files were removed. I looked at the page images at low resolution only to confirm they render; I did not proof-read the PDF closely.

## Gaps
- The PDF's numbers in prose (2.24, 2.40, 204480, 639, million-item arithmetic) are copied from `BIG_O.md`; `check_site.py` does not check the PDF.
- The report tables repeat `BIG_O.md`'s tables as static text; if the data change, regenerate by hand.
- "Headline plot" caption says bubble, selection and insertion "climb steeply" on log-log axes. Bubble and selection overlap exactly, so the chart shows fewer lines than five.
- Phone diagram scrolls sideways (above).
- No check that GitHub Pages is enabled (Flo's step); the README link will 404 until it is.
- Python 3.9 still untested.

Final code commit: `9a3544d` (this report is committed on top of it).
