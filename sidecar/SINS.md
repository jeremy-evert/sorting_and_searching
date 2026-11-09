# Sins: grievances about this repository

A Festivus airing, written on 2026-11-09. These are observations and judgments, not a list of accepted defects. Some repeat `TASKS.md`: they are here because they bother me, not because they have been independently resolved. This is a snapshot, not a verdict on the people or agents who built the work.

## The story we tell

- **The front door is behind the project.** `README.md` says the plots and home page are in progress, although they are present. A showcase should know its own state and give a visitor a direct route to the interesting results and to running the project.
- **The theory is simplified past the point of being quite true.** `BIG_O.md` says Big O is a statement about a doubling ratio. Big O is an asymptotic upper bound; a measured ratio at two sizes can illustrate a growth pattern, but it cannot establish one. The page also presents the two input-sensitive cases as exceptions, though its predictions already account for them.
- **We sound more certain about random quicksort than the evidence allows.** `BIG_O.md` says the observed difference comes from two causes, while `TASKS.md` explicitly says the explanation needs more trials. Five trials and two sizes are a thin basis for attributing the discrepancy.
- **The checkers oversell their reach.** `check_big_o.py` prints that every quoted number matches, but checks the marked tables, not the surrounding prose. `check_site.py` checks structure and local file existence, not whether alt text accurately describes the image, external links work, or the page reads well. Green output can give a stronger impression than the checks deserve.
- **The build record is harder to trust than it needs to be.** `LEDGER.md` leaves prompt 06 open; its report says FAILED, while its branch was merged. Prompt 07 has a report but remains in the open prompts folder and has no ledger row. The README for the record promises a cleaner trail than a new reader actually finds.

## The pictures

- **The search graph uses the wrong reference for the story we are telling.** `plotter.py` draws `n/2`, while half the searches miss and `BIG_O.md` explains that the mixed workload averages roughly `3n/4`. Without context, the reference invites a reader to infer a discrepancy that the workload itself explains.
- **Important curves hide each other.** Bubble and selection have the same comparison counts; both binary searches have the same probe counts. The plots use different markers, but the overlapping series still make comparison harder. The project already knows this and has not settled how to present it.
- **One alt description describes a curve that is not there.** The quicksort image in `docs/index.html` says it includes an `n log n` curve, but `plot_big_o` draws the measured points and one fitted prediction, `n squared` for sorted quicksort. A screen-reader user gets a different picture from a sighted reader.
- **The class diagram asks a phone reader to pan.** The page sets a 560-pixel minimum width and scrolls the diagram inside a box. It is a lot of detail before a newcomer has a simple map of the system.
- **Perceived grievance:** the site leads with small side-by-side graphs and a class diagram, but I have not done a fresh visual or accessibility review. I suspect the strongest story could be clearer and more legible, especially on a phone; that needs a real review, not a claim that it fails.

## The evidence and the code

- **Reproducing the whole exhibit is not a single obvious action.** The experiment and plotting scripts exist, but the README does not take a reader through generating both CSVs and images, and there is no automated check that fresh results match the committed ones. The original hash checks are historical evidence, not a continuous guard.
- **There is no visible automated test matrix.** The project promises Python 3.9 and newer, but there is no committed CI workflow showing supported versions being tested. During this inspection, `python -m pytest -q` produced 74 passed and 8 setup errors because pytest could not create its temporary directory in this environment; that is not evidence of an algorithm failure, nor a full passing run.
- **The design has drifted from its implementation.** `sidecar/DESIGN.md` gives a different `Plotter` interface from the one in `src/sortsearch/plotter.py` and omits `results_io.py` from its layout. It calls itself the truth, so these mismatches matter.
- **The counting rules are easy to misunderstand.** Search comparisons count one three-way decision per probe; sort moves exclude merge's final copy back; sorting's final validation is not counted. These are legitimate conventions, but generic labels like “comparisons” and “moves” can look like counts of every underlying operation. The definitions need to travel with the conclusions.
- **The sorter checks order, not preservation.** `Sorter.sort` rejects an unsorted output, but a broken child that discards or duplicates values could still return a sorted list. Tests check expected output for actual sorters, so this is a limitation of the base-class guarantee, not proof that a current sorter loses data.
- **The “no globals” rule and the code do not agree literally.** The manager and plotter have module-level constants. They are configuration and labels rather than mutable experiment state, but the rule should say that if that is what it means.
- **Perceived grievance:** the inheritance hierarchy may be teaching the requested class structure more than it is simplifying the algorithms. `RecursiveSearcher` and `RecursiveSorter` deserve a beginner-focused review of what each abstraction actually earns; this is a design question, not a demand to flatten them.

## Public polish

- **The published record needs a deliberate privacy review.** `questions/07_history_identity.md` identifies author identity in existing history, and `TASKS.md` records a pending metadata sweep of PDFs and images. The current observation is a known open question, not a claim that every artifact is unsafe. A mailmap can change display; it does not erase historical identities.
- **The root-level field guide is unexplained at the front door.** `Deciding_with_AI_Field_Guide_print.pdf` is prominent in the file list, but the README does not explain its relationship to this project.
- **Perceived grievance:** the formal PDF has not been proofread according to `TASKS.md`, and I have not independently read it for this pass. I would not call the final document polished until someone does.

These grievances are not automatically a work order. Verify the perceived ones, choose the fixes that best serve the showcase, and keep the useful history even when it is messy.
