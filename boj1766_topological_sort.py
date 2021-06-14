import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
degree = [0] * (n + 1)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    degree[b] += 1

queue = []
for i in range(1, n + 1):
    if degree[i] == 0:
        heappush(queue, i)

ans = []
while queue:
    i = heappop(queue)
    ans.append(i)
    for j in graph[i]:
        degree[j] -= 1
        if degree[j] == 0:
            heappush(queue, j)

print(*ans)
