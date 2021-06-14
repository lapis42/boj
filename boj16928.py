import sys
from collections import deque
r = lambda: map(int, sys.stdin.readline().split())

def bfs():
    x = 1
    q = deque([[0, x]])
    visited = [0] * 101
    while q:
        n, x = q.popleft()
        if x == 100:
            return n
        for ix in range(6):
            ix += x + 1
            if ix <= 100 and not visited[ix]:
                visited[ix] = 1
                q.append([n + 1, graph[ix]])
    return 0


n, m = r()
graph = list(range(101))
for _ in range(n + m):
    a, b = r()
    graph[a] = b

print(bfs())

