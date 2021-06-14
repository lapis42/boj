import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(int(input()))]
arr.sort()

ans = 0
l, r = arr[0]
for x, y in arr[1:]:
    if x > r:
        ans += r - l
        l, r = x, y
    elif y > r:
        r = y
ans += r - l
print(ans)
