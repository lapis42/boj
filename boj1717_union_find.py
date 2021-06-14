import sys
input = sys.stdin.readline


def find(i):
    while i != idx[i]:
        idx[i] = idx[idx[i]]
        i = idx[i]
    return i


def union(x, y):
    xset = find(x)
    yset = find(y)
    idx[xset] = yset


n, m = map(int, input().split())
idx = list(range(n + 1))

for _ in range(m):
    c, a, b = map(int, input().split())
    if c:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
    else:
        union(a, b)
