import sys
from heapq import heappush, heappop
input = sys.stdin.readline


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
    n_node, n_edge = map(int, input().split())

    graph = []
    for _ in range(n_edge):
        a, b, c = map(int, input().split())
        heappush(graph, (c, a, b))

    print(kruskal(graph, n_node))


if __name__ == "__main__":
    main()
