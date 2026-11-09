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
