[README-3.md](https://github.com/user-attachments/files/34011979/README-3.md)
# Q13: Troupes in Towns

**Authors:** Ranjit Kumar V J (bmat2437), Somendra Singh Kharola (bmat2240), ISI Bangalore
**Repository:** https://github.com/SomendraKharola/Q13-ISI-Bangalore-3rd-Year-DAA-Course-.git

Each town gets 0, 1 or 2 troupes. A town with 0 troupes must have a neighbour
with 2 troupes, or at least two neighbours with 1 troupe. The program finds an
assignment with the **minimum total number of troupes**. We assume the towns
and roads form a tree (or a forest). It runs in O(n) time; the proof and
analysis are in `report.pdf`.

## Files

- `troupes.py`: the solution (the program you run)
- `test_troupes.py`: tests
- `sample.txt`: example input
- `report.pdf`, `report.tex`: project report

## Requirements

Python 3.8 or newer (no extra libraries). Check with `python --version`
(Windows) or `python3 --version` (macOS/Linux). Open a terminal **in the folder
containing `troupes.py`**. On Windows type `python`; on macOS/Linux type
`python3`. We write `python3` below.

## Input format

```
n m
u1 v1
...
um vm
```

`n` towns numbered 1..n, `m` roads, then one road `u v` per line. The roads must
not form a cycle (for one tree, `m = n - 1`).

Example (`sample.txt`):

```
9 8
1 2
1 3
1 4
2 5
2 6
4 7
4 8
8 9
```

## Output format

Line 1: the minimum total number of troupes.
Line 2: the number of troupes in towns 1..n.

For `sample.txt`:

```
6
0 0 1 1 1 1 1 0 1
```

## How to run

**1. From a file (recommended, works everywhere):**

```
python3 troupes.py sample.txt
```

**2. Typing the input by hand:** run `python3 troupes.py`, type the input, then
signal the end of input:

- **Windows:** press Enter, then **Ctrl + Z**, then Enter
- **macOS / Linux:** press Enter, then **Ctrl + D**

Without this the program just keeps waiting and looks frozen (Ctrl + C quits).

**3. Redirecting a file:**

- Windows Command Prompt: `python troupes.py < sample.txt`
- Windows PowerShell: `Get-Content sample.txt | python troupes.py`
- macOS / Linux: `python3 troupes.py < sample.txt`

## Small examples

| Input | Minimum | Note |
| --- | --- | --- |
| `1 0` | 1 | a lone town needs 1 troupe |
| `3 2`, `1 2`, `2 3` | 2 (`0 2 0`) | 2 troupes in the middle town |

## Errors

- `ValueError: input graph is not a forest`: the roads contain a cycle.
- `IndexError` / `invalid literal for int()`: input is incomplete or has
  non-numbers; check that exactly `m` road lines follow `n m`.
- `can't open file ... troupes.py`: you are in the wrong folder.

## Tests

```
python3 test_troupes.py
```

Takes about 15 seconds. It checks hand-made cases, compares against brute force
on 1500 random small forests, and runs inputs with 300000 towns. It ends with
`all tests passed`.

## Rebuilding the report (optional)

Run `pdflatex report.tex` twice.
