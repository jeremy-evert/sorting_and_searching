import math
from pathlib import Path

import pytest

pytest.importorskip("matplotlib")

from sortsearch.plotter import Plotter, disagreement_flags, fit_constant, linear_reference
from sortsearch.results_io import read_search_rows, read_sort_rows


ROOT = Path(__file__).parent
FIXTURES = ROOT / "fixtures"


def test_fixture_readers_accept_prompt_02_search_label():
    sort_rows = read_sort_rows(FIXTURES / "sort_counts.csv")
    search_rows = read_search_rows(FIXTURES / "search_counts.csv")

    assert len(sort_rows) == 105
    assert len(search_rows) == 21
    assert {row.algorithm for row in search_rows} == {
        "linear", "binary", "recursive binary"
    }


def test_plot_methods_write_png_files(tmp_path):
    plotter = Plotter(
        read_sort_rows(FIXTURES / "sort_counts.csv"),
        read_search_rows(FIXTURES / "search_counts.csv"),
    )
    sorting = tmp_path / "sorting.png"
    big_o = tmp_path / "big_o.png"
    searching = tmp_path / "searching.png"

    plotter.plot_sorting("random", sorting)
    plotter.plot_big_o("merge", "random", big_o)
    plotter.plot_searching(searching)

    for path in (sorting, big_o, searching):
        assert path.read_bytes()[:8] == b"\x89PNG\r\n\x1a\n"


def test_fit_constant_recovers_exact_n_log_n_scale():
    sizes = [10, 20, 40, 80, 160, 320, 640]
    shape = [n * math.log2(n) for n in sizes]
    measured = [3 * value for value in shape]

    assert fit_constant(measured, shape) == 3.0


def test_disagreement_flag_marks_wrong_prediction():
    assert disagreement_flags([100, 100], [100, 50]) == [False, True]


def test_script_writes_all_nineteen_pngs(tmp_path):
    import subprocess
    import sys

    script = ROOT.parent / "scripts" / "make_plots.py"
    result = subprocess.run(
        [sys.executable, str(script), "--results", str(FIXTURES), "--out", str(tmp_path)],
        cwd=ROOT.parent, check=True, capture_output=True, text=True,
    )
    assert "Wrote 19 PNGs" in result.stdout
    assert len(list(tmp_path.glob("*.png"))) == 19


def test_linear_reference_is_three_quarters_of_n():
    # A hit looks at about n/2 elements and a miss looks at all n. With half
    # hits and half misses the average is (n/2 + n) / 2 = 3n/4.
    assert linear_reference([320, 640]) == [240.0, 480.0]
