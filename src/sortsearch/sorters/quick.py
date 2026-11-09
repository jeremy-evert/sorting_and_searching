"""QuickSort: partition around a pivot, then sort each side."""

from sortsearch.sorters.recursive import RecursiveSorter


class QuickSort(RecursiveSorter):
    """Quick sort that always uses the FIRST element as the pivot.

    This is deliberate. On already-sorted (or reversed) input the pivot is
    the smallest (or largest) value every time, so the split is lopsided,
    the work grows like n squared and the recursion depth equals n. That
    makes the worst case visible in the experiment.
    """

    name = "quick"

    def _sort(self, items, counter):
        """Sort items in place."""
        if not items:
            return
        self._quick_sort(items, 0, len(items) - 1, counter, 1)

    def _quick_sort(self, items, low, high, counter, depth):
        """Sort items[low..high] in place."""
        self._enter(counter, depth)
        if low >= high:
            return
        split = self._partition(items, low, high, counter)
        # Empty sides are skipped, so depth counts only calls on real data.
        if split > low:
            self._quick_sort(items, low, split - 1, counter, depth + 1)
        if high > split:
            self._quick_sort(items, split + 1, high, counter, depth + 1)

    def _partition(self, items, low, high, counter):
        """Move smaller-than-pivot values left of the pivot; return its index."""
        pivot = items[low]
        boundary = low
        for i in range(low + 1, high + 1):
            counter.comparisons += 1
            if items[i] < pivot:
                boundary += 1
                items[boundary], items[i] = items[i], items[boundary]
                counter.moves += 2
        if boundary != low:
            items[low], items[boundary] = items[boundary], items[low]
            counter.moves += 2
        return boundary
