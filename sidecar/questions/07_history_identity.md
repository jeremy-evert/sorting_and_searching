# Question 07: author identity in git history

**Asked by:** Anna, prompt 07. **Needs:** a person's decision. **Blocking:** nothing; the showcase can proceed either way.

Commit author lines in the public history include a machine name in the author field and an institutional email address on some commits (the rest use GitHub no-reply addresses). The current tree is clean. `AGENTS.md` says never rewrite published history as routine repair, so I have not touched it.

Options:
1. Leave it. Treat the identities as public already (they are on every clone).
2. Add a `.mailmap` mapping the old identities to the no-reply identity. It changes how `git log` and GitHub display authors, not the commits.
3. Rewrite history with a filter tool and force-push. Destroys commit hashes cited in reports; needs Owner approval and every clone re-cloned.

Recommendation: option 2, and set the author identity on the working machines so new commits stop adding it.
