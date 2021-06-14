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


n, m = int(input()), int(input())
idx = list(range(n + 1))

for i in range(1, n + 1):
    x = list(map(int, input().split()))
    for j in range(i + 1, n + 1):
        if x[j - 1]:
            union(i, j)

t = list(map(int, input().split()))
gx = find(t[0])
doable = True
for i in range(1, m):
    if find(t[i]) != gx:
        doable = False
        break

print('YES' if doable else 'NO')
