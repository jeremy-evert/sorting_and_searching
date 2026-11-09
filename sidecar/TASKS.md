# Tasks

What is still open. One line per task, with where it came from. When a task is done, delete its line and note the commit in the report for the prompt that did it; the ledger (`LEDGER.md`) keeps the history, this file keeps only what is pending.

## Prompts

- [ ] **06 clarity pass**: names, docstrings, dead code (`prompts/06_clarity_pass.md`).

## `DESIGN.md` updates

`DESIGN.md` is the truth, so these facts from the reports belong in it. Prompt 06 only lists out-of-date lines and does not rewrite the design, so these need their own step.

- [ ] State the counting conventions: a move is one write and a swap is 2; insertion counts each shift and the placement; merge counts values written while merging (reports 01).
- [ ] Say depth starts at 1 and calls on empty ranges are not counted (01).
- [ ] Add `recursive_searcher.py` to the folder layout (01).
- [ ] Describe how search targets are chosen: even-valued list, present targets from a seeded RNG, absent targets odd (02).
- [ ] Say `max_depth` in a sort row is the maximum over trials, not an average (02).
- [ ] Fix the search table: linear search averages 3n/4 on the mixed workload, not n/2 (04).

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
