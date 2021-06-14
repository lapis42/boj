import sys
input = sys.stdin.readline

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def dfs(x, y):
    data[x][y] = 0
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m and data[nx][ny]:
            dfs(nx, ny)


def bfs(x, y):
    cue = [(x, y)]
    while cue:
        x, y = cue.pop(0)
        if data[x][y]:
            data[x][y] = 0
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < n and 0 <= ny < m and data[nx][ny]:
                    cue.append((nx, ny))


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    data = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        data[y][x] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if data[i][j]:
                cnt += 1
                bfs(i, j)

    print(cnt)
