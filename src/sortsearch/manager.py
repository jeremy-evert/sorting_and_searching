"""ExperimentManager: runs the algorithms on generated data and collects counts."""

import random
from dataclasses import dataclass, field
from typing import List

from sortsearch.counter import Counter
from sortsearch.dataset import DataSet

DEFAULT_SIZES = (10, 20, 40, 80, 160, 320, 640)
DEFAULT_KINDS = ("random", "sorted", "reversed")
SEARCH_TARGETS = 200


@dataclass
class SortRow:
    """Average comparisons and moves, and maximum depth, over the trials."""

    kind: str
    algorithm: str
    size: int
    avg_comparisons: float
    avg_moves: float
    max_depth: int


@dataclass
class SearchRow:
    """Average probes per lookup for one algorithm and size."""

    algorithm: str
    size: int
    avg_probes: float


@dataclass
class ExperimentResult:
    """All rows from one experiment run."""

    sort_rows: List[SortRow] = field(default_factory=list)
    search_rows: List[SearchRow] = field(default_factory=list)


class ExperimentManager:
    """Runs every sorter and searcher over every size and returns the counts.

    It never prints, writes files or draws. Everything it needs is passed in.
    """

    def __init__(self, sorters, searchers, sizes=DEFAULT_SIZES,
                 kinds=DEFAULT_KINDS, trials=5):
        """Remember what to run."""
        self.sorters = list(sorters)
        self.searchers = list(searchers)
        self.sizes = list(sizes)
        self.kinds = list(kinds)
        self.trials = trials

    def run(self):
        """Run the whole experiment and return an ExperimentResult."""
        result = ExperimentResult()
        result.sort_rows = self._run_sorting()
        result.search_rows = self._run_searching()
        return result

    def _run_sorting(self):
        """Measure each sorter on each kind and size, averaged over trials."""
        rows = []
        for kind in self.kinds:
            for sorter in self.sorters:
                for size in self.sizes:
                    rows.append(self._measure_sorter(kind, sorter, size))
        return rows

    def _measure_sorter(self, kind, sorter, size):
        """Measure one sorter; trial t uses seed size*1000+t."""
        total_comparisons = 0
        total_moves = 0
        deepest = 0
        for trial in range(self.trials):
            data = DataSet.make(kind, size, size * 1000 + trial)
            counter = Counter()
            sorter.sort(data.values, counter)
            total_comparisons += counter.comparisons
            total_moves += counter.moves
            deepest = max(deepest, counter.max_depth)
        return SortRow(kind, sorter.name, size,
                       total_comparisons / self.trials,
                       total_moves / self.trials, deepest)

    def _run_searching(self):
        """Measure each searcher on the same targets at each size."""
        rows = []
        for size in self.sizes:
            values = [2 * i for i in range(size)]  # distinct, even numbers
            targets = self._make_targets(values, size)
            for searcher in self.searchers:
                counter = Counter()
                for target in targets:
                    searcher.search(values, target, counter)
                rows.append(SearchRow(searcher.name, size,
                                      counter.probes / len(targets)))
        return rows

    def _make_targets(self, values, size):
        """Return 200 targets, alternating present and absent (odd numbers are absent)."""
        rng = random.Random(size)
        targets = []
        for i in range(SEARCH_TARGETS):
            if i % 2 == 0:
                targets.append(values[rng.randrange(size)])
            else:
                targets.append(2 * rng.randrange(size) + 1)
        return targets
