def det(i, j, k):
    a = pts[i][0] - pts[j][0]
    b = pts[i][1] - pts[j][1]
    c = pts[k][0] - pts[j][0]
    d = pts[k][1] - pts[j][1]
    return a * d - b * c


def inrange(i, j, k):
    if pts[i][0] <= pts[j][0]:
        xmin, xmax = pts[i][0], pts[j][0]
    else:
        xmin, xmax = pts[j][0], pts[i][0]

    if pts[i][1] <= pts[j][1]:
        ymin, ymax = pts[i][1], pts[j][1]
    else:
        ymin, ymax = pts[j][1], pts[i][1]

    return xmin <= pts[k][0] <= xmax and ymin <= pts[k][1] <= ymax


pts = []
for _ in range(2):
    a, b, c, d = map(int, input().split())
    pts += [(a, b), (c, d)]

d1 = det(0, 1, 2)
d2 = det(0, 1, 3)
d3 = det(2, 3, 0)
d4 = det(2, 3, 1)

c1 = d1 * d2 < 0 and d3 * d4 < 0
c2 = d1 == 0 and inrange(0, 1, 2)
c3 = d2 == 0 and inrange(0, 1, 3)
c4 = d3 == 0 and inrange(2, 3, 0)
c5 = d4 == 0 and inrange(2, 3, 1)

if c1 or c2 or c3 or c4 or c5:
    print(1)
else:
    print(0)
