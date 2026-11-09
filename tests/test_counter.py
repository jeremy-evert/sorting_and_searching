from sortsearch.counter import Counter


def test_starts_at_zero():
    c = Counter()
    assert (c.comparisons, c.moves, c.probes, c.max_depth) == (0, 0, 0, 0)


def test_reset_clears_everything():
    c = Counter()
    c.comparisons, c.moves, c.probes, c.max_depth = 4, 3, 2, 1
    c.reset()
    assert (c.comparisons, c.moves, c.probes, c.max_depth) == (0, 0, 0, 0)
