import sys
import math
input = sys.stdin.readline

r = 1000000007


def build(idx, i, j):
    if i == j:
        st[idx] = arr[i]
    else:
        mid = i + (j - i) // 2
        st[idx] = (build(2 * idx + 1, i, mid) *\
                    build(2 * idx + 2, mid + 1, j)) % r
    return st[idx]


def query(qi, qj, idx, i, j):
    if qi <= i and qj >= j:
        return st[idx]
    if j < qi or i > qj:
        return 1
    mid = i + (j - i) // 2
    return query(qi, qj, 2 * idx + 1, i, mid) *\
           query(qi, qj, 2 * idx + 2, mid + 1, j) % r


def update(pos, val, idx, i, j):
    if pos < i or pos > j:
        return
    if i == j:
        st[idx] = val
        return
    mid = i + (j - i) // 2
    update(pos, val, 2 * idx + 1, i, mid)
    update(pos, val, 2 * idx + 2, mid + 1, j)
    st[idx] = st[2 * idx + 1] * st[2 * idx + 2] % r


n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

n_st = int(2**(math.ceil(math.log2(n)) + 1)) - 1
st = [1] * n_st
build(0, 0, n - 1)

for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(b - 1, c, 0, 0, n - 1)
    else:
        print(query(b - 1, c - 1, 0, 0, n - 1))
