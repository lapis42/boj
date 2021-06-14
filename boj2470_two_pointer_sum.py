import sys
input = sys.stdin.readline

n = int(input())
a = sorted(list(map(int, input().split())))

i = 0
j = n - 1
min_abs = int(2E9)
ans = [a[i], a[j]]

while i < j:
    if abs(a[i] + a[j]) < min_abs:
        min_abs = abs(a[i] + a[j])
        ans = [a[i], a[j]]
        if min_abs == 0:
            break

    if a[i] + a[j] > 0:
        j -= 1
    else:
        i += 1

print(*ans)
