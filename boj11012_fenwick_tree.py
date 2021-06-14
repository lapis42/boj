import sys
from bisect import bisect_left
input = sys.stdin.readline


def add(t, i):
    while i < n_y + 1:
        t[i] += 1
        i += i & -i


def get(t, i):
    ans = 0
    while i > 0:
        ans += t[i]
        i -= i & -i
    return ans


for _ in range(int(input())):
    n, m = map(int, input().split())
    xs, ys = set(), set()
    pts = []
    for _ in range(n):
        x, y = map(int, input().split())
        pts.append([x, y])
        xs.add(x)
        ys.add(y)
    pts.sort()
    xs = sorted(xs)
    ys = sorted(ys)
    n_x = len(xs)
    n_y = len(ys)

    t = [0] * (n_y + 1)
    ts = []
    px = pts[0][0]
    for x, y in pts:
        if px != x:
            ts.append(t.copy())
        idx = bisect_left(ys, y) + 1
        add(t, idx)
        px = x
    ts.append(t.copy())

    ans = 0
    for _ in range(m):
        l, r, b, t = map(int, input().split())
        il = bisect_left(xs, l) - 1
        ir = min(bisect_left(xs, r), n_x - 1)
        ib = bisect_left(ys, b)
        it = min(bisect_left(ys, t) + 1, n_y)
        ans += get(ts[ir], it) - get(ts[ir], ib)
        if il >= 0:
            ans -= get(ts[il], it) - get(ts[il], ib)
    print(ans)
