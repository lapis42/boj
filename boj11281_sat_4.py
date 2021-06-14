import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(i):
    visited[i] = 1
    for j in g[i]:
        if not visited[j]:
            dfs(j)
    stack.append(i)


def dfs_rev(i):
    component[i] = cnt
    for j in gr[i]:
        if component[j] == -1:
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
visited = [0] * (2 * n + 1)
for i in range(-n, n + 1):
    if i and not visited[i]:
        dfs(i)

cnt = 0
component = [-1] * (2 * n + 1)
for i in reversed(stack):
    if component[i] == -1:
        dfs_rev(i)
        cnt += 1

# Check 2-Satisfiability
issatisfiable = 1
assignment = [0] * (n + 1)
for i in range(1, n + 1):
    if component[i] == component[-i]:
        issatisfiable = 0
        break
    assignment[i] = int(component[i] > component[-i])

print(issatisfiable)
if issatisfiable:
    print(*assignment[1:])
