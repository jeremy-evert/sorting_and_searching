"""RecursiveSorter: abstract parent for sorters that call themselves."""

from abc import ABC

from sortsearch.sorters.base import Sorter


class RecursiveSorter(Sorter, ABC):
    """A Sorter that also tracks how deep its recursion goes.

    Depth counts calls: the first call is depth 1, the call it makes is
    depth 2, and so on. Counter.max_depth keeps the deepest value seen.
    """

    name = "recursive sorter"

    def _enter(self, counter, depth):
        """Call at the start of each recursive call to record its depth."""
        if depth > counter.max_depth:
            counter.max_depth = depth
