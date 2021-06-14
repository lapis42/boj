import sys
import math
from collections import deque
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dp = [[0] * (n + 1)]
cost_dp = [[0] * (n + 1)]
queue = deque([(1, 1)])
depth = [0] * (n + 1)
depth[1] = 1
while queue:
    i, d = queue.popleft()
    for j, c in graph[i]:
        if not depth[j]:
            dp[0][j] = i
            cost_dp[0][j] = c
            depth[j] = d + 1
            queue.append((j, d + 1))

m = int(math.log2(max(depth) - 1))
for i in range(1, m + 1):
    temp = [0] * (n + 1)
    cost_temp = [sys.maxsize] * (n + 1)
    for j in range(1, n + 1):
        k = dp[-1][j]
        temp[j] = dp[-1][k]
        cost_temp[j] = cost_dp[-1][j] + cost_dp[-1][k]
    dp.append(temp)
    cost_dp.append(cost_temp)

for _ in range(int(input())):
    q, *x = map(int, input().split())

    if q == 1:
        d, e = x
        if depth[d] > depth[e]:
            d, e = e, d

        diff = depth[e] - depth[d]
        cost = 0
        while diff:
            m = int(math.log2(diff))
            cost += cost_dp[m][e]
            e = dp[m][e]
            diff -= 2**m

        if d == e:
            print(cost)
            continue

        i = 0
        j = depth[d] - 1
        while i < j:
            m = int(math.log2(j - i))
            td = dp[m][d]
            te = dp[m][e]
            if td == te:
                i = j - 2**m + 1
            else:
                j -= 2**m
                cost += cost_dp[m][d] + cost_dp[m][e]
                d = td
                e = te
        cost += cost_dp[0][d] + cost_dp[0][e]
        print(cost)
    else:
        a, b, c = x

        if depth[a] > depth[b]:
            d, e = a, b
        else:
            d, e = b, a

        diff = depth[d] - depth[e]
        while diff:
            m = int(math.log2(diff))
            d = dp[m][d]
            diff -= 2**m

        if d != e:
            i = 1
            j = depth[e]
            while i < j:
                m = int(math.log2(j - i))
                td = dp[m][d]
                te = dp[m][e]
                if td == te:
                    i = j - 2**m + 1
                else:
                    j -= 2**m
                    d = td
                    e = te
        else:
            j = depth[e] + 1

        len_a = depth[a] - (j - 1)
        len_b = depth[b] - (j - 1)

        if c - 1 <= len_a:
            diff = c - 1
            while diff:
                m = int(math.log2(diff))
                a = dp[m][a]
                diff -= 2**m
            print(a)
        else:
            diff = len_a + len_b - c + 1
            while diff:
                m = int(math.log2(diff))
                b = dp[m][b]
                diff -= 2**m
            print(b)
