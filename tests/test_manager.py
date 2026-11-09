import importlib.util
import time
from pathlib import Path

import pytest

from sortsearch import (
    BinarySearch, BubbleSort, InsertionSort, LinearSearch, MergeSort,
    QuickSort, RecursiveBinarySearch, SelectionSort,
)
from sortsearch.manager import ExperimentManager

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "run_experiment.py"


def load_script():
    spec = importlib.util.spec_from_file_location("run_experiment", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def full_result():
    return load_script().build_default_manager().run()


def sort_row(result, kind, algorithm, size):
    matches = [r for r in result.sort_rows
               if (r.kind, r.algorithm, r.size) == (kind, algorithm, size)]
    assert len(matches) == 1
    return matches[0]


def test_tiny_run_is_fast_and_complete():
    start = time.time()
    manager = ExperimentManager(
        [BubbleSort(), QuickSort()], [LinearSearch(), BinarySearch()],
        sizes=[4, 8], trials=2)
    result = manager.run()
    assert time.time() - start < 1.0
    assert len(result.sort_rows) == 3 * 2 * 2
    assert len(result.search_rows) == 2 * 2


def test_run_is_repeatable():
    def make():
        return ExperimentManager([InsertionSort()], [LinearSearch()], sizes=[10, 20], trials=3)
    assert make().run() == make().run()


def test_row_counts(full_result):
    assert len(full_result.sort_rows) == 105
    assert len(full_result.search_rows) == 21


# These follow from the algorithms, not from the program's output.
def test_exact_values_at_640(full_result):
    n = 640
    pairs = n * (n - 1) // 2
    assert pairs == 204480
    for kind in ("random", "sorted", "reversed"):
        assert sort_row(full_result, kind, "bubble", n).avg_comparisons == pairs
        assert sort_row(full_result, kind, "selection", n).avg_comparisons == pairs
        assert sort_row(full_result, kind, "merge", n).avg_comparisons <= 640 * 10
    assert sort_row(full_result, "sorted", "insertion", n).avg_comparisons == n - 1
    assert sort_row(full_result, "sorted", "quick", n).avg_comparisons == pairs


def test_binary_pair_probes_identical(full_result):
    by_algorithm = {}
    for r in full_result.search_rows:
        by_algorithm.setdefault(r.algorithm, {})[r.size] = r.avg_probes
    assert by_algorithm["binary"] == by_algorithm["recursive binary"]


def test_script_writes_lf_csvs(tmp_path):
    script = load_script()
    manager = ExperimentManager([BubbleSort(), InsertionSort(), SelectionSort(),
                                 MergeSort(), QuickSort()],
                                [LinearSearch(), BinarySearch(), RecursiveBinarySearch()],
                                sizes=[4, 8], trials=2)
    script.write_results(manager.run(), tmp_path)
    for name, data_rows in (("sort_counts.csv", 30), ("search_counts.csv", 6)):
        raw = (tmp_path / name).read_bytes()
        assert b"\r" not in raw
        lines = raw.decode().split("\n")
        assert lines[-1] == ""
        assert len(lines) - 2 == data_rows
