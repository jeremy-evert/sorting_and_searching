# Tasks

What is still open. One line per task, with where it came from. When a task is done, delete its line and note the commit in the report for the prompt that did it; the ledger (`LEDGER.md`) keeps the history, this file keeps only what is pending.

## Prompts

- [ ] **06 clarity pass**: names, docstrings, dead code (`prompts/06_clarity_pass.md`).

## `DESIGN.md` updates

The counting, depth, layout, target selection, aggregation and search workload updates are recorded in `DESIGN.md`. Recursive binary search counts empty-range calls; see the prompt 06 report for the discrepancy.

## Checks not yet done

- [ ] Run the tests on Python 3.9 (only 3.12 has been run).
- [ ] Machine-check numbers quoted in prose in `BIG_O.md`, the home page and `report.pdf` (only tables are checked) (04, 05).
- [ ] Proof-read `docs/report.pdf` (05).
- [ ] Test the quick-sort-on-random explanation with more than five trials (04).

## Decisions for a person

- [ ] Enable GitHub Pages on `/docs`; the README link returns 404 until then.
- [ ] Track `sidecar/runs/02_run.log`? `.gitignore` ignores `*.log` (02).
- [ ] Set a rounding rule for CSV averages, currently raw floats (02).
- [ ] Bubble and selection coincide on combined plots, as do the two binary searches: keep, or draw them apart? (03, 05)
- [ ] Phone view: the class diagram scrolls sideways inside its box; accept or redraw (05).
- [ ] Delete the merged remote branches (`anna/*`, `hanna/03-plotter`, `claude/06-design-to-sidecar`).

## 2026-11-09 class notes and review (prompt 07, Anna)

Added beneath the existing sections; nothing above was rewritten. Items are phrased as design or process improvements. Each says what, why and which file. `[class]` came from how the Week 13 session went (de-identified); `[review]` came from reading the repo. Size: S under an hour, M a prompt's worth, L more. None are implemented.

### Stale lines to delete (this file's own rule: a done task loses its line)

- [ ] **[review] S** Delete "Enable GitHub Pages on `/docs`" under *Decisions for a person*. Why: the Pages API reports the site built at the published URL. File: `sidecar/TASKS.md`.
- [ ] **[review] S** Delete "Run the tests on Python 3.9" under *Checks not yet done*. Why: the lead Foreman reports 82 passed on 3.9 and 3.11. I could not re-run it (no 3.9 on the machine used for this review), so the CI item below is what makes the claim checkable by anyone. File: `sidecar/TASKS.md`.

### Tests and automation

- [ ] **[review] S** `tests/test_plotter.py` imports `sortsearch.plotter`, which imports `matplotlib` at module level, so collection errors on an install without it. Add `pytest.importorskip("matplotlib")` above the plotter import so the rest of the suite still runs. Why: `pip install -e .` without the `test` extra should not fail collection. File: `tests/test_plotter.py`.
- [ ] **[review] M** Add a GitHub Actions workflow that runs `pytest` on Python 3.9 and 3.11 (install with the `test` extra). Why: a visitor sees a green badge, and the "say tests pass only if you ran them" rule in `AGENTS.md` becomes something the repo shows. Add the badge to the README. Files: `.github/workflows/tests.yml`, `README.md`.
- [ ] **[review] M** One command that regenerates `results/*.csv` and `docs/plots/*.png` (a `scripts/regenerate.py` or `Makefile` target), plus a test that a fresh run of the experiment matches the committed CSVs. Why: the CSV is already hash-checked by hand (report 02); this makes it a test, and gives students "run it yourself" in one line. Files: `scripts/` (new), `tests/test_results_reproducible.py` (new), `README.md`.
- [ ] **[review] S** Machine-check the home page and `docs/report.pdf` prose numbers, not only tables (existing item) and add the 3n/4 claim to that check. File: `scripts/check_site.py`.

### Public safety (before the showcase)

- [ ] **[review] M** Sweep the whole git history, not only the current tree, for home paths, hostnames, tokens, email addresses and personal names. Current tree: a search for home paths, mount points, tokens and addresses found nothing. History: some commit author lines carry a machine name and an institutional email address. Rewriting published history is not routine, so this is a question for a person: see `sidecar/questions/07_history_identity.md`. Files: none until decided.
- [ ] **[review] S** Run the same sweep over the committed PDFs and images (metadata, EXIF, embedded paths). File: `docs/report.pdf`, `Deciding_with_AI_Field_Guide_print.pdf`, `docs/plots/`.
- [ ] **[review] S** `docs/report.pdf` has a blank Author and Title in its metadata even though `report/report.tex` sets `\author`. Set `\title` and `\author` metadata (for example `hyperref` `pdfauthor`) and rebuild. Files: `report/report.tex`, `docs/report.pdf`.

