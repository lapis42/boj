import sys
from math import log2, ceil
input = sys.stdin.readline


def build(st, idx, i, j, f):
    if i == j:
        st[idx] = arr[i]
    else:
        mid = i + (j - i) // 2
        a = build(st, 2 * idx + 1, i, mid, f)
        b = build(st, 2 * idx + 2, mid + 1, j, f)
        st[idx] = f(a, b)
    return st[idx]


def query(st, qi, qj, idx, i, j, f):
    if qi <= i and qj >= j:
        return st[idx]
    if j < qi or i > qj:
        if f == min:
            return 10**9
        else:
            return 0
    mid = i + (j - i) // 2
    a = query(st, qi, qj, 2 * idx + 1, i, mid, f)
    b = query(st, qi, qj, 2 * idx + 2, mid + 1, j, f)
    return f(a, b)


n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

n_st = (1 << ceil(log2(n) + 1)) - 1
st_min = [0] * n_st
st_max = [0] * n_st
build(st_min, 0, 0, n - 1, min)
build(st_max, 0, 0, n - 1, max)

for _ in range(m):
    a, b = map(int, input().split())
    print(query(st_min, a - 1, b - 1, 0, 0, n - 1, min),\
          query(st_max, a - 1, b - 1, 0, 0, n - 1, max))
