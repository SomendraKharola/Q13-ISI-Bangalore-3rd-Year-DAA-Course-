"""
Q13: assigning troupes (0, 1 or 2) to towns so that every town with 0 troupes
has a neighbour with 2 troupes, or at least two neighbours with 1 troupe each,
and the total number of troupes is as small as possible.

We assume the towns and the roads between them form a tree (or a forest).
The algorithm is a linear-time dynamic programme on the tree.

Authors: Ranjit Kumar V J (bmat2437), Somendra Singh Kharola (bmat2240)

Input format (stdin or a file given on the command line):
    n m
    u1 v1
    ...
    um vm
Towns are numbered 1..n and the graph must be a forest (m <= n - 1).

Output:
    line 1: minimum total number of troupes
    line 2: n integers, the number of troupes in towns 1..n
"""

import sys

INF = 10 ** 9


def solve(n, edges):
    """Return (minimum total, list f of length n with f[i] in {0,1,2}).

    Towns are 0-indexed here. `edges` is a list of pairs (u, v).
    Raises ValueError if the graph contains a cycle.
    """
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # --- cycle check (a forest has exactly n - #components edges) ---------
    seen = [False] * n
    parent = [-1] * n
    roots = []
    order = []          # all towns, parents before children
    for r in range(n):
        if seen[r]:
            continue
        roots.append(r)
        seen[r] = True
        stack = [r]
        while stack:
            v = stack.pop()
            order.append(v)
            for w in adj[v]:
                if w == parent[v]:
                    continue
                if seen[w]:
                    raise ValueError("input graph is not a forest")
                seen[w] = True
                parent[w] = v
                stack.append(w)

    children = [[] for _ in range(n)]
    for v in range(n):
        if parent[v] != -1:
            children[parent[v]].append(v)

    # dp[v][3*a + h] = cheapest way to fill the subtree of v when v itself
    # gets a troupes and its parent gets h troupes (h = 0 for a root).
    dp = [None] * n
    # hist[v][a] = list of the "capped sum" tables after adding each child,
    # kept only so that we can rebuild the actual assignment afterwards.
    hist = [None] * n

    for v in reversed(order):
        dpv = [INF] * 9
        histv = []
        for a in range(3):
            g = [0, INF, INF]            # g[s]: children's total, capped at 2
            h_list = [g]
            for c in children[v]:
                dpc = dp[c]
                ng = [INF, INF, INF]
                for s in range(3):
                    if g[s] >= INF:
                        continue
                    for b in range(3):
                        cost = dpc[3 * b + a]
                        if cost >= INF:
                            continue
                        t = s + b
                        if t > 2:
                            t = 2
                        val = g[s] + cost
                        if val < ng[t]:
                            ng[t] = val
                g = ng
                h_list.append(g)
            histv.append(h_list)
            for h in range(3):
                best = INF
                for s in range(3):
                    if (a > 0 or s + h >= 2) and g[s] < best:
                        best = g[s]
                if best < INF:
                    dpv[3 * a + h] = a + best
        dp[v] = dpv
        hist[v] = histv

    # --- pick the best value at every root and rebuild the assignment -----
    f = [0] * n
    total = 0
    work = []
    for r in roots:
        a_best = min(range(3), key=lambda a: dp[r][3 * a])
        total += dp[r][3 * a_best]
        f[r] = a_best
        work.append((r, a_best, 0))

    while work:
        v, a, h = work.pop()
        final = hist[v][a][-1]
        # best admissible capped sum for the children of v
        s = min((t for t in range(3) if a > 0 or t + h >= 2),
                key=lambda t: final[t])
        kids = children[v]
        for k in range(len(kids) - 1, -1, -1):
            c = kids[k]
            prev, cur = hist[v][a][k], hist[v][a][k + 1]
            found = False
            for sp in range(3):
                if prev[sp] >= INF:
                    continue
                for b in range(3):
                    if min(2, sp + b) == s and \
                            prev[sp] + dp[c][3 * b + a] == cur[s]:
                        f[c] = b
                        work.append((c, b, a))
                        s = sp
                        found = True
                        break
                if found:
                    break
    return total, f


def is_valid(n, edges, f):
    """Check the rule from the problem statement directly."""
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    for v in range(n):
        if f[v] not in (0, 1, 2):
            return False
        if f[v] == 0:
            twos = sum(1 for w in adj[v] if f[w] == 2)
            ones = sum(1 for w in adj[v] if f[w] == 1)
            if twos == 0 and ones < 2:
                return False
    return True


def main():
    data = (open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin).read().split()
    n, m = int(data[0]), int(data[1])
    edges = [(int(data[2 + 2 * i]) - 1, int(data[3 + 2 * i]) - 1)
             for i in range(m)]
    total, f = solve(n, edges)
    print(total)
    print(*f)


if __name__ == "__main__":
    main()
