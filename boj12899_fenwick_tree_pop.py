import sys
input = sys.stdin.readline


def pop(v):
    idx = 0
    for i in reversed(range(21)):
        j = idx + (1 << i)
        if j < n:
            if t[j] < v:
                idx = j
                v -= t[j]
            else:
                t[j] -= 1
    return idx + 1


def add(i):
    while i < n:
        t[i] += 1
        i += i & -i


n = 2000001
t = [0] * n

for _ in range(int(input())):
    q, x = map(int, input().split())
    if q == 1:
        add(x)
    else:
        print(pop(x))
