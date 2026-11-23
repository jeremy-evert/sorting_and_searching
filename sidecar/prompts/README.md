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

## A prompt you can give an agent about your own project: "is it ready to go public?"

Copy this, fill in the project name, and give it to an AI assistant that can read your repository. Line one is a rule, not a suggestion.

```
My project is called <NAME>. I plan to make its repository public.

Rule 1: anything I push is visible at once and may be copied or cached even if I
delete it later. Never commit secrets, passwords, tokens or keys, private data
about other people, personal file paths, or computer names.

Read the whole repository, then give me a numbered task list of what to do
before it goes public. Check, and say what you actually checked:
1. Secrets, passwords, tokens, personal paths or computer names, in the files
   and in the git history.
2. Does the README say what this is, how to run it, and how to run the tests?
3. Do the tests run and pass? (Run them and show me the output.)
4. Is there a license, and is the folder layout something a stranger can follow?
5. Does everything the README promises actually work?
Do not fix anything yet. Sort the list by how much it matters, mark each item
S (under an hour), M or L, and tell me the one thing that would hurt most if it
were wrong.
```

Then do the list one item at a time, commit after each, and run the tests before you say you are done.
