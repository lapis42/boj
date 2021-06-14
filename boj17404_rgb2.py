import sys
input = sys.stdin.readline

n = int(input())
x = [list(map(int, input().split())) for _ in range(n)]

ans = []
for s in range(3):
    dp = [[2000] * 3 for _ in range(n)]
    dp[0][s] = x[0][s]

    for i in range(1, n):
        for j in range(3):
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j - 2]) + x[i][j]

    ans.append(min(dp[-1][s - 1], dp[-1][s - 2]))

print(min(ans))
