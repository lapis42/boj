import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readlines


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


x = input()
n_x = len(x)
i_x = 0
while i_x < n_x:
    n, m = map(int, x[i_x].split())
    g = [set() for _ in range(2 * n + 1)]
    gr = [set() for _ in range(2 * n + 1)]
    for i in range(m):
        a, b = map(int, x[i_x + i + 1].split())
        g[-a].add(b)
        g[-b].add(a)
        gr[b].add(-a)
        gr[a].add(-b)
    g[-1].add(1)
    gr[1].add(-1)

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
    for i in range(1, n + 1):
        if component[i] == component[-i]:
            issatisfiable = False
            break
    if issatisfiable:
        print('yes')
    else:
        print('no')

    i_x += m + 1
