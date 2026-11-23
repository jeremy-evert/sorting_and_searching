# Sidecar

The build record for `sorting_and_searching`. Everything **outside** this folder is the product: the code, the tests, the design, the home page. It reads as if it were simply written well. Everything **inside** is how it was made: who asked for what, what came back, and what was unclear along the way.

- `LEDGER.md` : history. One page of what each prompt produced, what mattered, and what is still owed. Update it when a prompt finishes.
- `TASKS.md` : pending work only. When a task is done, delete its line; the ledger keeps the history.
- `DESIGN.md` : the plan and the design. Read it first; it is the truth the reports are measured against.
- `prompts/` : work orders from Flo (Foreman) to Anna (builder), numbered `NN_slug.md`. Open ones sit here; finished ones move to `prompts/completed/` and stay forever.
- `reports/` : Anna's result for each prompt, named `NN_slug_report.md` so it **matches its prompt by number and slug**. A prompt with no report has not been done.
- `questions/` : anything unresolved that needs a person's decision.
- `runs/` : raw or bulky output (logs, CSVs from test runs) that would clutter the product.

Read one prompt and its report together, then the next pair. You do not need the whole folder.

A sidecar file is not authoritative just because it exists. When a report establishes something that is now true of the code, the fact goes into `sidecar/DESIGN.md` or the code, and the report stays as provenance.

## What belongs in a sidecar, and what does not

Put in the sidecar anything that records **how the work was done**: the prompts, the reports, the open questions, raw run output. Keep in the product anything a user of the code needs: the code, its tests, how to run it, the home page.

A worked example from this repo: where does `DESIGN.md` go? It describes the product, which argues for keeping it with the product. But it is also the plan the build was measured against, an artifact of how the work was done. We put it in the sidecar and say so at the top of this file. Another repo could reasonably decide the other way. The skill is to pick a side, give the reason, and write the choice down.

Sub-steps share a number: `02_a_slug.md`, `02_b_slug.md`.
