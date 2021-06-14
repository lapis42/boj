import sys
from heapq import heappush, heappop
input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    d = [0] + list(map(int, input().split()))

    graph = [[] for _ in range(n + 1)]
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)

    degree = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in graph[i]:
            degree[j] += 1

    queue = []
    for i in range(1, n + 1):
        if degree[i] == 0:
            heappush(queue, [d[i], i])

    ans = [sys.maxsize] * (n + 1)
    while queue:
        [cost, node] = heappop(queue)
        if ans[node] > cost:
            ans[node] = cost

        for i in graph[node]:
            degree[i] -= 1
            if degree[i] == 0:
                heappush(queue, [cost + d[i], i])

    print(ans[int(input())])
