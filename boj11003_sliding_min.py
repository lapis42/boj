import sys
from collections import deque
read = lambda: map(int, sys.stdin.readline().split())

n, l = read()
a = list(read())

ans = []
q = deque()
for i, v in enumerate(a):
    while q and v < q[-1]:
        q.pop()
    q.append(v)
    ans.append(q[0])

    if i >= l - 1 and a[i - l + 1] == q[0]:
        q.popleft()
print(*ans)
