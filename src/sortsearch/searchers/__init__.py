"""Searching classes."""

from sortsearch.searchers.base import Searcher
from sortsearch.searchers.linear import LinearSearch
from sortsearch.searchers.binary import BinarySearch
from sortsearch.searchers.recursive_searcher import RecursiveSearcher
from sortsearch.searchers.recursive_binary import RecursiveBinarySearch

__all__ = [
    "Searcher", "LinearSearch", "BinarySearch",
    "RecursiveSearcher", "RecursiveBinarySearch",
]
