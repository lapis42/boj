"""BOJ14002: longest increasing subsequence 4
"""
import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

x = [a[0]]
arr = [0] * n
cnt = 0
for i in range(1, n):
    if a[i] > x[-1]:
        cnt += 1
        x.append(a[i])
        arr[i] = cnt
    else:
        idx = bisect_left(x, a[i])
        x[idx] = a[i]
        arr[i] = idx

ans = [0] * (cnt + 1)
for i in range(n-1, -1, -1):
    if arr[i] == cnt:
        ans[cnt] = a[i]
        cnt -= 1

print(len(ans))
print(*ans)
