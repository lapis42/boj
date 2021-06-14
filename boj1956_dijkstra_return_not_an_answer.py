import sys
import heapq
input = sys.stdin.readline

dist_max = sys.maxsize


def dijkstra_return(edges, n_node):
    dist = [dist_max] * (n_node + 1)
    queue = []

    for node_next, dist_next in edges[1]:
        dist[node_next] = dist_next
        heapq.heappush(queue, (dist_next, node_next))
    
    print(queue, dist)

    while queue:
        dist_now, node_now = heapq.heappop(queue)

        if node_now == 1:
            return dist_now

        if dist_now > dist[node_now]:
            continue

        for node_next, dist_next in edges[node_now]:
            dist_next += dist_now
            if dist_next < dist[node_next]:
                dist[node_next] = dist_next
                heapq.heappush(queue, (dist_next, node_next))
                print(queue, dist)
                

    return -1


def main():
    n_node, n_edge = map(int, input().split())

    edges = [[] for _ in range(n_node + 1)]
    for _ in range(n_edge):
        u, v, d = map(int, input().split())
        edges[u].append((v, d))

    print(dijkstra_return(edges, n_node))

if __name__ == "__main__":
    main()
