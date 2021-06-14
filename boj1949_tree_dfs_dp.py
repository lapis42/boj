import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(i):
    visited[i] = 1
    dp[i] = [0, w[i]]
    for j in graph[i]:
        if not visited[j]:
            dfs(j)
            dp[i][1] += dp[j][0]
            dp[i][0] += max(dp[j])


n = int(input())
w = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [[0, 0] for _ in range(n + 1)]
visited = [0] * (n + 1)
dfs(1)
print(max(dp[1]))
