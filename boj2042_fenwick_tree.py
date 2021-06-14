import sys
input = sys.stdin.readline


def update(i, diff):
    while i < n + 1:
        tree[i] += diff
        i += (i & -i)


def get(i):
    ans = 0
    while i > 0:
        ans += tree[i]
        i -= (i & -i)
    return ans


n, m, k = map(int, input().split())

arr = [0] * (n + 1)
tree = [0] * (n + 1)
for i in range(1, n + 1):
    arr[i] = int(input())
    update(i, arr[i])

for _ in range(m + k):
    a, b, c = map(int, input().split())

    if a == 1:
        diff = c - arr[b]
        arr[b] = c
        update(b, diff)
    else:
        print(get(c) - get(b - 1))
