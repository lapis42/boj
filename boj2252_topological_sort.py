import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

degree = [0] * (n + 1)
for i in range(1, n + 1):
    for j in graph[i]:
        degree[j] += 1

queue = deque()
for i in range(1, n + 1):
    if degree[i] == 0:
        queue.append(i)

ans = []
while queue:
    node = queue.popleft()
    ans.append(node)

    for i in graph[node]:
        degree[i] -= 1
        if degree[i] == 0:
            queue.append(i)

print(*ans)
