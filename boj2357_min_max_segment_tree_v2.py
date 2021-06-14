import sys
input = sys.stdin.readline


def build():
    for i in reversed(range(1, n)):
        tm[i] = min(tm[2 * i], tm[2 * i + 1])
        tM[i] = max(tM[2 * i], tM[2 * i + 1])


def get(i, j):
    ans = [10**9, 0]
    i += n
    j += n
    while i < j:
        if i & 1:
            ans[0] = min(ans[0], tm[i])
            ans[1] = max(ans[1], tM[i])
            i += 1
        if j & 1:
            j -= 1
            ans[0] = min(ans[0], tm[j])
            ans[1] = max(ans[1], tM[j])
        i >>= 1
        j >>= 1
    return ans


n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

tm = [10**9] * n + arr
tM = [0] * n + arr
build()

for _ in range(m):
    a, b = map(int, input().split())
    print(*get(a - 1, b))
