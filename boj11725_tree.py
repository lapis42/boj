import sys
from collections import deque
input = sys.stdin.readline


def bfs(edges, n_node):
    tree = [0] * (n_node + 1)
    Q = deque([1])

    while Q:
        parent = Q.popleft()
        for child in edges[parent]:
            if tree[child] == 0:
                tree[child] = parent
                Q.append(child)

    return tree


n_node = int(input())
edges = [[] for _ in range(n_node + 1)]
for _ in range(n_node - 1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

tree = bfs(edges, n_node)

print(*tree[2:])
