# sorting_and_searching

A public demonstration of code, in two parts:

1. **A modular sorting and searching comparison.** Bubble, insertion, selection, merge and quick sort; linear and binary search (iterative and recursive). It counts operations instead of timing them, plots the counts, and checks the curves against Big O.
2. **How one agent directs another.** Every prompt used to build it is in [`sidecar/prompts/`](sidecar/prompts/), with the report that came back in [`sidecar/reports/`](sidecar/reports/).

Published page: <https://jeremy-evert.github.io/sorting_and_searching/>

## Run it yourself

```
pip install -e ".[test]"
pytest
python scripts/run_experiment.py
python scripts/make_plots.py
```

The counts come from fixed seeds, so your CSVs and plots should match the committed ones exactly.

## Where to look

- [`sidecar/DESIGN.md`](sidecar/DESIGN.md): the plan and the class design. Start here.
- [`BIG_O.md`](BIG_O.md): Big O explained, checked against our measured numbers.
- [`sidecar/LEDGER.md`](sidecar/LEDGER.md): what each prompt produced. Open work is in [`sidecar/TASKS.md`](sidecar/TASKS.md).
- [`AGENTS.md`](AGENTS.md): the working rules for any agent or person in this repo.
- [`Deciding_with_AI_Field_Guide_print.pdf`](Deciding_with_AI_Field_Guide_print.pdf): a printable guide to working with AI. This repo is a worked example of its habits.

Every report says what it did not finish. For an example, see [report 04](sidecar/reports/04_big_o_report.md), where a number in the prose was caught and corrected against the data.

License: BSD 2-Clause.
