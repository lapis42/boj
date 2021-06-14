import sys
input = sys.stdin.readline

n, s = map(int, input().split())
x = list(map(int, input().split()))

sij = x[0]
j = 0
ans = sys.maxsize

for i in range(n):
    while sij < s and j < n - 1:
        j += 1
        sij += x[j]

    if sij >= s:
        ans = min(ans, j - i + 1)
        sij -= x[i]
    else:
        break

if ans == sys.maxsize:
    print(0)
else:
    print(ans)
