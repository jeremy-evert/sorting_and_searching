"""Quick sort on random input should match its exact expected comparison count."""

from sortsearch import QuickSort
from sortsearch.manager import ExperimentManager


def expected_quick_comparisons(n):
    """Return 2(n+1)H(n) - 4n, the expected comparisons for a first-item pivot.

    H(n) = 1 + 1/2 + ... + 1/n. This is the standard result for quick sort that
    compares every other item with the pivot once per partition.
    """
    harmonic = sum(1 / k for k in range(1, n + 1))
    return 2 * (n + 1) * harmonic - 4 * n


def test_expected_count_for_three_items_by_hand():
    # n = 3: H(3) = 1 + 1/2 + 1/3 = 11/6, so 2 * 4 * 11/6 - 12 = 88/6 - 12 = 16/6.
    # Directly: the pivot is compared with the 2 others (2 comparisons); then it is
    # the smallest, middle or largest with probability 1/3 each. Smallest or largest
    # leaves a 2-item part that needs 1 more comparison; the middle leaves two
    # 1-item parts that need none. So 2 + (1 + 0 + 1) / 3 = 8/3 = 16/6.
    assert abs(expected_quick_comparisons(3) - 16 / 6) < 1e-12


def test_five_hundred_random_lists_match_the_expected_count_within_one_percent():
    manager = ExperimentManager([QuickSort()], [], sizes=[320], kinds=["random"], trials=500)
    measured = manager.run().sort_rows[0].avg_comparisons
    expected = expected_quick_comparisons(320)
    assert abs(measured - expected) / expected < 0.01
