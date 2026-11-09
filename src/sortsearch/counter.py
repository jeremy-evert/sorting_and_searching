"""Counter: a tally of the work an algorithm does."""


class Counter:
    """Records comparisons, moves, probes and recursion depth.

    An algorithm is handed one Counter and adds to it as it works.
    The Counter knows nothing about the algorithms that use it.
    """

    def __init__(self):
        """Start with every tally at zero."""
        self.comparisons = 0
        self.moves = 0
        self.probes = 0
        self.max_depth = 0

    def reset(self):
        """Set every tally back to zero so the Counter can be reused."""
        self.comparisons = 0
        self.moves = 0
        self.probes = 0
        self.max_depth = 0

    def __repr__(self):
        """Show the four tallies on one line."""
        return (
            f"Counter(comparisons={self.comparisons}, moves={self.moves}, "
            f"probes={self.probes}, max_depth={self.max_depth})"
        )
