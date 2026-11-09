"""LinearSearch: look at every element from the front."""

from sortsearch.searchers.base import Searcher


class LinearSearch(Searcher):
    """Check each element in order until the target is found.

    Costs about n/2 probes for a hit on average and n for a miss.
    Returns the first matching index.
    """

    name = "linear"

    def _search(self, sorted_values, target, counter):
        """Return the first index of target, or -1."""
        for index in range(len(sorted_values)):
            counter.probes += 1
            counter.comparisons += 1
            if sorted_values[index] == target:
                return index
        return -1
