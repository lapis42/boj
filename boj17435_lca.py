import sys
import math
input = sys.stdin.readline

m = int(input())
f = [0] + list(map(int, input().split()))

fs = [f]
for i in range(int(math.log2(500000))):
    ftemp = [0]
    for j in range(1, m + 1):
        ftemp.append(fs[i][fs[i][j]])
    fs.append(ftemp)

q = int(input())
for _ in range(q):
    n, x = map(int, input().split())

    i = n
    j = x
    while i > 0:
        idx = int(math.log2(i))
        i -= 2**idx
        j = fs[idx][j]

    print(j)
