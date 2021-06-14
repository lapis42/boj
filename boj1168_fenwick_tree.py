def build():
    for i in range(1, n + 1):
        t[i] = i & -i


def pop(v):
    idx = 0
    for i in reversed(range(17)):
        j = idx + (1 << i)
        if j < n + 1:
            if t[j] < v:
                idx = j
                v -= t[j]
            else:
                t[j] -= 1
    return idx + 1


n, k = map(int, __import__('sys').stdin.readline().split())

t = [0] * (n + 1)
build()

ans = []
idx = 1
for i in range(n, 0, -1):
    idx = (idx + k - 2) % i + 1
    ans.append(pop(idx))

print('<', end='')
print(*ans, sep=', ', end='')
print('>')
