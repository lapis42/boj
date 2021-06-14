import sys
from operator import xor
input = sys.stdin.readline


def build():
    for i in reversed(range(1, n)):
        m[i] = min(m[2 * i], m[2 * i + 1])
        M[i] = max(M[2 * i], M[2 * i + 1])


def get(l, r):
    ans = [10**5, 0]
    l += n
    r += n
    while l < r:
        if l & 1:
            ans[0] = min(ans[0], m[l])
            ans[1] = max(ans[1], M[l])
            l += 1
        if r & 1:
            r -= 1
            ans[0] = min(ans[0], m[r])
            ans[1] = max(ans[1], M[r])
        l >>= 1
        r >>= 1
    return ans


def update(i, v):
    i += n
    m[i] = M[i] = v
    while i > 1:
        j = xor(i, 1)
        m[i >> 1] = min(m[i], m[j])
        M[i >> 1] = max(M[i], M[j])
        i >>= 1


for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(range(n))
    m = [10**5] * n + a
    M = [0] * n + a
    build()

    for _ in range(k):
        q, a, b = map(int, input().split())
        if q:
            print('YES' if [a, b] == get(a, b + 1) else 'NO')
        else:
            va, vb = m[a + n], m[b + n]
            update(a, vb)
            update(b, va)
