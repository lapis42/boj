def transversal(tree, mode, node=0):
    idx = tree[node]
    l_idx, r_idx = 2 * idx + 1, 2 * idx + 2
    d = [node_name[node]]
    l = transversal(tree, mode, tree.index(l_idx)) if l_idx in tree else []
    r = transversal(tree, mode, tree.index(r_idx)) if r_idx in tree else []
    if mode == 0:
        ans = d + l + r
    elif mode == 1:
        ans = l + d + r
    else:
        ans = l + r + d
    return ans


n_node = int(input())
node_name = list(map(chr, range(65, 65 + n_node)))
tree = [0] * n_node
for i in range(n_node):
    d, l, r = map(ord, input().split())
    parent_idx = tree[d - 65]
    if l > 64:
        tree[l - 65] = 2 * parent_idx + 1
    if r > 64:
        tree[r - 65] = 2 * parent_idx + 2

print(*transversal(tree, 0), sep='')
print(*transversal(tree, 1), sep='')
print(*transversal(tree, 2), sep='')
