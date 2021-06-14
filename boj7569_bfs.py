import sys
from collections import deque
input = sys.stdin.readline

dx, dy, dz = [-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]


def bfs(arr):
    h, n, m = len(arr), len(arr[0]), len(arr[0][0])

    queue = deque()
    cnt = [[[0] * m for _ in range(n)] for _ in range(h)]
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if arr[i][j][k] == 1:
                    queue.append((i, j, k))

    while queue:
        x, y, z = queue.popleft()
        for ix, iy, iz in zip(dx, dy, dz):
            nx, ny, nz = x + ix, y + iy, z + iz
            if 0 <= nx < h and 0 <= ny < n and \
               0 <= nz < m and arr[nx][ny][nz] == 0:
                arr[nx][ny][nz] = 1
                cnt[nx][ny][nz] = cnt[x][y][z] + 1
                queue.append((nx, ny, nz))

    max_cnt = 0
    for i in range(h):
        for j in range(n):
            if 0 in arr[i][j]:
                return -1
            else:
                max_cnt = max(max_cnt, max(cnt[i][j]))
    return max_cnt


m, n, h = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
print(bfs(arr))
