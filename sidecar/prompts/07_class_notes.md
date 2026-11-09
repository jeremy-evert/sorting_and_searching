# Prompt 07: class notes into TASKS.md

**From:** Flo **To:** Anna **Branch:** `anna/07-class-notes-tasks` off `origin/main`

## Why
The project was launched with a class. Turn what the session showed, and what a fresh read of the repo shows, into pending work in `sidecar/TASKS.md`, without implementing any of it and without putting anything from the class recording in a public repository.

## Do
1. Check the recordings and their hashes against their receipts; stop if a file is locked or unreadable.
2. Transcribe locally. Transcripts are private derived data and stay outside Git.
3. Write a private instructor review: what was taught against the plan, how this project's launch went, where students were stuck, what landed, how the room treated honesty about gaps, and short teaching phrases with timestamps. At most five ranked findings, each naming a file to change.
4. Add a section "For CS2" to that review: reusable moves, activity ideas, and where each Field Guide rule showed up or was missing.
5. On this branch, add a dated section to `sidecar/TASKS.md` and anything a person must decide to `sidecar/questions/`. Include de-identified class-driven items, phrased as design or process improvements and never as quotes, and project-strengthening items from reading the repo. Mark each `[class]` or `[review]` with a size guess. Check each suggested item against the repo and drop any already done. Do not rewrite existing items; add beneath them. Do not implement.
6. Run the name gate on the diff and on any text leaving private storage, plus a second independent check. Counts only.
7. Write `sidecar/reports/07_class_notes_report.md`, push the branch, do not merge or push to `main`.

## Acceptance test
- The instructor review exists in private storage with timestamped claims and at most five ranked findings.
- `TASKS.md` has a new dated section; each item states what, why and which file.
- The name gate reports zero names in the diff, and the diff contains no transcript text.
