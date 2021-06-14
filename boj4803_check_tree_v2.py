import sys
from collections import deque
input = sys.stdin.readline


def visit(node):
    visited[node] = 1
    Q = deque([(node, 0)])

    fail = False
    while Q:
        node_now, parent = Q.popleft()
        for node_next in graph[node_now]:
            if not visited[node_next]:
                visited[node_next] = 1
                Q.append((node_next, node_now))
            elif node_next != parent:
                fail = True

    if fail:
        return 0
    else:
        return 1


case = 1
while True:
    n_node, n_edge = map(int, input().split())

    if n_node == n_edge == 0:
        break

    graph = [[] for _ in range(n_node + 1)]
    for _ in range(n_edge):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [0] * (n_node + 1)
    cnt = 0

    for node in range(1, n_node + 1):
        if not visited[node]:
            cnt += visit(node)

    if cnt > 1:
        print('Case {}: A forest of {} trees.'.format(case, cnt))
    elif cnt == 1:
        print('Case {}: There is one tree.'.format(case))
    else:
        print('Case {}: No trees.'.format(case))

    case += 1
