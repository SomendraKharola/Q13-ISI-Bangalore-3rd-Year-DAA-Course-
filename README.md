# Q13: Troupes in towns

Authors: Ranjit Kumar V J (bmat2437) and Somendra Singh Kharola (bmat2240)

Given a set of towns joined by roads (the road network is a tree, or a forest),
put 0, 1 or 2 troupes in every town so that each town with 0 troupes has a
neighbour with 2 troupes or at least two neighbours with 1 troupe each. The
program finds an assignment with the smallest possible total number of troupes.
It runs in O(n) time with a dynamic programme on the tree. The full write-up
is in `report.pdf`.

## Files

| File | What it is |
| --- | --- |
| `troupes.py` | the algorithm (also a command line program) |
| `test_troupes.py` | tests, including a brute-force comparison |
| `sample.txt` | the 9-town example used in the report |
| `report.tex`, `report.pdf` | project report |

## Requirements

Python 3.8 or newer. No extra packages are needed.

## Running it

```
python3 troupes.py sample.txt
```

or, reading from standard input:

```
python3 troupes.py < sample.txt
```

### Input format

```
n m
u1 v1
...
um vm
```

`n` is the number of towns (numbered 1 to n) and `m` is the number of roads.
The roads must form a forest, i.e. no cycles. If there is a cycle the program
stops with an error.

### Output format

The first line is the minimum total number of troupes. The second line has n
numbers, the number of troupes placed in towns 1, 2, ..., n.

For `sample.txt` the output is

```
6
0 0 1 1 1 1 1 0 1
```

## Running the tests

```
python3 test_troupes.py
```

This checks a few hand-made cases, compares the answer with a brute force over
all 3^n assignments on 1500 random forests with up to 10 towns, and then runs
paths, stars and random trees with 300000 towns (takes about 15 seconds in
total). It prints `all tests passed` at the end.

## Rebuilding the report

```
pdflatex report.tex
pdflatex report.tex
```

(twice, so the cross-references settle).