### Repo layout and README

- [ ] **[review] S** The README status line ("plots, Big O write-up and home page in progress") is stale; the ledger shows all of it merged. Replace it with a one-line current status that points to `sidecar/LEDGER.md` and the published page, and drop "The home page and Big O write-up are built in later steps." File: `README.md`.
- [ ] **[review] S** Decide what lives at the repo root. Today: `Deciding_with_AI_Field_Guide_print.pdf`, `BIG_O.md`, `PROVENANCE.md`, `report/` (the LaTeX source for `docs/report.pdf`) and `AGENTS.md`. Proposal: move the Field Guide to `docs/` with a versioned filename (`Deciding_with_AI_Field_Guide_v1.0.2.pdf`), link it from the README, and say in `AGENTS.md` which root files are product and which are not. I found no root-level `prompts/` on `origin/main`; prompts live only in `sidecar/prompts/`, so there is nothing to move there. Files: `README.md`, `AGENTS.md`, `docs/`.
- [ ] **[review] S** `.gitignore` ignores `*.log`, yet an open item asks whether to track `sidecar/runs/02_run.log`. Decide once and close both. File: `.gitignore` or `sidecar/TASKS.md`.
- [ ] **[review] S** Say what `LEDGER.md` and `TASKS.md` each own in `sidecar/README.md`. `LEDGER.md` already says open work lives in `TASKS.md`; the sidecar README should state it once, in one sentence each, with the rule "history goes in the ledger, only pending work goes in tasks". File: `sidecar/README.md`.

### Field Guide and teaching

- [ ] **[review] M** "Find it in the repo": a table mapping each Field Guide v1.0.2 rule (define done first, run it yourself, keep save points, say how you used it, cross-check with a second AI) to the file or practice that shows it, for example acceptance tests in `sidecar/prompts/`, "Tests that mean something" in `AGENTS.md`, branches and commits in `AGENTS.md`, the report's commands section, and the `check_*.py` scripts. Mark any rule the repo does not yet demonstrate. File: `docs/FIELD_GUIDE_MAP.md` (new), linked from `README.md`.
- [ ] **[review] M** A "Your turn" prompt that asks a student to add one new sorter (for example shell sort) through the same prompt and report loop: hand-worked expected counts first, tests second, code third, report last. Use it as the template for next week. Files: `sidecar/prompts/07_your_turn_shell_sort.md` (draft), `sidecar/prompts/README.md`.
- [ ] **[review] S** The searching plot needs a caption that says linear search averages 3n/4 on the mixed workload (half hits, half misses). `BIG_O.md` explains it; the plot and home page do not. Files: `docs/index.html`, `scripts/make_plots.py`.
- [ ] **[class] S** Add a "Run it yourself" block at the top of the README: install, run the tests, run the experiment, regenerate the plots, in four lines. Why: the design was walked through in class, but the tests and the experiment were not run in the room. File: `README.md`.
- [ ] **[class] M** Add a short, hand-worked "what is a unit test" example (three lines of code, the expected value worked out in a comment, one failing and one passing run) that a beginner can read before the tests directory. Why: the session mentioned unit tests as an important late step, but they had not been taught earlier in the course. File: `docs/` (new `WHAT_IS_A_TEST.md`), linked from `AGENTS.md` "Tests that mean something".
- [ ] **[class] S** In `sidecar/README.md`, add two lines on what belongs in a sidecar and what does not, using the DESIGN.md placement decision as the worked example (the design is how it was made, not what is made). Why: the idea was new to the room and clicked only after a concrete example. File: `sidecar/README.md`.
- [ ] **[class] S** Make the class diagram readable at projector size and on a phone: either split it into "sorters" and "searchers" diagrams or add a one-glance overview above it. Combines with the existing phone-view item. File: `sidecar/DESIGN.md`.
- [ ] **[class] S** Add the "pre-publish checklist" prompt a student can give an agent about their own project ("what must be true before this goes public"), as `sidecar/prompts/README.md` guidance, with the public-repo rule from `AGENTS.md` as the checklist's first line. Why: next steps for the class are getting their own projects ready to publish. File: `sidecar/prompts/README.md`.
- [ ] **[class] S** Put the honesty rule where a visitor looks first: one line in the README saying every report lists what it did not finish, with a link to one example. File: `README.md`.
