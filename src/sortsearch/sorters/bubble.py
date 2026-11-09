"""BubbleSort: repeatedly swap neighbours that are out of order."""

from sortsearch.sorters.base import Sorter


class BubbleSort(Sorter):
    """Full bubble sort with no early exit, so every input costs about n squared.

    Pass k compares neighbours up to the last unsorted spot; the largest
    remaining value "bubbles" to the end of the list.
    """

    name = "bubble"

    def _sort(self, items, counter):
        """Sort items in place by comparing and swapping neighbours."""
        n = len(items)
        for end in range(n - 1, 0, -1):
            for i in range(end):
                counter.comparisons += 1
                if items[i] > items[i + 1]:
                    items[i], items[i + 1] = items[i + 1], items[i]
                    counter.moves += 2
