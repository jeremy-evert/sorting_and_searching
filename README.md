# sorting_and_searching

[![tests](https://github.com/jeremy-evert/sorting_and_searching/actions/workflows/tests.yml/badge.svg)](https://github.com/jeremy-evert/sorting_and_searching/actions/workflows/tests.yml)

A public demonstration of code, in two parts:

1. **A modular sorting and searching comparison.** Bubble, insertion, selection, merge and quick sort; linear and binary search (iterative and recursive). It counts operations instead of timing them, plots the counts, and checks the curves against Big O.
2. **How one agent directs another.** Every prompt used to build it is in [`sidecar/prompts/`](sidecar/prompts/), with the report that came back in [`sidecar/reports/`](sidecar/reports/).

Published page: <https://jeremy-evert.github.io/sorting_and_searching/>

## Run it yourself

```
pip install -e ".[test]"
pytest
python scripts/regenerate.py --check   # rebuild in a temp folder; do the CSVs match the committed ones?
python scripts/regenerate.py           # rewrite results/*.csv and the 19 plots in docs/plots
python scripts/check_big_o.py          # do the numbers quoted in the docs match the data?
python scripts/check_site.py           # does the home page have its sections, alt text and links?
```

The counts come from fixed seeds and count operations, not seconds, so a fresh run reproduces the committed CSVs **byte for byte** (a test checks this). The plots are drawn from those CSVs. Different matplotlib versions can change a few pixels, so the promise for the pictures is the same data and the same curves, not identical image files. (`run_experiment.py` and `make_plots.py` are the two halves of `regenerate.py` if you want them one at a time.)

## Where to look

- [`sidecar/DESIGN.md`](sidecar/DESIGN.md): the plan and the class design. Start here.
- [`BIG_O.md`](BIG_O.md): Big O explained, checked against our measured numbers.
- [`sidecar/LEDGER.md`](sidecar/LEDGER.md): what each prompt produced. Open work is in [`sidecar/TASKS.md`](sidecar/TASKS.md).
- [`AGENTS.md`](AGENTS.md): the working rules for any agent or person in this repo.
- [`docs/Deciding_with_AI_Field_Guide_v1.0.4.pdf`](docs/Deciding_with_AI_Field_Guide_v1.0.4.pdf): a printable four-page guide to working with an AI assistant (the same guide is on the [Deciding with AI page](https://jeremy-evert.github.io/swosu-computing/deciding-with-ai/)). This repo is a worked example of its habits: define done, run it yourself, save points, say how you used it.

Every report says what it did not finish. For an example, see [report 04](sidecar/reports/04_big_o_report.md), where a number in the prose was caught and corrected against the data.

License: BSD 2-Clause.
