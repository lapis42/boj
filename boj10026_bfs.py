import sys
from collections import deque
r = sys.stdin.readline

direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def bfs(i, j, blind):
    t = d[i][j]
    visited[i][j] = 1
    q = deque([(i, j)])
    while q:
        i, j = q.popleft()
        for k, l in direction:
            k += i
            l += j
            if 0 <= k < n and 0 <= l < n and not visited[k][l]:
                if blind:
                    if (t != 'B' and d[k][l] != 'B') or (t == 'B' and d[k][l] == 'B'):
                        visited[k][l] = 1
                        q.append((k, l))
                elif d[k][l] == t:
                    visited[k][l] = 1
                    q.append((k, l))


n = int(r())
d = [r().rstrip() for _ in range(n)]

cnt = 0
visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            cnt += 1
            bfs(i, j, False)

cnt_blind = 0
visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            cnt_blind += 1
            bfs(i, j, True)

print(cnt, cnt_blind)
