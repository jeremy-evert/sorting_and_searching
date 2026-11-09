"""RecursiveBinarySearch: binary search written as a function that calls itself."""

from sortsearch.searchers.recursive_searcher import RecursiveSearcher


class RecursiveBinarySearch(RecursiveSearcher):
    """Same steps as BinarySearch, so it returns the same index every time.

    Each call handles one range and calls itself on the half that remains.
    """

    name = "recursive binary"

    def _search(self, sorted_values, target, counter):
        """Return an index of target, or -1."""
        return self._look(sorted_values, target, 0, len(sorted_values) - 1, counter, 1)

    def _look(self, sorted_values, target, low, high, counter, depth):
        """Search sorted_values[low..high] for target."""
        self._enter(counter, depth)
        if low > high:
            return -1
        middle = (low + high) // 2
        counter.probes += 1
        counter.comparisons += 1
        if sorted_values[middle] == target:
            return middle
        if sorted_values[middle] < target:
            return self._look(sorted_values, target, middle + 1, high, counter, depth + 1)
        return self._look(sorted_values, target, low, middle - 1, counter, depth + 1)
