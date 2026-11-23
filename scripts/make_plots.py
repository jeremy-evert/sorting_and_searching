#!/usr/bin/env python3
"""Build all comparison plots from sorting and searching CSV results."""

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from sortsearch.plotter import Plotter  # noqa: E402
from sortsearch.results_io import read_search_rows, read_sort_rows  # noqa: E402


def build_plots(results_dir, out_dir):
    """Read the CSVs in results_dir and write all 19 PNGs into out_dir."""
    results_dir = Path(results_dir)
    out_dir = Path(out_dir)
    plotter = Plotter(
        read_sort_rows(results_dir / "sort_counts.csv"),
        read_search_rows(results_dir / "search_counts.csv"),
    )
    for kind in ("random", "sorted", "reversed"):
        plotter.plot_sorting(kind, out_dir / ("sorting_" + kind + ".png"))
        for algorithm in ("bubble", "insertion", "selection", "merge", "quick"):
            plotter.plot_big_o(algorithm, kind,
                               out_dir / ("bigo_" + algorithm + "_" + kind + ".png"))
    plotter.plot_searching(out_dir / "searching.png")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--results", type=Path, default=Path("results"),
                        help="directory containing sort_counts.csv and search_counts.csv")
    parser.add_argument("--out", type=Path, default=Path("docs/plots"),
                        help="directory for generated PNGs")
    arguments = parser.parse_args()
    build_plots(arguments.results, arguments.out)
    print("Wrote 19 PNGs to " + str(arguments.out))


if __name__ == "__main__":
    main()
