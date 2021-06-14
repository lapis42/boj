import sys
from operator import xor
r = sys.stdin.readline


def update(i, v):
    i += n
    dp[i] = v
    while i > 1:
        j = xor(i, 1)
        dp[i >> 1] = max(dp[i], dp[j])
        i >>= 1


def get(i, j):
    ans = -10**9
    i += n
    j += n
    while i < j:
        if i & 1:
            ans = max(ans, dp[i])
            i += 1
        if j & 1:
            j -= 1
            ans = max(ans, dp[j])
        i >>= 1
        j >>= 1
    return ans


n, d = map(int, r().split())
k = list(map(int, r().split()))

dp = [-10**9] * (2 * n)
for i in range(n):
    update(i, k[i] + max(get(max(i - d, 0), i), 0))

print(get(0, n))
