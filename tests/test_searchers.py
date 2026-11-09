import random

import pytest

from sortsearch import (
    BinarySearch, Counter, LinearSearch, RecursiveBinarySearch,
    RecursiveSearcher, Searcher,
)


def test_inheritance_shape():
    assert issubclass(LinearSearch, Searcher)
    assert issubclass(BinarySearch, Searcher)
    assert issubclass(RecursiveSearcher, Searcher)
    assert issubclass(RecursiveBinarySearch, RecursiveSearcher)


def test_abstract_classes_cannot_be_built():
    with pytest.raises(TypeError):
        Searcher()
    with pytest.raises(TypeError):
        RecursiveSearcher()


# Hand-worked: values [10,20,30,40,50], target 40.
#   linear looks at 10, 20, 30, 40 -> 4 probes
#   binary: middle index 2 (30) too small; range 3..4, middle 3 (40) found -> 2 probes
def test_hand_worked_probe_counts():
    values = [10, 20, 30, 40, 50]
    c = Counter()
    assert LinearSearch().search(values, 40, c) == 3
    assert c.probes == 4
    for cls in (BinarySearch, RecursiveBinarySearch):
        c = Counter()
        assert cls().search(values, 40, c) == 3
        assert c.probes == 2


def test_miss_costs_n_for_linear():
    c = Counter()
    assert LinearSearch().search([1, 2, 3, 4], 99, c) == -1
    assert c.probes == 4


def test_empty_list():
    for cls in (LinearSearch, BinarySearch, RecursiveBinarySearch):
        assert cls().search([], 1, Counter()) == -1


def test_search_leaves_input_alone():
    values = [1, 3, 5]
    BinarySearch().search(values, 3, Counter())
    assert values == [1, 3, 5]


def test_all_three_agree_on_200_seeded_cases_with_misses():
    rng = random.Random(2026)
    for _ in range(200):
        size = rng.randint(0, 60)
        values = sorted(rng.sample(range(0, 200), size))  # unique values
        if rng.random() < 0.5 and values:
            target = rng.choice(values)
        else:
            target = rng.randint(-5, 205)
        a = LinearSearch().search(values, target, Counter())
        b = BinarySearch().search(values, target, Counter())
        r = RecursiveBinarySearch().search(values, target, Counter())
        assert a == b == r
        if target in values:
            assert values[a] == target


def test_binary_pair_agrees_even_with_duplicates():
    rng = random.Random(5)
    for _ in range(200):
        values = sorted(rng.randint(0, 10) for _ in range(rng.randint(0, 30)))
        target = rng.randint(-1, 11)
        assert (BinarySearch().search(values, target, Counter())
                == RecursiveBinarySearch().search(values, target, Counter()))


def test_recursive_depth_is_logarithmic():
    c = Counter()
    RecursiveBinarySearch().search(list(range(640)), 639, c)
    assert c.max_depth <= 11
    c = Counter()
    BinarySearch().search(list(range(640)), 639, c)
    assert c.max_depth == 0
