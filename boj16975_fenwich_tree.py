import sys
input = sys.stdin.readline


def get(i):
    ans = a[i - 1]
    while i > 0:
        ans += t[i]
        i -= i & -i
    return ans


def update(i, v):
    while i < n + 1:
        t[i] += v
        i += i & -i


n = int(input())
a = list(map(int, input().split()))
t = [0] * (n + 1)

for _ in range(int(input())):
    q, *x = map(int, input().split())
    if q == 1:
        update(x[0], x[2])
        if x[1] < n: update(x[1] + 1, -x[2])
    else:
        print(get(x[0]))
