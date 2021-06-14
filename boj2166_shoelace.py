import sys
input = sys.stdin.readline

shoelace = lambda a, b: a[0] * b[1] - a[1] * b[0]

n = int(input())
pts = [list(map(int, input().split())) for _ in range(n)]

ans = shoelace(pts[-1], pts[0])
for i in range(n - 1):
    ans += shoelace(pts[i], pts[i + 1])

print("{:0.1f}".format(abs(ans / 2)))
