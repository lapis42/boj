import sys
from collections import deque
input = sys.stdin.readline


def bfs(graph, n_node, start):
    visited = [0] * (n_node + 1)
    visited[start] = 1
    max_dist = 0
    max_node = start
    Q = deque([(start, 0)])

    while Q:
        node_now, dist_now = Q.popleft()
        for node_next, dist_next in graph[node_now]:
            if visited[node_next] == 0:
                dist_next += dist_now
                visited[node_next] = 1
                Q.append((node_next, dist_next))
                if max_dist < dist_next:
                    max_dist = dist_next
                    max_node = node_next

    return max_node, max_dist


def dfs(graph, visited, node_now, dist_now = 0):
    visited[node_now] = 1
    dists = [dist_now]
    for node_next, dist_next in graph[node_now]:
        if not visited[node_next]:
            dist_next += dist_now
            dists.append(dfs(graph, visited, node_next, dist_next) - dist_now)

    dists.sort()
    if len(dists) == 1:
        return dists[-1]
    return dists[-1] + dists[-2]


def main():
    n_node = int(input())
    graph = [[] for _ in range(n_node + 1)]
    for _ in range(n_node):
        a, *b = map(int, input().split())
        for i in range(len(b) // 2):
            graph[a].append(b[2 * i:2 * i + 2])

    #start, _ = bfs(graph, n_node, 1)
    #_, max_dist = bfs(graph, n_node, start)

    visited = [0] * (n_node + 1)
    max_dist = dfs(graph, visited, 1, 0)
    print(max_dist)


if __name__ == "__main__":
    main()
