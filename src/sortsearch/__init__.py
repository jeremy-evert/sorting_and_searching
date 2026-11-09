"""sortsearch: sorting and searching algorithms that count their own work."""

from sortsearch.counter import Counter
from sortsearch.dataset import DataSet
from sortsearch.searchers import (
    BinarySearch,
    LinearSearch,
    RecursiveBinarySearch,
    RecursiveSearcher,
    Searcher,
)
from sortsearch.sorters import (
    BubbleSort,
    InsertionSort,
    MergeSort,
    QuickSort,
    RecursiveSorter,
    SelectionSort,
    Sorter,
)

__all__ = [
    "Counter", "DataSet",
    "Sorter", "BubbleSort", "InsertionSort", "SelectionSort",
    "RecursiveSorter", "MergeSort", "QuickSort",
    "Searcher", "LinearSearch", "BinarySearch",
    "RecursiveSearcher", "RecursiveBinarySearch",
]
