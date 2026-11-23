# Big O, explained and checked

Big O is a way to say **how the amount of work grows when the input grows**, ignoring small constant factors. Everything below is checked against the files in `results/`, not just claimed.

## The doubling question

Take a list of items and do some job on it. We call the number of items **n**. Now make the list **twice as long** (2n). How much more work is the job?

| if the work grows like... | doubling the list makes the work... | example |
|---|---|---|
| log n | go up by **one step** | halving a phone book to find a name: a book twice as thick needs just one more page-flip |
| n | about **2x** | reading every name once |
| n log n | a little **over 2x** (about 2.2x at our sizes) | merge sort |
| n squared (written n^2) | **4x** | comparing every name with every other name |

Strictly, Big O is an **upper bound on growth**: "the work is at most a constant times n squared once n is large enough." It says nothing about the exact count or the number of seconds. The doubling ratio is how we **illustrate** a bound from two measured sizes; it is not how a bound is proved. When someone says "bubble sort is n squared", the doubling question gives the practical meaning: give it a list twice as long and expect about four times as many comparisons. We can check that: run the sort at one size, run it at double the size, divide.

Our biggest two sizes are 320 and 640, exactly double. So **comparisons at 640 divided by comparisons at 320** is the measured doubling ratio. The prediction for that ratio is 2 for n, 4 for n^2, and about 2.24 for n log n (because 640 x log2(640) divided by 320 x log2(320) is 2.24).

## What we count, and why not seconds

The code counts comparisons, moves and probes, not seconds. Counts are exact and the same on every machine, and a clock is not. See [`sidecar/DESIGN.md`](sidecar/DESIGN.md). The tables below use **comparisons** for sorting and **probes** (elements looked at) for searching. Every number is an average over repeated runs with fixed seeds, produced by `scripts/run_experiment.py`.

**What exactly is counted**

- A **comparison** is one decision about two values. A search probe makes one three-way decision (equal, smaller or larger) and counts as one comparison and one probe.
- Merge sort's **moves** count each value written while merging. The final copy back into the caller's list is not counted again.
- The check that a sort's result is in order and holds the same values is **not** counted.
- Random inputs are averaged over 5 trials with fixed seeds (trial t at size n uses seed 1000n + t). Half of the search lookups are hits and half are misses.

## Sorting: prediction vs measurement

The "agrees" column is "yes" when the measured ratio is within 5% of the predicted ratio. The plots ([`docs/plots/sorting_random.png`](docs/plots/sorting_random.png), [`sorting_sorted.png`](docs/plots/sorting_sorted.png) and [`sorting_reversed.png`](docs/plots/sorting_reversed.png), plus one `bigo_*` plot per sorter and input) show the same data as curves.

<!-- sort-table:start -->
| input | sorter | predicted | predicted ratio | comparisons at 320 | comparisons at 640 | measured ratio | agrees |
|---|---|---|---|---|---|---|---|
| random | bubble | n^2 | 4.00 | 51040.0 | 204480.0 | 4.01 | yes |
| random | insertion | n^2 | 4.00 | 25451.8 | 102692.0 | 4.03 | yes |
| random | selection | n^2 | 4.00 | 51040.0 | 204480.0 | 4.01 | yes |
| random | merge | n log n | 2.24 | 2259.8 | 5182.8 | 2.29 | yes |
| random | quick | n log n | 2.24 | 2727.6 | 6544.8 | 2.40 | NO |
| sorted | bubble | n^2 | 4.00 | 51040.0 | 204480.0 | 4.01 | yes |
| sorted | insertion | n | 2.00 | 319.0 | 639.0 | 2.00 | yes |
| sorted | selection | n^2 | 4.00 | 51040.0 | 204480.0 | 4.01 | yes |
| sorted | merge | n log n | 2.24 | 1280.0 | 2880.0 | 2.25 | yes |
| sorted | quick | n^2 | 4.00 | 51040.0 | 204480.0 | 4.01 | yes |
| reversed | bubble | n^2 | 4.00 | 51040.0 | 204480.0 | 4.01 | yes |
| reversed | insertion | n^2 | 4.00 | 51040.0 | 204480.0 | 4.01 | yes |
| reversed | selection | n^2 | 4.00 | 51040.0 | 204480.0 | 4.01 | yes |
| reversed | merge | n log n | 2.24 | 1408.0 | 3136.0 | 2.23 | yes |
| reversed | quick | n^2 | 4.00 | 51040.0 | 204480.0 | 4.01 | yes |
<!-- sort-table:end -->

### Where measurement and prediction differ, or look like they might

