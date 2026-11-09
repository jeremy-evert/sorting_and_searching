"""RecursiveSearcher: abstract parent for searchers that call themselves."""

from abc import ABC

from sortsearch.searchers.base import Searcher


class RecursiveSearcher(Searcher, ABC):
    """A Searcher that also tracks how deep its recursion goes.

    The first call is depth 1, the call it makes is depth 2, and so on.
    """

    name = "recursive searcher"

    def _enter(self, counter, depth):
        """Call at the start of each recursive call to record its depth."""
        if depth > counter.max_depth:
            counter.max_depth = depth
