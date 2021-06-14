import sys
from collections import deque
input = sys.stdin.readline


def bfs(n, k):
    count = [0] * 100001
    queue = deque()
    queue.append(n)
    while queue:
        now = queue.popleft()
        if now == k:
            return count[now]
        after = [now - 1, now + 1, 2 * now]
        for i in after:
            if 0 <= i <= 100000 and count[i] == 0:
                queue.append(i)
                count[i] = count[now] + 1
    return -1


n, k = map(int, input().split())
print(bfs(n, k))
