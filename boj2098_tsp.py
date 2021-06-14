import sys
input = sys.stdin.readline

n = int(input())
c = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n] + [[10**8] * n for _ in range(2**n - 1)]

# Start from 0. Should return to 0 (check dp[-1][0])
for i in range(n):
    if c[0][i]:
        dp[1 << i][i] = c[0][i]

for idx in range(1, 2**n):
    for j in range(n):  # to j city
        if not (idx & 1 << j):  # if haven't visited j city
            for i in range(n):  # start from i city
                if c[i][j] and (idx & 1 << i): # road available & visited before
                    dp[idx | 1 << j][j] = min(dp[idx | 1 << j][j],
                                              dp[idx][i] + c[i][j])

print(dp[-1][0])
