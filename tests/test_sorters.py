import random

import pytest

from sortsearch import (
    BubbleSort, Counter, DataSet, InsertionSort, MergeSort, QuickSort,
    SelectionSort, Sorter, RecursiveSorter,
)

ALL = [BubbleSort, InsertionSort, SelectionSort, MergeSort, QuickSort]

INPUTS = {
    "random": DataSet.make("random", 60, 3).values,
    "sorted": list(range(30)),
    "reversed": list(range(30, 0, -1)),
    "empty": [],
    "one": [42],
    "duplicates": [5] * 12,
    "mixed duplicates": [3, 1, 3, 2, 1, 2, 3],
}


@pytest.mark.parametrize("cls", ALL)
@pytest.mark.parametrize("label", list(INPUTS))
def test_sorts_correctly_and_leaves_input_alone(cls, label):
    original = INPUTS[label]
    snapshot = list(original)
    result = cls().sort(original, Counter())
    assert result == sorted(snapshot)
    assert original == snapshot
    assert result is not original


def test_inheritance_shape():
    for cls in (BubbleSort, InsertionSort, SelectionSort, RecursiveSorter):
        assert issubclass(cls, Sorter)
    assert issubclass(MergeSort, RecursiveSorter)
    assert issubclass(QuickSort, RecursiveSorter)


def test_abstract_classes_cannot_be_built():
    with pytest.raises(TypeError):
        Sorter()
    with pytest.raises(TypeError):
        RecursiveSorter()


def test_sort_raises_if_a_child_forgets_to_sort():
    class Broken(Sorter):
        def _sort(self, items, counter):
            pass

    with pytest.raises(RuntimeError):
        Broken().sort([2, 1], Counter())


# Hand-worked counts for [3, 1, 2]. A swap is 2 moves.
#
# Bubble (no early exit), 2 passes:
#   pass 1: compare 3,1 -> swap [1,3,2]; compare 3,2 -> swap [1,2,3]
#   pass 2: compare 1,2 -> no swap
#   comparisons = 3, swaps = 2 -> moves = 4
def test_bubble_hand_counts():
    c = Counter()
    BubbleSort().sort([3, 1, 2], c)
    assert (c.comparisons, c.moves) == (3, 4)


# Insertion (each shift = 1 move, each held value written down = 1 move):
#   hold 1: compare 3 vs 1 -> 3 is bigger, shift 3 right (move 1);
#           ran off the left end; write 1 at front (move 2)         [1,3,2]
#   hold 2: compare 3 vs 2 -> shift 3 right (move 3);
#           compare 1 vs 2 -> 1 is not bigger, stop;
#           write 2 (move 4)                                        [1,2,3]
#   comparisons = 1 + 2 = 3, moves = 4
def test_insertion_hand_counts():
    c = Counter()
    InsertionSort().sort([3, 1, 2], c)
    assert (c.comparisons, c.moves) == (3, 4)


# Selection:
#   start 0: compare 1 vs 3 (new smallest), compare 2 vs 1 (no) -> 2 comparisons
#            smallest is index 1, swap with index 0 -> 2 moves   [1,3,2]
#   start 1: compare 2 vs 3 (new smallest) -> 1 comparison
#            smallest is index 2, swap with index 1 -> 2 moves   [1,2,3]
#   comparisons = 3, moves = 4
def test_selection_hand_counts():
    c = Counter()
    SelectionSort().sort([3, 1, 2], c)
    assert (c.comparisons, c.moves) == (3, 4)


# Insertion on already-sorted [1,2,3] is the best case: one comparison per
# round (2 total), and each held value is written back once (2 moves).
def test_insertion_best_case_hand_counts():
    c = Counter()
    InsertionSort().sort([1, 2, 3], c)
    assert (c.comparisons, c.moves) == (2, 2)


# Merge sort on [3, 1, 2]: split [3] | [1,2]; split [1,2] into [1] | [2].
#   merge [1],[2]: compare 1,2 -> 1 comparison, 2 moves
#   merge [3],[1,2]: compare 3,1 (take 1), compare 3,2 (take 2), then 3 left over
#                    -> 2 comparisons, 3 moves
#   comparisons = 3, moves = 5
def test_merge_hand_counts():
    c = Counter()
    MergeSort().sort([3, 1, 2], c)
    assert (c.comparisons, c.moves) == (3, 5)


# Quick sort on [3, 1, 2], pivot 3:
#   compare 1<3 (swap with itself position 1: boundary 1, 2 moves)
#   compare 2<3 (boundary 2, swap items 2,2: 2 moves)
#   pivot goes to index 2: swap 3 and 2 -> 2 moves   [2,1,3]
#   then sort [2,1], pivot 2: compare 1<2 (2 moves), final swap (2 moves) [1,2]
#   comparisons = 2 + 1 = 3, moves = 2+2+2+2+2 = 10
def test_quick_hand_counts():
    c = Counter()
    QuickSort().sort([3, 1, 2], c)
    assert (c.comparisons, c.moves) == (3, 10)


def test_quick_sorted_input_hits_depth_n():
    # First-element pivot on sorted input of 100: calls on 100, 99, ..., 1
    # elements nest one inside the other, so depth is exactly 100.
    c = Counter()
    QuickSort().sort(list(range(100)), c)
    assert c.max_depth == 100


def test_merge_depth_stays_small():
    c = Counter()
    MergeSort().sort(list(range(100)), c)
    # 100 -> 50 -> 25 -> 13 -> 7 -> 4 -> 2 -> 1 : 8 levels
    assert c.max_depth == 8 < 10


def test_bubble_cost_is_the_same_for_every_input():
    counts = set()
    for kind in ("random", "sorted", "reversed"):
        c = Counter()
        BubbleSort().sort(DataSet.make(kind, 20, 1).values, c)
        counts.add(c.comparisons)
    assert counts == {20 * 19 // 2}


def test_random_seeded_agreement_with_builtin_sorted():
    rng = random.Random(11)
    for _ in range(50):
        data = [rng.randint(0, 20) for _ in range(rng.randint(0, 40))]
        for cls in ALL:
            assert cls().sort(data, Counter()) == sorted(data)


class _DropsAValue(Sorter):
    """A deliberately broken sorter: its output is in order but one value is missing."""

    name = "drops a value"

    def _sort(self, items, counter):
        items.sort()
        items.pop()


class _InventsAValue(Sorter):
    """A deliberately broken sorter: its output is in order but one value is replaced."""

    name = "invents a value"

    def _sort(self, items, counter):
        items.sort()
        items[0] = items[0] - 1


@pytest.mark.parametrize("broken", [_DropsAValue, _InventsAValue])
def test_sort_rejects_output_that_is_sorted_but_not_the_same_values(broken):
    # [3, 1, 2] sorts to [1, 2, 3]. Each broken sorter returns an ordered list
    # ([1, 2] or [0, 2, 3]) that is not a rearrangement of the input, so sort()
    # must raise even though the order check alone would pass.
    with pytest.raises(RuntimeError, match="values"):
        broken().sort([3, 1, 2], Counter())
