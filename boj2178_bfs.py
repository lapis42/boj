import sys
from collections import deque
input = sys.stdin.readline

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(arr, cnt):
    n, m = len(arr), len(arr[0])
    arr[0][0] = 0
    cnt[0][0] = 1
    cue = deque([(0, 0)])
    while cue:
        x, y = cue.popleft()
        for ix, iy in zip(dx, dy):
            nx = x + ix
            ny = y + iy
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny]:
                arr[nx][ny] = 0
                cnt[nx][ny] = cnt[x][y] + 1
                cue.append((nx, ny))


n, m = map(int, input().split())
arr = [list(map(int, list(input().rstrip()))) for _ in range(n)]
cnt = [[0] * m for _ in range(n)]
bfs(arr, cnt)
print(cnt[-1][-1])
