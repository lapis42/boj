import sys
input = sys.stdin.readline


def find(i):
    while i != idx[i]:
        idx[i] = idx[idx[i]]
        i = idx[i]
    return i


def union(x, y):
    xset = find(name_idx[x])
    yset = find(name_idx[y])
    if xset != yset:
        idx[xset] = yset
        size[yset] += size[xset]
    print(size[yset])


for _ in range(int(input())):
    f = int(input())

    cnt = 0
    idx = list(range(2 * f))
    size = [1] * (2 * f)
    name_idx = {}

    for _ in range(f):
        a, b = input().split()

        if a not in name_idx:
            name_idx[a] = cnt
            cnt += 1
        if b not in name_idx:
            name_idx[b] = cnt
            cnt += 1

        union(a, b)
