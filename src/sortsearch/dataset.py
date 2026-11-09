"""DataSet: reproducible input lists for the experiments."""

import random
from dataclasses import dataclass, field
from typing import List

KINDS = ("random", "sorted", "reversed")


@dataclass
class DataSet:
    """A list of distinct integers 0..size-1 in a chosen order.

    The same kind, size and seed always give the same list.
    """

    kind: str
    size: int
    seed: int
    values: List[int] = field(default_factory=list)

    @classmethod
    def make(cls, kind, size, seed):
        """Build a DataSet of the given kind ('random', 'sorted' or 'reversed').

        Raises ValueError for an unknown kind or a negative size.
        """
        if kind not in KINDS:
            raise ValueError(f"unknown kind {kind!r}; expected one of {KINDS}")
        if size < 0:
            raise ValueError("size must not be negative")
        values = list(range(size))
        if kind == "random":
            random.Random(seed).shuffle(values)
        elif kind == "reversed":
            values.reverse()
        return cls(kind=kind, size=size, seed=seed, values=values)
