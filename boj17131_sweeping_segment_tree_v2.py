import sys
input = sys.stdin.readline
m = 10**9 + 7


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


n = int(input())
x = []
y = []
for _ in range(n):
    nx, ny = map(int, input().split())
    x.append(nx)
    y.append(ny)


a = [list(map(int, input().split())) for _ in range(n)]
a.sort()

t = [0] * (n + 1)
update(t, 1, 1)
b = [[a[0][1], -1]]
for i in range(1, n):
    if a[i][0] == a[i - 1][0]:
        j = b[-1][1]
    else:
        j = -(i + 1)
    b.append([a[i][1], j])
    update(t, -j, 1)
b.sort()

ans = 0
prev = -3 * 10**5
for i in range(n):
    if b[i][0] != prev:
        prev = b[i][0]
        j = i
        while j < n and b[j][0] == b[i][0]:
            update(t, -b[j][1], -1)
            j += 1
    l = get(t, -b[i][1] - 1)
    r = get(t, n) - get(t, -b[i][1])
    ans = (ans + l * r) % m
print(ans)
