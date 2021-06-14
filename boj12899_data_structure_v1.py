import sys
from math import ceil, log2
sys.setrecursionlimit(10**7)

input = sys.stdin.readline
n = 2000000
tree = [0] * (1 << 22)


def add(index, node=1, start=0, end=n - 1):
    if index < start or index > end:
        return
    if start == end:
        tree[node] = 1
    else:
        tree[node] += 1
        mid = (start + end) // 2
        add(index, node * 2, start, mid)
        add(index, node * 2 + 1, mid + 1, end)


def pop(value, node=1, start=0, end=n - 1):
    if start == end:
        tree[node] = 0
        return start + 1
    tree[node] -= 1
    mid = (start + end) // 2
    if value > tree[node * 2]:
        return pop(value - tree[node * 2], node * 2 + 1, mid + 1, end)
    else:
        return pop(value, node * 2, start, mid)


for _ in range(int(input())):
    t, x = map(int, input().split())
    if t == 1:
        add(x - 1)
    else:
        print(pop(x))
