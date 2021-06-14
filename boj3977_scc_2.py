import sys
from collections import deque
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(g, i, ans):
    global cnt
    visited[i] = cnt
    for j in g[i]:
        if not visited[j]:
            dfs(g, j, ans)
    ans.append(i)


t = int(input())
for i_t in range(t):
    n, m = map(int, input().split())

    g = [[] for _ in range(n)]
    gr = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a].append(b)
        gr[b].append(a)

    cnt = 0
    stack = []
    visited = [0] * n
    for i in range(n):
        if not visited[i]:
            cnt += 1
            dfs(g, i, stack)

    cnt = 0
    visited = [0] * n
    for i in reversed(stack):
        if not visited[i]:
            cnt += 1
            dfs(gr, i, [])

    indegree = [0] * cnt
    for i in range(n):
        for j in g[i]:
            if visited[i] != visited[j]:
                indegree[visited[j] - 1] += 1

    if indegree.count(0) != 1:
        print('Confused')
    else:
        idx = indegree.index(0) + 1
        for i in range(n):
            if visited[i] == idx:
                print(i)
    print()

    if i_t < t - 1:
        input()
