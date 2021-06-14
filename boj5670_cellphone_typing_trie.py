import sys
input = sys.stdin.readlines

xall = input()
n = len(xall)
i = 0
while i < n:
    m = int(xall[i])

    trie = {}
    for j in range(m):
        x = xall[i + j + 1].rstrip()
        node = trie
        for k in range(len(x)):
            if x[k] not in node:
                node[x[k]] = {}
            node = node[x[k]]
        node['.'] = {}


    cnt = [1] * m
    for j in range(m):
        x = xall[i + j + 1].rstrip()
        node = trie[x[0]]
        for k in range(1, len(x)):
            if len(node) > 1:
                cnt[j] += 1
            node = node[x[k]]

    print('{:0.2f}'.format(sum(cnt) / m))

    i += m + 1
