import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
d = list(map(int, input().split()))

x = [d[0]]
arr = [0] * n
for i in range(1, n):
    if d[i] > x[-1]:
        x.append(d[i])
        arr[i] = len(x) - 1
    else:
        idx = bisect_left(x, d[i])
        x[idx] = d[i]
        arr[i] = idx

ans = []
k = len(x) - 1
for i in reversed(range(n)):
    if k == arr[i]:
        ans.append(d[i])
        k -= 1

print(len(x))
print(*reversed(ans))
