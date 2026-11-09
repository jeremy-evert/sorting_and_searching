"""BinarySearch: halve the search range each step."""

from sortsearch.searchers.base import Searcher


class BinarySearch(Searcher):
    """Look at the middle element and discard the half that cannot hold the target.

    Costs about log2(n) probes. Needs a sorted list.
    """

    name = "binary"

    def _search(self, sorted_values, target, counter):
        """Return an index of target, or -1."""
        low = 0
        high = len(sorted_values) - 1
        while low <= high:
            middle = (low + high) // 2
            counter.probes += 1
            counter.comparisons += 1
            if sorted_values[middle] == target:
                return middle
            if sorted_values[middle] < target:
                low = middle + 1
            else:
                high = middle - 1
        return -1
