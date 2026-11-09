# Prompt 05: the home page and the LaTeX report

**From:** Flo (Foreman) **To:** Anna (builder) **Date:** 2026-11-09
**Follows:** `01` to `04` (all merged to `main`: classes, results CSVs, 19 plots in `docs/plots/`, `BIG_O.md`).

## Where
Repo `sorting_and_searching`. Branch `anna/05-home-page` off `origin/main`. Fresh worktree. Read `sidecar/DESIGN.md` ("Home page"), `BIG_O.md` and `AGENTS.md` first.

## Why
This is what a visitor sees first. It has two jobs in the order a newcomer needs them: show the result (the picture says bubble sort bends upward and merge sort doesn't), then show the design that produced it (the classes, and how one agent directed another). If a visitor reads only the first screen, they should already understand the point.

## What to build
1. `docs/index.html`: static HTML and CSS, no build step, no framework, works on a phone and in light and dark mode. Sections in this order:
   1. One sentence of what this is, and the two headline plots (`sorting_random.png` and `searching.png`) with a one-line caption each saying what to notice.
   2. "Does the theory match?": the Big O in two short paragraphs, the doubling question, and a link to `BIG_O.md`. Embed `bigo_quick_sorted.png` and `bigo_insertion_sorted.png` as the two surprises and say why each differs from the textbook answer (use `BIG_O.md`'s explanations; do not invent new numbers).
   3. "How it is built": the class diagram. Draw it as a clean inline SVG or HTML/CSS box diagram that shows the inheritance (`Sorter` and `RecursiveSorter` with its two children; `Searcher` and `RecursiveSearcher`; the manager and plotter). Do not rely on Mermaid or any CDN script; the page must work offline.
   4. "Read the code": five links into `src/` (a sorter, the recursive base, the manager, the plotter, a test) with one line on what each shows.
   5. "How one agent directed another": link `sidecar/prompts/completed/` and `sidecar/reports/`, and explain in four sentences the prompt/report pairing and the acceptance tests.
   6. Link to the LaTeX report PDF and to `AGENTS.md`.
2. A small `scripts/check_site.py`: confirms every image and local link in `docs/index.html` points at a file that exists, and that the page has the six sections. Exits non-zero otherwise.
3. `report/report.tex` (standard article class): a 3-to-4 page report with the sorting figure, the searching figure, the two summary tables from `BIG_O.md`, and a short discussion. Build it with `pdflatex` if installed and commit `docs/report.pdf`; if `pdflatex` is not available on the machine, commit the `.tex` only and say so in your report (do not fake a PDF).
4. In `README.md`, add the link to the published page: `https://jeremy-evert.github.io/sorting_and_searching/` (GitHub Pages must be enabled; Flo will do that, not you).

## Constraints
`AGENTS.md` applies. Do not edit `src/`, `results/` or `BIG_O.md`; if you find a wrong number, report it. Images use relative paths. Alt text on every image. No external fonts, scripts or images. Public repo: no secrets, hostnames, personal paths. Nothing to `main`; push your branch.

## Acceptance test
1. `python scripts/check_site.py` exits 0.
2. Open the page in a real browser (headless Chromium screenshot is fine) at about 400 px and 1200 px wide; save the two screenshots under `sidecar/runs/` and say in your report what you saw and fixed.
3. Every number on the page also appears in `BIG_O.md` or the CSVs.
4. `pytest` passes (all tests; give the summary line).
5. `git status --short` is clean and the branch is pushed.

## Report
`sidecar/reports/05_home_page_report.md`: files, commands with output, the two screenshots' findings, whether the PDF was built, gaps, final commit hash. Terminal state COMPLETE / HUMAN_GATE / FAILED. Do not mark your own work accepted. Standard: done enough to talk about.
