import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    if a > b:
        arr.append((b, a))
arr.sort()

l, r = arr[0]
ans = m
for x, y in arr[1:]:
    if x > r:
        ans += 2 * (r - l)
        l, r = x, y
    elif y > r:
        r = y
ans += 2 * (r - l)
print(ans)
