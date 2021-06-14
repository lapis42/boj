import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def dfs(i, parent):
    if dp[i] == 0:
        ans = 1
        for j in graph[i]:
            if j == parent: continue
            ans += dfs(j, i)
        dp[i] = ans
    return dp[i]


n, r, q = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [0] * (n + 1)
dfs(r, 0)

for _ in range(q):
    print(dp[int(input())])
