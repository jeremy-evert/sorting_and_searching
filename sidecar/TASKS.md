# Tasks

What is still open. One line per task, with where it came from. When a task is done, delete its line and note the commit in the report for the prompt that did it; the ledger (LEDGER.md) keeps the history, this file keeps only what is pending.

Size: S under an hour, M a prompt's worth, L more. Sources: (NN) is a prompt or report number; [class] came from the Week 13 session (de-identified); [review] came from prompt 07's read of the repo; [sins] came from SINS.md (08).

## Do first: the README makes a claim nobody has checked

- **S** Run `pytest`, `python scripts/run_experiment.py`, `python scripts/make_plots.py`, then `git status --short`. If any CSV or PNG changes, the README sentence "your CSVs and plots should match the committed ones exactly" is false; fix the sentence or the cause. File: README.md.

## Prompts

- **06 clarity pass**: names, docstrings, dead code (prompts/06_clarity_pass.md). Its report says FAILED but the branch was merged; decide whether 06 is done, redone, or closed as failed, then move the prompt to completed/ or rewrite it. [sins]
- **07 class notes**: report exists, prompt still in prompts/. Accept it and move it to prompts/completed/. [sins]

## Build record

- **S** LEDGER.md: set the true state of row 06, add a row for 07, and mark 08 reviewed once the SINS decisions below are made. [sins] File: sidecar/LEDGER.md.
- **S** Say what LEDGER.md and TASKS.md each own in sidecar/README.md, one sentence each: "history goes in the ledger, only pending work goes in tasks". [review] File: sidecar/README.md.
- **S** In sidecar/README.md, add two lines on what belongs in a sidecar and what does not, using the DESIGN.md placement decision as the worked example. [class] File: sidecar/README.md.

## DESIGN.md is the truth, so it must match the code

- **S** Plotter interface in the class map differs from src/sortsearch/plotter.py; results_io.py and scripts/make_plots.py are missing from the folder layout; the layout says run_experiment.py "writes results and plots". Make the document match the code. [sins] File: sidecar/DESIGN.md.
- **S** Recursive binary search counts empty-range calls; the prompt 06 report records the discrepancy. Confirm DESIGN.md states it once, plainly. (06)
- **S** "No global variables" is not literally true: manager and plotter have module-level constants. Reword the rule to "no mutable module-level state; constants are fine". [sins] Files: sidecar/DESIGN.md, AGENTS.md.
- **S** Make the class diagram readable at projector size and on a phone: split into sorters and searchers, or add a one-glance overview above it. Closes the phone-view decision below. [class] (05) File: sidecar/DESIGN.md.

## Correctness of what we say

- **S** BIG_O.md defines Big O as a doubling ratio. Say it is an upper bound on growth, and that the doubling ratio is how we *illustrate* it from two sizes, not how we prove it. Drop "exceptions" for insertion and quick sort; the predictions already account for them. [sins] File: BIG_O.md.
- **S** BIG_O.md names two causes for the random quicksort gap; five trials cannot carry that. Soften to "likely" until the trials check below is done. [sins] (04) File: BIG_O.md.
- **S** Counting definitions must travel with the conclusions: one short "what we count" box on the home page and in BIG_O.md (a search comparison is one three-way decision per probe; merge moves exclude the final copy back; the final sortedness check is not counted). [sins] Files: docs/index.html, BIG_O.md.
- **S** Checkers oversell: check_big_o.py says every quoted number matches but checks only marked tables; check_site.py checks structure and local files only. Make each success message say exactly what it checked. [sins] Files: scripts/check_big_o.py, scripts/check_site.py.

## Checks not yet done

- **M** Machine-check numbers quoted in prose in BIG_O.md, the home page and report.pdf, not only tables, including the 3n/4 claim. (04, 05) [review] File: scripts/check_site.py.
- **S** Proof-read docs/report.pdf. (05)
- **M** Test the quick-sort-on-random explanation with more than five trials. (04)

## Pictures and the home page

