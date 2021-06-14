import sys
input = sys.stdin.readline

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

a = x1 - x2
b = -(x3 - x4)
c = y1 - y2
d = -(y3 - y4)
e = x4 - x2
f = y4 - y2

det = a * d - b * c

if det == 0:
    print(0)
else:
    k = (d * e - b * f) / det
    l = (a * f - c * e) / det

    if 0 <= k <= 1 and 0 <= l <= 1:
        print(1)
    else:
        print(0)
