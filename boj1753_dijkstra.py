import sys, heapq
input = sys.stdin.readline

max_dist = 200000


def dijkstra(edges, start):
    n_node = len(edges)
    dist = [max_dist] * n_node
    dist[start] = 0

    queue = []
    heapq.heappush(queue, (dist[start], start))
    while queue:
        dist_now, node_now = heapq.heappop(queue)
        if dist[node_now] < dist_now: continue
        for node_next, dist_edge in edges[node_now]:
            dist_next = dist_now + dist_edge
            if dist_next < dist[node_next]:
                dist[node_next] = dist_next
                heapq.heappush(queue, (dist_next, node_next))

    return dist


def main():
    n_node, n_edge = map(int, input().split())
    start = int(input()) - 1

    edges = [[] for _ in range(n_node)]
    for _ in range(n_edge):
        u, v, w = map(int, input().split())
        edges[u - 1].append((v-1, w))

    distance = dijkstra(edges, start)

    for d in distance:
        if d == max_dist:
            print("INF")
        else:
            print(d)


if __name__ == "__main__":
    main()
