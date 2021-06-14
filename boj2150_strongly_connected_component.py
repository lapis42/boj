import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(i):
    if not visited[i]:
        visited[i] = 1
        for j in graph[i]:
            if not visited[j]:
                dfs(j)
        stack.append(i)


def dfs_backwards(i):
    if not visited[i]:
        ans = [i]
        visited[i] = 1
        for j in graph_backwards[i]:
            if not visited[j]:
                ans += dfs_backwards(j)
        return ans
    return []


v, e = map(int, input().split())

graph = [[] for _ in range(v + 1)]
graph_backwards = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph_backwards[b].append(a)

stack = []
visited = [0] * (v + 1)
for i in range(1, v + 1):
    dfs(i)

ans = []
visited = [0] * (v + 1)
for i in stack[::-1]:
    temp = dfs_backwards(i)
    if temp:
        ans.append(sorted(temp))
ans.sort()

print(len(ans))
for i in ans:
    print(*sorted(i), -1)
