"""MergeSort: split in half, sort each half, merge."""

from sortsearch.sorters.recursive import RecursiveSorter


class MergeSort(RecursiveSorter):
    """Merge sort: always about n log n, and recursion depth about log n.

    Moves count each value written while merging (the final copy back into
    the list included).
    """

    name = "merge"

    def _sort(self, items, counter):
        """Sort items in place; the work happens in _merge_sort."""
        items[:] = self._merge_sort(items, counter, 1)

    def _merge_sort(self, part, counter, depth):
        """Return a sorted copy of part."""
        self._enter(counter, depth)
        if len(part) <= 1:
            return list(part)
        middle = len(part) // 2
        left = self._merge_sort(part[:middle], counter, depth + 1)
        right = self._merge_sort(part[middle:], counter, depth + 1)
        return self._merge(left, right, counter)

    def _merge(self, left, right, counter):
        """Combine two sorted lists into one sorted list."""
        merged = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            counter.comparisons += 1
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
            counter.moves += 1
        while i < len(left):
            merged.append(left[i])
            i += 1
            counter.moves += 1
        while j < len(right):
            merged.append(right[j])
            j += 1
            counter.moves += 1
        return merged
