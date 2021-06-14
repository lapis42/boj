import sys
from heapq import heappush, heappop
from collections import deque
input = sys.stdin.readline

move = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def bfs(i, j):
    visited[i][j] = 1
    points = [(i, j)]
    Q = deque([(i, j)])

    while Q:
        x, y = Q.popleft()
        for nx, ny in move:
            nx += x
            ny += y
            if 0 <= nx < n and 0 <= ny < m and arr[nx][
                    ny] and not visited[nx][ny]:
                points.append((nx, ny))
                visited[nx][ny] = 1
                Q.append((nx, ny))

    return points


def dist(x, y):
    ans = 10
    for a, b in group[x]:
        for c, d in group[y]:
            if a == c:
                if b > d:
                    s, e = d, b
                else:
                    s, e = b, d
                diff = e - s - 1
                if diff > 1 and diff < ans:
                    noland = True
                    for i in range(s + 1, e):
                        if arr[a][i]:
                            noland = False
                            break
                    if noland:
                        ans = diff
            elif b == d:
                if a > c:
                    s, e = c, a
                else:
                    s, e = a, c
                diff = e - s - 1
                if diff > 1 and diff < ans:
                    noland = True
                    for i in range(s + 1, e):
                        if arr[i][b]:
                            noland = False
                            break
                    if noland:
                        ans = diff
    if ans == 10:
        return 0
    else:
        return ans


def kruskal(graph, n_node):
    def find(i):
        while i != idx[i]:
            idx[i] = idx[idx[i]]
            i = idx[i]
        return i

    idx = list(range(n_node))
    cnt = 0
    ans = 0
    while graph:
        d, x, y = heappop(graph)
        xset, yset = find(x), find(y)
        if xset != yset:
            idx[xset] = yset
            cnt += 1
            ans += d

    if cnt == n_node - 1:
        return ans
    else:
        return -1


# input
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# check lands
visited = [[0] * m for _ in range(n)]
group = []
cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] and not visited[i][j]:
            group.append(bfs(i, j))
            cnt += 1

# check distance between lands
graph = []
n_group = len(group)
for i in range(n_group):
    for j in range(i):
        d = dist(i, j)
        if d:
            heappush(graph, (d, i, j))

# kruskal algorithm
print(kruskal(graph, n_group))
