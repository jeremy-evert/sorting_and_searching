# Tasks

What is still open. One line per task, with where it came from. When a task is done, delete its line and note the commit in the report for the prompt that did it; the ledger (LEDGER.md) keeps the history, this file keeps only what is pending.

Size: S under an hour, M a prompt's worth, L more. Sources: (NN) is a prompt or report number; [class] came from the Week 13 session (de-identified); [review] came from prompt 07's read of the repo; [sins] came from SINS.md (08).

## Prompts

- **06 clarity pass**: names, docstrings, dead code (prompts/06_clarity_pass.md). Its report says FAILED but the branch was merged; decide whether 06 is done, redone, or closed as failed, then move the prompt to completed/ or rewrite it. [sins]
- **07 class notes**: report exists, prompt still in prompts/. Accept it and move it to prompts/completed/. [sins]

## Build record

- **S** LEDGER.md: set the true state of row 06, add a row for 07, and mark 08 reviewed once the SINS decisions below are made. [sins] File: sidecar/LEDGER.md.
- **S** Say what LEDGER.md and TASKS.md each own in sidecar/README.md, one sentence each: "history goes in the ledger, only pending work goes in tasks". [review] File: sidecar/README.md.
- **S** In sidecar/README.md, add two lines on what belongs in a sidecar and what does not, using the DESIGN.md placement decision as the worked example. [class] File: sidecar/README.md.

## Checks not yet done

- **S** Proof-read docs/report.pdf. (05)

## Pictures and the home page

- **M** Fresh visual and accessibility review of the home page at phone and desktop width; record findings before changing anything. [sins] File: sidecar/runs/ (screenshots), then docs/index.html.

## Public safety (before the showcase)

- **Done by 09 (read-only):** the current files and every commit's contents are clean of home paths, tokens, keys and hostnames; PDF and PNG metadata are clean. **Still open, a person's decision:** 40 of 62 commits carry a machine name in the author line (april 25, brandy 13, windows_desktop 2), and 23 carry an institutional email address (10 and 13, two addresses). Rewriting published history is not ours to do; see sidecar/questions/07_history_identity.md.

## Repo layout

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
