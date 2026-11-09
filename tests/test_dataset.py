import pytest
from sortsearch.dataset import DataSet


def test_sorted_and_reversed():
    assert DataSet.make("sorted", 5, 0).values == [0, 1, 2, 3, 4]
    assert DataSet.make("reversed", 5, 0).values == [4, 3, 2, 1, 0]


def test_random_is_repeatable_and_a_permutation():
    a = DataSet.make("random", 50, 7).values
    b = DataSet.make("random", 50, 7).values
    assert a == b
    assert sorted(a) == list(range(50))


def test_different_seeds_differ():
    assert DataSet.make("random", 50, 1).values != DataSet.make("random", 50, 2).values


def test_empty_size_is_allowed():
    assert DataSet.make("random", 0, 1).values == []


def test_bad_inputs_raise():
    with pytest.raises(ValueError):
        DataSet.make("zigzag", 5, 0)
    with pytest.raises(ValueError):
        DataSet.make("sorted", -1, 0)
