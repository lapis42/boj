import sys
input = sys.stdin.readline

pts = []
for _ in range(2):
    a, b, c, d = map(int, input().split())
    if a <= c:
        pts += [(a, b), (c, d)]
    else:
        pts += [(c, d), (a, b)]

det = lambda pts, i, j, k: (pts[i][0] - pts[j][0]) * (pts[k][1] - pts[j][
    1]) - (pts[i][1] - pts[j][1]) * (pts[k][0] - pts[j][0])

d1 = det(pts, 0, 1, 2)
d2 = det(pts, 0, 1, 3)
d3 = det(pts, 2, 3, 0)
d4 = det(pts, 2, 3, 1)

c1 = d1 * d2 < 0 and d3 * d4 < 0
c2 = d1 == 0 and pts[0][0] <= pts[2][0] <= pts[1][0]
c3 = d2 == 0 and pts[0][0] <= pts[3][0] <= pts[1][0]

if c1 or c2 or c3:
    print(1)
else:
    print(0)
