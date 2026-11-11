#!/usr/bin/env python3
"""Regenerate every result file and plot from scratch, or check that they still match.

Usage (from the repository root):
    python scripts/regenerate.py           rewrite results/*.csv and docs/plots/*.png
    python scripts/regenerate.py --check   rebuild in a temporary folder and compare
                                           the CSVs with the committed ones; change nothing

The CSVs come from fixed seeds and counted operations, so --check expects them
to match byte for byte on any machine. The PNGs are drawn from the CSVs by
matplotlib; pictures can differ in small pixel details between matplotlib
versions, so --check compares only that every expected PNG gets drawn.
"""

import argparse
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))

from make_plots import build_plots  # noqa: E402
from run_experiment import build_default_manager, write_results  # noqa: E402

CSV_NAMES = ("sort_counts.csv", "search_counts.csv")
PNG_COUNT = 19


def rebuild(results_dir, plots_dir):
    """Run the experiment, write the CSVs, then draw the plots from them."""
    write_results(build_default_manager().run(), results_dir)
    build_plots(results_dir, plots_dir)


def csv_differences(fresh_dir, committed_dir):
    """Return the names of CSV files whose bytes differ between two folders."""
    return [name for name in CSV_NAMES
            if (Path(fresh_dir) / name).read_bytes() != (Path(committed_dir) / name).read_bytes()]


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true",
                        help="compare against the committed files instead of rewriting them")
    arguments = parser.parse_args()
    results_dir = ROOT / "results"
    if not arguments.check:
        rebuild(results_dir, ROOT / "docs" / "plots")
        print("Rewrote results/*.csv and " + str(PNG_COUNT) + " plots in docs/plots.")
        return 0
    with tempfile.TemporaryDirectory() as scratch:
        fresh = Path(scratch)
        rebuild(fresh / "results", fresh / "plots")
        different = csv_differences(fresh / "results", results_dir)
        drawn = len(list((fresh / "plots").glob("*.png")))
    for name in different:
        print("DIFFERS from the committed file: results/" + name)
    if drawn != PNG_COUNT:
        print("Drew " + str(drawn) + " plots, expected " + str(PNG_COUNT))
    if different or drawn != PNG_COUNT:
        print("FAILED.")
        return 1
    print("OK: the CSVs match the committed ones byte for byte, and all "
          + str(PNG_COUNT) + " plots were drawn.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
