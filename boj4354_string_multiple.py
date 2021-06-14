import sys
input = sys.stdin.readline


while True:
    x = input().rstrip()
    if x == '.': break
    n = len(x)

    j = 0
    m = 1
    for i in range(1, n):
        if x[i] == x[j]:
            j += 1
            if j == m:
                j = 0
        else:
            if j > 0 and x[i] == x[0]:
                m = i
                j = 1
            else:
                m = i + 1
                j = 0

    ans, r = divmod(n, m)
    if r:
        print(1)
    else:
        print(ans)

