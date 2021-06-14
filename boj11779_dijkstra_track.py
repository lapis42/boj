import sys
from heapq import heappush, heappop
input = sys.stdin.readline

# input
n_node, n_edge = int(input()), int(input())
edges = [[] for _ in range(n_node + 1)]
for _ in range(n_edge):
    a, b, c = map(int, input().split())
    edges[a].append((c, b))
start, end = map(int, input().split())

# variables
dist = [sys.maxsize] * (n_node + 1)
track = [0] * (n_node + 1)

# dijkstra
Q = [(0, start)]  # dist / start
while Q:
    dist_now, node_now = heappop(Q)

    if dist_now > dist[node_now]:
        continue

    for dist_next, node_next in edges[node_now]:
        dist_next += dist_now
        if dist_next < dist[node_next]:
            dist[node_next] = dist_next
            track[node_next] = node_now
            heappush(Q, (dist_next, node_next))

# backward
i = end
ans = [end]
while i != start:
    i = track[i]
    ans.append(i)

# output
print(dist[end])
print(len(ans))
print(*ans[::-1])
