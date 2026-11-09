# sorting_and_searching

A public demonstration of code, in two parts:

1. **A modular sorting and searching comparison.** Bubble, insertion, selection, merge and quick sort; linear and binary search (iterative and recursive). It counts operations, plots them, and shows how the curves match Big O.
2. **How one agent directs another.** Every prompt used to build it is in [`prompts/`](prompts/), with the report that came back in `reports/`.

Start with [`DESIGN.md`](DESIGN.md). The home page and Big O write-up are built in later steps.

## Run the tests

```
pip install -e '.[test]'
pytest
```

Status: design done; build in progress (see `prompts/`).

License: BSD 2-Clause.
