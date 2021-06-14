import sys
input = sys.stdin.readline


def get(t, i):
    ans = 0
    while i > 0:
        ans += t[i]
        i -= i & -i
    return ans


def update(t, i, v):
    while i < n + 1:
        t[i] += v
        i += i & -i


for _ in range(int(input())):
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    a.sort(key=lambda i: i[1])

    t = [0] * (n + 1)
    update(t, 1, 1)
    b = [[a[0][0], -1]]
    for i in range(1, n):
        if a[i][1] == a[i - 1][1]:
            j = b[-1][1]
        else:
            j = -(i + 1)
        b.append([a[i][0], j])
        update(t, -j, 1)
    b.sort()

    ans = 0
    for _, i in b:
        ans += get(t, -i) - 1
        update(t, -i, -1)
    print(ans)
