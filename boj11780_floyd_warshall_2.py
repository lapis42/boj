import sys
input = sys.stdin.readline

max_dist = 10**7

def floyd_warshall(edges, track, n_node):
    for m in range(1, n_node + 1):
        for s in range(1, n_node + 1):
            for e in range(1, n_node + 1):
                if edges[s][e] > edges[s][m] + edges[m][e]:
                    edges[s][e] = edges[s][m] + edges[m][e]
                    track[s][e] = m


def tracking(track, s, e):
    if s == e: return []
    m = track[s][e]
    if m == 0: return [s, e]
    return tracking(track, s, m)[:-1] + tracking(track, m, e)


n_node, n_edge = int(input()), int(input())
edges = [[max_dist] * (n_node + 1) for _ in range(n_node + 1)]
track = [[0] * (n_node + 1) for _ in range(n_node + 1)]

for i in range(1, n_node + 1):
    edges[i][i] = 0
for _ in range(n_edge):
    a, b, c = map(int, input().split())
    if edges[a][b] > c:
        edges[a][b] = c

floyd_warshall(edges, track, n_node)

for s in edges[1:]:
    s = [i if i < max_dist else 0 for i in s[1:]]
    print(*s)

for i in range(1, n_node + 1):
    for j in range(1, n_node + 1):
        if edges[i][j] < max_dist:
            ans = tracking(track, i, j)
            print(len(ans), *ans)
        else:
            print(0)