- **S** The search plot draws n/2 as the linear reference, but the mixed workload averages about 3n/4. Draw 3n/4 (or both, labeled) and add a caption saying half the lookups miss. [sins] [review] Files: src/sortsearch/plotter.py, scripts/make_plots.py, docs/index.html.
- **S** The quicksort image's alt text describes an n log n curve that is not drawn. Make every alt text describe what is actually on the image. [sins] File: docs/index.html.
- **M** Fresh visual and accessibility review of the home page at phone and desktop width; record findings before changing anything. [sins] File: sidecar/runs/ (screenshots), then docs/index.html.

## Code

- **S** Sorter.sort checks the output is sorted but not that it holds the same values. Also check it is a permutation of the input (compare sorted copies or a Counter of values), with a test that a broken sorter dropping a value is rejected. [sins] Files: src/sortsearch/sorters/base.py, tests/.
- **S** tests/test_plotter.py fails collection without matplotlib. Add `pytest.importorskip("matplotlib")` above the plotter import. [review] File: tests/test_plotter.py.

## Tests and automation

- **M** GitHub Actions workflow running pytest on Python 3.9 and 3.11 with the test extra; badge in the README. [review] Files: .github/workflows/tests.yml, README.md.
- **M** One command that regenerates results/*.csv and docs/plots/*.png, plus a test that a fresh experiment run matches the committed CSVs. Turns the README's "match exactly" claim into a test. [review] Files: scripts/regenerate.py (new), tests/test_results_reproducible.py (new), README.md.

## Public safety (before the showcase)

- **M** Sweep the whole git history for home paths, hostnames, tokens, email addresses and personal names. Some commit author lines carry a machine name and an institutional email address; rewriting published history is a person's decision: see sidecar/questions/07_history_identity.md. [review] [sins]
- **S** Same sweep over committed PDFs and images (metadata, EXIF, embedded paths): docs/report.pdf, Deciding_with_AI_Field_Guide_print.pdf, docs/plots/. [review]
- **S** docs/report.pdf has blank Title and Author metadata. Set them via hyperref and rebuild. [review] Files: report/report.tex, docs/report.pdf.

## Repo layout

- **S** Decide what lives at the repo root. Proposal: move the Field Guide to docs/ with a versioned name (Deciding_with_AI_Field_Guide_v1.0.2.pdf), update the README link, and say in AGENTS.md which root files are product. [review] Files: README.md, AGENTS.md, docs/.
- **S** .gitignore ignores *.log, yet sidecar/runs/02_run.log is an open question. Decide once; closes the decision below. (02) [review]

## Teaching

- **M** "Find it in the repo": a table mapping each Field Guide v1.0.2 rule to the file or practice that shows it; mark any rule the repo does not yet demonstrate. [review] File: docs/FIELD_GUIDE_MAP.md (new), linked from README.md.
- **M** "Your turn" prompt: a student adds shell sort through the same loop (hand-worked counts, tests, code, report). [review] Files: sidecar/prompts/NN_your_turn_shell_sort.md (next free number), sidecar/prompts/README.md.
- **M** Hand-worked "what is a unit test" page: three lines of code, expected value worked out in a comment, one failing and one passing run. [class] File: docs/WHAT_IS_A_TEST.md (new), linked from AGENTS.md.
- **S** "Pre-publish checklist" prompt a student can give an agent about their own project, with the public-repo rule from AGENTS.md as line one. [class] File: sidecar/prompts/README.md.

## Decisions for a person

- Track sidecar/runs/02_run.log, or keep ignoring *.log? (02)
- Rounding rule for CSV averages, currently raw floats. (02)
- Bubble and selection coincide on combined plots, as do the two binary searches: keep, or draw them apart? (03, 05)
- Phone view of the class diagram: accept the sideways scroll, or redraw (see DESIGN.md item above). (05)
- Do RecursiveSorter and RecursiveSearcher earn their place for a beginner, or flatten them? A design question, not a defect. [sins]
- Delete the merged remote branches (anna/*, hanna/03-plotter, claude/06-design-to-sidecar) and the local codex/08-repo-grievances.
