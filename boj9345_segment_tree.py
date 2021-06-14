import sys
from operator import xor
input = sys.stdin.readline


class SegmentTree():
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)

        self.t_min = [10**5] * (2 * self.n)
        self.t_max = [0] * (2 * self.n)
        self.t_min[self.n:] = arr
        self.t_max[self.n:] = arr

        for i in range(self.n - 1, 0, -1):
            self.t_min[i] = min(self.t_min[i << 1], self.t_min[i << 1 | 1])
            self.t_max[i] = max(self.t_max[i << 1], self.t_max[i << 1 | 1])

    def query(self, l, r):
        l_old, r_old = l, r
        ans_min, ans_max = 10**5, 0
        l += self.n
        r += self.n + 1
        while l < r:
            if l & 1:
                ans_min = min(ans_min, self.t_min[l])
                ans_max = max(ans_max, self.t_max[l])
                l += 1
            if r & 1:
                r -= 1
                ans_min = min(ans_min, self.t_min[r])
                ans_max = max(ans_max, self.t_max[r])
            l >>= 1
            r >>= 1
        return ans_min == l_old and ans_max == r_old

    def update(self, pos, val):
        self.t_min[pos + self.n] = val
        self.t_max[pos + self.n] = val
        pos += self.n
        while pos > 1:
            self.t_min[pos >> 1] = min(self.t_min[pos], self.t_min[xor(pos,
                                                                       1)])
            self.t_max[pos >> 1] = max(self.t_max[pos], self.t_max[xor(pos,
                                                                       1)])
            pos >>= 1

    def value(self, pos):
        return self.t_min[pos + self.n]


for _ in range(int(input())):
    n, k = map(int, input().split())
    t = SegmentTree(list(range(n)))

    for _ in range(k):
        q, a, b = map(int, input().split())
        if q:
            print('YES' if t.query(a, b) else 'NO')
        else:
            val_b = t.value(b)
            val_a = t.value(a)
            t.update(a, val_b)
            t.update(b, val_a)
