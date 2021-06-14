import sys
import bisect
input = sys.stdin.readline

t_size = 10**5 + 2


def update(x, y):
    while x < t_size:
        tree[x].append(y)
        x += x & -x


def insort():
    for i in range(1, t_size):
        tree[i].sort()


def get(i, b, t):
    ans = 0
    while i > 0:
        r = bisect.bisect(tree[i], t)
        l = bisect.bisect_left(tree[i], b)
        ans += r - l
        i -= i & -i
    return ans


for _ in range(int(input())):
    n, m = map(int, input().split())
    tree = [[] for _ in range(t_size)]
    for _ in range(n):
        x, y = map(int, input().split())
        update(x + 1, y)
    insort()

    ans = 0
    for _ in range(m):
        l, r, b, t = map(int, input().split())
        ans += get(r + 1, b, t) - get(l, b, t)
    print(ans)
