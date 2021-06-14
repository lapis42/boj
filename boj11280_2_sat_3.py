import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(i):
    visited[i] = 0
    for j in g[i]:
        if visited[j]:
            dfs(j)
    stack.append(i)


def dfs_rev(i):
    visited[i] = cnt
    for j in gr[i]:
        if not visited[j]:
            dfs_rev(j)


# Input
n, m = map(int, input().split())
g = [set() for _ in range(2 * n + 1)]
gr = [set() for _ in range(2 * n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[-a].add(b)
    g[-b].add(a)
    gr[b].add(-a)
    gr[a].add(-b)

# Kosaraju's algorithm
stack = []
visited = [1] * (2 * n + 1)
for i in range(-n, n + 1):
    if i and visited[i]:
        dfs(i)

cnt = 0
for i in reversed(stack):
    if not visited[i]:
        cnt += 1
        dfs_rev(i)

# Check 2-Satisfiability
issatisfiable = 1
for i in range(1, n + 1):
    if visited[i] == visited[-i]:
        issatisfiable = 0
        break
print(issatisfiable)
