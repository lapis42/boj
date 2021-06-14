import sys
input = sys.stdin.readline
n = 2 ** ((2000000).bit_length())
tree = [0] * (2 * n)


def add(node, val=1):
    node += n
    while node > 0:
        tree[node] += val
        node >>= 1


def pop(value):
    node = 1
    while node < n:
        if value > tree[node * 2]:
            value -= tree[node * 2]
            node = node * 2 + 1
        else:
            node = node * 2
    node -= n
    add(node, -1)
    return node + 1


for _ in range(int(input())):
    t, x = map(int, input().split())
    if t == 1:
        add(x - 1)
    else:
        print(pop(x))
