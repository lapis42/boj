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


f = lambda l, c: int(l) if c == 'R' else -int(l)

n, m = map(int, input().split())
g = [set() for _ in range(2 * n + 1)]
gr = [set() for _ in range(2 * n + 1)]
for i in range(m):
    l0, c0, l1, c1, l2, c2 = input().split()
    a, b, c = f(l0, c0), f(l1, c1), f(l2, c2)
    g[-a].add(b)
    g[-a].add(c)
    g[-b].add(a)
    g[-b].add(c)
    g[-c].add(a)
    g[-c].add(b)
    gr[a].add(-b)
    gr[a].add(-c)
    gr[b].add(-a)
    gr[b].add(-c)
    gr[c].add(-a)
    gr[c].add(-b)

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

issatisfiable = True
ans = ['' for _ in range(n)]
for i in range(1, n + 1):
    if component[i] == component[-i]:
        issatisfiable = False
        break
    ans[i - 1] = 'R' if component[i] > component[-i] else 'B'

if issatisfiable:
    print(''.join(ans))
else:
    print(-1)
