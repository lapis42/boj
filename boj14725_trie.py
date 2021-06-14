import sys
input = sys.stdin.readline


def print_trie(trie, step=0):
    for i, v in sorted(trie.items()):
        print('--' * step, i, sep='')
        if v:
            print_trie(v, step + 1)


trie = {}
for _ in range(int(input())):
    k, *x = input().split()
    node = trie
    for i in range(int(k)):
        if x[i] not in node:
            node[x[i]] = {}
        node = node[x[i]]

print_trie(trie)
