import sys
from math import ceil, log2
input = sys.stdin.readline


class SegmentTree(arr, f):
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        t = [0] * (2 * n)
        self.init()

    def init():
        


for _ in range(int(input())):
    n, k = map(int, input().split())

    arr = list(range(n))
    n_st = (1 << ceil(log2(n) + 1)) - 1
    st_min = [n] * n_st
    st_max = [0] * n_st
    build(st_min, 0, 0, n - 1, min)
    build(st_max, 0, 0, n - 1, max)

    for _ in range(k):
        q, a, b = map(int, input().split())
        if q:
            min_val = query(st_min, a, b, 0, 0, n - 1, min)
            max_val = query(st_max, a, b, 0, 0, n - 1, max)
            if a == min_val and b == max_val:
                print('YES')
            else:
                print('NO')
        else:
            val_b = arr[b]
            val_a = arr[a]
            update(a, val_b, st_min, 0, 0, n - 1, min)
            update(a, val_b, st_max, 0, 0, n - 1, max)
            update(b, val_a, st_min, 0, 0, n - 1, min)
            update(b, val_a, st_max, 0, 0, n - 1, max)
