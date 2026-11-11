"""A fresh experiment run must reproduce the committed result files exactly."""

import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent


def _load(name):
    """Import a script from scripts/ by file name."""
    import sys
    sys.path.insert(0, str(ROOT / "scripts"))
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_fresh_run_matches_committed_csvs_byte_for_byte(tmp_path):
    # Counts come from fixed seeds and count operations, not seconds, so the
    # same code must write the same bytes. If this fails, either the code
    # changed (rerun scripts/regenerate.py and commit) or something is
    # nondeterministic (a real bug).
    run_experiment = _load("run_experiment")
    run_experiment.write_results(run_experiment.build_default_manager().run(), tmp_path)
    for name in ("sort_counts.csv", "search_counts.csv"):
        assert (tmp_path / name).read_bytes() == (ROOT / "results" / name).read_bytes(), name


def test_csv_difference_check_names_a_changed_file(tmp_path):
    regenerate = pytest.importorskip("matplotlib") and _load("regenerate")
    (tmp_path / "sort_counts.csv").write_bytes((ROOT / "results" / "sort_counts.csv").read_bytes())
    (tmp_path / "search_counts.csv").write_bytes(b"algorithm,size,avg_probes\n")
    assert regenerate.csv_differences(tmp_path, ROOT / "results") == ["search_counts.csv"]
