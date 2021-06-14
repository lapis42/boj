import math
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# bfs
dp = [[0] * (n + 1)]
queue = deque([(1, 1)])
depth = [0] * (n + 1)
depth[1] = 1
while queue:
    i, d = queue.popleft()
    for j in graph[i]:
        if not depth[j]:
            queue.append((j, d + 1))
            dp[0][j] = i
            depth[j] = d + 1

# sparse dp
k = int(math.log2(max(depth) - 1))
for i in range(1, k + 1):
    temp = [0] * (n + 1)
    for j in range(1, n + 1):
        temp[j] = dp[i - 1][dp[i - 1][j]]
    dp.append(temp)

for _ in range(int(input())):
    a, b = map(int, input().split())

    if depth[a] < depth[b]:
        a, b = b, a

    # matching depth
    d = depth[a] - depth[b]
    for i in range(k, -1, -1):
        if d & 1 << i:
            a = dp[i][a]
            d -= 1 << i

    if a == b:
        print(a)
        continue

    # trace parents
    i = 0
    j = depth[b] - 1
    while i < j:
        m = int(math.log2(j - i))
        ta = dp[m][a]
        tb = dp[m][b]
        if ta == tb:
            i = j - 2**m + 1
        else:
            j -= 2**m
            a = ta
            b = tb

    print(dp[0][a])
