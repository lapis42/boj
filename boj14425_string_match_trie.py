import sys
input = sys.stdin.readline

trie = {}
n, m = map(int, input().split())

for _ in range(n):
    x = list(input().rstrip())
    node = trie
    for i in range(len(x)):
        if x[i] not in node:
            node[x[i]] = {}
        node = node[x[i]]
    node['.'] = {}

cnt = 0
for _ in range(m):
    x = list(input().rstrip())
    node = trie
    done = True
    for i in range(len(x)):
        if x[i] in node:
            node = node[x[i]]
        else:
            done = False
            break
    if done and '.' in node:
        cnt += 1

print(cnt)
