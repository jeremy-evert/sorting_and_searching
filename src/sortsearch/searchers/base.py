"""Searcher: the abstract parent of every search algorithm."""

from abc import ABC, abstractmethod


class Searcher(ABC):
    """Template for a search over a sorted list.

    Counting rules shared by all searchers:
      probes: one per list element looked at.
      comparisons: one per probe (each look decides equal / smaller / larger).
    """

    name = "searcher"

    def search(self, sorted_values, target, counter):
        """Return the index of target in sorted_values, or -1 if absent.

        The list is never changed. If target appears more than once, which
        index is returned depends on the algorithm.
        """
        return self._search(sorted_values, target, counter)

    @abstractmethod
    def _search(self, sorted_values, target, counter):
        """Find target, adding to counter as work is done."""
