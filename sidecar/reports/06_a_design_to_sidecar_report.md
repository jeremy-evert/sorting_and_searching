# Report 06_a: move DESIGN.md into the sidecar, and the merges that followed

**From:** Claude **To:** Jeremy **Date:** 2026-11-09
**Terminal state: COMPLETE** (not self-accepted)

There was no prompt for this work. Jeremy asked for it in conversation, so this report has no matching file in `prompts/`. It is numbered `06_a` because the branch was named `claude/06-design-to-sidecar` before prompt 06 (`06_clarity_pass`) appeared on `main`; the two are unrelated, and the name collision is a mistake worth knowing about.

## What was asked, in order
1. Move `DESIGN.md` into `sidecar/` and update `AGENTS.md` to say where to find it. Drop a `Plan.md` (none existed; nothing was deleted).
2. Commit everything and push to `main`.
3. Get all work done, all pull requests accepted, everything on `main` and pushed.
4. Write a durable record of what was done and what mattered (`LEDGER.md`), then a place for open work (`TASKS.md`).

## Choices I made
- **Why `DESIGN.md` moved.** It is the plan for the build, not part of the sorting and searching product. `AGENTS.md` now lists it under "Inside `sidecar/`" and no longer under the product.
- **References rewritten** in `AGENTS.md`, `README.md`, `BIG_O.md`, `PROVENANCE.md`, `sidecar/README.md`, `sidecar/prompts/README.md` and the open prompts `05` and `06`. **Left alone:** the completed prompts and the existing reports, because they are the historical record and still say `DESIGN.md` without the folder.
- **Branch, not `main`, for the first change** (`claude/06-design-to-sidecar`), following `AGENTS.md`. I pushed to `main` only after Jeremy said to.
- **Merge, not rebase,** when `main` had moved on (`a445d6a`, prompt 06 plus `.gitattributes`): `git merge --no-ff`, so history shows the branch.
- **`anna/05-home-page` merged** on Jeremy's instruction to accept all open work. It had four commits that were not on `main`. No open pull requests existed; the branches were pushed but never turned into PRs.
- **The `README.md` conflict.** Both sides edited the "Start with" line. I kept Anna's added line with the published-page link and kept this branch's `sidecar/DESIGN.md` path, so the result has both changes.
- **Two further fixes needed after that merge:** the new home page linked to `blob/main/DESIGN.md`, which made `check_site.py` fail, so I changed it to `blob/main/sidecar/DESIGN.md`; and prompt 05 moved to `prompts/completed/`.
- **`LEDGER.md` and `TASKS.md`** are new. The ledger is history (what was done, what mattered); the tasks file is only what is pending. The ledger points to the tasks file rather than repeating it.
- **Prompt 06 was not run.** It was not asked for and it belongs to the builder.

## Commands and results
- After the conflict fix: `python -m pytest -q` gave `82 passed in 4.87s`. `python scripts/check_site.py` gave `OK: six sections present, every image and local link resolves.`
- Before the fix, the same two commands gave `1 failed, 81 passed` and `FAILED: 1 problem(s)` (the stale `DESIGN.md` link).
- `git diff --check` clean. `git status --short --branch` showed `main...origin/main` with nothing ahead or behind, after the last push.

## Commits, oldest first
- `8c5d901` Move `DESIGN.md` into sidecar and update every reference.
- `cf63ecb` Show `DESIGN.md`'s own place under `sidecar/` in the folder layout. (I had left this edit unstaged in the first commit; I found it when the branch switch refused.)
- `1439414` Merge of `claude/06-design-to-sidecar` into `main`.
- `af72513` Prompt 06 now points at `sidecar/DESIGN.md`.
- `b5c2760` Merge of `anna/05-home-page`, with the README conflict resolved and links fixed.
- `4dcadaa` Add `LEDGER.md`.
- `44103d2` Add `TASKS.md`.

## Gaps
- The remote branches are all merged but still exist. I did not delete them (`AGENTS.md`: ask first). It is a task in `TASKS.md`.
- I merged `anna/05-home-page` without a separate review of its content beyond the tests and `check_site.py` passing. The home page itself was not opened in a browser in this session.
- I pushed small documentation changes straight to `main` after Jeremy's general instruction, which `AGENTS.md` otherwise asks to confirm each time.
- The `DESIGN.md` updates the reports asked for are still not made; they are in `TASKS.md`.
