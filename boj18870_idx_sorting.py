import sys
r = sys.stdin.readline

r()
x = list(map(int, r().split()))
idx = {v: i for i, v in enumerate(sorted(set(x)))}
print(*[idx[v] for v in x])
