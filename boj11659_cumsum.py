import sys
input = sys.stdin.readline

n, m = map(int, input().split())
x = list(map(int, input().split()))

cumsum = [0] * (n + 1)
for i in range(n):
    cumsum[i + 1] = cumsum[i] + x[i]

for _ in range(m):
    i, j = map(int, input().split())
    print(cumsum[j] - cumsum[i - 1])
