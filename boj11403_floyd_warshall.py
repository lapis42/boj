import sys
r = sys.stdin.readline

n = int(r())
d = [list(map(int, r().split())) for _ in range(n)]

for m in range(n):
    for s in range(n):
        for e in range(n):
            if d[s][m] and d[m][e]:
                d[s][e] = 1

for i in d:
    print(*i)
