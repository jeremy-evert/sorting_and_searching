"""Create sorting, searching, and Big O comparison plots."""

from collections import defaultdict
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


SORT_NAMES = {
    "bubble": "Bubble sort",
    "insertion": "Insertion sort",
    "selection": "Selection sort",
    "merge": "Merge sort",
    "quick": "Quick sort",
}
SEARCH_NAMES = {
    "linear": "Linear search",
    "binary": "Binary search",
    "recursive binary": "Recursive binary search",
}
SORT_ORDER = tuple(SORT_NAMES)
SEARCH_ORDER = tuple(SEARCH_NAMES)
SORT_COLORS = {
    "bubble": "#0072B2",
    "insertion": "#D55E00",
    "selection": "#009E73",
    "merge": "#CC79A7",
    "quick": "#E69F00",
}
SORT_MARKERS = {
    "bubble": "o",
    "insertion": "s",
    "selection": "^",
    "merge": "D",
    "quick": "P",
}
SEARCH_COLORS = {
    "linear": "#0072B2",
    "binary": "#D55E00",
    "recursive binary": "#009E73",
}
SEARCH_MARKERS = {
    "linear": "o",
    "binary": "s",
    "recursive binary": "^",
}


def fit_constant(measured, shape):
    """Return the least-squares scale for a prediction through the origin."""
    measured = np.asarray(measured, dtype=float)
    shape = np.asarray(shape, dtype=float)
    denominator = float(np.dot(shape, shape))
    if denominator == 0:
        raise ValueError("prediction shape must contain a nonzero value")
    return float(np.dot(shape, measured) / denominator)


def disagreement_flags(measured, predicted, threshold=0.25):
    """Return per-point flags where measurements differ by over the threshold."""
    flags = []
    for actual, expected in zip(measured, predicted):
        if expected == 0:
            flags.append(actual != 0)
        else:
            flags.append(abs(actual - expected) / abs(expected) > threshold)
    return flags


def linear_reference(sizes):
    """Return the expected probes per lookup for linear search on our workload.

    Half the lookups hit (about n/2 probes) and half miss (always n probes),
    so the average is 3n/4.
    """
    return [0.75 * size for size in sizes]


class Plotter:
    """Plot supplied result rows without running experiments or reading files."""

    def __init__(self, sort_rows, search_rows):
        self.sort_rows = list(sort_rows)
        self.search_rows = list(search_rows)

    @staticmethod
    def _finish(figure, path):
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        figure.tight_layout()
        figure.savefig(path, format="png", dpi=150, metadata={"Software": None})
        plt.close(figure)

    @staticmethod
    def _sort_shape(algorithm, kind, sizes):
        if algorithm in ("bubble", "selection"):
            return "n squared", sizes ** 2
        if algorithm == "merge":
            return "n log n", sizes * np.log2(sizes)
        if algorithm == "insertion":
            return ("n", sizes) if kind == "sorted" else ("n squared", sizes ** 2)
        if algorithm == "quick":
            return (("n log n", sizes * np.log2(sizes)) if kind == "random"
                    else ("n squared", sizes ** 2))
        raise ValueError("unknown sorting algorithm: " + algorithm)

    def plot_sorting(self, kind, path):
        """Write a log-log comparisons plot for all sorting algorithms of kind."""
        rows_by_algorithm = defaultdict(list)
        for row in self.sort_rows:
            if row.kind == kind:
                rows_by_algorithm[row.algorithm].append(row)
        if not rows_by_algorithm:
            raise ValueError("no sorting rows for kind: " + kind)
        figure, axis = plt.subplots(figsize=(8, 5))
        for algorithm in SORT_ORDER:
            rows = sorted(rows_by_algorithm.get(algorithm, []), key=lambda row: row.size)
            if rows:
                axis.plot([row.size for row in rows],
                          [row.avg_comparisons for row in rows],
                          marker=SORT_MARKERS[algorithm],
                          markerfacecolor=("white" if algorithm == "bubble" else None),
                          color=SORT_COLORS[algorithm], label=SORT_NAMES[algorithm])
        axis.set_xscale("log")
        axis.set_yscale("log")
        axis.set_xlabel("input size n")
        axis.set_ylabel("comparisons")
        axis.set_title("Sorting comparisons — " + kind + " input")
        axis.grid(True, which="both", alpha=0.25)
        axis.legend()
        self._finish(figure, path)

    def plot_big_o(self, algorithm, kind, path):
        """Plot measured comparisons and a fitted Big O curve for one sorter."""
        if algorithm not in SORT_NAMES:
            raise ValueError("unknown sorting algorithm: " + algorithm)
        rows = sorted(
            (row for row in self.sort_rows
             if row.algorithm == algorithm and row.kind == kind),
            key=lambda row: row.size,
        )
        if not rows:
            raise ValueError("no sorting rows for " + algorithm + " / " + kind)
        sizes = np.asarray([row.size for row in rows], dtype=float)
        measured = np.asarray([row.avg_comparisons for row in rows], dtype=float)
        prediction, shape = self._sort_shape(algorithm, kind, sizes)
        scale = fit_constant(measured, shape)
        predicted = scale * shape
        flags = disagreement_flags(measured, predicted)

        figure, axis = plt.subplots(figsize=(8, 5))
        color = SORT_COLORS[algorithm]
        axis.scatter(sizes, measured, color=color,
                     label="Measured: " + SORT_NAMES[algorithm], zorder=3)
        axis.plot(sizes, predicted, color="#333333", linestyle="--",
                  label="Prediction: " + prediction + " (least-squares fit)")
        if any(flags):
            axis.scatter(sizes[flags], measured[flags], marker="x", s=90,
                          color="#B00020", linewidths=2,
                          label="Over 25% from prediction", zorder=4)
        axis.set_xscale("log")
        axis.set_yscale("log")
        axis.set_xlabel("input size n")
        axis.set_ylabel("comparisons")
        axis.set_title(SORT_NAMES[algorithm] + " — predicted " + prediction +
                       ", measured comparisons (" + kind + " input)")
        axis.grid(True, which="both", alpha=0.25)
        axis.legend()
        self._finish(figure, path)

    def plot_searching(self, path):
        """Write probes-per-lookup plots with 3n/4 and log2 n reference lines."""
        rows_by_algorithm = defaultdict(list)
        for row in self.search_rows:
            rows_by_algorithm[row.algorithm].append(row)
        if not rows_by_algorithm:
            raise ValueError("no searching rows")
        sizes = sorted({row.size for row in self.search_rows})
        figure, axis = plt.subplots(figsize=(8, 5))
        for algorithm in SEARCH_ORDER:
            rows = sorted(rows_by_algorithm.get(algorithm, []), key=lambda row: row.size)
            if rows:
                axis.plot([row.size for row in rows], [row.avg_probes for row in rows],
                          marker=SEARCH_MARKERS[algorithm], color=SEARCH_COLORS[algorithm],
                          markerfacecolor=("white" if algorithm == "binary" else None),
                          label=SEARCH_NAMES[algorithm])
        size_values = np.asarray(sizes, dtype=float)
        axis.plot(size_values, linear_reference(size_values), color="#555555",
                  linestyle="--", label="3n/4 reference (half the lookups miss)")
        axis.plot(size_values, np.log2(size_values), color="#999999", linestyle=":",
                  label="log2 n reference")
        axis.set_xlabel("input size n")
        axis.set_ylabel("probes per lookup")
        axis.set_title("Searching probes per lookup")
        axis.grid(True, alpha=0.25)
        axis.legend()
        self._finish(figure, path)
