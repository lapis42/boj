import sys
input = sys.stdin.readline

n = int(input())
a = sorted(list(map(int, input().split())))
x = int(input())

i = 0
j = n - 1
cnt = 0

while i < j:
    if a[i] + a[j] == x:
        cnt += 1
        i += 1
    elif a[i] + a[j] > x:
        j -= 1
    else:
        i += 1

print(cnt)
