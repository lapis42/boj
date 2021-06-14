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
    while i < m + 1:
        t[i] += v
        i += i & -i


# input
n = int(input())
d = []
x = []
for _ in range(n):
    nx, ny = map(int, input().split())
    d.append([ny, nx])
    x.append(nx)

# build
idx = {x: i + 1 for i, x in enumerate(sorted(set(x)))}
ni = len(idx)
t = [0] * (ni + 1)
for i in x:
    update(t, idx[i], 1)

# main
d.sort()
ans = 0
prev = -3 * 10**5
for i in range(n):
    if d[i][0] != prev:
        prev = d[i][0]
        j = i
        while j < n and d[j][0] == d[i][0]:
            update(t, idx[d[j][1]], -1)
            j += 1
    l = get(t, idx[d[i][1]] - 1)
    r = get(t, ni) - get(t, idx[d[i][1]])
    ans = (ans + l * r) % m
print(ans)
