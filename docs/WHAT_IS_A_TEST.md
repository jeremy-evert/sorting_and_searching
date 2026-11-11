# What is a unit test?

A unit test is a small program that checks one small piece of your code and shouts if the answer is wrong. You decide the right answer **first, by hand**, then let the computer check your code against it. If your code and your hand-worked answer disagree, one of them is wrong, and finding out which is the whole point.

## The smallest example

Your code, `shapes.py`:

```python
def area(width, height):
    return width * height
```

Your test, `test_shapes.py`:

```python
from shapes import area


def test_area_of_a_3_by_4_rectangle():
    # Worked out by hand, before running anything: 3 rows of 4 squares is 12.
    assert area(3, 4) == 12
```

Three things to notice:

1. The test name says what is being checked.
2. The comment shows **where the expected answer came from**. It was not copied from what the program printed. A test that only repeats what the code already does proves nothing.
3. `assert` means "this must be true, or stop and complain."

## A passing run

```
$ pytest -q
.                                                                        [100%]
1 passed in 0.00s
```

One dot is one test that passed.

## A failing run

Now suppose someone "fixes" the code and gets it wrong:

```python
def area(width, height):
    return width + height
```

```
$ pytest -q
F                                                                        [100%]
=================================== FAILURES ===================================
_______________________ test_area_of_a_3_by_4_rectangle ________________________

    def test_area_of_a_3_by_4_rectangle():
        # Worked out by hand, before running anything: 3 rows of 4 squares is 12.
>       assert area(3, 4) == 12
E       assert 7 == 12
E        +  where 7 = area(3, 4)

test_shapes.py:6: AssertionError
=========================== short test summary info ============================
FAILED test_shapes.py::test_area_of_a_3_by_4_rectangle - assert 7 == 12
1 failed in 0.01s
```

The `F` is the big red "no." It says what the code returned (7), what you expected (12), and the line that disagreed. Fix the code, run again, and the dot comes back.

## Rules that keep tests honest

- Work the expected answer out **before** you run the code.
- If the test and the code disagree, **stop and find out which is wrong.** Do not change the test just to make it pass.
- Test the edges too: an empty list, a single item, zero.
- Say "my tests pass" only if you ran them just now.

## Where to see it in this repository

`tests/test_sorters.py` works out the expected counts for a three-item list by hand, in comments, before asserting them. Run `pytest` from the repository root to see all of them pass.
