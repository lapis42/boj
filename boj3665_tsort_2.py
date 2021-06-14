import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    t = list(map(int, input().split()))

    graph = [set() for _ in range(n + 1)]

    degree = [0] * (n + 1)
    degree[t[-1]] = n - 1
    for i in range(n - 2, -1, -1):
        graph[t[i]] = graph[t[i + 1]].copy()
        graph[t[i]].add(t[i + 1])
        degree[t[i]] = i

    m = int(input())
    isfail = False
    for i in range(m):
        a, b = map(int, input().split())
        if b in graph[a]:
            graph[a].remove(b)
            graph[b].add(a)
            degree[a] += 1
            degree[b] -= 1
        elif a in graph[b]:
            graph[a].add(b)
            graph[b].remove(a)
            degree[a] -= 1
            degree[b] += 1
        else:
            isfail = True

    queue = deque()
    isexact = True
    cnt = [0] * n
    for i in range(1, n + 1):
        if degree[i] == 0:
            queue.append(i)
        cnt[degree[i]] += 1
        if cnt[degree[i]] > 1:
            isexact = False

    ans = []
    cnt = len(queue)
    while queue:
        node = queue.popleft()
        ans.append(node)
        for i in graph[node]:
            degree[i] -= 1
            if degree[i] == 0:
                queue.append(i)
                cnt += 1

    if cnt != n or isfail:
        print('IMPOSSIBLE')
    elif not isexact:
        print('?')
    else:
        print(*ans)
