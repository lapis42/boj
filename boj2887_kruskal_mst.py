import sys
from heapq import heappop, heappush
input = sys.stdin.readline


def dist(a, b, i):
    return abs(nodes[a][i] - nodes[b][i])


def find(i):
    while i != idx[i]:
        idx[i] = idx[idx[i]]
        i = idx[i]
    return i


def union(x, y):
    xset, yset = find(x), find(y)
    if xset != yset:
        idx[xset] = yset
        return True
    else:
        return False


n_node = int(input())
nodes = [list(map(int, input().split())) + [i] for i in range(n_node)]

graph = []
for i in range(3):
    nodes.sort(key=lambda x: x[i])
    for j in range(n_node - 1):
        heappush(graph, (dist(j, j + 1, i), nodes[j][3], nodes[j + 1][3]))

idx = list(range(n_node))
cnt = 0
ans = 0
while cnt < n_node - 1:
    d, x, y = heappop(graph)

    if union(x, y):
        ans += d
        cnt += 1

print(ans)
