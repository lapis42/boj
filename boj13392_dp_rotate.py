import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

max_n = 10**5


def solve(i, t):
    if i == n:
        return 0
    if dp[i][t] == max_n:
        c = (x[i] + t) % 10
        l = (y[i] - c) % 10
        r = (c - y[i]) % 10
        ans_l = l + solve(i + 1, (t + l) % 10)
        ans_r = r + solve(i + 1, t)
        dp[i][t] = min(ans_l, ans_r)
    return dp[i][t]


n = int(input())
x = list(map(int, input().rstrip()))
y = list(map(int, input().rstrip()))

dp = [[max_n] * 10 for _ in range(n)]
solve(0, 0)
print(dp[0][0])
