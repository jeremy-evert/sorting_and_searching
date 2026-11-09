# Prompts

This folder is a record of how one agent directed another.

**Flo** is the Foreman: it plans, writes the work order, and reviews. **Anna** is the builder: she reads the work order, writes the code, and reports back. Every prompt Flo sent Anna for this repo is saved here, numbered in the order it was sent, before Anna started that step.

```
sidecar/prompts/NN_slug.md          the work order Flo sent
sidecar/reports/NN_slug_report.md   what Anna did, what she ran, what she could not do
```

## What a good prompt contains

Anna cannot lean over and ask a question, so each prompt answers the questions up front.

1. **Where.** The repo, the branch name, and the folder to work in.
2. **Why.** What this step is for and how it fits the whole (`sidecar/DESIGN.md`).
3. **What to build.** Specific files and classes.
4. **Constraints.** What not to do: no globals, no new dependencies, no pushing to `main`.
5. **Acceptance test.** A check that can fail, such as "`pytest` passes and the hand-worked counts match." If Anna can't say whether she passed, the prompt wasn't finished.
6. **What to report.** Commands run, results, anything skipped, and the final commit.

## How to read it

Read `01` first, then its report, then `02`. Notice what the prompts leave out as well as what they say, and how each report's findings shape the next prompt.
