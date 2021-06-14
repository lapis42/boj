import sys
import math
input = sys.stdin.readline

n = int(input())
k = int(input())
d = 1000000003

dp = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(n + 1):
    dp[i][1] = i

for i in range(2, k + 1):
    for j in range(2 * i, n + 1):
        dp[j][i] = (dp[j - 1][i] + dp[j - 2][i - 1]) % d

print(dp[n][k])
