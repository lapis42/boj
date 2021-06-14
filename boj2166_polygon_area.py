import sys
input = sys.stdin.readline

area = lambda a, b, c: (a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] *
                        (a[1] - b[1])) / 2

n = int(input())
pts = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(2, n):
    ans += area(pts[0], pts[i-1], pts[i])

print("{:0.1f}".format(abs(ans)))

