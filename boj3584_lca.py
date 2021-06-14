import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    graph = [0] * (n + 1)
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[b] = a
    x, y = map(int, input().split())

    x_parents = set()
    i = x
    while i:
        x_parents.add(i)
        i = graph[i]

    j = y
    while j:
        if j in x_parents:
            break
        j = graph[j]

    print(j)
