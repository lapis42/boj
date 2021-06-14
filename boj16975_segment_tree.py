import sys
from operator import xor
input = sys.stdin.readline


class SegmentTree():
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.t = [0] * (2 * self.n)

    def query(self, r):
        idx = r - 1
        l = self.n
        r += self.n
        ans = 0
        while l < r:
            if l & 1:
                ans += self.t[l]
                l += 1
            if r & 1:
                r -= 1
                ans += self.t[r]
            l >>= 1
            r >>= 1
        return ans + t.arr[idx]

    def update(self, pos_a, pos_b, val):
        pos_a += self.n - 1
        self.t[pos_a] += val
        while pos_a > 1:
            self.t[pos_a >> 1] = self.t[pos_a] + self.t[xor(pos_a, 1)]
            pos_a >>= 1

        pos_b += self.n
        if pos_b < 2 * self.n:
            self.t[pos_b] -= val
            while pos_b > 1:
                self.t[pos_b >> 1] = self.t[pos_b] + self.t[xor(pos_b, 1)]
                pos_b >>= 1


n = int(input())
arr = list(map(int, input().split()))
t = SegmentTree(arr)

for _ in range(int(input())):
    q, *x = map(int, input().split())
    if q == 1:
        t.update(x[0], x[1], x[2])
    else:
        print(t.query(x[0]))
