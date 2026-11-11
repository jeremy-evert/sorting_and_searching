"""Check the numbers quoted in BIG_O.md, the home page and the report source against the result CSVs.

Usage (from the repository root):  python scripts/check_big_o.py [BIG_O.md] [results_dir]

Two checks run:
  1. The two marked tables in BIG_O.md are recomputed from the CSVs and
     compared line by line.
  2. A fixed list of numbers quoted in sentences (in BIG_O.md, docs/index.html
     and report/report.tex) is recomputed from the CSVs and each sentence is
     looked up in its file. Numbers in other sentences are not checked.
When BIG_O.md is given explicitly, only that file's sentences are checked.
Exits 1 if anything differs, 0 if everything matches.
"""

import csv
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SMALL, BIG = 320, 640
TOLERANCE = 0.05  # a ratio within 5% of the prediction counts as "agrees"

SORTERS = ["bubble", "insertion", "selection", "merge", "quick"]
KINDS = ["random", "sorted", "reversed"]

# Predicted growth for each (sorter, kind), as a short label.
PREDICTED = {
    ("bubble", "random"): "n^2", ("bubble", "sorted"): "n^2", ("bubble", "reversed"): "n^2",
    ("insertion", "random"): "n^2", ("insertion", "sorted"): "n", ("insertion", "reversed"): "n^2",
    ("selection", "random"): "n^2", ("selection", "sorted"): "n^2", ("selection", "reversed"): "n^2",
    ("merge", "random"): "n log n", ("merge", "sorted"): "n log n", ("merge", "reversed"): "n log n",
    ("quick", "random"): "n log n", ("quick", "sorted"): "n^2", ("quick", "reversed"): "n^2",
}


def predicted_ratio(label):
    """Return the ratio of work at BIG to work at SMALL for a growth label."""
    if label == "n":
        return BIG / SMALL
    if label == "n^2":
        return (BIG / SMALL) ** 2
    return (BIG * math.log2(BIG)) / (SMALL * math.log2(SMALL))


