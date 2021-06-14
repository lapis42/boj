import sys
import math
input = sys.stdin.readline


def check_length(idx):
    cnt = 0
    for i in range(n):
        if idx >> i & 1:
            cnt += x_length[i]
    return cnt


# input
n = int(input())
x = [int(input()) for _ in range(n)]
k = int(input())


x_length = [len(str(i)) for i in x]
x_modulo = [[(j * 10**i) % k for i in range(sum(x_length))] for j in x]

dp = [[0] * k for _ in range(2**n)]
dp[0][0] = 1
'''dp[i][j]: count of (i) combination with j modulo
    i: bitmask
    j: modulo
    answer will be dp[-1][0] / n!
'''
for idx in range(2**n):
    for m in range(k): # previous modulo
        if dp[idx][m] == 0: continue
        for i in range(n): # next component to pick
            if (idx & 1 << i): continue # pass if already picked
            next_m = (x_modulo[i][check_length(idx)] + m) % k
            dp[idx | 1 << i][next_m] += dp[idx][m]

N = math.factorial(n)
d = math.gcd(dp[-1][0], N)
print('{}/{}'.format(dp[-1][0] // d, N // d))
