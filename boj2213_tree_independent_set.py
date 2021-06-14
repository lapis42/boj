import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def dfs(i, parent, include_self):
    if include_self:
        # you can either include or exclude self
        if dp[i][1] == -1:
            ans = w[i]
            group = [i]
            for j in graph[i]:
                if j == parent: continue
                cnt, g = dfs(j, i, 0)
                ans += cnt
                group += g
            dp[i][1] = ans
            s[i][1] = group

        if dp[i][0] == -1:
            ans = 0
            group = []
            for j in graph[i]:
                if j == parent: continue
                cnt, g = dfs(j, i, 1)
                ans += cnt
                group += g
            dp[i][0] = ans
            s[i][0] = group

        if dp[i][0] > dp[i][1]:
            return dp[i][0], s[i][0]
        else:
            return dp[i][1], s[i][1]

    else:
        # exclude self
        if dp[i][0] == -1:
            ans = 0
            group = []
            for j in graph[i]:
                if j == parent: continue
                cnt, g = dfs(j, i, 1)
                ans += cnt
                group += g
            dp[i][0] = ans
            s[i][0] = group

        return dp[i][0], s[i][0]


n = int(input())
w = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [[-1] * 2 for _ in range(n + 1)]
s = [[[] for _ in range(2)] for _ in range(n + 1)]
ans, group = dfs(1, -1, 1)
print(ans)
print(*sorted(group))
