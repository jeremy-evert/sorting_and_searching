#!/usr/bin/env python3
"""Build all comparison plots from sorting and searching CSV results."""

import argparse
from pathlib import Path

from sortsearch.plotter import Plotter
from sortsearch.results_io import read_search_rows, read_sort_rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--results", type=Path, default=Path("results"),
                        help="directory containing sort_counts.csv and search_counts.csv")
    parser.add_argument("--out", type=Path, default=Path("docs/plots"),
                        help="directory for generated PNGs")
    arguments = parser.parse_args()
    plotter = Plotter(
        read_sort_rows(arguments.results / "sort_counts.csv"),
        read_search_rows(arguments.results / "search_counts.csv"),
    )
    for kind in ("random", "sorted", "reversed"):
        plotter.plot_sorting(kind, arguments.out / ("sorting_" + kind + ".png"))
        for algorithm in ("bubble", "insertion", "selection", "merge", "quick"):
            plotter.plot_big_o(algorithm, kind,
                               arguments.out / ("bigo_" + algorithm + "_" + kind + ".png"))
    plotter.plot_searching(arguments.out / "searching.png")
    print("Wrote 19 PNGs to " + str(arguments.out))


if __name__ == "__main__":
    main()
