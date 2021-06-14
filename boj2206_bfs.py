import sys
from collections import deque
input = sys.stdin.readline

dx, dy = [-2, -2, -1, -1, 1, 1, 2, 2], [-1, 1, -2, 2, -2, 2, -1, 1]


def bfs(start, goal, size):
    count = [[0] * size for _ in range(size)]
    queue = deque([start])

    while queue:
        x, y = queue.popleft()

        if (x, y) == goal:
            return count[x][y]

        for ix, iy in zip(dx, dy):
            nx, ny = x + ix, y + iy
            if 0 <= nx < size and 0 <= ny < size and count[nx][ny] == 0:
                queue.append((nx, ny))
                count[nx][ny] = count[x][y] + 1

    return -1


T = int(input())
for _ in range(T):
    size = int(input())
    start = tuple(map(int, input().split()))
    goal = tuple(map(int, input().split()))
    print(bfs(start, goal, size))
