"""Sorting classes."""

from sortsearch.sorters.base import Sorter
from sortsearch.sorters.bubble import BubbleSort
from sortsearch.sorters.insertion import InsertionSort
from sortsearch.sorters.selection import SelectionSort
from sortsearch.sorters.recursive import RecursiveSorter
from sortsearch.sorters.merge import MergeSort
from sortsearch.sorters.quick import QuickSort

__all__ = [
    "Sorter", "BubbleSort", "InsertionSort", "SelectionSort",
    "RecursiveSorter", "MergeSort", "QuickSort",
]
