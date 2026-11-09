"""Sorter: the abstract parent of every sorting algorithm."""

from abc import ABC, abstractmethod


class Sorter(ABC):
    """Template for a sorting algorithm.

    The public method sort() does the steps that must always happen: copy the
    input, run the algorithm, and check the answer. A child class only writes
    _sort(), the algorithm itself.

    Counting rules shared by all sorters:
      comparisons: one per time two values are compared.
      moves: one per time a value is written into a list position
             (so a swap is 2 moves).
    """

    name = "sorter"

    def sort(self, values, counter):
        """Return a new sorted list; the caller's list is never changed."""
        items = list(values)
        self._sort(items, counter)
        if any(items[i] > items[i + 1] for i in range(len(items) - 1)):
            raise RuntimeError(f"{self.name} produced an unsorted result")
        return items

    @abstractmethod
    def _sort(self, items, counter):
        """Sort items in place, adding to counter as work is done."""
