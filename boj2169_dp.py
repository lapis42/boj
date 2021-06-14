import sys
input = sys.stdin.readline

n, m = map(int, input().split())
v = [list(map(int, input().split())) for _ in range(n)]

dp = [[[-10**5] * 2 for _ in range(m)] for _ in range(n)]
dp[0][0][0] = v[0][0]
for i in range(1, m):
    dp[0][i][0] = dp[0][i - 1][0] + v[0][i]

for i in range(1, n):
    dp[i][0][0] = max(dp[i - 1][0]) + v[i][0]
    dp[i][-1][1] = max(dp[i - 1][-1]) + v[i][-1]
    for j in range(1, m):
        dp[i][j][0] = max(max(dp[i - 1][j]), dp[i][j - 1][0]) + v[i][j]
    for j in reversed(range(m - 1)):
        dp[i][j][1] = max(max(dp[i - 1][j]), dp[i][j + 1][1]) + v[i][j]

print(max(dp[-1][-1]))
