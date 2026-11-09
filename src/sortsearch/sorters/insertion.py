"""InsertionSort: grow a sorted prefix one value at a time."""

from sortsearch.sorters.base import Sorter


class InsertionSort(Sorter):
    """Insertion sort: take the next value and slide it left into place.

    Fast (about n) on sorted input, about n squared on random or reversed input.
    Each larger value shifted right is 1 move, and the held value is written
    down once per round (1 move), even if it ends up where it started.
    """

    name = "insertion"

    def _sort(self, items, counter):
        """Sort items in place by inserting each value into the sorted prefix."""
        for i in range(1, len(items)):
            held = items[i]
            j = i - 1
            while j >= 0:
                counter.comparisons += 1
                if items[j] <= held:
                    break
                items[j + 1] = items[j]
                counter.moves += 1
                j -= 1
            items[j + 1] = held
            counter.moves += 1
