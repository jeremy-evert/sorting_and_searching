# Session review: tidying the front door with Copilot (2026-11-09)

A record of one working session in which a person, Copilot (planner and reviewer) and the terminal tidied the public face of this repository. It is not a numbered prompt, so it has no matching report; it lives in `sidecar/runs/` as raw provenance. What it established that is now true already lives in `README.md`, `sidecar/TASKS.md` and `docs/`.

## How the work was split

| Role | Who |
|---|---|
| Ran commands, saved files, committed, pushed | The person, in PowerShell |
| Read the evidence, explained it, wrote replacement files | Copilot |
| Decided what was accepted | The person |

Copilot cannot see a local working tree. It could read only part of the public GitHub page, and the copy it got was out of date (it still showed `DESIGN.md` at the root). So every decision was based on snapshot files the person generated and uploaded, not on Copilot's view of GitHub.

**Good:** the snapshots were the single source of truth, so Copilot never had to guess at the repo's state.
**Lesson:** an AI's view of a website is not evidence. Ask your terminal.

## What we did, in order

| # | Step | Commit |
|---|---|---|
| 1 | Generated `repo_snapshot.txt` and `sidecar_snapshot.txt` (read-only) and uploaded them | — |
| 2 | Committed both snapshots with `git add .`; they landed in `sidecar/reports/` | `fe5037e` |
| 3 | Moved them to `sidecar/runs/` with `git mv` | `2f7fe3d` |
| 4 | Replaced the root `README.md`: current status, a run-it-yourself block, where to look, the Field Guide explained | `151c907` |
| 5 | First `TASKS.md` replacement: removed finished README, Pages and Python 3.9 lines | `cc85668` |
| 6 | Second `TASKS.md` replacement: brought in the `SINS.md` grievances and grouped tasks by the kind of work | between `cc85668` and `4145a35` |
| 7 | Explained `pyproject.toml` and turned it into a handout, `docs/WHAT_IS_PYPROJECT_TOML.md` | `4b3bddb` |

## What went well, and why

- **Evidence first.** Snapshots before changes meant every replacement file was written against the real contents, not memory.
- **One document at a time.** Narrowing to a single file per step kept each commit small and each diff readable, which is the habit `AGENTS.md` asks for.
- **Whole-file downloads beat pasted scripts.** Once the person said "just give me the file," the work sped up and stopped breaking. A saved file has no clipboard, shell-quoting or HTML-link problems.
- **Stage by name.** `git add README.md`, `git add sidecar/TASKS.md` and `git add docs/...` kept scratch files out of commits after step 2.
- **`git mv` for the fix.** Moving the snapshots kept their history and showed the correction openly instead of hiding it.
- **The repo's own rules did the steering.** `AGENTS.md` and `sidecar/README.md` decided where files belonged (`reports/` holds only numbered reports; raw output goes to `runs/`; handouts go to `docs/`).
- **A useful tangent became an artifact.** A curious question ("what is TOML, and does it have to be at the root?") became a handout students can use.

## What went badly, and why

- **`git add .` on main (step 2).** It committed the snapshots into the wrong folder. `AGENTS.md` says to stage by name. The fix cost one extra commit; the lesson is cheaper than the fix.
- **A paste that broke (step 4).** Copilot put a code block inside another code block. The chat display split it, and the paste turned into a broken PowerShell here-string that had to be stopped with Ctrl+C. This was Copilot's fault. The fix was to switch to downloadable files.
- **Rich-text paste.** Copying from the chat turned the README's URL into HTML link markup. Plain text or file downloads avoid this.
- **A claim committed before it was checked.** The new README says a fresh run reproduces the committed CSVs and plots exactly. It was committed without running that check. It is now the first item in `TASKS.md`.
- **The first `TASKS.md` pass was too shallow.** It cleaned up finished lines but missed about ten grievances already written down in `SINS.md`. A second pass fixed it. Lesson: when tidying a task list, read every source of tasks, not just the list.
- **Saved to the wrong folder once (step 7).** The handout was first saved at the repo root, so `git add docs/...` failed. `git status` showed the untracked file, the person moved it, and it went in cleanly. Git's error message did its job.
- **Work on `main` directly.** `AGENTS.md` asks agents to use a branch per prompt. This session committed straight to `main` because a person was doing small, reviewed documentation edits. Acceptable here, but worth saying out loud.
- **Unexplained push size.** The README push sent 26 objects (about 1 MiB), far more than one small file. There was already one local commit ahead of `origin/main` before it. `git log --stat -3` was suggested but not yet run, so the cause is unknown.

## Still open from this session

1. Run the "Do first" check in `sidecar/TASKS.md` (`pytest`, both scripts, then `git status --short`) and fix the README sentence or the cause.
2. Run `git log --stat -4` around `151c907` and record what the 1 MiB push contained.
3. Check the two committed snapshot files in `sidecar/runs/` for personal paths, user names or hostnames. This repository is public.
4. Next document in the one-at-a-time pass: `sidecar/LEDGER.md` (true state of row 06, a row for 07, 08 marked reviewed).

## Habits to keep

- Take a read-only snapshot before asking for advice; give the advisor the file, not a description.
- Ask for whole-file replacements you download and save, not scripts that edit in place.
- `git status` before every `git add`, and stage files by name.
- Don't commit a claim you have not run.
- When something goes wrong, fix it in a new commit and say so. Do not rewrite public history.
