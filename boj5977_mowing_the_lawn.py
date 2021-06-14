import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
q = deque([0])
total = 0
a = [0] * (n + 1)
for i in range(1, n + 1):
    x = int(input())
    a[i] = x
    total += x

    while q and i - q[0] > k + 1:
        q.popleft()
    if q:
        a[i] = a[q[0]] + x
    while q and a[i] <= a[q[-1]]:
        q.pop()
    q.append(i)

print(total - min(a[n-k:]))