- **Insertion sort on sorted input is linear, not squared.** Each new item is compared once with its left neighbour, finds it is already in place, and stops. n - 1 comparisons: 319 at size 320, 639 at size 640, ratio 2.00. On random and reversed input it must slide items a long way, so it is n^2 there. Same algorithm, different input, different growth.
- **Quick sort on sorted (and reversed) input is n^2, not n log n.** Our quick sort always picks the **first** item as the pivot. On sorted input the first item is the smallest, so the "split" puts nothing on one side and everything else on the other, every time. The list shrinks by one per round instead of in half. That gives n(n-1)/2 comparisons, exactly the same as bubble sort: 204480 at size 640. This is deliberate; see `sidecar/DESIGN.md`.
- **Quick sort on random input is flagged "NO" (ratio 2.40 vs 2.24).** It is still clearly n log n, not n^2 (that would be 4.0). Two things are at work, and we tested both. First, five random lists are few: rerunning with 500 lists per size gives 2793.3 comparisons at size 320 and 6441.0 at size 640, a ratio of **2.31**, so most of the 2.40 was luck of the draw. Second, the true ratio is not 2.24 at these sizes: the exact expected number of comparisons for a first-item pivot on random input is 2(n+1)H(n) - 4n (H(n) is the harmonic number, about ln n), which is 2794.8 at 320 and 6464.6 at 640, a ratio of **2.313**. The 500-list measurement matches it. So the ratio drifts down toward 2 only slowly; 2.24 is the right prediction for large n, not for 640. The table keeps the 5-trial numbers and its "NO"; `tests/test_quick_sort_expectation.py` checks the 500-list claim.
- **Merge sort's ratio is slightly above 2.** Doubling the list doubles the items to merge, and also adds one more level of splitting, so the ratio lands a bit over 2 (2.23 to 2.29 here, against the predicted 2.24). That "a little over 2" is what n log n looks like.
- **Bubble and selection sort do the same number of comparisons on every input.** Neither stops early, so sorted, reversed and random lists all cost n(n-1)/2 comparisons (204480 at size 640). Selection sort still makes far fewer *moves*; this table counts only comparisons.

## Searching: prediction vs measurement

Searching counts **probes**, the elements looked at. Half of our lookups are for items that are in the list and half for items that are not. The plot is [`docs/plots/searching.png`](docs/plots/searching.png).

<!-- search-table:start -->
| searcher | predicted | predicted at 320 | predicted at 640 | probes at 320 | probes at 640 |
|---|---|---|---|---|---|
| linear | 3n/4 | 240.00 | 480.00 | 249.50 | 481.25 |
| binary | log2 n | 8.32 | 9.32 | 7.87 | 8.88 |
| recursive binary | log2 n | 8.32 | 9.32 | 7.87 | 8.88 |
<!-- search-table:end -->

- **Linear search is about 3n/4, not n and not n/2.** A hit looks at about half the list on average (n/2), a miss always looks at all of it (n). With half hits and half misses the average is halfway between: 3n/4. Measured 481.25 against 480 predicted at size 640. Doubling the list doubles the probes: linear.
- **Binary search is about log2 n, but a little below it.** The prediction is the worst case. On average a hit is found slightly before the last halving, so the measured value sits about half a probe under log2 n. What matters is the doubling: from 320 to 640 it rises by one probe (7.87 to 8.88), the "+1 step" of a log n curve.
- **Binary and recursive binary search are identical.** Same steps, same probes; the recursive one only differs in how it is written.

## What this means in practice

At 640 items nothing here is slow, so n^2 versus n log n looks academic. Scale up to **one million items**:

- n log n: 1,000,000 x log2(1,000,000), about 1,000,000 x 20, so about **20 million** comparisons.
- n^2 (really n(n-1)/2 for bubble or selection sort): about **500,000,000,000** comparisons (five hundred billion).

That is about 25,000 times as much work. A computer doing a billion comparisons a second finishes the first in a fiftieth of a second and the second in roughly **eight minutes**. At ten million items the n^2 sort would take about 14 hours. Same answer, same list, and it is the algorithm's growth rate that decides whether you wait a blink or a day.

## Glossary

- **Big O**: a label for how the work grows with the input size, ignoring constant factors.
- **n**: the number of items in the list.
- **log n**: the number of times you can halve n before reaching 1. log2 of 1,000,000 is about 20.
- **n log n**: n times log n. The best a comparison-based sort can do in general.
- **comparison**: asking "is this value smaller than that one?"
- **probe**: looking at one element of a list during a search.
- **doubling ratio**: the work at size 2n divided by the work at size n.
- **worst case**: the input that makes an algorithm do the most work, such as sorted input for our quick sort.

## Try it

1. **Change the sizes.** In `scripts/run_experiment.py`, change the sizes passed to the manager (for example to 1000, 2000, 4000) and rerun. Expect the bubble-sort doubling ratio to stay near 4 and merge sort's to drift toward 2. Quick sort on sorted input needs a size under Python's recursion limit (about 1000), or it will stop with a recursion error: that error is the n^2 depth you can see.
2. **Make the pivot smarter.** In `src/sortsearch/sorters/quick.py`, make `_partition` swap the middle item to the front before choosing the pivot. Rerun. Expect quick sort on sorted input to drop from n^2 to about n log n, and its doubling ratio to fall from about 4 to about 2.3 (we measured 2.31 with a middle pivot: 2058 comparisons at 320, 4747 at 640). Then run `python scripts/check_big_o.py`: it will say the old table no longer matches, which is the point of the check.

Check the tables in this file at any time with `python scripts/check_big_o.py`.
