import sys
from heapq import heappush, heappop
input = sys.stdin.readline


def dist(nodes, a, b):
    return ((nodes[a][0] - nodes[b][0])**2 +
            (nodes[a][1] - nodes[b][1])**2)**0.5


def find(idx, i):
    while i != idx[i]:
        idx[i] = idx[idx[i]]
        i = idx[i]
    return i


def union(idx, x, y):
    xset = find(idx, x)
    yset = find(idx, y)
    if xset != yset:
        idx[xset] = yset
        return True
    else:
        return False


def kruskal(graph, n_node):
    idx = list(range(n_node + 1))
    weight = 0
    cnt = n_node - 1
    while cnt > 0:
        c, a, b = heappop(graph)
        if union(idx, a, b):
            weight += c
            cnt -= 1
    return weight


def main():
    n_node = int(input())

    nodes = []
    for _ in range(n_node):
        a, b = map(float, input().split())
        nodes.append((a, b))

    graph = []
    for i in range(n_node):
        for j in range(i):
            heappush(graph, (dist(nodes, i, j), i, j))

    print(kruskal(graph, n_node))


if __name__ == "__main__":
    main()
