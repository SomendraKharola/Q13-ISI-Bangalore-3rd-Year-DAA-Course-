"""
Tests for troupes.py. Run with:  python3 test_troupes.py

1. hand-made cases with known answers,
2. random trees/forests of up to 10 towns compared with brute force over
   all 3^n assignments,
3. a large-input run to see that it really is linear time.
"""

import itertools
import random
import time

from troupes import solve, is_valid


def brute(n, edges):
    best = None
    for f in itertools.product(range(3), repeat=n):
        if is_valid(n, edges, f):
            s = sum(f)
            if best is None or s < best:
                best = s
    return best


def random_forest(n, rng):
    edges = []
    for v in range(1, n):
        if rng.random() < 0.9:          # sometimes leave a component apart
            edges.append((rng.randrange(v), v))
    perm = list(range(n))
    rng.shuffle(perm)
    return [(perm[u], perm[v]) for u, v in edges]


def check(n, edges, expected=None):
    total, f = solve(n, edges)
    assert is_valid(n, edges, f), ("invalid assignment", n, edges, f)
    assert sum(f) == total, ("sum mismatch", n, edges, f, total)
    if expected is not None:
        assert total == expected, (n, edges, total, expected)
    return total


def main():
    # hand cases -----------------------------------------------------------
    check(1, [], 1)                                   # lonely town needs 1
    check(2, [(0, 1)], 2)                             # 1+1 or 0+2
    check(3, [(0, 1), (1, 2)], 2)                     # 0 2 0
    check(5, [(0, i) for i in range(1, 5)], 2)        # star: 2 at the centre
    check(4, [(0, 1), (1, 2), (2, 3)], 3)             # path on 4 towns
    print("hand cases ok")

    # random vs brute force -----------------------------------------------
    rng = random.Random(2437)
    count = 0
    for n in range(1, 11):
        for _ in range(150):
            edges = random_forest(n, rng)
            total = check(n, edges)
            assert total == brute(n, edges), (n, edges)
            count += 1
    print(f"{count} random forests agree with brute force")

    # big inputs -----------------------------------------------------------
    n = 300000
    path = [(i, i + 1) for i in range(n - 1)]
    star = [(0, i) for i in range(1, n)]
    rand = [(rng.randrange(v), v) for v in range(1, n)]
    for name, edges in (("path", path), ("star", star), ("random tree", rand)):
        t0 = time.time()
        total = check(n, edges)
        print(f"n = {n}, {name}: answer {total}, {time.time() - t0:.2f}s")
    print("all tests passed")


if __name__ == "__main__":
    main()
