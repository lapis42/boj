import sys
from operator import xor
input = sys.stdin.readline


def get(r):
    ans = a[r - 1]
    l = n
    r += n
    while l < r:
        if l & 1:
            ans += t[l]
            l += 1
        if r & 1:
            r -= 1
            ans += t[r]
        l >>= 1
        r >>= 1
    return ans


def update(i, v):
    i += n
    t[i] += v
    while i > 1:
        t[i >> 1] = t[i] + t[xor(i, 1)]
        i >>= 1


n = int(input())
a = list(map(int, input().split()))
t = [0] * (2 * n)

for _ in range(int(input())):
    q, *x = map(int, input().split())
    if q == 1:
        update(x[0] - 1, x[2])
        if x[1] < n: update(x[1], -x[2])
    else:
        print(get(x[0]))
