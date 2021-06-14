import sys
input = sys.stdin.readline


def find(i):
    while i != idx[i]:
        idx[i] = idx[idx[i]]
        i = idx[i]
    return i


def union(x, y):
    xset = find(x)
    yset = find(y)
    if xset == yset:
        return True
    else:
        idx[xset] = yset
        return False


n, m = map(int, input().split())
idx = list(range(n))
ans = 0
for i in range(m):
    a, b = map(int, input().split())

    if ans == 0:
        done = union(a, b)

    if done:
        ans = i + 1
        done = False

print(ans)
