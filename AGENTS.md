# AGENTS.md

Instructions for any coding agent (or person) working in this repository. Short on purpose. This repo is a showcase, so these rules are also teaching: they are the working habits that made the build go smoothly.

## What this repo is
A sorting and searching comparison written as clean object-oriented Python, plus a public record of how it was built. Read `sidecar/DESIGN.md` first; it is the plan. Then `sidecar/README.md`.

## Git is the safety belt. Use it, don't ask about it.
Everything here is under version control and pushed to GitHub, so almost any mistake can be undone. That is the reason to work freely inside the rules below.

- **Do without asking:** create a branch, commit, push your branch, run tests, read any file, make a worktree, delete your own scratch files.
- **Do ask first:** push to `main`, force-push, rewrite history, delete a branch you did not create, delete an unmerged branch, change the license, make or change anything outside this repository.
- **Commit small and often.** One commit per class or per tight group of files, with a plain message that says what and why. Stage files by name (`git add path/file.py`), not `git add .`.
- **Branches:** `<agent>/<NN>-<slug>`, one per prompt (`anna/02-manager-and-results`). You never merge your own branch; the reviewer does.
- **Never leave the tree dirty.** Finish with `git status --short` empty and your branch pushed. If something unrelated was already dirty, say so in your report and leave it alone.

## Questions: ask few, ask once, and only the ones a person must answer
- If the repo, the prompt, or `sidecar/DESIGN.md` answers it, don't ask. Read them again.
- If a choice is ordinary and reversible (a name, a file layout, which of two reasonable ways), choose, write the choice in your report, and keep going.
- If you hit a real boundary (a permission, a rule, a tool that refuses), **stop and say what you needed and why.** Don't look for a side door around it, and don't re-ask the same thing reworded. A refusal with a stated reason is information.
- Put anything that needs a person's decision in `sidecar/questions/`, not in a long chat.

## How the repo is organized
- Outside `sidecar/` is the product: `src/`, `tests/`, `scripts/`, `docs/`, `results/`. It should read as if it were simply well made. No process narration in code or docstrings.
- Inside `sidecar/` is how it was made: `DESIGN.md` (the plan and design, read it first), `prompts/NN_slug.md` (the work order) and `reports/NN_slug_report.md` (what came back), always matched by number and slug. Finished prompts move to `prompts/completed/`.
- When the build teaches you something true about the design, update `sidecar/DESIGN.md` and say so in your report. The report is provenance; `sidecar/DESIGN.md` is truth.
- Borrowed code goes in `PROVENANCE.md`: what, from where, what you changed.

## Code rules
- Python 3.9 or newer. Standard library for the classes; `pytest` for tests; `matplotlib` only for plots.
- **Count operations, not seconds.** Counts are exact and repeatable; timings are noise. Fixed seeds everywhere.
- No mutable module-level state. State is passed in (`Counter`, `DataSet`); constants are fine.
- Every class has a docstring of one or two plain sentences, and names a beginner can read. Prefer the obvious version to the clever one.
- Write files with LF line endings (`newline=""`, `lineterminator="\n"`). A mismatch here once broke a project's own tests.
- Classes do one job: algorithms don't print, the manager doesn't draw, the plotter doesn't run experiments.

## Tests that mean something
- A test that only copies what the code printed proves nothing. Work the expected value out **by hand or from the algorithm's definition**, write the reasoning in a comment, then assert it.
- If a test and the code disagree, **stop and report the disagreement.** Do not edit the test until it passes. The disagreement is often the most useful thing you found.
- Say "tests pass" only if you ran them in this session. Paste the command and the summary line in your report.

## Reports: honest beats tidy
Every prompt gets a report: files changed, commands run and their output, which acceptance items passed, what you did not finish, what was unclear, the final commit hash. A listed gap helps the next person; a hidden one costs them an afternoon. End with a terminal state: `COMPLETE`, `HUMAN_GATE` (a person must decide) or `FAILED`. Never mark your own work accepted; the reviewer does.

## Standard of done
"Done enough to talk about" beats "perfect and late." Meet the acceptance test, skip the polish, name the gaps.

## This repository is public
Anything pushed is visible at once and may be copied or cached even if deleted. Never commit secrets, tokens, keys, student data, personal paths, hostnames or private-repo content. If you think you committed something you shouldn't have, say so right away; don't try to quietly rewrite history.

## Starting a session (checklist)
1. `git status --short --branch`; fetch; read `sidecar/DESIGN.md`, this file, and the prompt you were given.
2. Work on your own branch in a clean worktree.
3. Before you finish: tests run, `git diff --check` clean, report written, branch pushed, tree clean.
