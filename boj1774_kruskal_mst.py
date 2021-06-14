import sys
from heapq import heappush, heappop
input = sys.stdin.readline


def dist(a, b):
    return ((nodes[a][0] - nodes[b][0])**2 +
            (nodes[a][1] - nodes[b][1])**2)**0.5


def find(i):
    while i != idx[i]:
        idx[i] = idx[idx[i]]
        i = idx[i]
    return i


def union(x, y):
    xset = find(x)
    yset = find(y)
    if xset != yset:
        idx[xset] = yset
        return True
    else:
        return False


n_node, n_connected = map(int, input().split())
nodes = [list(map(int, input().split())) for _ in range(n_node)]

idx = list(range(n_node))
for _ in range(n_connected):
    a, b = map(int, input().split())
    union(a - 1, b - 1)

graph = []
for i in range(n_node):
    for j in range(i):
        heappush(graph, (dist(i, j), i, j))

ans = 0
while graph:
    c, a, b = heappop(graph)
    if union(a, b):
        ans += c

print("%0.2f" % ans)
