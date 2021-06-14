import sys
from collections import deque
input = sys.stdin.readline


def dets(i, j):
    a = pts[i][0] - pts[i][2]
    b = pts[i][1] - pts[i][3]
    c = pts[j][0] - pts[i][2]
    d = pts[j][1] - pts[i][3]
    e = pts[j][2] - pts[i][2]
    f = pts[j][3] - pts[i][3]
    return ((a * d - b * c), (a * f - b * e))

def inrange(i, j):
    if pts[i][0] <= pts[i][2]:
        xmin, xmax = pts[i][0], pts[i][2]
    else:
        xmin, xmax = pts[i][2], pts[i][0]
    if pts[i][1] <= pts[i][3]:
        ymin, ymax = pts[i][1], pts[i][3]
    else:
        ymin, ymax = pts[i][3], pts[i][1]
    inr1 = xmin <= pts[j][0] <= xmax and ymin <= pts[j][1] <= ymax
    inr2 = xmin <= pts[j][2] <= xmax and ymin <= pts[j][3] <= ymax
    return inr1, inr2


def cross(i, j):
    d1, d2 = dets(i, j)
    d3, d4 = dets(j, i)

    if d1 * d2 < 0 and d3 * d4 < 0:
        return True

    inr1, inr2 = inrange(i, j)
    inr3, inr4 = inrange(j, i)

    if d1 == 0 and inr1:
        return True
    if d2 == 0 and inr2:
        return True
    if d3 == 0 and inr3:
        return True
    if d4 == 0 and inr4:
        return True

    return False

def find(i):
    while i != idx[i]:
        idx[i] = idx[idx[i]]
        i = idx[i]
    return i


def union(x, y):
    xset, yset = find(x), find(y)
    idx[xset] = yset


n = int(input())
pts = [list(map(int, input().split())) for _ in range(n)]

idx = list(range(n))
for i in range(n):
    for j in range(i):
        if cross(i, j):
            union(i, j)

ans = {}
for i in range(n):
    temp = find(i)
    if temp not in ans:
        ans[temp] = 1
    else:
        ans[temp] += 1

print(len(ans))
print(max(ans.values()))
