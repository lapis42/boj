import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(i):
    visited[i] = 1
    dp[i] = [0, 1]
    for j in graph[i]:
        if not visited[j]:
            dfs(j)
            dp[i][0] += dp[j][1]
            dp[i][1] += min(dp[j])


n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [[0, 0] for _ in range(n + 1)]
visited = [0] * (n + 1)
dfs(1)
print(min(dp[1]))
