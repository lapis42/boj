import sys
input = sys.stdin.readline

pts = [list(map(int, input().split())) for _ in range(3)]

a, b = pts[0][0] - pts[1][0], pts[0][1] - pts[1][1]
c, d = pts[2][0] - pts[1][0], pts[2][1] - pts[1][1]

ans = a * d - b * c
if ans > 0:
    print(-1)
elif ans < 0:
    print(1)
else:
    print(0)
