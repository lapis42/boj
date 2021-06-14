import sys
r = sys.stdin.readline


isconnected = lambda i, j: abs(p[i][0] - p[j][0]) + abs(p[i][1] - p[j][1]) <= 1000


for _ in range(int(r())):
    n = int(r())
    p = [list(map(int, r().split())) for _ in range(n + 2)]

    connected = [[0] * (n + 2) for _ in range(n + 2)]
    for i in range(n + 2):
        for j in range(i + 1, n + 2):
            if isconnected(i, j):
                connected[i][j] = connected[j][i] = 1

    for m in range(n + 2):
        for s in range(n + 2):
            for e in range(n + 2):
                if connected[s][m] and connected[m][e]:
                    connected[s][e] = 1

    print('happy' if connected[0][-1] else 'sad')