def read_rows(path):
    """Return the CSV at path as a list of dictionaries."""
    with open(path, newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def sort_table(results_dir):
    """Return the sorting table as a list of Markdown lines."""
    comparisons = {}
    for row in read_rows(Path(results_dir) / "sort_counts.csv"):
        key = (row["kind"], row["algorithm"], int(row["size"]))
        comparisons[key] = float(row["avg_comparisons"])
    lines = [
        "| input | sorter | predicted | predicted ratio | comparisons at 320 | comparisons at 640 | measured ratio | agrees |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for kind in KINDS:
        for sorter in SORTERS:
            small = comparisons[(kind, sorter, SMALL)]
            big = comparisons[(kind, sorter, BIG)]
            label = PREDICTED[(sorter, kind)]
            expected = predicted_ratio(label)
            measured = big / small
            agrees = "yes" if abs(measured - expected) / expected <= TOLERANCE else "NO"
            lines.append(
                f"| {kind} | {sorter} | {label} | {expected:.2f} | {small:.1f} | {big:.1f} | {measured:.2f} | {agrees} |"
            )
    return lines


def search_table(results_dir):
    """Return the searching table as a list of Markdown lines."""
    probes = {}
    for row in read_rows(Path(results_dir) / "search_counts.csv"):
        probes[(row["algorithm"], int(row["size"]))] = float(row["avg_probes"])
    predictions = {
        "linear": ("3n/4", lambda n: 0.75 * n),
        "binary": ("log2 n", math.log2),
        "recursive binary": ("log2 n", math.log2),
    }
    lines = [
        "| searcher | predicted | predicted at 320 | predicted at 640 | probes at 320 | probes at 640 |",
        "|---|---|---|---|---|---|",
    ]
    for name in ["linear", "binary", "recursive binary"]:
        label, formula = predictions[name]
        lines.append(
            f"| {name} | {label} | {formula(SMALL):.2f} | {formula(BIG):.2f} "
            f"| {probes[(name, SMALL)]:.2f} | {probes[(name, BIG)]:.2f} |"
        )
    return lines


def prose_claims(results_dir):
    """Return {file: [sentence fragments]} for numbers quoted in prose, built from the data."""
    sorts = {}
    for row in read_rows(Path(results_dir) / "sort_counts.csv"):
        sorts[(row["kind"], row["algorithm"], int(row["size"]))] = float(row["avg_comparisons"])
    probes = {}
    for row in read_rows(Path(results_dir) / "search_counts.csv"):
        probes[(row["algorithm"], int(row["size"]))] = float(row["avg_probes"])
    quick_sorted_big = int(sorts[("sorted", "quick", BIG)])
    insertion_small = int(sorts[("sorted", "insertion", SMALL)])
    insertion_big = int(sorts[("sorted", "insertion", BIG)])
    quick_ratio = sorts[("random", "quick", BIG)] / sorts[("random", "quick", SMALL)]
    linear_big = probes[("linear", BIG)]
    binary_small, binary_big = probes[("binary", SMALL)], probes[("binary", BIG)]
    return {
        "BIG_O.md": [
            f"{insertion_small} at size 320, {insertion_big} at size 640",
            f"{quick_sorted_big} at size 640",
            f"Measured {linear_big:.2f} against {0.75 * BIG:.0f} predicted at size 640",
            f"({binary_small:.2f} to {binary_big:.2f})",
            f"ratio {quick_ratio:.2f} vs 2.24",
        ],
        "docs/index.html": [
            f"the same {quick_sorted_big} comparisons as bubble sort at size 640",
            f"{insertion_big} comparisons at size 640",
            f"about {round(linear_big)} probes at size 640",
        ],
        "report/report.tex": [
            f"{insertion_big} comparisons at size 640",
            f"{quick_sorted_big} at size 640",
            f"ratio of {quick_ratio:.2f} against a predicted 2.24",
        ],
    }


def prose_problems(results_dir, only_doc=None):
    """Return problem lines for quoted sentences that are missing from their files."""
    problems = []
    for name, fragments in prose_claims(results_dir).items():
        if only_doc is not None and name != only_doc.name:
            continue
        path = only_doc if only_doc is not None else ROOT / name
        text = path.read_text(encoding="utf-8")
        for fragment in fragments:
            if fragment not in text:
                problems.append(f"{name}: expected the data's wording but did not find: {fragment!r}")
    return problems


def block(text, name):
    """Return the lines between <!-- name:start --> and <!-- name:end -->."""
    lines = text.split("\n")
    start = lines.index(f"<!-- {name}:start -->")
    end = lines.index(f"<!-- {name}:end -->")
    return [line for line in lines[start + 1:end] if line.strip()]


def main(argv):
    """Compare BIG_O.md to the recomputed tables; return the exit code."""
    doc = Path(argv[1]) if len(argv) > 1 else ROOT / "BIG_O.md"
    results_dir = Path(argv[2]) if len(argv) > 2 else ROOT / "results"
    text = doc.read_text(encoding="utf-8")
    problems = 0
    for name, expected in (("sort-table", sort_table(results_dir)),
                           ("search-table", search_table(results_dir))):
        print(f"{name}:")
        print("\n".join(expected))
        print()
        try:
            found = block(text, name)
        except ValueError:
            print(f"MISSING markers for {name} in {doc}")
            problems += 1
            continue
        for line in expected:
            if line not in found:
                print(f"EXPECTED but not in {doc.name}: {line}")
                problems += 1
        for line in found:
            if line not in expected:
                print(f"QUOTED but does not match the data: {line}")
                problems += 1
    explicit = len(argv) > 1
    for line in prose_problems(results_dir, doc if explicit else None):
        print(line)
        problems += 1
    print("OK: both marked tables, and the listed numbers quoted in sentences, match the data. "
          "Other numbers in the prose are not checked." if problems == 0
          else f"FAILED: {problems} mismatched line(s).")
    return 0 if problems == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
