"""SelectionSort: repeatedly pick the smallest remaining value."""

from sortsearch.sorters.base import Sorter


class SelectionSort(Sorter):
    """Selection sort: find the smallest unsorted value and swap it to the front.

    Always about n squared comparisons, but never more than n swaps.
    A swap is only made when the smallest value is not already in place.
    """

    name = "selection"

    def _sort(self, items, counter):
        """Sort items in place by selecting the minimum of the unsorted part."""
        n = len(items)
        for start in range(n - 1):
            smallest = start
            for i in range(start + 1, n):
                counter.comparisons += 1
                if items[i] < items[smallest]:
                    smallest = i
            if smallest != start:
                items[start], items[smallest] = items[smallest], items[start]
                counter.moves += 2
