import sys
from collections import deque, defaultdict

input = sys.stdin.readline


def bfs(edge, start, visited):
    visited[start] = 1
    queue = deque([(start, 1)])  # index / group

    while queue:
        now, group = queue.popleft()
        for i in edge[now]:
            if visited[i] == 0:
                queue.append((i, -group))
                visited[i] = -group
            elif visited[i] == group:
                return 1
    return 0


def main():
    K = int(input())
    for _ in range(K):
        V, E = map(int, input().split())

        edge = defaultdict(set)
        for _ in range(E):
            a, b = map(int, input().split())
            edge[a - 1].add(b - 1)
            edge[b - 1].add(a - 1)

        visited = [0] * V
        fail = False
        for i in edge.keys():
            if visited[i] == 0:
                if bfs(edge, i, visited):
                    fail = True
                    break

        if fail:
            print('NO')
        else:
            print('YES')


if __name__ == '__main__':
    main()
