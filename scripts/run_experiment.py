"""Run the full experiment and write the CSV result files.

Usage (from the repository root):  python scripts/run_experiment.py
"""

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from sortsearch import (  # noqa: E402
    BinarySearch, BubbleSort, InsertionSort, LinearSearch, MergeSort,
    QuickSort, RecursiveBinarySearch, SelectionSort,
)
from sortsearch.manager import ExperimentManager  # noqa: E402

SORT_HEADER = ["kind", "algorithm", "size", "avg_comparisons", "avg_moves", "max_depth"]
SEARCH_HEADER = ["algorithm", "size", "avg_probes"]


def write_csv(path, header, rows):
    """Write rows to path with LF line endings."""
    with open(path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(header)
        writer.writerows(rows)


def write_results(result, results_dir):
    """Write sort_counts.csv and search_counts.csv into results_dir."""
    results_dir = Path(results_dir)
    results_dir.mkdir(parents=True, exist_ok=True)
    write_csv(results_dir / "sort_counts.csv", SORT_HEADER, [
        [r.kind, r.algorithm, r.size, r.avg_comparisons, r.avg_moves, r.max_depth]
        for r in result.sort_rows])
    write_csv(results_dir / "search_counts.csv", SEARCH_HEADER, [
        [r.algorithm, r.size, r.avg_probes] for r in result.search_rows])


def build_default_manager():
    """Return the manager with all five sorters, three searchers and default sizes."""
    return ExperimentManager(
        sorters=[BubbleSort(), InsertionSort(), SelectionSort(), MergeSort(), QuickSort()],
        searchers=[LinearSearch(), BinarySearch(), RecursiveBinarySearch()],
    )


def main():
    """Run the experiment, write the CSVs and a one-line log."""
    result = build_default_manager().run()
    write_results(result, ROOT / "results")
    log = ROOT / "sidecar" / "runs" / "02_run.log"
    log.parent.mkdir(parents=True, exist_ok=True)
    line = f"wrote {len(result.sort_rows)} sort rows and {len(result.search_rows)} search rows\n"
    with open(log, "w", newline="", encoding="utf-8") as handle:
        handle.write(line)


if __name__ == "__main__":
    main()
