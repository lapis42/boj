import sys
from collections import deque

sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(i):
    if not visited[i]:
        visited[i] = 1
        for j in graph[i]:
            if not visited[j]:
                dfs(j)
        stack.append(i)


def bfs(i):
    visited[i] = 1
    queue = deque([i])
    while queue:
        i = queue.popleft()
        for j in graph[i]:
            if not visited[j]:
                visited[j] = 1
                queue.append(j)


for _ in range(int(input())):
    n, m = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)

    stack = []
    visited = [0] * (n + 1)
    for i in range(1, n + 1):
        dfs(i)

    cnt = 0
    visited = [0] * (n + 1)
    for i in stack[::-1]:
        if not visited[i]:
            bfs(i)
            cnt += 1

    print(cnt)
