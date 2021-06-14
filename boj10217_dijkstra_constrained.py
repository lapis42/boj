import sys
import heapq
input = sys.stdin.readline

dist_max = sys.maxsize


def dijkstra_constrained(edges, n_node, cost_max):
    dist = [[dist_max] * (cost_max + 1) for _ in range(n_node + 1)]
    dist[1][0] = 0
    queue = [(0, 0, 1)]

    while queue:
        dist_now, cost_now, node_now = heapq.heappop(queue)

        if node_now == n_node:
            return dist_now

        if dist_now > dist[node_now][cost_now]:
            continue

        for node_next, cost_next, dist_next in edges[node_now]:
            cost_next += cost_now
            dist_next += dist_now

            if cost_next > cost_max or dist_next >= dist[node_next][cost_next]:
                continue

            for c in range(cost_next, cost_max + 1):
                if dist[node_next][c] > dist_next:
                    dist[node_next][c] = dist_next
                else:
                    break

            heapq.heappush(queue, (dist_next, cost_next, node_next))

    return -1


for _ in range(int(input())):
    n_node, cost_max, n_edge = map(int, input().split())

    edges = [[] for _ in range(n_node + 1)]
    for _ in range(n_edge):
        u, v, c, d = map(int, input().split())
        if c > cost_max: continue
        edges[u].append((v, c, d))

    dist = dijkstra_constrained(edges, n_node, cost_max)

    if dist == -1:
        print('Poor KCM')
    else:
        print(dist)
