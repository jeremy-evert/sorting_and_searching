"""Read the CSV result files produced by the experiment manager."""

from dataclasses import dataclass
import csv
from pathlib import Path


@dataclass(frozen=True)
class SortRow:
    """One averaged sorting result."""

    kind: str
    algorithm: str
    size: int
    avg_comparisons: float
    avg_moves: float
    max_depth: int


@dataclass(frozen=True)
class SearchRow:
    """One averaged searching result."""

    algorithm: str
    size: int
    avg_probes: float


def read_sort_rows(path):
    """Load sorting result rows from a CSV file."""
    with Path(path).open(newline="", encoding="utf-8") as source:
        return [
            SortRow(
                kind=row["kind"], algorithm=row["algorithm"],
                size=int(row["size"]),
                avg_comparisons=float(row["avg_comparisons"]),
                avg_moves=float(row["avg_moves"]), max_depth=int(row["max_depth"]),
            )
            for row in csv.DictReader(source)
        ]


def read_search_rows(path):
    """Load searching result rows from a CSV file."""
    with Path(path).open(newline="", encoding="utf-8") as source:
        return [
            SearchRow(
                algorithm=row["algorithm"], size=int(row["size"]),
                avg_probes=float(row["avg_probes"]),
            )
            for row in csv.DictReader(source)
        ]
