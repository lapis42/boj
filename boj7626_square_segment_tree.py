import sys
from bisect import bisect_left
input = sys.stdin.readline


def update_range(i, start, end, left, right, diff):
    if left > end or right < start:
        return
    if left <= start and end <= right:
        cnt[i] += diff
    else:
        mid = (start + end) // 2
        update_range(2*i + 1, start, mid, left, right, diff)
        update_range(2*i + 2, mid + 1, end, left, right, diff)

    if cnt[i]:
        t[i] = ys[end + 1] - ys[start]
    else:
        if start != end:
            t[i] = t[2*i + 1] + t[2*i + 2]
        else:
            t[i] = 0


n = int(input())
a = []
ys = set()
for _ in range(n):
    x1, x2, y1, y2 = map(int, input().split())
    a.append([x1, y1, y2, 1])
    a.append([x2, y1, y2, -1])
    ys.update({y1, y2})

a.sort()
ys = sorted(ys)
n_ys = len(ys) - 1

p2 = 1
while p2 < n_ys:
    p2 <<= 1
M = 2 * p2 - 1

t = [0] * M
cnt = [0] * M

ans = 0
px = a[0][0]
for x, y1, y2, diff in a:
    ans += (x - px) * t[0]
    px = x

    left = bisect_left(ys, y1)
    right = bisect_left(ys, y2) - 1
    update_range(0, 0, n_ys - 1, left, right, diff)

print(ans)
