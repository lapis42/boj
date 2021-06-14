import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(i):
    visited[i] = 1
    for j in g[i]:
        if not visited[j]:
            dfs(j)
    stack.append(i)


def dfs_rev(i):
    global cnt
    ans = cash[i]
    visited[i] = cnt
    for j in gr[i]:
        if not visited[j]:
            ans += dfs_rev(j)
    return ans


def dfs_cash(i):
    global dp
    if dp[i] == -1:
        temp = 0
        for j in g_scc[i]:
            temp = max(temp, dfs_cash(j))
        if temp == 0 and not r_scc[i]:
            dp[i] = 0
        else:
            dp[i] = sums[i] + temp
    return dp[i]


# input
n, m = map(int, input().split())

g = [[] for _ in range(n + 1)]
gr = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    gr[b].append(a)

cash = [0] + [int(input()) for _ in range(n)]
s, p = map(int, input().split())
restaurant = list(map(int, input().split()))

# Kosaraju's algorithm
cnt = 0
stack = []
visited = [0] * (n + 1)
for i in range(1, n + 1):
    if not visited[i]:
        cnt += 1
        dfs(i)

cnt = 0
visited = [0] * (n + 1)
sums = []
for i in reversed(stack):
    if not visited[i]:
        cnt += 1
        sums.append(dfs_rev(i))

# graph between sccs
g_scc = [set() for _ in range(cnt)]
r_scc = [0] * cnt
for i in range(1, n + 1):
    for j in g[i]:
        if visited[i] != visited[j]:
            g_scc[visited[i] - 1].add(visited[j] - 1)
    if i in restaurant:
        r_scc[visited[i] - 1] = 1

# search
dp = [-1] * cnt
print(dfs_cash(visited[s] - 1))
